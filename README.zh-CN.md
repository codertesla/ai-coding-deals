# AI 编程工具定价与省钱指南

> 持续核实 30+ 款 AI 编程 IDE、CLI 终端代理与大模型 API 的订阅价格、免费额度、邀请返利、教育优惠及 BYOK 零成本方案。

**[English](README.md) · [简体中文](README.zh-CN.md)**

[![GitHub stars](https://img.shields.io/github/stars/codertesla/ai-coding-deals?style=social)](https://github.com/codertesla/ai-coding-deals/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/codertesla/ai-coding-deals)](https://github.com/codertesla/ai-coding-deals/commits)
[![Contributors](https://img.shields.io/github/contributors/codertesla/ai-coding-deals)](https://github.com/codertesla/ai-coding-deals/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/codertesla/ai-coding-deals)](https://github.com/codertesla/ai-coding-deals/issues)
![收录工具](https://img.shields.io/badge/收录工具-30+-blue)
![最后核实](https://img.shields.io/badge/最后核实-2026--11-brightgreen)
[![欢迎PR](https://img.shields.io/badge/PR-欢迎-orange)](CONTRIBUTING.md)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

**[精选方案](#-精选高性价比方案与免费额度) · [零元方案](#-零成本-ai-编程方案0--byok) · [原生 IDE](#-agentic-ide-价格与配额对比) · [编程插件](#-vs-code-与-jetbrains-编程插件) · [终端代理](#-cli-与终端编程-agent) · [限时促销](#-限时优惠与截止日历) · [教育优惠](#-学生与教育专属免费权益edu) · [选型矩阵](#-ai-编程工具选型与决策矩阵) · [省钱策略](#-7-条-ai-编程算力省钱法则) · [信息来源](#-信息来源与核实记录)**

AI 编程工具的订阅档位、积分倍率与免费配额几乎每月都在变动。本仓库对照各厂商官方文档，横向拉通 **Cursor、Claude Code、GitHub Copilot、Cline、OpenCode、Devin、Google Antigravity、Kiro、DeepSeek V4.1 Flash、Kimi K3** 等主流工具的**实时定价、免费层限流规则、邀请金、学生包及开源 BYOK 低价调用路径**（最近全量核实：**2026 年 11 月**）。

## 精选高性价比方案与免费额度

按「单价产出比」由高到低排列。已下线、暂停注册或仅面向企业的方案已移出本表，归档于下方对应分类章节。

> [!TIP]
> **DeepSeek-V4.1-Flash（2026-09-10 正式上线；当前实际服务快照为 V4.1-Flash-1017）：** 原生多模态。**两个入口的模型 ID 不同，不能混用：**
> - **DeepSeek 官方 API：** `deepseek-flash`（base `https://api.deepseek.com`）。旧名 `deepseek-v4-flash` 与 `deepseek-v4-flash-vision-exp` 仍可调用，但对应模型已退役，请求由 V4.1-Flash-1017 承接并按 Flash 价计费。
> - **OpenCode Go：** `deepseek-v4.1-flash`（base `https://opencode.ai/inference/go/openai/v1/...`）。官方名 `deepseek-flash` 不是该端点的模型 ID。
>
> 官方**非高峰**单价（每百万 Tokens）：Flash **输入 $0.15 / 输出 $0.60 / 缓存命中 $0.003**；DeepSeek V4 Pro **$0.66 / $1.98 / $0.022**。高峰为 2×（周一至周五 UTC 01:00–04:00 与 06:00–10:00，**中国法定节假日除外**）。Search 与 Fetch API 自 2026-11-01（北京时间）起按 **$0.75 / 千次**计费，此前免费。**当前成本最低的两条接入路径：**
> 1. **Freebuff（免费）：** 广告支持的 CLI / Web / Desktop 编程 Agent，免 API Key 直接调用。
> 2. **OpenCode Go（$10/月）：** DeepSeek V4.1 Flash 在 Go 档享常驻 **$100/月额度**（Go Plus 为 **$200**）——无促销代号，也无截止日期。

| 工具 | 当前方案与额度规则 | 选型判断 |
|------|--------------------|----------|
| **OpenCode Go** *（已核实）* | **Go：$10/月一口价**——首月 $5 活动已于 2026-08-24 结束，现仅此一档。通过[邀请链接](https://opencode.ai/go?ref=J9E8732NMP)订阅后双方各得 **$5 Go 用量**。Go 端模型 ID 为 **`deepseek-v4.1-flash`**。**DeepSeek V4.1 Flash 月额度 $100**（5 小时窗口 $20、每周 $50），按官方高/非高峰单价计费；DeepSeek V4 Pro 月额度 $15。档位：**Go Plus $40/月**（额度 2×）、**Go Teams $20/席/月**。触顶后自动回落免费模型（Beam Free、Iceman Contributor Free）；开启 Extra Usage 则回落按量余额。另含 Grok 4.7、Kimi K3 与 K3.1 Pro、GLM-5.3 / 5.3-Flash、Qwen3.8 Max/Flash、MiniMax M3、GPT 6 Luna、Claude Haiku 5.5、Gemini 4 Argon 等约 30 款模型。 | **付费调用 DeepSeek V4.1 Flash 的最高性价比方案**：$100 额度、与官方一致的 Token 单价，外加可移植 API Key。 |
| **Freebuff** *（已核实）* | **免费编程 Agent**（广告支持，官网标价 **€0**；覆盖 CLI / Web / Chat / Desktop 及移动端——Android 已上线，iOS 即将支持），官网 [freebuff.com](https://freebuff.com/)（[Web 邀请链接](https://freebuff.com/web/?ref=ref-b3046190-1d77-44c1-915c-b71b4f36ae5e)）。免绑卡、免配 API Key，内置 DeepSeek Flash/Pro（旧 V4 ID 上游已直连 **V4.1 Flash**）、Kimi、MiniMax。高频会话触发日限额后自动降级至轻量模型。 | **零成本体验 DeepSeek V4.1 Flash 的首选通道**；一行 `npm install -g freebuff` 即可启动终端 Agent。 |
| **CodeBuddy / WorkBuddy** *（腾讯国内站，已核实）* | 通过 [WorkBuddy 邀请链接](https://www.workbuddy.cn/events/invite?inviteCode=qm4gyc1daqn)（微信登录）注册立得 **2,000 积分**新用户礼包（有效期 1 个月）。叠加站内新手任务后，官方与社区宣传口径为最高累计 **3,600 积分**（约为标准版首月 4,000 积分的 90%）——**超出礼包的 1,600 积分并未在邀请页逐项列明，请按上限理解而非承诺**。注册后 30 天内首次付费升级个人版，双方再各得 **500 积分**（有效期 6 个月）。DeepSeek 官方合作伙伴，已接入 **V4.1 Flash** 与 **Kimi K3**（消耗倍率约 1.62×）。*（HY3 全员免费期已于 2026-07-22 结束。）* | **国内新用户赠送额度最厚的原生 IDE**；零成本实测 **Kimi K3** 与 **DeepSeek V4.1 Flash** 优先走这条。 |
| **腾讯云 AI 模型广场** *（已核实）* | 新用户进入[模型广场](https://curl.qcloud.com/PN0cvBnI)右上角点击「**新用户福利免费体验**」，**全部语言模型与多模态模型各赠 100 万 Token**，领取后 **90 天有效**（覆盖 HY3、GLM、DeepSeek、Kimi Code 等）；混元 **HY3** 另有 **Hy Token Plan**（**¥28/月包 3,500 万 Token**）。 | **国内开源 BYOK 客户端的首选低成本 API 底座**；一张 Key 即可在 Aider、Cline、Continue 中切换多款旗舰模型。 |
| **OpenAI Codex** | **ChatGPT 免费版直接内置**，覆盖 Web、CLI 与 **macOS / Windows 桌面端**，无需绑定信用卡。 | **零门槛启用 OpenAI 官方编程工作流**；已有 ChatGPT 免费账号即可开箱即用。 |
| **Google Antigravity / Gemini** | 提供高配额**免费层**（行内 Tab 补全完全免费）；升级 **Google AI Pro** 仅需 **$19.99/月**。 | **全栈 Web 开发体验最完整的免费层**，原生打通多 Agent 并行执行与内置浏览器沙箱调试。 |
| **Grok / SuperGrok** *（xAI，已核实）* | 在 [grok.com/plans](https://grok.com/plans) 开通 **SuperGrok 7 天免费试用**，完整解锁 **Grok 4.5+** 与终端编程代理 **Grok Build** 的付费额度。需绑信用卡，第 7 天前取消不扣费，逾期按 **$30/月** 自动续费（仅限首次订阅账号）。 | **7 天零成本压测 Grok 4.5+ 与终端 Agent 的窗口**；记得在试用期结束前取消订阅。 |
| **Cline (ClinePass)** *（已核实）* | **ClinePass：$9.99/月**（[cline.bot/cline-pass](https://cline.bot/cline-pass)），打包 **GLM 5.3 Flash / 5.3 / 5.2**、**Kimi K3**、Kimi K2.7 Code / K2.6、**DeepSeek V4 Pro / V4 Flash**、MiniMax M3、MiMo V2.5、Qwen3.7-Max / 3.7-Plus / 3.8-Max，通用于 Cline IDE 插件、CLI 与桌面端。该订阅在 Cline 内生效，无需另行管理厂商 Key。*（早期 $1.99 首发价已下线，以结账页实时标价为准。）* | **固定 $9.99/月畅用主流开源权重编程模型**，直接集成在自主性极强的 Cline 代理框架内。 |
| **Cursor** | 已并入 **The X Subscription**（Grok、Cursor、X 合一订阅）。现行档位：**Plus $8/月 · Premium $30/月 · Super $100/月 · Ultra $200/月**；团队 **$30 / $100 / $200 每席**；年付 **$80 / $300 / $1,000 / $2,000**。旧版 Cursor 套餐（Pro $20、Pro+ $60、Teams Standard $40）**已对新用户关闭**，存量用户维持原价。Plus 仅限 Grok 系列模型；第三方模型需 Premium 及以上，按 API 目录价从预付额度扣费。 | **多模型协同与交互响应的标杆 Agentic IDE**；老 Pro 用户切换档位前需重算额度。 |

> **订阅计费规律：** 主流商业 AI 编程工具从月付切换为年付，通常可直接减免 **15%–20%** 账单成本。发现新折扣或价格调整？欢迎[提交 Pull Request](CONTRIBUTING.md)。

## 零成本 AI 编程方案（$0 / BYOK）

不花一分钱软件订阅费，可以通过以下 7 条路径搭建完整的 AI 编程工作流：

- **免 Key 广告支持全免费 Agent：** [Freebuff](https://freebuff.com/) 提供 CLI（`npm install -g freebuff`）、Web、Desktop 与 Chat 全端支持，免绑卡直连 **DeepSeek V4.1 Flash**、Kimi 与 MiniMax。（由 [Codebuff](https://www.codebuff.com) 团队出品，作为独立免费产品线运营。）
- **开源客户端 + 本地模型（$0 纯本地）：** 使用 [Aider](https://aider.chat)、[Continue.dev](https://www.continue.dev)、[Cline](https://cline.bot) 或 [OpenCode](https://opencode.ai) 接入本地 Ollama 模型，软件与算力成本均为 $0，代码完全不出本机。
- **既有免费账号直接复用：** [OpenAI Codex](https://openai.com/codex)（ChatGPT 免费版与 Plus 直接内置）、[GitHub Copilot Free](https://github.com/features/copilot)（每月 2,000 次代码补全）。
- **大厂 IDE 高配额免费层：** [Google Antigravity](https://antigravity.google)（行内 Tab 补全免费 + 每 5 小时重置 Agent 算力池）、[Cursor](https://cursor.com)（Free 档，限量）。
- **免费 OpenAI 兼容推理接口（NVIDIA NIM）：** [NVIDIA NIM](https://build.nvidia.com/)（`base_url="https://integrate.api.nvidia.com/v1"`）凭单个 API Key 即可调用庞大的[开源模型目录](https://build.nvidia.com/models)，速率上限约 40 RPM（注册需手机验证码，适合原型开发与横向评测，无生产 SLA）。**社区实测首选模型：** `nvidia/nemotron-3-super-120b-a12b`，响应快且 `message.content` 输出稳定。
- **腾讯云 90 天百万 Token 体验池：** 新用户在[腾讯云 AI 模型广场](https://curl.qcloud.com/PN0cvBnI)右上角领取福利后，每款语言模型与多模态模型均获 **100 万免费 Token**（有效期 90 天）；混元 **HY3** 另有 **¥28/月包 3,500 万 Token** 的低价流量包，适合搭配 Aider、Cline 等 BYOK 客户端长期使用。
- **更多免费 LLM API / BYOK 端点：** 硅基流动、阿里云百炼、火山方舟、Cloudflare Workers AI、魔搭社区、Telnyx 等厂商官方免费额度，配额与接入门槛详见 [免费 LLM API 与 BYOK 端点](#免费-llm-api-与-byok-端点)。

## Agentic IDE 价格与配额对比

原生集成全局代码库索引、跨文件重构与终端沙箱执行能力的独立开发环境。

| 工具 | 定价（2026-11） | 已核实折扣与配额规则 | 核心适用场景 | 官方链接 |
|------|-----------------|----------------------|--------------|----------|
| **Cursor** | 免费：限量<br>Plus：**$8/月**<br>Premium：**$30/月**<br>Super：**$100/月**<br>Ultra：**$200/月**<br>Teams：$30 / $100 / $200 每席<br>年付：$80 / $300 / $1,000 / $2,000 | 现通过 **The X Subscription** 售卖；旧版 Cursor 套餐**已对新注册关闭**（Pro $20、Pro+ $60、Ultra $200、Teams Standard $40、Teams Premium $120 对存量用户继续有效）。付费档共用**一个跨 Cursor 与 Grok 的每周算力池**；Plus 仅限 Grok 4.7 / 4.6 / 4.5 与 Composer 2.5 的固定参数，**第三方模型自 Premium 起开放**，按 API 目录价从预付额度扣费。邀请 5 折计划已于 2026-07-23 下线。 | 以周额度支撑多文件协同修改、后台并行 Agent 与 Grok 4.7 调用，并与 Grok、X 共用一份订阅。 | [cursor.com](https://cursor.com) |
| **Devin Desktop** *（原 Windsurf）* | 免费（轻量配额，无限 Tab 补全）<br>Pro：**$20/月**<br>Max：$200/月<br>Teams：$80/月基座 + $40/席 | **新用户绑定 Git 仓库完成引导立赠 $10 AI 额度**；**免费档另可零成本使用 SWE-2 Flash Medium（截至 2026-12-05）**；Pro 及以上档位免费调用 SWE 1.6 模型。*（GLM-5.2 / Kimi K2.7 限时免费已于 2026-07-05 结束。）* | 将长链路异步研发任务托管给 Devin Cloud，自动执行测试并提交 PR。 | [devin.ai](https://devin.ai) |
| **Google Antigravity** | 免费层可用<br>AI Plus：$7.99/月<br>AI Pro：**$19.99/月**<br>AI Ultra：**$99.99–$200/月**（原 $250） | 全档位**行内 Tab 补全完全免费**；Ultra 顶配于 2026-05 从 $249.99 降至 $200；Agent 算力池每 5 小时重置一次（设每周总上限）。 | 多 Agent 并行开发与内置浏览器实时交互调试的全栈 Web 工程。 | [antigravity.google](https://antigravity.google) |
| **Kiro** *（AWS）* | 免费：50 credits<br>Pro：**$20/月（含 1,000 credits）**<br>Pro+：$40/月（2,000 credits）<br>Pro Max：**$100/月（5,000 credits）**<br>Power：$200/月（10,000 credits） | 支持年付折扣，超额按 $0.04/credit 计费。模型消耗倍率：Auto 1.0×、Sonnet 1.3×、**Opus 4.8 2.2×**、Haiku 0.4×、GLM-5 0.5×、**Qwen3 Coder Next 0.05×**。 | 规格驱动（Spec-driven）生产级交付，以及 Amazon Q Developer 插件用户的官方迁移目标。 | [kiro.dev](https://kiro.dev) |
| **Trae** *（字节跳动）* | 免费（月 5,000 次补全，2 路并发）<br>Pro：**$20/月**（含 $20 用量）<br>Pro+：**$60/月**（含 $60 用量，3×）<br>Ultra：**$200/月**（含 $200 用量，10×） | **国内版（`trae.cn`）面向个人开发者完全免费**，内置豆包与 DeepSeek 模型；国内免费账号另可**每日签到领 100 积分（每月 500）**，新注册一次性赠 **2,000 积分**（31 天有效）。 | $20/月 的类 Cursor 交互体验，或直接用 `trae.cn` 零成本获取同等能力。 | [trae.ai](https://trae.ai) |
| **ZCode** *（智谱）* | 新用户试用 / GLM Coding Plan | **新用户 5 天体验：每天 GLM-5.3 300 万 + GLM-5.3-Flash 500 万 Token**（两模型独立日额、每日刷新）；Coding Plan 主打 **GLM-5.3 与 GLM-5.3-Flash**（Flash 可用配额约为 GLM-5.3 的 **3×**）。*（原 1.5× 配额加成已于 2026-06-30 结束。）* | 围绕智谱 GLM-5.3 系列模型构建工作流的官方原生 IDE。 | [zcode.z.ai](https://zcode.z.ai/cn/docs/welcome) |
| **CodeBuddy** *（腾讯国际站）* | 免费：250 credits / 2 周<br>Pro：**$9.95/月**（半价促销，原价 $19.90）或 $119.40/年（1,000 credits/月）<br>Team：$40/席/月 | 每两周自动发放 250 免费 credits；加量包 $9.95 / 1,000 credits 起。DeepSeek 官方合作伙伴，支持 **V4.1 Flash**。 | 海外腾讯云生态团队，以主流 IDE 一半的月费（$9.95）获取标准化辅助开发环境。 | [codebuddy.ai](https://www.codebuddy.ai/) |
| **CodeBuddy / WorkBuddy** *（腾讯国内站）* | 体验版：**免费（500 credits/月）**<br>标准版：**¥99/月**（基础 2,000 + 赠送 2,000 = **4,000 积分**）<br>高级版：¥199/月（4,000 + 5,000 = 9,000）<br>旗舰版：¥999/月（20,000 + 30,000）<br>Buddy One VIP：¥700/月（原价 ¥1,399）<br>连续包月 7 折、连续包年 5.6 折 | 通过 [WorkBuddy 邀请链接](https://www.workbuddy.cn/events/invite?inviteCode=qm4gyc1daqn) 注册获 **2,000 积分**新用户礼包（1 个月有效）；叠加站内新手任务后宣传上限 **3,600 积分**（约合标准版一个月的 90%，**超出部分未逐项公示**）；注册 30 天内首次付费升级，双方各得 **500 积分**。已接入 **Kimi K3**（约 1.62×）与 **DeepSeek V4.1 Flash**。 | 国内腾讯云生态研发，以及用首月积分充分体验 **Kimi K3** 与 **DeepSeek V4.1 Flash** 后再决定是否付 ¥99。 | [workbuddy.cn](https://www.workbuddy.cn/events/invite?inviteCode=qm4gyc1daqn) / [codebuddy.cn](https://www.codebuddy.cn/pricing/) |
| **Qoder CN** *（原通义灵码，阿里）* | 社区版：**免费**（限量，含 2 周 Pro 试用 + 300 credits）<br>专业版：¥59/月（2,000 credits）<br>企业版：¥99–¥199/席/月 | **2026-05-20 完成品牌更名与调价**，大幅收紧免费层补全频次与对话配额，终结此前无限免费政策。个人用户另可**每日 10 点领 100 通用 Credits**（10:00→次日 10:00，30 天有效）。 | 阿里云技术栈团队在单 IDE 内按需切换 Qwen、GLM 与 Kimi 模型。 | [cn.aliyun.com/product/lingma](https://cn.aliyun.com/product/lingma) |
| **Zed** | 核心编辑器：**免费**<br>Zed Pro：低门槛月度订阅 | Rust 原生开源编辑器；**高校学生认证免费领 1 年 Zed Pro 会员**（含每月约 **$10 AI 模型额度**）。**14 天 Zed Pro 试用另赠 $5 GPT-6 Luna 额度**（无需绑卡，到期自动转免费版）。 | 重视毫秒级键盘响应、本地优先架构及高校免费算力额度的开发者。 | [zed.dev](https://zed.dev) |
| **MiniMax Code** | 免费：限量 | **每日签到 +400 积分**（连签第 4、7 天各 1,000，一周约 4,000，30 天有效）；不定期限时送 H3 Image 生图额度。积分为产品内额度，不是通用 API 余额。 | 基于 MiniMax M 系列文本与多模态模型的桌面编程 Agent。 | [minimax.io](https://www.minimax.io/) |
| **华为云码道** | 免费：邀请制 | **邀请活动：邀请人每次有效邀请 +1,000 积分（累计上限 5 万），被邀请人 +1,000 积分**，叠加新用户 **4,000 基础积分**（邀请链接见「限时优惠与截止日历」，**2026-11-15 截止**）。内置 Kimi K3.1 Pro、GLM-5.3-Flash、DeepSeek V4.1 Flash；积分仅限码道客户端内使用。 | 华为云面向国内团队的自研编程 Agent。 | [codearts.huaweicloud.com](https://codearts.huaweicloud.com) |
| **智谱 AutoClaw** *（国内版）* | 免费：活动制 | **双十一登录领 5,000 万 Token**（2026-11-09→11-15，北京时间 11-15 23:59 失效）；**升级 2.2.0 送 +5,000 积分**（约 5,000 万 Token，7 天有效）。内置 GLM-5.3 / 5.3-Flash / 5-Turbo / 5V-Turbo；仅限 AutoClaw 内使用。 | 智谱围绕 GLM-5.x 家族打造的国内桌面编程 Agent。 | 见官网 |

## VS Code 与 JetBrains 编程插件

直接安装在现有 VS Code 或 JetBrains IDE 中，提供行内代码补全、代码库问答与跨文件自主修改能力。

| 工具 | 定价（2026-11） | 已核实折扣与配额规则 | 核心适用场景 | 官方链接 |
|------|-----------------|----------------------|--------------|----------|
| **GitHub Copilot** | 免费（2,000 次补全/月）<br>Pro：**$10/月（1,500 credits）**<br>Pro+：$39/月（7,000 credits）<br>Max：$100/月（20,000 credits）<br>Business：$19/席（1,900 credits）<br>Enterprise：$39/席（3,900 credits） | 个人版 Pro/Pro+/Max 自 2026-06-17 起恢复开放注册；企业版信用卡/PayPal 通道自 2026-09-01 起重开。1 credit = $0.01；**付费档行内补全与 Next Edit 不限量免费**。学生可免费领 Pro。*（企业版 3,000/7,000 临时促销额度已于 2026-09-01 恢复为 1,900/3,900。）* | $10/月获取无限量丝滑行内补全，并与 GitHub PR 及 Actions 深度联动。 | [github.com/features/copilot](https://github.com/features/copilot) |
| **Continue.dev** | 核心插件：**$0（开源免费）**<br>Team：约 $20/席/月 | 100% 开源，支持自带 API Key（BYOK）或连接本地 Ollama 模型，软件授权费为 $0。 | 企业内网隐私合规、自定义模型路由及纯本地离线推理。 | [continue.dev](https://www.continue.dev) |
| **Cline** | 核心插件：**$0（开源 BYOK）**<br>**ClinePass：$9.99/月** | BYOK 与本地模型始终 $0。**ClinePass（$9.99/月）** 包含 GLM 5.3 Flash/5.3/5.2、Kimi K3、**DeepSeek V4 Pro / V4 Flash**、MiniMax M3、MiMo、Qwen3.7/3.8，通用于插件、CLI 与桌面端（配额约为标准 API 的 2–5×）。 | 在 VS Code 内执行自主多步文件改写与终端命令，兼顾 BYOK 灵活性与 $9.99 包月低成本。 | [cline.bot](https://cline.bot) |
| **Roo Code** | **$0（开源 BYOK）** | 零软件加价，接入个人或企业 API Key 后仅按上游模型实际 Token 消耗计费。 | 在 Cline 架构基础上细分 Architect、Coder、Debugger 等多角色自定义 Agent 工作流。 | [roocode.com](https://roocode.com) |
| **Augment Code** | Community：免费（受限）<br>试用：30,000 credits（需绑卡）<br>Business：**$100/月一口价**（最多 50 席，含 $100 用量） | 提供 3 万 credits 试用；**Business 档 $100/月一口价覆盖最多 50 个席位**，免收按人头递增的席位税。 | 维护超大型单体仓库（Monorepo）的中小研发团队，多人平摊席位成本极低。 | [augmentcode.com](https://www.augmentcode.com) |
| **Amazon Q Developer** | **2026-05-15 起停止 IDE 插件与付费新注册**；**2027-04-30 正式停服** | 存量用户可过渡使用至 2027-04-30，AWS 控制台内嵌 Q 功能保留。**请勿在 Q Developer 插件上新建项目，直接迁移至 Kiro。** | 存量 AWS 插件团队向 [kiro.dev](https://kiro.dev) 平滑迁移的过渡期维护。 | [aws.amazon.com/q/developer](https://aws.amazon.com/q/developer/) |
| **Supermaven** | 免费层（高速补全）<br>Pro：**$10/月**（1M 上下文、风格自适应 + $5 对话额度）<br>Team：$10/席/月 | 免费档已支持大型代码库极速补全；Pro 档提供 **30 天免费试用**。 | 对敲击补全延迟极度敏感、需要百万 Token 级上下文感知的高频编码。 | [supermaven.com](https://supermaven.com) |
| **Qodo** *（原 CodiumAI）* | Developer：**免费**（每月 30 次组织级 PR 审查 + 250 IDE/CLI credits）<br>Teams：$30/席/月（年付）或 $38/月 | 免费档即可覆盖日常单元测试自动生成与每月 30 次 PR 自动化代码审查。 | 自动化补齐单元测试覆盖率、在合并前拦截 PR 边界缺陷。 | [qodo.ai](https://www.qodo.ai) |

### 历史免费方案变更说明（已转纯企业版或取消免费算力）

以下工具曾是个人开发者的热门免费选择，现已全面关停个人档或移除免费云端算力。请直接使用右侧替代方案，避免被过时教程误导。

| 工具 | 当前授权状态 | 变更时间与具体调整 | 个人开发者平替方案 |
|------|--------------|--------------------|--------------------|
| **Sourcegraph Cody** | 仅限企业订阅（约 $59/席/月，年付） | **2025-07 下线个人 Free 与 Pro 计划**，官方引导个人开发者迁往 Amp。 | [Amp](https://ampcode.com)（零加价按量 API 计费）或 [Continue.dev](https://www.continue.dev) |
| **Tabnine** | 仅限企业订阅（$39–$59/席/月，年付） | **2025-04 关停个人免费版、个人付费版及学生计划**。 | [Cline](https://cline.bot)、[Continue.dev](https://www.continue.dev) 或 [Aider](https://aider.chat) |
| **Warp** | 终端免费；内置 AI 需订 **Build（$20/月）** | 取消免费版附赠的云端 AI 额度；免费用户仅能通过 **BYOK 模式**填入自有 OpenAI / Anthropic / Google API Key。 | [Cursor](https://cursor.com) 或上述开源 CLI Agent（[Aider](https://aider.chat)、[OpenCode](https://opencode.ai)）配合自有 Key |

## CLI 与终端编程 Agent

原生运行在命令行中的自主 Agent，直接读写本地代码库、执行测试套件并自动提交 Git 变更。

| 工具 | 定价（2026-11） | 已核实折扣与配额规则 | 核心适用场景 | 官方链接 |
|------|-----------------|----------------------|--------------|----------|
| **Freebuff** | **免费（100% 广告支持，官网标价 €0）**<br>安装：`npm install -g freebuff` | 免 API Key、免绑卡；上游支持 **DeepSeek V4.1 Flash**（含旧 V4 路由）、Kimi 与 MiniMax，覆盖 CLI、Web、Chat、Desktop 与移动端（Android 已上线）（[Web 邀请链接](https://freebuff.com/web/?ref=ref-b3046190-1d77-44c1-915c-b71b4f36ae5e)）。 | **零预算在命令行直接调用 DeepSeek V4.1 Flash**，免去一切密钥配置。 | [freebuff.com](https://freebuff.com/) |
| **Codebuff** | 订阅：**$100/月**（1×）、**$200/月**（2.5×）、**$500/月**（7×）<br>按量：**$0.01/credit** | **新注册即赠 500 credits**（可支撑新项目数小时高强度开发），随时可取消。与 Freebuff 同属一家公司，定位商业高阶版。 | 深度代码库索引与高并发终端重构，不受免费层降级与日限额约束。 | [codebuff.com](https://www.codebuff.com) |
| **Claude Code** | Pro：**$17/月（年付）** 或 $20/月<br>Max：$100/月（5×）或 $200/月（20×）<br>Team：$20–$100/席/月 | **年付约享 85 折**；配额按 5 小时滚动窗口与 Claude 网页端共享，Max 档叠加双周限额（Claude 免费版不含此功能）。 | 跨模块复杂架构重构、深层疑难 Bug 定位及百万 Token 上下文全局推理。 | [claude.com/claude-code](https://www.claude.com/product/claude-code) |
| **Grok Build** *（xAI）* | Grok 免费层（仅限网页问答）<br>**SuperGrok：$30/月** | 在 [grok.com/plans](https://grok.com/plans) 开通 **7 天 SuperGrok 免费试用**，共享 Grok 4.5+ 与 Grok Build 正式付费额度（需绑卡，第 7 天前取消免扣 $30/月）。 | 利用 7 天免费窗口在终端实测 xAI 前沿编码模型的真实工程表现。 | [grok.com/plans](https://grok.com/plans) |
| **Kimi Code** *（月之暗面）* | Adagio：**免费**<br>Andante：**¥49/月** · Moderato：¥99/月（国际 $19）<br>Allegretto：¥199/月 · Allegro：¥699/月 | 一期邀请抽奖已结束。旗舰 **Kimi K3** 已全线接入 Web、Code 与 API（见[会员定价](https://www.kimi.com/membership/pricing)）。**想零成本实测 Kimi K3 建议先领 WorkBuddy 注册积分。** | 以包月会员额度池统一调用 Kimi K3 网页端与 Kimi Code 终端代理。 | [kimi.com/membership/pricing](https://www.kimi.com/membership/pricing) |
| **OpenAI Codex** | **ChatGPT 免费版直接包含**<br>Go：$8/月 · Plus：$20/月<br>Pro：$100–$200/月 | ChatGPT 免费账号免绑卡直接用（受 5 小时滚动窗口限额）；支持填入个人 **OpenAI API Key** 按量计费以突破窗口限制（不含云端沙箱）。 | OpenAI 生态开发者通过 **macOS / Windows 官方桌面客户端**或云端沙箱执行异步任务。 | [openai.com/codex](https://openai.com/codex) |
| **Gemini CLI / Antigravity CLI** | **免费层开放**（每日请求配额充裕） | 无需绑卡或订阅，免费层每日调用上限宽松。 | 超长上下文代码库检索、日志分析与终端脚本批处理。 | [antigravity.google](https://antigravity.google) |
| **Ollama Cloud** | Free：**$0**（1 路云端并发）<br>Pro：**$20/月**（$200/年，50× 云端用量，3 路并发）<br>Max：$100/月（10 路并发） | 本地运行模型永久无限免费；云端算力按 GPU 时间计量，设 **5 小时会话**与 **7 天周度**重置窗口。 | 保持纯正本地优先工作流，同时按需弹性调用云端大参数模型，免管多厂商 Key。 | [ollama.com/pricing](https://ollama.com/pricing) |
| **Aider** | **$0（开源 BYOK / 本地运行）** | 软件完全免费；仅支付上游 LLM API 实际 Token 消耗，接入本地 Ollama 模型则为 $0。 | Git 原生结对编程，自动生成规范 Commit 记录，兼容 75+ 款商业与开源模型。 | [aider.chat](https://aider.chat) |
| **Amp** *（Sourcegraph）* | **按量计费（原始 API 零加价透传）**；首充门槛 $5 | 全程无广告；原每日约 $10 的按小时免费补充额度**自 2026-05 起对部分账号已暂停或缩减**。 | 不设上下文窗口硬上限，按原始 Token 成本在多模型间动态路由。 | [ampcode.com](https://ampcode.com) |
| **Cline CLI** | 开源版：**$0（BYOK）**<br>**ClinePass：$9.99/月**（`npm i -g cline`） | BYOK 保持 $0；订阅 ClinePass（$9.99/月）可直接调用套餐内 GLM 5.3、Kimi K3、**DeepSeek V4 Pro / V4 Flash**、MiniMax 与 Qwen3.8 额度（[详情](https://cline.bot/cline-pass)）。 | 在终端或 CI 流水线中无头（Headless）运行 Cline 代理循环，以 $9.99/月锁定开源模型包月成本。 | [cline.bot](https://cline.bot) |
| **OpenCode** | 开源版：**$0（BYOK）**<br>**Go：$10/月** · Go Plus：$40/月 · Go Teams：$20/席/月 | 通过[邀请链接](https://opencode.ai/go?ref=J9E8732NMP)订阅**双方各得 $5 Go 额度**。**DeepSeek V4.1 Flash 月额度 $100**（模型 ID `deepseek-v4.1-flash`；5 小时窗口 $20、每周 $50），DeepSeek V4 Pro $15/月；另含 Grok 4.7、Kimi K3 / K3.1 Pro、GLM-5.3、Qwen3.8、MiniMax M3、GPT 6 Luna、Claude Haiku 5.5 等约 30 款模型。另在 OpenCode 内**限时免费开放** MiniMax M3.1 Flash、LongCat 2.5（每日 100 次）、DeepSeek V4.1 Flash、GLM-5.3-Flash、MiMo-V2.6-Flash 与 Nemotron 免费版等模型。 | **$10 档付费调用 DeepSeek V4.1 Flash 的主力终端工具**，一张 Key 通用于多款第三方 Agent。 | [opencode.ai](https://opencode.ai) |
| **Crush** *（Charm）* | **$0（开源 BYOK）** | 零软件授权费，接入任意自定义 API Key 按量付费。 | Charm 团队出品的高颜值终端交互界面（TUI），支持多模型灵活路由。 | [github.com/charmbracelet/crush](https://github.com/charmbracelet/crush) |
| **Goose** *（Block）* | **$0（开源 BYOK / 本地运行）** | 零软件授权费，支持本地模型或自有 API Key。 | 原生围绕 MCP（Model Context Protocol）插件生态构建的可扩展本地自动化 Agent。 | [block.github.io/goose](https://block.github.io/goose) |
| **Qwen Code** | **$0（开源免费）** | 搭配本地或云端通义千问模型享受零软件授权费。 | 针对 Qwen3 Coder 系列模型深度调优的低成本终端编码方案。 | [github.com/QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) |

## 免费 LLM API 与 BYOK 端点

以下为可直接接入 **Aider、Cline、Continue.dev、OpenCode** 等任意 OpenAI 兼容客户端的厂商官方免费额度。额度数据截至 **2026-11-14** 厂商公布口径，实际数字请以链接页面为准；标 **见官网** 的条目暂无稳定的公开额度页。

| 端点 | 免费额度（2026-11） | 模型 / 兼容性 | 接入门槛 | 官方链接 |
|------|---------------------|---------------|----------|----------|
| **硅基流动 SiliconFlow** | 实名认证后送 **16 元通用代金券**（老用户亦可，180 天有效）；**邀请好友完成实名后，你和 TA 各再得 16 元、不设上限**（邀请链接见「限时优惠与截止日历」）；部分 OCR / 语音 / 向量 / 生图模型长期免费（非 LLM）。 | 平台模型含 Pro 与高速档；API、批量推理、微调均可用。 | 实名认证。 | [siliconflow.cn](https://siliconflow.cn/) |
| **阿里云百炼** | 新用户每个模型（含快照）**各送 100 万 Token**（北京地域，90 天）；在读学生 **300 元抵扣金**（每 12 个月一次，至 2027-03-31）。另有**「邀新有礼」邀请活动**：邀请人最高 **1000 元**、被邀请人新客首购低至 **4.5 折**（邀请链接见「限时优惠与截止日历」）。 | qwen3.8-max、deepseek-v4-pro、kimi-k3 等（仅北京地域）。 | 实名；北京地域；通用 API Key。 | [bailian.console.aliyun.com](https://bailian.console.aliyun.com/) |
| **火山方舟** | 新用户 4 款豆包模型**各送 50 万 Token**。其 **Coding Plan**（GLM-5.3 系列、DeepSeek-V4.1-Flash 1017、Doubao-Seed-Evolving；工具不限）另有新用户 **9.5 折**邀请活动（邀请链接与邀请码见「限时优惠与截止日历」）。 | Doubao-Seed-2.1-pro / 2.1-turbo / Evolving / Character。 | 仅在线推理；不含插件与存储。 | [volcengine.com/product/ark](https://www.volcengine.com/product/ark) |
| **腾讯云 TokenHub** | 新用户每模型 **100 万 Token**（语言 + 多模态），1 年有效。 | TokenHub 模型广场内模型。 | 实名。 | 见官网 |
| **百度千帆** | 新用户 **20 元代金券**（1 个月有效）。 | DeepSeek V4.1、GLM-5.3 等。 | 实名。 | [qianfan.cloud.baidu.com](https://qianfan.cloud.baidu.com/) |
| **蚂蚁百灵 Ling** | 每月 1 日发 **10 元券** + 新人 **20 元券**；**Ling-3.2-flash 上线期免费**调用。 | Ling 系列模型。 | 绑定支付宝；免费期后按官网计费。 | 见官网 |
| **超算互联网 SCNet** | 新用户领 **1 亿 Token**（GLM-5.3-Flash，30 天有效），另有 **1,000 万 Token** 档。 | GLM-5.3-Flash（型号可能调整）。 | 实名；限量；活动至 2026-12-31。 | [scnet.cn](https://www.scnet.cn/) |
| **腾讯 EdgeOne Makers** | 每账号每月共享 **50 万 Token**。 | 内置 DeepSeek V4.x、Kimi K2.6、MiniMax M3/M2.7、混元 Hy3；兼容 OpenAI/Anthropic。 | 仅限技术验证；自接 Key 另行计费。 | [edgeone.ai](https://edgeone.ai/) |
| **Cloudflare Workers AI** | 每天 **1 万 Neurons**（北京时间 08:00 重置）。 | Qwen3.8-27B、GPT-OSS 120B/20B、Gemma 4 26B、Llama 4 Scout、BGE-M3。 | 免费档超额即停；REST API 或 Workers 调用。 | [developers.cloudflare.com/workers-ai](https://developers.cloudflare.com/workers-ai/) |
| **魔搭社区 ModelScope** | 每天 **200 魔粒**（绑阿里云账号再 +50）。 | API-Inference：DeepSeek-V4.1-Flash-1017、MiniMax-M3.1-Flash。 | 实名 + 绑阿里云 + 验证邮箱。 | [modelscope.cn](https://modelscope.cn/) |
| **Telnyx** | 新用户 **$25 AI 额度**（升级后降为 $5）。 | DeepSeek V4.1 Flash、GLM-5.3、GLM-5.3 Flash、Kimi K3（Telnyx Inference）。 | 无需绑卡。 | [telnyx.com](https://telnyx.com/) |
| **OpenRouter** | 免费 `baidu/ernie-5.5-flash-preview:free`（共享每日 50 次 / 每分钟 20 次）。 | ERNIE 5.5 Flash Preview 及轮换免费模型。 | 官方聚合接入；受免费档速率限制。 | [openrouter.ai](https://openrouter.ai/) |
| **书生·端砚** *（上海 AI Lab）* | 测试期每月赠墨点 Token Plan。 | DeepSeek-V4.1-Flash-1017、GLM-5.3、Qwen3.8-27B。 | 需创建 API Key；额度见账户。 | 见官网 |
| **DeepSeek Harness** | 桌面版登录送 **6 元开放平台赠金**（限量）。 | deepseek-flash 与 deepseek-v4-pro。 | 桌面客户端；+86 手机号。 | [deepseek.com](https://www.deepseek.com/) |

## 限时优惠与截止日历

以下为带有明确截止日期或试用窗口的活跃促销。仓库每周通过自动化脚本扫描本节并提醒即将到期的条目。

| 工具 | 促销内容 | 截止日期 | 关键条款与核实链接 |
|------|----------|----------|--------------------|
| **Grok / SuperGrok** *（xAI）* | **SuperGrok 7 天免费试用**——完整解锁 Grok 4.5+ 与 Grok Build 付费额度，入口 [grok.com/plans](https://grok.com/plans) | **待定** *（官方未公布截止日期）* | 需绑信用卡；务必在第 7 天前取消，否则按 **$30/月** 自动续费。仅限从未订阅过的新账号。 |
| **CodeBuddy / WorkBuddy** *（腾讯国内站）* | 通过[邀请链接](https://www.workbuddy.cn/events/invite?inviteCode=qm4gyc1daqn)领取 **2,000 积分**新用户礼包；受邀者 30 天内首次付费升级个人版，双方再各得 **500 积分** | **2026-11-30** | 需在截止日前完成注册并跑通一次对话/任务，积分有效期 1 个月。邀请人每激活一位好友得 **50 积分**，好友首周活跃满 3 天再得 **100 积分**。 |
| **智谱 AutoClaw** *（国内版）* | **双十一登录领 5,000 万 Token**（GLM-5.3 / 5.3-Flash / 5-Turbo / 5V-Turbo） | **2026-11-15** | 每账号一次；仅限 AutoClaw 内使用（非通用 API 额度）；北京时间 2026-11-15 23:59 失效。 |
| **WorkBuddy / CodeBuddy** *（腾讯国内站）* | **Hy4 限时免费额度**——客户端内免费体验 Hy4 的代码、文档与视觉任务 | **2026-11-15** | 产品内免费额度，超额消耗账户积分；具体量以客户端提示为准。 |
| **Devin Desktop** | **免费使用 SWE-2 Flash Medium**（桌面端 / CLI） | **2026-12-05** | 免费账号有少量 Agent 额度；High/Max 需付费档；不含 Devin 云端会话。 |
| **蚂蚁百灵 Ling** | **Ling-3.2-flash 免费调用**（支持文本 / 图片 / 视频输入） | **2026-11-19** | 先绑支付宝并开通模型服务；两周上线期结束后恢复收费。 |
| **OpenCode** | **限时免费模型**——MiniMax M3.1 Flash、LongCat 2.5、DeepSeek V4.1 Flash、GLM-5.3-Flash 等 | **2026-11-23** | 仅限 OpenCode 内使用；LongCat 2.5 每日 100 次、托管于中国；部分模型会用于训练。 |
| **火山方舟 Coding Plan** | **（邀请链接）** 新用户订阅邀请：经此[邀请链接](https://volcengine.com/L/ikpXOgCIUiE/)订阅（邀请码 **M4AAF2XN**）；支持 GLM-5.3 系列、DeepSeek-V4.1-Flash 1017、Doubao-Seed-Evolving 等模型，工具不限 | **2026-11-19** | 被邀请人首单享 **9.5 折**（低至 ¥9.4，订阅越多越划算）；邀请人获首单实付 **5%** 代金券，上不封顶。已标注为邀请链接，不劣于官网公开价。 |
| **硅基流动 SiliconFlow** | **（邀请链接）** 经此[邀请链接](https://cloud.siliconflow.cn/i/6UosFyoo)注册；好友完成实名认证后，你和 TA 各得 **16 元**代金券，不设上限 | **2026-12-31** | 需实名认证；代金券全平台通用，含 Pro/高速模型。已标注为邀请链接，双方受益，不劣于官网公开价。 |
| **阿里云百炼** | **（邀请链接）** 经此[邀请链接](https://www.aliyun.com/benefit/ai/aistar?clubBiz=subTask..13023094..10274..)参加「邀新有礼」：邀请人最高得 **1000 元**；被邀请人新客首购大模型入门套餐低至 **4.5 折** | **待定** *（以活动页为准）* | 具体金额/门槛随活动调整，以活动页实时规则为准；已标注为邀请链接，被邀请人不劣于官网公开价。 |
| **华为云码道 CodeArts** | **（邀请链接）** 经此[邀请链接](https://devcloud.cn-north-4.huaweicloud.com/chat?source=dmzntgwlb&sourcead=dmzntgwlb1&invitecode=INV-fa8e5gx7GHFDRYdkR7FzMF_XAaAvSOscSfK75SuWars9sUEyWjToTrjhoSKyI5QoLqirtJK3X1qTryYa1XjqQlzGfgg2TlPwxGPrd6p0FOBo634AKceCCl9VXraFp-EfJXNjsZDrroKtj7ow-j1SDaX_CwRH7317UIaZm21Az_MgPjbt)邀请新用户；邀请人每次有效邀请 **+1,000 积分**（累计上限 5 万），被邀请人 **+1,000 积分**（叠加新用户 4,000 基础积分） | **2026-11-15** | 需先切换积分制套餐；积分 1 个月有效；积分仅限码道客户端内使用。已标注为邀请链接，双方受益。 |

> **近期已下线活动归档（已移出活跃表）：** Copilot 企业版 3,000/7,000 额度加成（**2026-09-01**）；OpenCode Go 4× 额度膨胀（**2026-09-20**，已由 Go 档常驻 $100/月额度取代）；OpenCode Go 首月 $5（**2026-08-24**）；Cursor 邀请首月 5 折（**2026-07-23**）；WorkBuddy HY3 全员免费（**2026-07-22**）；Devin GLM-5.2 / Kimi K2.7 免费期（**2026-07-05**）；ZCode / GLM Coding Plan 1.5× 加成（**2026-06-30**）；Kimi 一期邀请抽奖（**2026-09 核实已结束**）。

## 学生与教育专属免费权益（.edu）

持有 `.edu` 教育邮箱或学籍证明的学生与教职工，可直接免费申领多款商业工具的 Pro 订阅。**将以下认证全部走完，即可零成本配齐一整套顶配开发环境（$0/年）：**

| 工具 | 学生专属免费权益 | 官方认证入口 |
|------|------------------|--------------|
| **Google Gemini & Antigravity** | **免费领 1 年 Google AI Pro 会员**——解锁 **Gemini Pro** 及 **Google Antigravity** 完整高阶算力池 | [gemini.google/students](https://gemini.google/students) |
| **Zed Pro** | **免费领 1 年 Zed Pro 会员**——每月附赠约 **$10 AI 模型调用额度** | 在 Zed 客户端内提交学籍认证（[zed.dev](https://zed.dev)） |
| **GitHub Copilot Pro** | 通过 GitHub Student Developer Pack **免费开通 Copilot Pro** | [education.github.com/pack](https://education.github.com/pack) |
| **JetBrains 全家桶** | 在读期间**免费获取全系 JetBrains IDE 个人授权**（含内置 AI 辅助功能） | [jetbrains.com/student](https://www.jetbrains.com/student/) |
| **Cursor** | 学生优惠原绑定旧版 Cursor 套餐；并入 **The X Subscription** 后是否延续，需以官网实时规则为准 | [cursor.com](https://cursor.com) |
| **阿里云百炼** | **每年 ¥300 模型抵扣金**（有效 12 个月；仅限国内高校在读学生；至 2027-03-31） | 在读期间完成实名与学籍认证（[aliyun.com](https://www.aliyun.com)） |

## AI 编程工具选型与决策矩阵

根据团队预算与研发场景，直接匹配最省钱的组合方案：

| 开发者画像与核心场景 | 推荐组合方案 | 选型逻辑与成本账 |
|----------------------|--------------|------------------|
| **零预算 / 纯本地隐私优先** | **Freebuff** + **Aider / Cline** + 本地 Ollama | 订阅支出为 $0；日常云端任务走 Freebuff 免费调 V4.1 Flash，核心敏感代码走本地 Ollama。 |
| **高频调用 DeepSeek V4.1 Flash** | **Freebuff（免费）** → **OpenCode Go（$10/月）** | 先用 Freebuff 零成本摸底；需要稳定高配额与跨工具 API Key 时选 OpenCode Go——常驻 **$100/月 Flash 额度**（5 小时窗口 $20、每周 $50），Go Plus（$40/月）额度翻倍。 |
| **个人开发者 / $10 档稳健基座** | **GitHub Copilot Pro（$10/月）** | 大厂商业方案中月费最低，提供不限量行内补全、Next Edit 及每月 1,500 额度。 |
| **个人开发者 / 主力 Agentic IDE** | **Cursor Premium（$30/月）** 或 **Kiro Pro（$20/月）** | Cursor 交互手感与多模型生态最成熟；Kiro 主打规格驱动（Spec-driven），且是 Amazon Q Developer 用户的顺滑迁入地。 |
| **重度架构重构 / 跨模块攻坚** | **Cursor Premium（$30/月）** + **Claude Code（$17–$20/月）** | 双轨分工：Cursor 负责日常多文件编辑与秒级补全，遇到超大规模重构与疑难排障时切终端调用 Claude Code。 |
| **全栈 Web 与前端交互调试** | **Google Antigravity（免费层 / $19.99 AI Pro）** | 多 Agent 并行协同，内置浏览器沙箱可自动点击、截图并验证前端渲染结果。 |
| **已有 ChatGPT 免费版 / Plus 账号** | **OpenAI Codex（macOS/Windows 桌面端 & CLI）** | 零新增订阅费，直接激活账号内含的云端沙箱与本地终端 Agent 能力。 |
| **国内开发者 / 国产旗舰模型低成本组合** | **WorkBuddy**（邀请礼 2,000 积分 + 新手任务，宣传上限 3,600）+ **腾讯云模型广场**（各赠 100 万 Token）+ **OpenCode Go / ClinePass（$9.99/月）** | 先用 WorkBuddy 邀请礼与新手任务积分（宣传上限约合标准版首月 90%）与腾讯云 90 天百万 Token 池打磨 **Kimi K3** 与 **DeepSeek V4.1 Flash**，后续再按需接 $9.99/$10 包月通道。 |

## 7 条 AI 编程算力省钱法则

1. **算清「模型消耗倍率」，别只看月费标价。** $20/月往往只是入场券：例如 Kiro 调用 Opus 4.8 的消耗倍率是 **2.2×**，而调用 Qwen3 Coder Next 仅 **0.05×**（相差 44 倍）；Copilot、Antigravity 与 Cursor 同样按模型档位扣减积分或算力池。
2. **按任务难度分级路由模型。** 行内补全、单测生成与常规 CRUD 固定绑定轻量高速模型（DeepSeek V4.1 Flash、GLM-5.3 Flash、Haiku、Gemini Flash）；仅在跨文件架构重构与深层逻辑排障时切换至 Opus、Sonnet 等高成本推理模型。
3. **吃透 DeepSeek V4.1 Flash 的错峰半价。** 日常编码优先走 **Freebuff（免费）** 或 **OpenCode Go（$10/月，$100 Flash 额度）**；若直接调用官方按量 API（官方端 `deepseek-flash`，Go 端 `deepseek-v4.1-flash`），将批量生成与长上下文分析排在非高峰时段（避开周一至周五 UTC 01:00–04:00 与 06:00–10:00），Token 账单直接减半。
4. **用「开源外壳 + BYOK」解耦工具与模型锁定。** 采用 **Aider、Cline、Continue.dev、OpenCode、Roo Code** 等开源客户端，底层可随时切换至腾讯云模型广场（每模型 100 万免费 Token）、NVIDIA NIM（$0）或本地 Ollama，彻底告别单一 IDE 涨价绑架。
5. **先串用新用户赠送额度，跑通真实项目再付费。** 决定包月前，先依次领取 WorkBuddy 的 **2,000 邀请积分与新手任务积分（宣传上限 3,600）**、腾讯云模型广场的 **90 天百万 Token**、Codebuff 的 **500 注册 credits** 以及 SuperGrok 的 **7 天免费试用**，用真实仓库压测出最顺手的工具链。
6. **主力工具稳定后切年付锁价。** 经过 1 个月高强度实测确认留用的商业工具，从月付切换至年付可直接砍掉 **15%–20%** 常规预算。
7. **每季度做一次 15 分钟订阅复盘。** AI 编程赛道的配额与模型代际每 60–90 天洗牌一次，上季度的付费主力很可能在本季度已有免费或十分之一价格的平替通道。

## 参与贡献

本指南的价值取决于每一条价格与配额数据的**准确与新鲜度**，欢迎社区共同维护：

- **发现价格变动、新促销上线或优惠过期？** 欢迎直接[提交 Issue](issues/new/choose) 或发起 Pull Request。
- **PR 必填信息：** 请附上**厂商官方定价/公告链接**、**核实日期**，以及限时活动的**截止日期**。
- **格式与双语同步规范：** 表格字段与提交流程请参见 [CONTRIBUTING.md](CONTRIBUTING.md)。

如果这份指南帮你的团队省下了订阅费或 Token 预算，欢迎点亮 **Star**，让更多开发者看到。

## 信息来源与核实记录

本仓库收录的定价档位、Token 费率与配额规则均直接核对自各厂商官方定价页与更新日志（最近一次全量复核：**2026 年 11 月**），核心核实源包括：[DeepSeek API 文档](https://api-docs.deepseek.com/)、[DeepSeek 官方定价](https://api-docs.deepseek.com/quick_start/pricing)、[DeepSeek V4.1 Flash 发布公告](https://api-docs.deepseek.com/news/news260910)、[OpenCode Go 文档](https://opencode.ai/docs/go/)、[ClinePass](https://cline.bot/cline-pass)、[GitHub Copilot Changelog](https://github.blog/changelog/)、[Cursor 邀请计划下线说明](https://forum.cursor.com/t/is-the-cursor-referral-discount-program-over-will-there-be-future-referral-campaigns/166990) 及 [Amazon Q Developer 停服公告](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/)。

下单前请通过表格内的官网链接确认实时条款。本项目为独立社区维护项目，与任何 AI 工具厂商无隶属关系；文中明确标注的邀请/返利链接用于补贴日常核实与维护成本，不会增加你的任何实际付费支出。

**免费 LLM API 与 BYOK 端点**表（硅基流动、阿里云百炼、火山方舟、Cloudflare Workers AI、魔搭社区、Telnyx 等）系依据各厂商额度页整理，数据截至 **2026-11-14**，具体 Token 数量请以链接页面为准。
