#!/usr/bin/env python3
"""
financial_rigor.py — 金融严谨性验算工具

目的：杜绝 LLM 心算误差。所有涉及金额、倍数、增长率的计算，
一律通过本工具的 Decimal 精确十进制运算完成，禁止用浮点数或心算。

子命令：
  verify-market-cap   市值验算（股价 × 股本 vs 报告市值）
  cross-validate      多源交叉验证（偏差 > 阈值即告警）
  verify-valuation    估值指标验算（PE / PB / ROE / FCF Yield / 股息率）
  three-scenario      三情景估值（乐观/中性/悲观，复合增长 + 目标倍数）
  reverse-dcf         反向 DCF（当前价格隐含的增长预期）

设计原则：
  1. 全程 Decimal，绝不使用 float 做金额运算
  2. 偏差阈值默认 1%，超出即 ❌ 打回
  3. 输出为可直接嵌入 Markdown 报告的表格
"""

import argparse
import json
import sys
from decimal import Decimal, getcontext, InvalidOperation

getcontext().prec = 28

TOLERANCE_DEFAULT = Decimal("0.01")  # 1%


def D(x):
    """安全转 Decimal。接受 str/int/float/Decimal。"""
    if isinstance(x, Decimal):
        return x
    try:
        return Decimal(str(x))
    except (InvalidOperation, ValueError):
        raise SystemExit(f"❌ 无法解析为数字: {x!r}")


def pct(x):
    """Decimal 转百分比字符串，保留 2 位。"""
    return f"{(x * 100).quantize(Decimal('0.01'))}%"


def fmt(x, places="0.0001"):
    """量化到指定精度并去掉无意义的尾随零，但不退化为科学计数法。"""
    q = x.quantize(Decimal(places))
    s = format(q, "f")          # 强制定点表示，避免 1E+2
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    return s if s not in ("", "-") else "0"


def rel_dev(a, b):
    """相对偏差 |a-b| / |b|。b 为基准。"""
    if b == 0:
        return Decimal("Infinity") if a != 0 else Decimal(0)
    return abs(a - b) / abs(b)


# ---------------------------------------------------------------- market cap
def cmd_verify_market_cap(args):
    price = D(args.price)
    shares = D(args.shares)
    reported = D(args.reported)
    tol = D(args.tolerance)

    computed = price * shares
    dev = rel_dev(computed, reported)
    ok = dev <= tol

    print("## 市值验算")
    print()
    print("| 项目 | 数值 |")
    print("|------|------|")
    print(f"| 股价 | {fmt(price, '0.0001')} {args.currency} |")
    print(f"| 总股本 | {fmt(shares, '0.0001')} |")
    print(f"| **计算市值** | **{fmt(computed, '0.01')} {args.currency}** |")
    print(f"| 报告市值 | {fmt(reported, '0.01')} {args.currency} |")
    print(f"| 相对偏差 | {pct(dev)} |")
    print(f"| 容差 | {pct(tol)} |")
    print(f"| **判定** | **{'✅ 通过' if ok else '❌ 偏差过大，须排查'}** |")
    print()
    if not ok:
        print("> ⚠️ 常见原因：单位错位（亿/百万/十亿）、币种混用、"
              "股本口径不同（基本 vs 稀释 vs 流通）、数据时点不一致。")
        sys.exit(1)


# ------------------------------------------------------------ cross validate
def cmd_cross_validate(args):
    try:
        values = json.loads(args.values)
    except json.JSONDecodeError as e:
        raise SystemExit(f"❌ --values 不是合法 JSON: {e}")
    if len(values) < 2:
        raise SystemExit("❌ 交叉验证至少需要 2 个来源")

    tol = D(args.tolerance)
    items = [(k, D(v)) for k, v in values.items()]
    nums = [v for _, v in items]
    baseline = min(nums, key=lambda v: abs(v))  # 以绝对值最小者为保守基准
    mean = sum(nums) / D(len(nums))
    spread = (max(nums) - min(nums))
    max_dev = max(rel_dev(v, mean) for v in nums)
    ok = max_dev <= tol

    print(f"## 交叉验证：{args.field}")
    print()
    print("| 来源 | 数值 | 相对均值偏差 |")
    print("|------|------|--------------|")
    for k, v in items:
        print(f"| {k} | {fmt(v, '0.0001')} {args.unit} | {pct(rel_dev(v, mean))} |")
    print(f"| **均值** | **{fmt(mean, '0.0001')} {args.unit}** | — |")
    print(f"| 极差 | {fmt(spread, '0.0001')} {args.unit} | — |")
    print(f"| 最大偏差 | {pct(max_dev)} | 容差 {pct(tol)} |")
    print(f"| **判定** | **{'✅ 一致' if ok else '⚠️ 来源分歧，须注明差异原因'}** | |")
    print()
    if not ok:
        print(f"> ⚠️ 来源间偏差 {pct(max_dev)} 超过容差。报告中必须**全部列出**各来源数值，"
              f"并说明采信哪一个、为什么。保守取值建议：{fmt(baseline, '0.0001')} {args.unit}")


