# Daversa Partners 研究报告
## ——行业结构 + 尽调笔记（非估值报告）

**研究日期**：2026-08-16
**研究模式**：**第一性原理模式（3 Agent），框架已重构**
**标注规范**：【事实】= 可溯源公开信息｜*【推理】* = 分析师推断
**置信度**：🟢 高（SEC/法院一手）｜🟡 中（单一可信源）｜🔴 低（推算/未证实）

---

## 0. 为什么这不是一份"未上市公司估值报告"

**Daversa Partners（法律实体：Resource Systems Group, Inc. t/a Daversa Partners）是一家 26 年历史、从未融资的合伙人制高管猎头公司**，不是风投支持的创业公司。

本研究框架的以下模块**在结构上不适用**——不是查不到，是**客观不存在**：

| 框架模块 | 为什么不适用 |
|---|---|
| 融资历史与估值演变 | **EDGAR 零申报**，无 Form D、无 cap table（🟢 已核实） |
| 最近融资估值法 / 优先清算权 / 反稀释条款 | 无优先股 |
| 退出路径（IPO / 二级转让） | 服务业主流是创始人套现或合伙人接盘 |
| 技术栈与专利护城河 | 资产是关系网与候选人数据库，不是技术 |
| App 数据 / MAU / DAU / ARR | 无产品 |

**硬套六维框架会产出四个空报告，并把"从未融资"误读成负面信号——而对一家健康的猎头公司，从不融资恰恰是常态。**

**因此本报告重构为**：① 用上市猎头公司财报反推单位经济与规模；② 法律与声誉风险专项；③ 行业结构与 AI 冲击。**它是一份行业结构 + 尽调笔记，不是估值报告。**

### 通道状态

| 通道 | 状态 |
|---|---|
| WebSearch | ❌ 配额耗尽（400/400） |
| DuckDuckGo HTML | ❌ 返回 202 机器人挑战，**本轮不可用** |
| **SEC EDGAR + Bash curl** | ✅ 主力通道 |
| **CourtListener REST API v4** | ✅ **本轮新解锁，免认证**（Justia 与 CourtListener 的 HTML 页均 Cloudflare 403，**必须走 API**） |
| `daversa.com` | ✅（`daversapartners.com` 301 跳转至此） |
| brightonparkcapital.com | ❌ 全站 Azure 404 + TLS 证书不匹配 |

---

## 1. 一句话结论

> Daversa 是一门**高毛利、零资本开支、但结构性天花板很低**的生意：推算收入 **$5,000 万–$1.4 亿**，天花板约 $1.5–2 亿收入。**这门生意的贝塔不是"猎头业"，是"美国 VC 部署额"。** 行业老二 Heidrick & Struggles 已于 2025-12 被 PE 以约 **6–8× EBITDA** 私有化——**这就是市场对"人走了资产就没了"的生意的定价判决**。叠加一起已和解但公开记录极不堪的联邦性骚扰诉讼，**对一家卖"我们懂人、我们公正"的公司构成持续性声誉负债**。

---

## 2. 公司画像（仅列已核实项）

| 项目 | 内容 | 置信度 |
|---|---|---|
| 品牌名 | Daversa Partners（官网已迁至 **daversa.com**） | 🟢 |
| **法律实体** | **Resource Systems Group, Inc. t/a Daversa Partners** | 🟢（法院文书抬头） |
| 成立时间 | **不晚于 2000 年**（有 Partner 简介称 "founding Partner since 2000"） | 🟡 |
| 创始人 / CEO | **Paul Daversa**（仍在任） | 🟢 |
| President | **Laura Kinder**（接班/分权信号） | 🟢 |
| 业务 | retained executive search，面向 VC 支持的科技公司 | 🟢 |
| 办公室 | 8 处：纽约 330 Madison、圣莫尼卡、旧金山、Waterford CT、Westport CT、奥兰多、迈阿密、伦敦 | 🟢 |
| 官网团队页人数 | **约 79 人**（Partner ~23、MD ~18、Director ~14；早期口径 59） | 🟡 |
| 客户 | OpenAI、Anduril、Palantir、Scale AI、CoreWeave、Cursor、Figma、Robinhood、Databricks、Snowflake、Nubank、Brex、Oura、Baseten、Chime、DoorDash、MrBeast | 🟢 |
| 官网展示的创始人关系 | Sam Altman、Tony Xu、Jimmy Donaldson、Palmer Luckey | 🟢 |
| **外部融资** | **无。EDGAR 零申报**（45 条全文命中全部是第三方提及） | 🟢 |
| 收入 / 费率 / placement 数 / 员工总数 | **官网零披露** | 🔴 |

---

