#!/usr/bin/env python3
"""
report_audit.py — 报告数据抽检（准出流程）

目的：报告写完后，随机抽取其中的财务数据点，独立复取核验，
      偏差 > 阈值即打回。防止 LLM 在长报告中夹带未经核实的数字。

用法：
  # Step 1 抽样，输出待填 JSON
  python3 tools/report_audit.py extract --report reports/Ether/Ether-research-20260730.md

  # Step 2 人工/Agent 按 skills/financial-data.md 规范取数，填入
  #        fetched_value / fetched_source / fetched_value2 / fetched_source2

  # Step 3 判决
  python3 tools/report_audit.py verdict --results '<填好的JSON>' --report <报告文件名>
  python3 tools/report_audit.py verdict --results-file audit.json --report <报告文件名>

设计要点：
  1. 只抽「可外部核验的财务数字」——自动排除日期、章节号、星级评分、
     概率假设、以及被作者本人标注为 🔴（推算/低置信）的数字。
  2. 抽样确定性：种子由报告内容哈希导出，同一份报告抽样结果可复现，
     但作者无法预先挑选对自己有利的抽样。
  3. 全程 Decimal，与 financial_rigor.py 一致。
  4. 未填写 fetched_value 的条目视为「未核验」，阻断准出。
"""

import argparse
import hashlib
import json
import random
import re
import sys
from decimal import Decimal, getcontext, InvalidOperation

getcontext().prec = 28

TOLERANCE_DEFAULT = Decimal("0.01")   # 1%
SAMPLE_RATE_DEFAULT = Decimal("0.15")  # 15%
MIN_SAMPLE = 5

# ---------------------------------------------------------------- 单位换算
SCALE = {
    "": Decimal(1),
    "k": Decimal(10) ** 3, "K": Decimal(10) ** 3,
    "m": Decimal(10) ** 6, "M": Decimal(10) ** 6,
    "b": Decimal(10) ** 9, "B": Decimal(10) ** 9,
    "t": Decimal(10) ** 12, "T": Decimal(10) ** 12,
    "million": Decimal(10) ** 6, "billion": Decimal(10) ** 9,
    "万": Decimal(10) ** 4, "億": Decimal(10) ** 8, "亿": Decimal(10) ** 8,
    "兆": Decimal(10) ** 12,
}

CURRENCIES = ["US$", "HK$", "RMB", "NT$", "$", "€", "£", "¥", "₩"]

# 数字主体：支持千分位与小数
NUM = r"-?\d{1,3}(?:,\d{3})+(?:\.\d+)?|-?\d+(?:\.\d+)?"

# 三类可核验的数字
PAT_CURRENCY = re.compile(
    r"(?P<cur>US\$|HK\$|NT\$|RMB|\$|€|£|¥|₩)\s?(?P<num>" + NUM + r")\s?"
    r"(?P<scale>亿|億|万|兆|billion|million|[kKmMbBtT])?\b"
)
PAT_UNIT_NUM = re.compile(
    r"(?<![\w.])(?P<num>" + NUM + r")\s?(?P<scale>亿|億|万|兆|billion|million|[kKmMbBtT])?\s?"
    r"(?P<unit>ETH|BTC|SOL|股|shares|枚|张|台|人|名)\b"
)
PAT_MULTIPLE = re.compile(r"(?<![\w.])(?P<num>" + NUM + r")\s?(?P<unit>[x×])(?![\w])")
PAT_PERCENT = re.compile(r"(?<![\w.])(?P<num>" + NUM + r")\s?(?P<unit>%)")

# ---------------------------------------------------------------- 排除规则
RE_ISO_DATE = re.compile(r"\d{4}-\d{1,2}(-\d{1,2})?")
RE_HEADING_NUM = re.compile(r"^\s*#{1,6}\s*[\d.]+")
RE_LIST_NUM = re.compile(r"^\s*\|?\s*\d+\s*\|")          # 表格首列纯序号
RE_URL = re.compile(r"https?://\S+")
RE_STARS = re.compile(r"★+☆*")
RE_FENCE = re.compile(r"^\s*```")

# 作者标注为低置信/推算 → 不可作为外部核验对象
RE_LOWCONF = re.compile(r"🔴|数据缺失|數據缺失|未能核实|未能核實|不可采信|不可採信")
RE_MIDCONF = re.compile(r"🟡")
RE_HICONF = re.compile(r"🟢")