# ---------------------------------------------------------- verify valuation
def cmd_verify_valuation(args):
    price = D(args.price)
    rows = []

    if args.eps is not None:
        eps = D(args.eps)
        rows.append(("PE (TTM)", (price / eps) if eps != 0 else None,
                     f"股价 {fmt(price)} ÷ EPS {fmt(eps)}"))
    if args.bvps is not None:
        bvps = D(args.bvps)
        rows.append(("PB", (price / bvps) if bvps != 0 else None,
                     f"股价 {fmt(price)} ÷ 每股净资产 {fmt(bvps)}"))
        if args.eps is not None and bvps != 0:
            rows.append(("ROE", D(args.eps) / bvps,
                         f"EPS {fmt(D(args.eps))} ÷ 每股净资产 {fmt(bvps)}"))
    if args.fcf_per_share is not None:
        f = D(args.fcf_per_share)
        rows.append(("FCF Yield", (f / price) if price != 0 else None,
                     f"每股FCF {fmt(f)} ÷ 股价 {fmt(price)}"))
        if f != 0:
            rows.append(("P/FCF", price / f, f"股价 ÷ 每股FCF"))
    if args.dividend is not None:
        d = D(args.dividend)
        rows.append(("股息率", (d / price) if price != 0 else None,
                     f"每股股息 {fmt(d)} ÷ 股价 {fmt(price)}"))

    if not rows:
        raise SystemExit("❌ 至少提供 --eps / --bvps / --fcf-per-share / --dividend 之一")

    print("## 估值指标验算")
    print()
    print("| 指标 | 数值 | 计算式 |")
    print("|------|------|--------|")
    for name, val, formula in rows:
        if val is None:
            print(f"| {name} | n/a（分母为 0） | {formula} |")
        elif name in ("ROE", "FCF Yield", "股息率"):
            print(f"| {name} | {pct(val)} | {formula} |")
        else:
            print(f"| {name} | {fmt(val, '0.01')}x | {formula} |")
    print()


# ----------------------------------------------------------- three scenario
def cmd_three_scenario(args):
    price = D(args.price)
    base = D(args.eps)  # 可为 EPS，也可为任意"每股基准量"（如每股费用收入）
    years = int(args.years)
    growth = [D(g) for g in args.growth]
    mult = [D(m) for m in args.pe]
    labels = ["乐观", "中性", "悲观"]

    if len(growth) != 3 or len(mult) != 3:
        raise SystemExit("❌ --growth 与 --pe 各需 3 个值（乐观 中性 悲观）")

    print(f"## 三情景估值（{years} 年）")
    print()
    print(f"当前价格：**{fmt(price, '0.0001')} {args.currency}**　"
          f"当前每股基准量：**{fmt(base, '0.0001')}**")
    print()
    print("| 情景 | 年增速 | 终期基准量 | 目标倍数 | 目标价 | 累计涨跌 | 年化(IRR) |")
    print("|------|--------|-----------|---------|--------|---------|-----------|")

    results = []
    for lab, g, m in zip(labels, growth, mult):
        terminal = base * (Decimal(1) + g) ** years
        target = terminal * m
        total_ret = (target / price - Decimal(1)) if price != 0 else Decimal(0)
        # IRR = (target/price)^(1/years) - 1，用对数避免 Decimal 分数次幂限制
        ratio = target / price if price != 0 else Decimal(0)
        if ratio > 0:
            irr = ratio ** (Decimal(1) / Decimal(years)) - Decimal(1)
        else:
            irr = Decimal(-1)
        results.append((lab, target, total_ret, irr))
        print(f"| {lab} | {pct(g)} | {fmt(terminal, '0.0001')} | {fmt(m, '0.01')}x | "
              f"**{fmt(target, '0.01')}** | {pct(total_ret)} | {pct(irr)} |")

    print()
    lo = min(r[1] for r in results)
    hi = max(r[1] for r in results)
    mid = results[1][1]
    print(f"**估值区间：{fmt(lo, '0.01')} – {fmt(hi, '0.01')} {args.currency}**"
          f"（中性情景 {fmt(mid, '0.01')}）")
    print()
    margin = (mid / price - Decimal(1)) if price != 0 else Decimal(0)
    print(f"中性情景相对当前价格：**{pct(margin)}**　"
          f"{'（有安全边际）' if margin > 0 else '（无安全边际，当前价已透支）'}")
    print()