## 3. 用上市猎头公司反推单位经济

### 3.1 一个改变对标基准的事件：HSII 已退市私有化

**Advent International + Corvex Private Equity 全现金收购 Heidrick & Struggles**（🟢）：

| 项 | 内容 |
|---|---|
| 对价 | **$59.00/股**，股权价值约 **$12–13 亿**，较 90 日 VWAP 溢价 **26%** |
| 时间线 | 2025-10-06 签约 → 2025-12-05 股东批准 → **2025-12-10 交割** → 2025-12-22 提交 Form 15-12G 注销登记 |
| 交易逻辑（8-K EX-99.1 原文） | "…return to private ownership, with **significantly more equity participation by current and future partners and leaders**… implement a **new equity plan for current and future partners**" |

**⚠️ 隐含倍数存在口径分歧**（两位分析师算出不同结果）：

| 分析师 | 净现金口径 | EBITDA 基准 | 隐含倍数 |
|---|---|---|---|
| 单位经济 | Q2'25 净现金 $2.11 亿 | FY24 实际 Adj EBITDA $1.112 亿 | **~8.3×** |
| 行业结构 | Q3'25 现金+证券 $5.28 亿 | FY25 估 $1.35–1.45 亿 | **~6×** |

> **裁定：约 6–8× EBITDA（EV/Revenue 约 0.7–0.9×）。无论取哪端，结论不变——行业老二被 PE 用个位数 EBITDA 倍数买走。**
>
> **一家 70 年历史、全球第二大的猎头公司，市场只肯给这个价。**

### 3.2 人均产能锚定（10-K 一手，🟢）

| 指标 | HSII（FY2024/12） | KFY（FY2026/04） |
|---|---|---|
| 总收入 | $11.157 亿（+7.0%） | $29.386 亿；fee revenue $29.075 亿（+6.5%） |
| **Executive Search 收入** | **$8.184 亿**（+4.9%） | **$9.241 亿**（+9.2%） |
| **创收顾问数** | **503 人（418 专注 ES）** | **ES 平均 563 人** |
| **人均产能** | **$1.96M/顾问** | **$1.64M/顾问** |
| 单笔搜索均价 | $149K（24Q3）→ **$162K（25Q3）** | ≈$142K（$9.241 亿 ÷ 6,500+ engagements） |
| ES 分部 EBITDA margin | 美洲 ES **31.3%** | **25.7%**（FY24 21.2% → FY26 25.7%） |
| **创收顾问 : 支持人员** | **1 : 4.4**（2,201 人 / 503 顾问） | **1 : 2.07** |

### 3.3 Daversa 收入推算：**$5,000 万–$1.4 亿**（两法仲裁后）

**两位分析师给出不同区间，根因有二**：

| 分析师 | 估算 | 团队页人数 | 创收人数 |
|---|---|---|---|
| 单位经济 | **$8,600 万–$1.42 亿** | **约 79**（实际重新抓取） | 55 |
| 行业结构 | **$5,000 万–$8,000 万** | 59（沿用早期口径） | 25–30（仅 Partner 级） |

**裁定：采用 $5,000 万–$1.4 亿的合并区间，中枢 $7,000 万–$1.1 亿。** 🔴

- **人数取 79 更可靠**（实际抓取 > 早期口径）
- **但"谁算创收"的分歧是真实的**——精品所的 Director 层常为交付而非开单，行业结构分析师的保守假设有道理
- **诚实的答案是：误差带压不到 ±30% 以内。**

**单位经济分析师的分层推算（透明展示）**：

| 层级 | 人数 | 低情形单产 | 高情形单产 | 低 | 高 |
|---|---|---|---|---|---|
| Partner 级（含 CEO/President） | 23 | $2.5M | $4.0M | $57.5M | $92.0M |
| Managing Director | 18 | $1.2M | $2.0M | $21.6M | $36.0M |
| Director | 14 | $0.5M | $1.0M | $7.0M | $14.0M |
| **合计** | **55** | | | **$86M** | **$142M** |

*交叉验算：55 × $1.6–2.4M = $88–132M，两法一致。*

**一个连带推论**：既然行业的创收顾问 : 支持人员是 **1:2 到 1:4.4**，**Daversa 官网列出的 79 人背后很可能还有一倍以上未列名的 associate/researcher——实际总人数远高于 79。**

### 3.4 商业模式：两条核心已被 10-K 证实

**HSII 10-K Item 1 原文**（🟢）：
> "our executive search services derive revenue through the fees generated for each search engagement, which generally are **based on the annual compensation for the placed executive**"
> "Retained executive search firms generally are compensated for their services **regardless of whether the client employs a candidate**"

**即"按薪酬比例计费"+"不问结果照收"两条成立。**