# 明显是假设/情景而非事实的行
RE_ASSUMPTION = re.compile(
    r"假设|假設|情景|情境|概率|機率|折现率|折現率|终值倍数|終值倍數|"
    r"隐含|隱含|目标价|目標價|推算|推理|estimate|assume"
)

# 报告内部自算或自评的数字 —— 无外部信源可复取，抽检它们没有意义
RE_SELF_COMPUTED = re.compile(
    r"置信度|信心度|信賴度|完整度|自评|自評|评分|評分|权重|權重|"
    r"偏差|容差|现值|現值|加权|加權|IRR|年化\(|复算|複算|验算|驗算|"
    r"安全边际|安全邊際|概率加权|概率加權|口径|口徑|中性|悲观|悲觀|乐观|樂觀|"
    r"P/F|P/E|P/S|P/B|P/FCF|EV/|市值/|倍数 =|倍數 =|= *\d+(\.\d+)?x"
)

# 外部可核验性分级：决定抽样权重
VERIFIABILITY = {
    "currency": 3,    # 收入/市值/费用 —— 最应核验
    "quantity": 3,    # 供应量/质押量/用户数
    "multiple": 1,    # 多为自算倍数
    "percentage": 1,  # 多为自算比率
    "other": 1,
}


def D(x):
    try:
        return Decimal(str(x).replace(",", "").strip())
    except (InvalidOperation, ValueError):
        return None


def normalize(num_str, scale_str, currency=None, unit=None):
    """把 '$255.0M' / '121,884,168 ETH' / '910x' / '0.49%' 归一化为 Decimal。"""
    base = D(num_str)
    if base is None:
        return None
    mult = SCALE.get(scale_str or "", Decimal(1))
    return base * mult


def classify(line, currency, unit):
    if currency:
        return "currency"
    if unit in ("ETH", "BTC", "SOL", "股", "shares", "枚", "张", "台", "人", "名"):
        return "quantity"
    if unit in ("x", "×"):
        return "multiple"
    if unit == "%":
        return "percentage"
    return "other"


def confidence_of(line):
    if RE_LOWCONF.search(line):
        return "low"
    if RE_MIDCONF.search(line):
        return "mid"
    if RE_HICONF.search(line):
        return "high"
    return "unmarked"


def extract_candidates(text):
    """从 Markdown 抽取候选数据点。返回 list[dict]。"""
    out = []
    in_fence = False
    seen = set()

    for lineno, raw in enumerate(text.splitlines(), start=1):
        if RE_FENCE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue                      # 代码块内多为工具输出，已被 financial_rigor 验算过
        if RE_HEADING_NUM.match(raw):
            continue
        line = RE_URL.sub(" ", raw)
        line = RE_STARS.sub(" ", line)
        # 去掉日期，避免 2026-07-30 被当成数字
        line_nodate = RE_ISO_DATE.sub(" ", line)

        conf = confidence_of(raw)
        is_assumption = bool(RE_ASSUMPTION.search(raw))
        is_self = bool(RE_SELF_COMPUTED.search(raw))

        def add(m, currency=None, unit=None):
            num = m.group("num")
            scale = m.groupdict().get("scale")
            val = normalize(num, scale, currency, unit)
            if val is None:
                return
            raw_txt = m.group(0).strip()
            key = (lineno, raw_txt)
            if key in seen:
                return
            seen.add(key)
            ctx = raw.strip()
            if len(ctx) > 220:
                ctx = ctx[:217] + "..."
            out.append({
                "line": lineno,
                "raw": raw_txt,
                "value": str(val),
                "category": classify(raw, currency, unit),
                "currency": currency,
                "unit": unit,
                "confidence_marked": conf,
                "looks_like_assumption": is_assumption,
                "self_computed": is_self,
                "context": ctx,
            })

        for m in PAT_CURRENCY.finditer(line_nodate):
            add(m, currency=m.group("cur"))
        for m in PAT_UNIT_NUM.finditer(line_nodate):
            add(m, unit=m.group("unit"))
        for m in PAT_MULTIPLE.finditer(line_nodate):
            add(m, unit="x")
        for m in PAT_PERCENT.finditer(line_nodate):
            add(m, unit="%")

    return out