# --------------------------------------------------------------- reverse DCF
def cmd_reverse_dcf(args):
    """给定当前价格与基准现金流，反解市场隐含的增长率。"""
    price = D(args.price)
    cf = D(args.cash_flow)          # 每股当期自由现金流 / 费用收入
    disc = D(args.discount)         # 折现率
    years = int(args.years)         # 高增长期年数
    term_g = D(args.terminal_growth)

    if disc <= term_g:
        raise SystemExit("❌ 折现率必须大于永续增长率")

    print("## 反向 DCF：当前价格隐含的增长预期")
    print()
    print(f"当前价格 **{fmt(price, '0.0001')} {args.currency}**　"
          f"当期每股现金流 **{fmt(cf, '0.0001')}**　"
          f"折现率 **{pct(disc)}**　高增长期 **{years} 年**　"
          f"永续增长 **{pct(term_g)}**")
    print()
    print("| 隐含年增速 | 现值合计 | 相对当前价 |")
    print("|-----------|---------|-----------|")

    best = None
    g = Decimal("-0.20")
    step = Decimal("0.001")   # 0.1pp 网格，使反解价格偏差通常 < 0.5%
    while g <= Decimal("1.50"):
        pv = Decimal(0)
        c = cf
        for t in range(1, years + 1):
            c = c * (Decimal(1) + g)
            pv += c / (Decimal(1) + disc) ** t
        terminal_cf = c * (Decimal(1) + term_g)
        tv = terminal_cf / (disc - term_g)
        pv += tv / (Decimal(1) + disc) ** years
        dev = rel_dev(pv, price)
        if best is None or dev < best[2]:
            best = (g, pv, dev)
        g += step

    g, pv, dev = best
    print(f"| **{pct(g)}** | {fmt(pv, '0.01')} {args.currency} | 偏差 {pct(dev)} |")
    print()
    print(f"> **解读**：以 {pct(disc)} 折现率、{years} 年高增长期、{pct(term_g)} 永续增长为假设，"
          f"当前价格 {fmt(price, '0.0001')} {args.currency} 隐含市场预期未来 {years} 年"
          f"每股现金流年增速约 **{pct(g)}**。")
    print("> 判断这个价格贵不贵，等价于判断这个增速能否兑现。")
    print()


def main():
    p = argparse.ArgumentParser(description="金融严谨性验算工具（Decimal 精确运算）")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("verify-market-cap", help="市值验算")
    a.add_argument("--price", required=True)
    a.add_argument("--shares", required=True)
    a.add_argument("--reported", required=True)
    a.add_argument("--currency", default="USD")
    a.add_argument("--tolerance", default=str(TOLERANCE_DEFAULT))
    a.set_defaults(func=cmd_verify_market_cap)

    b = sub.add_parser("cross-validate", help="多源交叉验证")
    b.add_argument("--field", required=True)
    b.add_argument("--values", required=True, help='JSON，如 \'{"来源A":123,"来源B":124}\'')
    b.add_argument("--unit", default="")
    b.add_argument("--tolerance", default=str(TOLERANCE_DEFAULT))
    b.set_defaults(func=cmd_cross_validate)

    c = sub.add_parser("verify-valuation", help="估值指标验算")
    c.add_argument("--price", required=True)
    c.add_argument("--eps")
    c.add_argument("--bvps")
    c.add_argument("--fcf-per-share")
    c.add_argument("--dividend")
    c.set_defaults(func=cmd_verify_valuation)

    d = sub.add_parser("three-scenario", help="三情景估值")
    d.add_argument("--price", required=True)
    d.add_argument("--eps", required=True, help="每股基准量（EPS 或每股费用收入等）")
    d.add_argument("--shares", help="（可选，仅用于展示）")
    d.add_argument("--growth", nargs=3, required=True, metavar=("乐观", "中性", "悲观"))
    d.add_argument("--pe", nargs=3, required=True, metavar=("乐观", "中性", "悲观"))
    d.add_argument("--years", default="3")
    d.add_argument("--currency", default="USD")
    d.set_defaults(func=cmd_three_scenario)

    e = sub.add_parser("reverse-dcf", help="反向 DCF")
    e.add_argument("--price", required=True)
    e.add_argument("--cash-flow", required=True, help="当期每股现金流/费用收入")
    e.add_argument("--discount", default="0.15")
    e.add_argument("--years", default="10")
    e.add_argument("--terminal-growth", default="0.03")
    e.add_argument("--currency", default="USD")
    e.set_defaults(func=cmd_reverse_dcf)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