⚠️ **但"25–33%、分三期支付"这个广为流传的行业惯例，在 10-K 中未检索到任何字样**——属行业传闻而非可证事实（🟡）。

**经济性**：
- **好**：零资本开支（KFY 全年 capex 仅 $8,470 万，占收入 2.9%）、retainer 前置收现、ES 分部 EBITDA margin 25–31%
- **差**：**人即产能即成本**（HSII 美洲 ES 薪酬 $3.393 亿占该分部收入 61%）；顾问离职即带走收入；无经常性收入；**10-K 风险因素明说行业进入门槛极低**

### 3.5 VC 寒冬在财报上是可测量的（本报告最硬的一段，🟢）

**HSII Executive Search 分部收入（$M）**：

| 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|
| 868.8 | **901.9（峰）** | **780.0（−13.5%）** | 818.4（+4.9%，**仍低于 2022 峰值 9.3%**） |

其中**美洲 ES：$6.129 亿 → $5.230 亿，−14.7%**。

**KFY Executive Search fee revenue（$M）**：

| FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| **935.6（峰）** | 875.8 | **806.2（谷，−13.8%）** | 846.2 | **924.1（+9.2%）** |

HSII 2024 年计提 **$5,950 万减值**，经营利润塌到 $750 万（0.7%），次年被 PE 买走。

> *【推理】* **HSII 有金融 26%、工业 23% 的行业对冲，而 Daversa 是纯科技/VC 敞口。若 HSII 美洲 ES 寒冬跌 15%，纯科技精品所同期跌幅合理估计 25–40%，2023 年很可能出现绝对收入腰斩级波动。**
>
> **反过来，2024–2026 的 AI 融资超级周期对它是超额顺风。**
>
> **这门生意的贝塔不是"猎头业"，是"美国 VC 部署额"。**

---

## 4. AI 冲击：打在哪一环，剩下什么

### 4.1 两家上市公司在 10-K 里的自认（🟢，本轮要找的对应表述，找到了）

**HSII 10-K（FY2024）Item 1A**：
> "Our competitors may be further along in the development and design of technological solutions… **including solutions involving generative artificial intelligence**… We may also face increasing competitive pressure as a result of **our clients leveraging such technologies in-house to perform all or a portion of the services we offer in a manner that ultimately decreases the demand for our services, which could in turn require us to reduce our fees. There are limited barriers to entry into the search industry.**"

**KFY 10-K（FY2026）Item 1A 独立风险标题**：
> **"Technological advances may significantly disrupt the labor market and weaken demand for human capital at a rapid rate."**
> "…rapid changes in AI, such as with **generative and agentic AI**… demand for our services could be further reduced by **new competitors leveraging AI and other technologies to offer competitive services at lower costs and quicker turnaround, disrupting our business model.**"

另一处直接打在定价上：
> "The billing rates of our consultants… are also affected by… **the introduction of new technologies, such as generative and agentic AI, which may compete with or affect the pricing of our services.**"

> **这是猎头版的 DocuSign/Gartner 自白。** 但注意两点限定：**KFY 明确把风险圈定在 "lower-skill job categories"；HSII 担心的是客户自己用 AI 内做、并直言 "require us to reduce our fees"。管理层自己的判断是：AI 打的是量级招聘和费率，不是 C-suite 判断。**

### 4.2 价值链拆解

| 环节 | 传统壁垒 | AI 判断 |
|---|---|---|
| **Sourcing（找到人）** | 数据库 + 人脉名录 | **🔴 已商品化。** Juicebox 称 8 亿+ 档案、"1/10th LinkedIn Recruiter's cost"；SeekOut 10 亿+ 档案。**此环节价值趋零。** |
| **Screening（筛选）** | 经验判断 | **🟡 部分替代。** 结构化筛选可自动化；但高管评估是"低样本、高后果"判断，无标注数据可训 |
| **Persuasion（说服跳槽）** | 信任关系 | **🟢 AI 动不了。** 说服一位在职 CTO 离开上市公司，是**承担声誉背书的行为**，不是信息传递 |
| **Closing（谈成 offer）** | 谈判与人情 | **🟢 AI 动不了。** 涉及双向私密信息 |
| **客户获取（拿到委托）** | **VC 合伙人私交** | **🟢 AI 动不了——但这不是护城河，是人的资产** |

### 4.3 一个反直觉的短期悖论

| 指标 | HSII | KFY |
|---|---|---|
| ES 顾问人数 | 418 → **421**（几乎零增长） | 572 → **563**（微降） |
| 人均产能 | $2.0M → **$2.3M（+15%）** | — |
| 单笔搜索均价 | $149K → **$162K（+8.7%）** | — |
| ES EBITDA margin | — | 21.2% → **25.7%（+450bp）** |