def auditable(item, include_low=False, include_assumptions=False):
    """是否应纳入抽检池。"""
    if item["confidence_marked"] == "low" and not include_low:
        return False
    if item["looks_like_assumption"] and not include_assumptions:
        return False
    if item["self_computed"]:
        return False          # 报告内部自算/自评，无外部信源可复取
    return True


def stratified_sample(pool, n, rng):
    """分层抽样：优先抽外部可核验性高的类别（金额、数量），
    避免样本被大量自算百分比稀释。"""
    hi = [c for c in pool if VERIFIABILITY.get(c["category"], 1) >= 3]
    lo = [c for c in pool if VERIFIABILITY.get(c["category"], 1) < 3]
    # 目标：高可核验类占样本 ≥ 70%（池子不够时全取）
    n_hi = min(len(hi), max(1, int(n * 0.7 + 0.5)))
    n_lo = min(len(lo), n - n_hi)
    n_hi = min(len(hi), n - n_lo)     # 低可核验不足时回补
    return rng.sample(hi, n_hi) + rng.sample(lo, n_lo)


# ------------------------------------------------------------------ extract
def cmd_extract(args):
    try:
        text = open(args.report, encoding="utf-8").read()
    except OSError as e:
        raise SystemExit(f"❌ 无法读取报告: {e}")

    cands = extract_candidates(text)
    pool = [c for c in cands
            if auditable(c, args.include_low_confidence, args.include_assumptions)]

    if not pool:
        raise SystemExit("❌ 未从报告中提取到任何可核验数据点。"
                         "请检查报告格式，或用 --include-assumptions 放宽。")

    rate = D(args.sample_rate)
    n = max(MIN_SAMPLE, int((D(len(pool)) * rate).to_integral_value(rounding="ROUND_CEILING")))
    n = min(n, len(pool))

    # 种子由报告内容导出：可复现，但作者无法预先挑选
    seed = int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:16], 16)
    rng = random.Random(seed)
    sample = stratified_sample(pool, n, rng)
    sample.sort(key=lambda c: c["line"])

    payload = {
        "report": args.report,
        "total_candidates": len(cands),
        "auditable_pool": len(pool),
        "sample_rate": str(rate),
        "sample_size": n,
        "seed_sha256_prefix": hashlib.sha256(text.encode("utf-8")).hexdigest()[:16],
        "tolerance": str(D(args.tolerance)),
        "items": [
            {
                "id": i + 1,
                "line": c["line"],
                "raw": c["raw"],
                "reported_value": c["value"],
                "category": c["category"],
                "confidence_marked": c["confidence_marked"],
                "context": c["context"],
                "fetched_value": "",
                "fetched_source": "",
                "fetched_value2": "",
                "fetched_source2": "",
                "note": "",
            }
            for i, c in enumerate(sample)
        ],
    }

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    from collections import Counter
    cat = Counter(c["category"] for c in sample)
    print(f"\n# 样本构成：" + "｜".join(f"{k} {v}" for k, v in cat.most_common()),
          file=sys.stderr)
    print(f"# 抽检池 {len(pool)} 项（候选 {len(cands)}，已排除 🔴低置信 / 假设类 / 报告内部自算）"
          f"｜抽样 {n} 项（{rate * 100:.0f}%）", file=sys.stderr)
    print("# 请按 skills/financial-data.md 规范填写 fetched_value / fetched_source"
          "（至少 2 个独立来源），再执行 verdict", file=sys.stderr)


