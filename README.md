![Caerus](Caerus_github.png)
# Caerus — 投資研究報告

> Caerus governs asymmetric opportunity and critical timing.

基於巴菲特、芒格、段永平、李錄四位投資大師方法論的系統化投資研究。

所有報告遵循三條原則：客觀（基於事實和數據，嚴禁主觀臆斷）、不預設立場（先擺數據、再推邏輯、最後得結論）、呈現正反兩面（每個核心判斷附帶反面論據）。

所有關鍵數據經多源交叉驗證，所有計算經精確十進位驗算，報告發布前須通過數據抽檢（偏差 ≤ 1%）。

## 报告列表

| 日期 | 公司 | 报告 | 核心结论 |
|---|---|---|---|
| 2026-07-12 | Meta Platforms (NASDAQ: META) | [Meta 投资研究报告](reports/Meta/Meta-research-20260712.md) | 觀望。多空雙方在爭論損益表的不同行——多方擁有收入行（+33% 且在加速），空方擁有現金流行與 2027-28 折舊行。兩邊都還沒被證偽 |
| 2026-07-12 | 美光科技 (NASDAQ: MU) | [美光投资研究报告](reports/美光/美光-research-20260712.md) | 迴避。一家管理良好的公司，一門平庸的生意，一個荒謬的價格。PB 10.98x vs 十年中位數 1.93x |
| 2026-07-12 | Churchill Capital Corp XI (NASDAQ: CCXI)<br>— 暨 Agility Robotics 借殼上市案 | [CCXI 投资研究报告](reports/CCXI-Agility/CCXI-research-20260712.md) | 強烈迴避。結論不依賴對人形機器人前景的判斷——股價相對信託價溢價 54.4%，發起人 promote 佔公眾股 33.3% 且無任何業績條件，最低現金條件形同虛設。Churchill 系列前 6 只 de-SPAC 中位數回報 −85% |
| 2026-07-30 | Snorkel AI（未上市） | [Snorkel AI 未上市公司研究報告](reports/snorkel-ai/snorkel-ai-private-20260730.md) | 迴避。用軟體公司的估值（$1.3B）做著已變成人力密集服務的生意。市面流傳的「$148M ARR」極可能是含專家薪酬穿透的總開票額，真實淨收入約 $70M，對應 18.6x EV/S。合理估值中樞 $1.05–1.15B |
| 2026-07-30 | Handshake AI（未上市） | [Handshake AI 未上市公司研究報告](reports/handshake-ai/handshake-ai-private-20260730.md) | 觀望。執行力頂級的一次性資產再利用，15 個月 0→$1.1B gross。但零 CAC 的院校圖譜優勢未轉化為任何溢價（take rate 31% vs Mercor 30%），且一手招聘數據顯示業務實質正下沉為廣譜職業人力池。合理估值 $4.0–5.0B |
| 2026-07-30 | Ether (ETH) | [Ether 投资研究報告](reports/Ether/Ether-research-20260730.md) | 迴避。以太坊贏得技術戰爭、輸掉經濟戰爭：Dencun 後使用量翻倍（日交易 +92%）而 L1 費用跌 91.4%，L2→L1 take rate 從 20.43% 壓縮至 0.49%，質押收益 94.7% 來自增發而非費用。但現金流僅能解釋市值的 2.75–11.85%，其餘為無法證偽的貨幣溢價 |

## 工具

`tools/financial_rigor.py` — 金融嚴謹性驗算工具。全程使用 Python `Decimal` 精確十進制運算，杜絕浮點誤差與 LLM 心算誤差。偏差閾值預設 1%，超出即打回。

```bash
python3 tools/financial_rigor.py verify-market-cap --price 1918.78 --shares 121884168 --reported 232000000000
python3 tools/financial_rigor.py cross-validate --field "營收" --values '{"來源A":123,"來源B":124}' --unit "億"
python3 tools/financial_rigor.py verify-valuation --price 100 --eps 5 --bvps 20 --fcf-per-share 4
python3 tools/financial_rigor.py three-scenario --price 100 --eps 5 --growth 0.20 0.10 -0.05 --pe 30 20 12 --years 3
python3 tools/financial_rigor.py reverse-dcf --price 100 --cash-flow 4 --discount 0.15 --years 10
```

輸出為可直接嵌入報告的 Markdown 表格。

## 免責聲明

本儲存庫內容僅為研究記錄與個人觀點，不構成任何投資建議。所有數據來源均已標註，但不保證其完整性與準確性。據此操作，風險自負。