> **AI 目前提升了在位者的利润——冲击尚未体现在损益表上，只体现在风险因素里。**
>
> *【推理】* **费率不降反升，因为客户付的从来不是 sourcing，是"这个人值得你信"的背书 + 失败的替换保证**（HSII 10-K 按 ASC 460 担保准则处理 replacement guarantee，🟢）。**AI 侵蚀的是成本端，红利暂时归了猎头自己——这正是 margin 扩张的来源。**
>
> **风险在于：一旦客户内部 talent team 用 Juicebox 类工具自建，25–33% 的费率就会被拆分定价。HSII 自己写了 "require us to reduce our fees"。**

### 4.4 我的假设被验证了，且有上市公司法定文件背书

我在派单中假设："说服跳槽与 VC 私交 AI 动不了——**但它们是人的资产，不是公司的资产**。"

**KFY FY2026 10-K 原文**（🟢）：
> "**a small number of consultants have primary responsibility for a client relationship. Because client responsibility is so concentrated, the loss of key consultants may lead to the loss of client relationships.** … This risk is heightened due to the **general portability of a consultant's business**"

**HSII 前瞻性声明风险清单第二条**（🟢）：
> "our ability to **prevent our consultants from taking our clients with them** to another firm"

> **两家上市公司在法定文件里承认：客户关系属于顾问个人，可携带。这是"人的资产不是公司的资产"的第三方证明。**
>
> **反证也在同一份文件：KFY 前六位顾问仅贡献约 3% 总 fee revenue，前十位约 4%——规模化恰恰是靠稀释单点依赖。一家 79 人的机构没有这个稀释，Daversa 的集中度必然高一个数量级。**
>
> **而 Advent 收购 HSII 后的第一个动作，是 "a new equity plan for current and future partners"——PE 也知道买的是人，必须用股权拴住。**

### 4.5 AI 原生招聘公司扫描（全部经官网核实，🟡 融资数字均为公司自述）

| 公司 | 定位 | 融资 | 是否切入高管猎头 |
|---|---|---|---|
| **Mercor** | AI 实验室专家标注/评测劳动力市场 | $350M C 轮 @ $100 亿估值（2025-10，公司 blog 转引 CNBC） | **否** |
| **Juicebox / PeopleGPT** | AI sourcing SaaS，8 亿档案 | 官网称 "raised $116 million"；2025-09 达 $10M ARR | 否 |
| **SeekOut** | Agentic sourcing + 托管招聘（称比传统 agency 便宜约 70%） | 官网称累计 >$189M | 否 |
| **Hunt Club** | **retained executive search，明确面向 VC/PE 支持成长期公司**；官网："Our AI models map who's in our network…" | 未检索到 | **是——唯一直接对手** |
| Paraform | 独立招聘人 marketplace + AI agents | 未检索到 | 否 |

> **巨额资本全部涌向 sourcing 与量级招聘，几乎无人正面攻击 C-suite retained search。Hunt Club 是唯一验证到的、与 Daversa 定位重叠的 AI-enabled 玩家。**
>
> ⚠️ **而这恰恰是最大的盲区之一——唯一的正面竞争威胁，是我们看不见融资与规模的那一个。**

---

## 5. 法律与声誉风险专项

### ⚠️ 必须先明确的三条边界

1. **案件以和解结案，从未有任何责任认定。** 2023-08-25 以 **Rule 41(a)(1)(A)(ii) 双方合意撤诉（有既判力）**，发生在陪审团开庭前 17 天。**未检索到和解金额**（该撤诉形式不披露金额）。
2. 下文所述"被告不争执"的事实，**是简易判决阶段为程序目的的不争执，不等于承认**，也从未经陪审团认定。
3. **被指控的个人 Bruce Brown 已于 2020-12 离职**，且于 2022-02 前与原告**单独和解**并被移出本案。

### 5.1 Feighan v. Resource Systems Group Inc.（D.D.C. 1:20-cv-03759）

**案件性质**（🟢，三份判决书原文经 CourtListener API 取 PDF 后提取）：

**不是**种族或年龄歧视——**是员工被主管性骚扰 + 基于性取向的敌意工作环境**。

| 项 | 内容 |
|---|---|
| 原告 | **Vaughn Feighan**，2019-07 至 2020-07（11 个月）任 DC 办公室 recruiter，**大学毕业第一份工作，起薪 $55,000**；任内交付 9 个高管职位 |
| 被告二 | **Bruce Brown**，1999–2020 年任合伙人兼 DC 办公室 Managing Partner，公司最高创收合伙人之一，**与 Paul Daversa 私交逾 20 年** |
| 主审 | 首席法官 **Beryl Howell** |
| 诉因 | Amended Complaint 共 9 项：DCHRA 敌意工作环境与报复、DC 工资支付法、殴击、故意造成精神损害、疏于监管 |