# ------------------------------------------------------------------ verdict
def cmd_verdict(args):
    if args.results_file:
        try:
            data = json.load(open(args.results_file, encoding="utf-8"))
        except OSError as e:
            raise SystemExit(f"❌ 无法读取结果文件: {e}")
    elif args.results:
        try:
            data = json.loads(args.results)
        except json.JSONDecodeError as e:
            raise SystemExit(f"❌ --results 不是合法 JSON: {e}")
    else:
        raise SystemExit("❌ 需要 --results 或 --results-file")

    tol = D(args.tolerance) if args.tolerance else D(data.get("tolerance", "0.01"))
    items = data.get("items", [])
    if not items:
        raise SystemExit("❌ 结果中没有 items")

    print(f"# 数据抽检判决 — {args.report or data.get('report', '')}")
    print()
    print(f"抽样 **{len(items)}** 项｜容差 **{(tol * 100).quantize(Decimal('0.01'))}%**")
    print()
    print("| # | 行 | 数据点 | 报告值 | 复取值A | 复取值B | 偏差 | 判定 |")
    print("|---|----|--------|--------|---------|---------|------|------|")

    failed, unverified, passed = [], [], []

    for it in items:
        rep = D(it.get("reported_value"))
        f1 = D(it.get("fetched_value")) if str(it.get("fetched_value", "")).strip() else None
        f2 = D(it.get("fetched_value2")) if str(it.get("fetched_value2", "")).strip() else None

        raw = str(it.get("raw", ""))[:28]
        if f1 is None:
            print(f"| {it.get('id')} | {it.get('line')} | {raw} | {rep} | — | — | — | ⬜ 未核验 |")
            unverified.append(it)
            continue

        refs = [v for v in (f1, f2) if v is not None]
        # 以复取值均值为基准（多源时），与 financial_rigor 的 cross-validate 一致
        base = sum(refs) / Decimal(len(refs))
        dev = abs(rep - base) / abs(base) if base != 0 else (
            Decimal(0) if rep == 0 else Decimal("Infinity"))
        ok = dev <= tol
        mark = "✅" if ok else "❌"
        f2s = str(f2) if f2 is not None else "—"
        print(f"| {it.get('id')} | {it.get('line')} | {raw} | {rep} | {f1} | {f2s} | "
              f"{(dev * 100).quantize(Decimal('0.01'))}% | {mark} |")
        (passed if ok else failed).append((it, dev))

        if f2 is not None:
            src_dev = abs(f1 - f2) / abs(f2) if f2 != 0 else Decimal(0)
            if src_dev > tol:
                it["_source_conflict"] = str((src_dev * 100).quantize(Decimal("0.01")))

    print()
    conflicts = [it for it in items if "_source_conflict" in it]
    if conflicts:
        print("### ⚠️ 来源间分歧（复取的两个来源自身不一致）")
        print()
        for it in conflicts:
            print(f"- 第 {it.get('line')} 行 `{it.get('raw')}`："
                  f"{it.get('fetched_source')} vs {it.get('fetched_source2')} "
                  f"相差 {it['_source_conflict']}% — **报告中必须全部列出并说明采信理由**")
        print()

    print(f"**通过 {len(passed)}｜超差 {len(failed)}｜未核验 {len(unverified)}**")
    print()

    if failed or unverified:
        print("## 【打回】")
        print()
        if failed:
            print("偏差超过容差，须修正报告中对应数据后重新抽检：")
            for it, dev in failed:
                print(f"- **第 {it.get('line')} 行** `{it.get('raw')}`："
                      f"报告 {it.get('reported_value')} vs 复取 {it.get('fetched_value')}"
                      f"（偏差 {(dev * 100).quantize(Decimal('0.01'))}%）")
                if it.get("context"):
                    print(f"  - 上下文：{it['context']}")
        if unverified:
            print()
            print("以下条目未填写复取值，无法准出：")
            for it in unverified:
                print(f"- 第 {it.get('line')} 行 `{it.get('raw')}`")
        sys.exit(1)
    else:
        print("## 【准出】")
        print()
        print(f"全部 {len(passed)} 个抽检点偏差均 ≤ {(tol * 100).quantize(Decimal('0.01'))}%，报告可发布。")
        print()


def main():
    p = argparse.ArgumentParser(description="报告数据抽检（准出流程）")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("extract", help="抽样，输出待填 JSON")
    a.add_argument("--report", required=True)
    a.add_argument("--sample-rate", default=str(SAMPLE_RATE_DEFAULT))
    a.add_argument("--tolerance", default=str(TOLERANCE_DEFAULT))
    a.add_argument("--include-low-confidence", action="store_true",
                   help="把作者标注为 🔴 的数字也纳入抽检池（默认排除）")
    a.add_argument("--include-assumptions", action="store_true",
                   help="把假设/情景类数字也纳入抽检池（默认排除）")
    a.set_defaults(func=cmd_extract)

    b = sub.add_parser("verdict", help="判决")
    b.add_argument("--results", help="填好的 JSON 字符串")
    b.add_argument("--results-file", help="填好的 JSON 文件路径")
    b.add_argument("--report", help="报告文件名（仅用于表头）")
    b.add_argument("--tolerance", help="覆盖 JSON 中的容差")
    b.set_defaults(func=cmd_verdict)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