**三份判决的裁决**（🟢）：

| 日期 | 裁决 |
|---|---|
| 2021-02-25 | 驳回原告发回州法院动议；**指出原告未满足匿名起诉门槛，须实名**——这是 Doe → Feighan 改名的原因，**非对实体问题的评价** |
| 2023-03-30 | 简易判决**部分准许、部分驳回**。**存续进入审判**：DCHRA 敌意工作环境、疏于监管、DCWPCL、IIED。**判给被告**：替代责任下的 battery、Count IX 报复索赔 |
| 2023-07-19 | 审前裁定；审判定于 **2023-09-11** 开庭 |

**结案方式**（🟢）：2023-08-25 **ECF 102 被告方提交 Stipulation of Dismissal with Prejudice**，同日法院依 Rule 41(a)(1)(A)(ii) 以有既判力驳回结案（docket 终结 2023-08-28）。**这是双方合意撤诉的标准和解形式。**

另有一笔独立和解：原告与 **Bruce Brown 个人于 2022-02-08 前和解**，Brown 被有既判力移出本案；**法院明令和解金额须对陪审团隐藏**——金额同样未披露。

### 5.2 "对原告父亲采取法律行动"的线索：属实，但性质与传闻不同（🟢）

准确事实链：
1. 原告把父亲 Robert Feighan 列为知情证人
2. 被告向父亲的公司发出传票；父亲 2021-08 在 D. Conn.（3:21-mc-00061）提出撤销传票动议，后撤回并出庭作证
3. 期间**被告律师向父亲律师表示，将利用本案开示程序构建对父亲的"违反受信义务"主张**（被告**否认**说过）
4. 原告据此增列 Count IX 报复索赔；**法院判被告胜**（依 *Gaujacq* 标准，该表述"简短、转瞬、无修饰"，不足以构成实质不利行为）
5. **从未有任何针对父亲的诉讼被实际提起**

> **定性：这是诉讼战术层面的攻击性行为，不是行业人际报复。**
>
> **但 Howell 法官在判决中写下：该类行为"可被视为恐吓证人、越过职业伦理红线，甚至更糟"（引 D.C. 职业行为规则 8.4(d)）。这句 dicta 是可引用的独立声誉负债。**

### 5.3 Osherow v. Daversa Partners（Bankr. W.D. Tex. 21-05027）

- 原告：**Randolph Osherow**，Legendary Field Exhibitions / AAF（美式橄榄球联盟）Chapter 7 破产受托人
- 母案案由代码含 **13 = §548 欺诈性转移追回**
- 2021-03-26 立案，**2021-07-15 出判决**，2021-08-26 结案
- 🔴 **诉状与判决 PDF 在 RECAP 中均 `is_available: false`——是否追回猎头费、金额、判决类型全部无法确认**

> *【推理】* 仅 4 个月即出判决，符合"默认判决或快速合意"形态，但这是推测。**若确为追回猎头费，反映的是客户信用风险而非不当行为——猎头费在客户破产时可依 §548 被倒追。**

### 5.4 其他诉讼扫描

CourtListener 全库检索 "Daversa" 与 "Resource Systems Group"：**联邦层面仅上述两案 + D. Conn. 撤销传票附属程序**。其余为同名自然人或噪声。

- `Hilton v. Resource Systems Group`（N.D. Cal. 2023）🔴 **无法确认被告是否为本公司**——"Resource Systems Group" 亦是佛蒙特一家交通咨询公司。**待核，未采信。**
- **off-limits 条款违反、挖角客户、竞业禁止、合伙人出走、客户欠费、候选人隐私：均未检索到**

> ⚠️ **重要方法论提醒：此类纠纷在猎头业通常走 AAA/JAMS 保密仲裁或州法院，联邦数据库天然看不见——"未检索到"不等于"不存在"。**

### 5.5 风险定性

> **杀伤力不在判决（没有判决），在判决书的公开文本。**
>
> 三份首席法官署名的联邦判决永久公开。**对一家卖"我们懂人、我们公正"的猎头公司而言，最致命的不是被诉，而是这些文字可被任何客户 CHRO、任何候选人、任何竞争对手在 30 秒内检索到**——尤其当卖点是高管人品判断力时。

**缓释因素**：加害者已离职并单独和解；公司选择开庭前付费和解，避免了陪审团裁决与惩罚性赔偿的媒体化。

**Paul Daversa 个人**：从未作为个人被告承担责任，但**深度出现在事实记录中**（被取证作证、是申诉委员会成员、2020-05 收到员工关于 Brown 的报告邮件后未作进一步追问——此为法院对记录的表述）。

> **结论：属"CEO 事实卷入型"关键人风险，非个人法律责任风险。在任何以他为核心的客户 reference 或尽调访谈中，这段记录会被问到。**

**法律与声誉风险评级：★★★☆☆（3/5）**。无败诉、无监管处分、无系列诉讼模式；但公开判决文本构成持续性、可检索的声誉负债。**若发现保密仲裁中存在同类案件，应上调至 ★4。**

---

## 6. TAM 与天花板

### 6.1 正确的 TAM 锚（拒绝分母欺诈）

不能用"全球招聘市场 $5000 亿"。自下而上：

```
单笔 retained 高管搜索均价 = $162K（HSII 实际值，2025Q3，🟢）
顶级 VC 圈 C-level 单价更高 → 取 $250–400K

美国 VC 支持公司每年新增 C 级/VP 级 retained 搜索：
Series B 及以上活跃公司约 3,000–5,000 家 × 年均 1–1.5 个 retained 高管岗
≈ 4,000–6,000 笔/年

TAM ≈ 4,000–6,000 × $250K ≈ $10–15 亿/年
```

**交叉校验**（🟢）：**HSII Executive Search Americas 全行业全客户收入仅 $5.569 亿（2024）；KFY ES North America $5.834 亿（FY26）。两大全球龙头在整个北美的高管搜索合计约 $11 亿。**

> *一个 $10–15 亿的 VC 细分 TAM 与两大龙头的北美全行业收入同量级，说明该推算上限偏乐观；**更审慎的锚是 $6–10 亿**。*

### 6.2 天花板判断

- 按人均产能推算，Daversa 当前收入 **$5,000 万–$1.4 亿**
- *即使做到 VC 细分 TAM 的 20–25% 份额（已是极限统治力），**天花板约 $1.5–2 亿收入***
- **结构性天花板**：TAM 与 VC 投资额同频；**无订阅收入层**——对比 KFY Digital 分部（$3.635 亿收入 / 31% margin，含 $1.486 亿订阅收入），**那才是 KFY 值 9× 而非 6× 的原因。Daversa 没有这一层。**

### 6.3 这门生意值多少钱（按服务业标准，非 VC 式估值）

**锚点**（🟢）：
- KFY：EV/Revenue **1.29×**，**EV/EBITDA 9.08×**，P/E 16.1
- HSII 私有化成交：**约 6–8× EBITDA，EV/Revenue 约 0.7–0.9×**
- 先例并购区间（BofA 于 DEFM14A 采用）：**8.0–11.0× EV/LTM Adj EBITDA**
- HSII DCF 终值倍数：**6.0–8.0×**，WACC 10–12%

**私有精品所折价**：流动性、规模、**关键人依赖**、单一垂直周期性——合计 **35–50%**。

> **条件式结论：若归一化 EBITDA（合伙人取市场化薪酬后）为收入的 15–25%，即 $1,000 万–3,500 万，按 4.0–5.5× 计，企业价值约 $4,000 万–$1.9 亿。**
>
> ⚠️ **但精品猎头的真实交易结构从来不是一次性倍数，而是 earn-out + 顾问留任绑定**——HSII 交易中 Advent 明确要求 "Post-Closing Equity Plan"，并把**核心顾问的反应视为交易成败关键**（DEFM14A "Background of the Merger"）。

**经济性评级：★★★☆☆（3/5）**——毛利极高、零资本、现金前置；但无经常性收入、人力即产能、贝塔完全绑定 VC 周期、行业进入门槛低（KFY 10-K 原文）。

---

## 7. 终局与创始人的个人安排

### 7.1 精品猎头的历史归宿

1. **PE 收购**——先例就是本轮最大数据点：**Advent + Corvex 收 HSII，约 6–8× EBITDA，26% 溢价，2025-12-10 交割**（🟢）。**行业老二的归宿就是 PE + 合伙人股权计划。**
   - ⚠️ EDGAR 8-K 全文检索（"executive search firm" + "purchase price"，2018–2026，26 条命中）**全部为无关误命中，未检索到任何已披露的精品猎头并购倍数**（🟢）——**检索为空本身也是结论：这类交易规模低于 8-K 重大性门槛。**
2. **合伙人分家**——KFY/HSII 均在 10-K 承认 "portability of a consultant's business"
3. **创始人套现**

### 7.2 ⭐ Paul Daversa 的个人流动性安排——EDGAR 找到直接证据

| 项 | 内容 | 置信度 |
|---|---|---|
| 实体 | **Tidal Wave Ventures, LLC**（CIK 1887172） | 🟢 |
| 注册地 | Westport CT **55 Greens Farms Road——与 Daversa 同址** | 🟢 |
| 性质 | 2021 年设立的特拉华 LLC，Form D 申报类型 **Pooled Investment Fund / Hedge Fund** | 🟢 |
| Paul Daversa 角色 | 列名 **Executive Officer**，"MANAGER OF DP EQUITY INVESTMENTS LLC, THE ISSUER'S MANAGER" | 🟢 |
| **累计募集额** | **2021-10 首次 $75 万 → 2025-09-26 最新 D/A $1,530 万，五年增长 20 倍** | 🟢 |

> *【推理】* **他在把"看见每一家顶级 VC 支持公司最早期信号"的信息优势，转化为自己的股权敞口。Daversa Partners 是现金流与信息源，Tidal Wave 是终局。**
>
> **对一家没有 VC 退出路径的合伙人制公司，创始人的个人资本安排就是最重要的"退出信号"。**

⚠️ **Brighton Park Capital "Senior Advisor" 头衔：未能证实**——brightonparkcapital.com 全站返回 Azure 404 且 TLS 证书不匹配（`*.azurewebsites.net`），/team 与 /people 均 404，**无法证实或证伪**。

---

## 8. 综合判断

### 行业吸引力：★★☆☆☆（2/5）

低增长（KFY ES 四年 CAGR ≈ −0.3%）、高周期性、无递延收入、人力资产可携带、**市场只肯给 6–9× EBITDA**。

### AI 冲击的明确判断

- **打在 Sourcing（已归零）与 Screening 下半段，以及费率的长期议价权**（HSII 亲口："require us to reduce our fees"）
- **剩下的是**：Persuasion + Closing + 客户获取——三者共同的本质是**声誉承担与信任**，AI 结构性无法提供
- **短期悖论**：AI 目前**提升**了在位者利润。**冲击尚未体现在损益表上，只体现在风险因素里。**

### 三条主要风险

| 风险 | 严重度 | 说明 |
|---|---|---|
| **VC 周期同频** | ★★★★★ | 纯科技敞口，无行业对冲；2023 年寒冬对纯科技精品所的冲击应显著大于 HSII 的 −14.7% |
| **关键人依赖** | ★★★★☆ | 客户关系属顾问个人且可携带（两家 10-K 均承认）；79 人机构无 KFY 那样的稀释 |
| **声誉负债（可检索的公开判决文本）** | ★★★☆☆ | 已和解无责任认定，但文本永久公开，且直接触及 CEO 与公司文化 |

---

## 9. 信息盲区地图

| 缺失项 | 影响 | 获取路径 |
|---|---|---|
| **合伙人分成结构与实际 take-home vs 公司留存 EBITDA**（最致命） | **合伙制专业服务公司可以把 EBITDA 做到 0 也可以做到 30%，完全取决于分配政策——不解开这一点，任何估值都是空中楼阁** | 仅尽调可得 |
| 单笔 fee 绝对值与年度 placement 数量 | 二者缺一，收入推算误差带压不到 ±20% 以内 | 未披露 |
| Osherow §548 追回案的标的、金额与判决 | 是否有大额猎头费被倒追，完全未知 | RECAP PDF 不可得 |
| **保密仲裁与州法院纠纷** | off-limits 违约、合伙人出走、竞业禁止在联邦库天然不可见 | 结构性不可得 |
| 两起和解的金额、保密条款、是否有保险承担 | 财务影响未知 | 不披露 |
| Hunt Club 的融资与规模 | **唯一的正面竞争威胁，恰恰看不见** | 需搜索通道 |
| 诉讼对顶级客户关系的实际影响 | 无任何可观察证据 | 新闻通道不可用 |
| HSII 退市后的行业数据 | **行业半壁江山的一手数据自 2025Q3 起永久断流**，未来只剩 KFY 单一样本 | 结构性 |

**结论置信度声明**：
- **不受盲区影响的硬结论**（🟢）：HSII 私有化及其倍数；HSII/KFY 人均产能与 ES 收入曲线；两家 10-K 的 AI 自认与"顾问可携带"自认；三份 Feighan 判决的内容与结案方式；Tidal Wave Ventures 的 Form D 记录；Daversa EDGAR 零申报。
- **收入推算置信度约 40%**（区间宽达 $5,000 万–$1.4 亿）；**"这门生意的贝塔是 VC 部署额"约 85%**；**"AI 打在 sourcing 而非 persuasion"约 80%**。

---

## 10. 持续跟踪清单

| 事项 | 频率 | 来源 | 预警阈值 |
|---|---|---|---|
| **KFY ES 分部收入与顾问数** | 季 | SEC EDGAR | 转负 → 周期见顶 |
| KFY 单笔 fee / 人均产能 | 季 | 10-Q | 下滑 → 费率议价权开始流失 |
| **Tidal Wave Ventures 的 Form D 增量** | 半年 | EDGAR CIK 1887172 | 快速扩张 → 创始人重心转移 |
| Daversa 官网 `/team` 人数与合伙人名单 | 季 | daversa.com/team | 合伙人流失 → 关键人风险兑现 |
| 新增诉讼 | 季 | CourtListener API | 第三起同类 → 声誉评级上调至 ★4 |
| Hunt Club 等 AI-enabled 竞品动向 | 半年 | 需搜索通道 | 拿到顶级 VC 客户 → 正面竞争成真 |
| 美国 VC 部署额 | 季 | 公开数据 | 大幅下滑 → 收入直接同频承压 |

---

## 11. 总结

**这门生意的本质**：Daversa 把"认识谁、以及能说服谁"卖给风投支持的科技公司，按被安置高管首年薪酬的比例收费，且不问结果照收。**它是一门高毛利、零资本开支、现金前置的好生意——但它的产能就是它的人，它的人可以带着客户走，而它的需求曲线与美国 VC 部署额完全同频。**

**规模判断**：推算收入 **$5,000 万–$1.4 亿**（误差带宽，因为团队构成与创收人数的口径存在真实分歧）；**天花板约 $1.5–2 亿收入**，受制于一个 $6–10 亿的 VC 细分 TAM。

**估值判断**：**这不是一份估值报告，但可以给一个条件式区间**——若归一化 EBITDA 为收入的 15–25%，按 4.0–5.5× 计，企业价值约 **$4,000 万–$1.9 亿**。**而最大的不确定性不在市场，在合伙人分成政策：合伙制公司的 EBITDA 是被分配政策决定的，不是被生意决定的。**

**最大的确定性**：**行业已经给出了定价判决。** 全球第二大猎头 Heidrick & Struggles，70 年历史，2025-12 被 PE 以约 6–8× EBITDA 私有化退市。而 PE 接手后的第一个动作，是给合伙人发股权——**因为所有人都知道，买的是人。**

**最大的不确定性**：**AI 冲击的时滞。** 两家上市公司都在 10-K 里承认了威胁（"require us to reduce our fees"、"disrupting our business model"），但**当期数据显示 AI 正在提升它们的利润**——顾问数持平、人均产能 +15%、单笔均价 +8.7%、margin +450bp。**冲击写在风险因素里，红利记在损益表上。这个背离能维持多久，是这门生意未来五年最重要的问题。**

---

### 附录：研究方法、更正与局限

**框架重构**：本报告放弃了六维未上市公司框架，改为"行业结构 + 尽调笔记"。原因见第 0 节——这是一家从未融资的专业服务公司，六个模块客观不存在。

**两处对我派单内容的更正**：
1. **官网团队页人数**：我派单时用的 59 人已过时，实际重新抓取为**约 79 人**。
2. **Brighton Park Capital "Senior Advisor" 头衔**：我在派单中引用了这条（来自侦察阶段），**核实时发现该公司官网全站失效，无法证实或证伪**。报告中已标为未核实。

**一处对侦察兵的补充与修正**：侦察兵把 Springer 式的"IPO 专业户"框架用在了 Daversa 上不适用；而它发现的两起诉讼线索经深挖后，**案件性质与初步描述不同**（是性骚扰/性取向敌意工作环境，非种族或年龄歧视），且**"对原告父亲采取法律行动"是诉讼战术而非行业报复**。

**方法论收获**：
- **CourtListener REST API v4 免认证可用**——这是研究私营公司法律风险的高价值通道。变通要点：`/dockets/{id}/` 需认证，但 `/search/?type=r&q=docket_id:XXXX` 免认证；`/opinions/{id}/` 的 `plain_text` 常为空，需取 `local_path` 从 storage 下载 PDF 后本地提取。
- **EDGAR 全文检索可用于查私营公司在他人财报中的提及**——本案借此确认了 Daversa 被 Hershey、Robinhood、Upbound 的 DEF 14A 列为聘用猎头。

**主要局限**：
1. WebSearch 全程不可用；**DuckDuckGo 本轮返回 202 机器人挑战，完全不可用**。
2. Daversa 自身财务零披露，收入为纯推算，误差带宽达 ±40%。
3. **HSII 退市后行业一手数据永久断流**，未来只剩 KFY 单一样本。
4. 保密仲裁与州法院纠纷结构性不可见。
5. 全程未执行中文检索。
