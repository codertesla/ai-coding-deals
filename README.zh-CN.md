# AI 编程工具成本优化与选型指南 💰

> 聚合全网主流 AI 编程工具的成本优化方案：涵盖免费额度、新用户优惠、邀请返利及开源平替方案。

**[English](README.md) · [简体中文](README.zh-CN.md)**

[![GitHub stars](https://img.shields.io/github/stars/codertesla/ai-coding-deals?style=social)](https://github.com/codertesla/ai-coding-deals/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/codertesla/ai-coding-deals)](https://github.com/codertesla/ai-coding-deals/commits)
[![Contributors](https://img.shields.io/github/contributors/codertesla/ai-coding-deals)](https://github.com/codertesla/ai-coding-deals/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/codertesla/ai-coding-deals)](https://github.com/codertesla/ai-coding-deals/issues)
![收录工具](https://img.shields.io/badge/收录工具-30+-blue)
![最后核实](https://img.shields.io/badge/最后核实-2026--09-brightgreen)
[![欢迎PR](https://img.shields.io/badge/PR-欢迎-orange)](CONTRIBUTING.md)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

AI 编程工具的定价与配额政策演进**极快**。本仓库致力于系统性追踪 **免费额度、商业折扣、邀请返利以及最具性价比的部署与配置方案**，旨在帮助开发者与技术团队优化 AI 算力支出。本项目由社区共同维护，并持续对照各厂商官网文档进行核实。

> [!IMPORTANT]
> **免责声明：** 本仓库所有信息均整理自公开渠道，具有时效性。**在进行任何付费决策前，请务必以相关厂商官网的最新官方政策为准。** 若发现任何信息偏差或失效，欢迎 [提交 Issue](../../issues/new/choose) 或发起 Pull Request。**最近一次全量核实时间：2026 年 09 月。**

## 📑 目录

- [🔥 高性价比推荐方案](#-高性价比推荐方案)
- [💵 零边际成本 AI 辅助开发方案](#-零边际成本-ai-辅助开发方案)
- [🏗️ Agentic IDE（AI 原生集成开发环境）](#️-agentic-ideai-原生集成开发环境)
- [🧩 助手与 IDE 插件](#-助手与-ide-插件)
  - [⚠️ 历史免费方案变更说明（已转企业版）](#️-历史免费方案变更说明已转企业版)
- [⌨️ CLI 与终端 Agent](#️-cli-与终端-agent)
- [⏳ 限时优惠与促销活动](#-限时优惠与促销活动)
- [🎓 学术与教育专属优惠](#-学术与教育专属优惠)
- [🎯 技术选型与决策矩阵](#-技术选型与决策矩阵)
- [💡 成本优化策略与技巧](#-成本优化策略与技巧)
- [🤝 参与贡献](#-参与贡献)
- [📚 信息来源](#-信息来源)

## 🔥 高性价比推荐方案

按推荐优先级排序的精选方案（越靠前越优先考虑）。已过期、暂停注册或受众过窄的条目已移出本表，详情仍见下方分类章节。（2026-09 整理，付费前请前往官网确认最新条款。）

> [!TIP]
> **DeepSeek-V4.1-Flash（2026-09-10 正式发布）：** 新架构家族，原生多模态；调用名请用 **`deepseek-flash`**（见 [DeepSeek API Docs](https://api-docs.deepseek.com/) / [公告](https://api-docs.deepseek.com/news/news260910)）。旧 ID `deepseek-v4-flash` / `deepseek-v4-flash-vision-exp` 会临时路由到 V4.1 Flash。官方非高峰价：**$0.15 / $0.60 / 缓存命中 $0.003** 每 1M tokens（高峰为 2×；高峰时段为周一至周五 UTC 01:00–04:00 与 06:00–10:00）。**目前最划算的两条渠道：** ① **Freebuff**（广告支持，$0）；② **OpenCode Go**（**$10/月**；**DeepSeek V4.1 Flash** 当前享 **4×** 额度促销——**$15 → $60/月**——**截止 2026-09-20**）。

| 工具 | 优惠 | 选型依据 |
|------|------|----------|
| **OpenCode Go** ✅ *已验证* | **Go 计划：$10/月**（首月 **$5** 促销已于 **2026-08-24** 下线）；受邀人订阅后，双方可通过[邀请链接](https://opencode.ai/go?ref=J9E8732NMP)各得 **$5 Go 用量额度**。**DeepSeek V4.1 Flash** 现享 **4×** 促销（月额度 **$15 → $60**；4× 时约 $12/5 小时、$30/周），单价对齐官方高峰/非高峰价，**截止 2026-09-20**——促销结束后 Flash 基础额度回到 **$15**（除非官方延期）。另含 GLM-5.3 / Flash、Kimi K3、Qwen3.8、MiniMax M3、MiMo、Hy3/Hy4 等 | **4× 窗口期内付费体验 V4.1 Flash 的主路径**；API Key 可用于 OpenCode 及其他已验证 Agent |
| **Freebuff** ✅ *已验证* | **100% 免费**（广告支持）的编程 Agent（CLI / Web / Chat / Desktop），官网 [freebuff.com](https://freebuff.com/) — 无需 API Key 或订阅；DeepSeek Flash/Pro 路由（旧 V4 ID 上游已指向 **V4.1 Flash**）及 Kimi、MiniMax 等；[Web 邀请链接](https://freebuff.com/web/?ref=ref-b3046190-1d77-44c1-915c-b71b4f36ae5e)。高级会话可能有每日上限并静默降级 | **白嫖 DeepSeek V4.1 的首选**——真正的 $0 |
| **CodeBuddy / WorkBuddy**（腾讯，国内站）✅ *已验证* | 通过 [WorkBuddy 邀请链接](https://www.workbuddy.cn/events/invite?inviteCode=fmfw2whmh) 注册（**微信登录**）：受邀新用户获 **注册礼 2000 积分**（有效期 **1 个月**），完成新手任务另有额外赠送，合计最高 **3600 credits**，约等于首月免费标准版（**¥99/月**）；**首次付费双方各得 500 积分**（受邀人仅一次，有效期 **6 个月**）。DeepSeek 官方合作伙伴——已支持 **V4.1 Flash**；另含 **Kimi K3**（消耗约 **1.62×**）。*（HY3 全员免费窗口已于 **2026-07-22** 结束。）* | 国内站新用户额度最扎实；**想免费体验 Kimi K3 / V4.1 可优先走这条** |
| **腾讯云 AI 模型广场** ✅ *已验证* | 新用户可在[模型广场](https://curl.qcloud.com/PN0cvBnI)页面右上角点击「**新用户福利免费体验**」领取——**所有语言模型**与**多模态理解模型**均各享 **100 万 Token** 免费体验额度，自领取起 **90 天内**有效（含 HY3、GLM、DeepSeek、Kimi Code 等）；混元 **HY3** 另有专属 **Hy Token Plan**，最低 **¥28/月** 可获 **3500 万 Token** | 国内 BYOK / 开源客户端的首选低成本 API 底座；一张 Key 覆盖多款旗舰模型 |
| **OpenAI Codex** | **ChatGPT 免费版已内置 Codex 功能**——支持 Web、CLI 及 **桌面客户端（macOS/Windows）**，无需绑定信用卡 | 覆盖面最广的零成本入门；已有 ChatGPT 账号即可直接用 |
| **Google Antigravity / Gemini** | 提供**高额度免费层**；AI Pro 订阅仅需 **$19.99/月** | 免费层额度慷慨；想试多 Agent / 高速 Gemini 工作流时门槛最低 |
| **Grok / SuperGrok**（xAI）✅ *已验证* | 前往 [grok.com/plans](https://grok.com/plans) 选择 SuperGrok，开通 **7 天免费试用**——可用 **Grok 前沿模型** 与 **Grok Build**（xAI 终端编程 Agent）正式付费额度；**需绑定信用卡**；试用结束前取消，否则按 **$30/月** 扣款。多半仅限**从未开通过订阅**的账号；活动下线时间暂不明确 | 一周内零成本摸清前沿模型 + 终端 Agent；记得试用结束前取消 |
| **Cline (ClinePass)** ✅ *已验证* | **ClinePass：$9.99/月**（[cline.bot/cline-pass](https://cline.bot/cline-pass)）——含 **GLM 5.3 Flash / 5.3 / 5.2**、**Kimi K3**、Kimi K2.7 Code、DeepSeek V4 Pro/Flash、MiniMax M3、MiMo、Qwen3.7/3.8 等；支持 Cline IDE、CLI 与 Desktop；API Key 可接入其他 Agent。*（早期 **$1.99** 首发价已非官网标价——以结账页为准。）* | 开源权重模型的低固定成本方案；国内想免费试 K3 仍优先 WorkBuddy |
| **Cursor** | ⚠️ **邀请首月 5 折活动已于 2026-07-23 官方下线**。当前可省：**年付约 8 折**；部分地区学生优惠；个人版仍**支持支付宝** | 仍是主流 Agentic IDE——只是已无公开邀请首月折扣 |

> 💡 **提示：** 多数商业 AI 编程工具选择年付方案，通常可节省 **约 15%–20%** 的预算。

> 若您持有有效的邀请链接或最新的促销信息，欢迎提交 Pull Request 进行补充——详见 [参与贡献](#-参与贡献)。

## 💵 零边际成本 AI 辅助开发方案

无需预算投入，依然可以构建高效的 AI 辅助开发工作流：

- **完全免费且无需 API Key：** [Freebuff](https://freebuff.com/) — 广告支持的 CLI（`npm install -g freebuff`）、Web / Desktop / Chat；DeepSeek Flash/Pro 路由（旧 V4 ID 上游已指向 **V4.1 Flash**）及其他开源权重模型。（与 [Codebuff](https://www.codebuff.com) 同公司，但是独立的免费产品线。）
- **开源自建（支持自带 Key 或本地运行，如 Ollama = $0）：** [Aider](https://aider.chat)、[Continue.dev](https://www.continue.dev)、[Cline](https://cline.bot)、[OpenCode](https://opencode.ai)。
- **既有订阅权益复用：** [OpenAI Codex](https://openai.com/codex)（已包含在 ChatGPT 免费版 / Plus 中）、[GitHub Copilot Free](https://github.com/features/copilot)（受限免费额度）。
- **厂商高额度免费层：** [Google Gemini / Antigravity](https://antigravity.google)、[Cursor Hobby](https://cursor.com)。
- **免费 OpenAI 兼容推理端点（自带 Key / BYOK）：** **NVIDIA NIM Free Tier** — 一个 API Key 覆盖较大的模型目录（包含多款热门中文模型），通过 OpenAI SDK 直接兼容：`base_url="https://integrate.api.nvidia.com/v1"`。适合原型验证与模型对比（动态限流、无 SLA，不建议高并发生产；隐私/日志条款以官网为准）。注册/开通可能需要手机号 OTP；速率限制以控制台为准（例如显示 “up to 40 RPM”）。**建议先试的默认模型（社区实测）：** `nvidia/nemotron-3-super-120b-a12b`（速度快且 `message.content` 正常返回）；部分模型可能需要调参（例如增大 `max_tokens`）。入口见 [build.nvidia.com](https://build.nvidia.com/) 与[模型目录](https://build.nvidia.com/models)。
- **腾讯云 AI 模型广场（Tencent Cloud AI Model Square）：** 新用户可在[模型广场](https://curl.qcloud.com/PN0cvBnI)页面右上角点击「**新用户福利免费体验**」领取。**所有语言模型**与**多模态理解模型**均各提供 **100 万 Token** 免费体验额度，自领取起 **90 天内**有效（含 HY3、GLM、DeepSeek、Kimi Code 等）。混元 **HY3** 另有专属 **Hy Token Plan**（最低 **¥28/月** 含 **3500 万 Token**，另含 Hy3 preview）。配合开源 BYOK 客户端（Aider、Cline、Continue 等）使用，是国内开发者零/极低成本调用旗舰模型的优选渠道。

💡 **国内开发者部署建议：** 采用开源 CLI/插件方案（如 Aider、OpenCode、Cline、Continue）并接入国内低单价的 API（如 **腾讯云模型广场、通义千问 Qwen、DeepSeek、智谱 GLM、月之暗面 Kimi、MiniMax**），可将实际运行成本降至接近于零。**最新 DeepSeek V4.1 Flash** 可优先走 **Freebuff（$0）** 或 **OpenCode Go**（抓紧 **4×** 促销窗口至 **2026-09-20**）。

## 🏗️ Agentic IDE（AI 原生集成开发环境）

具备深度 Agent 协同能力的完整 IDE——Agent 能够理解全局项目上下文、执行跨文件编辑，并在本地或沙箱环境中运行/调试代码。

| 工具 | 定价(2026-09) | 折扣 / 免费额度 | 适合 | 链接 |
|------|----------------|------------------|------|------|
| **Cursor** | Hobby: 免费（受限）<br>Pro: **$20/月（含 $20 额度）**<br>Pro+: **$60（含 $70 额度）**<br>Ultra: $200（含 $400 额度）<br>Teams Standard: $40/席（年付 $32）<br>Premium: $120/席 | ⚠️ **邀请首月 5 折活动已于 2026-07-23 官方下线**（Cursor 论坛确认）。当前可省：**年付约 8 折**；部分地区学生优惠；个人版仍**支持支付宝**。<br>· ⚠️ **GLM-5.2 免费调用已于 2026-06-26 取消**；现与其他模型一样按订阅额度扣减。 | 追求极致效率的重度用户；支持多模型切换与并行 Agent；拥有目前最活跃的社区生态 | [cursor.com](https://cursor.com) |
| **Devin Desktop**（原 Windsurf） | 免费（轻量配额，无限量 Tab 补全）<br>Pro: **$20/月**<br>Max: $200/月<br>Teams: $80/月起 + $40/全功能席位 | ✅ **新用户完成新手引导（绑定 Git 仓库）即赠送 $10 AI 额度**；订阅 Pro 及以上档位可免费调用 SWE 1.6 模型。<br>*（Pro/Max/Teams 的 GLM-5.2 / Kimi K2.7 免费窗口已于 **2026-07-05** 结束。）* | 适合需要将复杂、耗时的研发任务托管给 Devin Cloud 自动提交 PR 的场景 | [devin.ai](https://devin.ai) |
| **Google Antigravity** | 提供免费层<br>或通过 **Google AI Pro（$19.99/月）** 接入<br>AI Plus: $7.99/月<br>AI Ultra: **$99.99** / **$200（原 $250 降价）** | 包含高额度免费层；顶配 Ultra 档位已于 2026-05 从 $249.99 降至 $200；算力池每 5 小时重置一次（受限于每周总上限）；行内 Tab 补全完全免费。 | 适合多 Agent 并行协同工作流、需要内置浏览器交互及全栈 Web 开发的场景 | [antigravity.google](https://antigravity.google) |
| **Kiro**（AWS，规格驱动） | 免费: 50 credits<br>Pro: **$20/月（含 1000 credits）**<br>Pro+: $40（含 2000 credits）<br>Pro Max: **$100（含 5000 credits）**<br>Power: $200（含 10000 credits） | 支持年付折扣；超出配额按 $0.04/credit 计费。<br>· 模型消耗倍率：Auto 1.0×、Sonnet 1.3×、**Opus 4.8 2.2×**、Haiku 0.4×、GLM-5 0.5×、**Qwen3 Coder Next 0.05×** | 适用于规格驱动（Spec-driven）、强调代码可维护性与生产级交付的场景；深度集成 AWS 生态的团队 | [kiro.dev](https://kiro.dev) |
| **Trae**（字节跳动） | 免费层（每月 5000 次补全，2 个并发任务）<br>Lite: **$3/月**<br>Pro: **$10/月**（提供 7 天试用）<br>Pro+: $30/月<br>Ultra: $100/月 | ✅ **国内版（trae.cn）面向个人用户完全免费**（内置豆包与 DeepSeek 模型） | 追求类似 Cursor 交互体验、且对预算控制有极高要求的开发者 | [trae.ai](https://trae.ai) |
| **ZCode**（智谱） | 试用额度 / GLM Coding Plan | ✅ **新用户试用**仍常见（历史上为 5 天高日额度——请以官网为准）。Coding Plan 现以 **GLM-5.3 / GLM-5.3-Flash** 为主（Flash 官方宣传可用配额约 GLM-5.3 的 **3×**）。*（此前 Coding Plan **1.5×** 加成促销已于 **2026-06-30** 结束。）* | 智谱 GLM 生态深度用户、希望使用官方原生 IDE 的开发者 | [zcode.z.ai](https://zcode.z.ai/cn/docs/welcome) |
| **CodeBuddy**（腾讯，国际站） | 免费: 250 credits / 2周<br>Pro: **$9.95/月**（限时促销，原价 $19.90）或 $119.40/年（每月 1000 credits）<br>Team: $40/席/月 | 提供每两周 250 credits 的免费额度；额外加量包起售价为 $9.95/1000 credits；DeepSeek 官方合作伙伴——已支持 **V4.1 Flash** | 腾讯云海外生态用户；需要标准化云端代码助手的团队 | [codebuddy.ai](https://www.codebuddy.ai/) |
| **CodeBuddy / WorkBuddy**（腾讯，国内站） | 体验版: **免费（每月 500 credits 基础额度）**（对话功能有频次限制）<br>标准版: **¥99/月**（2000 credits）<br>旗舰版: ¥198/月<br>专享版: ¥316/月 | ✅ 通过 [WorkBuddy 邀请链接](https://www.workbuddy.cn/events/invite?inviteCode=fmfw2whmh) 注册：受邀用户获 **注册礼 2000 积分**（有效期 1 个月）+ 新手任务合计最高 **3600 credits**；**首次付费双方各得 500 积分**（受邀人仅一次，有效期 6 个月）；现已接入 **Kimi K3**（约 **1.62×**）与 **DeepSeek V4.1 Flash**（官方合作伙伴）。<br>*（HY3 全员免费窗口已于 **2026-07-22** 结束。）* | 深度依赖腾讯云生态、习惯中文研发环境的开发者；**想免费体验 Kimi K3 / V4.1 的新用户可优先尝试** | [workbuddy.cn](https://www.workbuddy.cn/events/invite?inviteCode=fmfw2whmh) / [codebuddy.cn](https://www.codebuddy.cn/pricing/) |
| **Qoder CN**（原通义灵码，阿里） | 个人社区版: **免费**（受限额度，含 2 周 Pro 试用及 300 credits）<br>个人专业版: ¥59/月（2000 credits）<br>企业版: ¥99 或 ¥199/席/月 | ⚠️ **于 2026-05-20 完成品牌重塑与定价调整**，免费层额度大幅收紧（补全频次及配额受限），原“无限期免费”政策正式终结 | 阿里云生态开发者；需要灵活切换国内主流模型（Qwen、GLM、Kimi）的团队 | [cn.aliyun.com/product/lingma](https://cn.aliyun.com/product/lingma) |
| **Zed** | 编辑器核心功能免费<br>提供 Pro 低成本订阅档位 | 核心编辑器开源且免费；<br>✅ **通过学生身份认证可获得 1 年免费会员资格**，每月包含约 $10 AI 模型调用额度 | 追求极致响应速度、本地优先及强隐私合规保障的开发者 | [zed.dev](https://zed.dev) |

## 🧩 助手与 IDE 插件

无缝集成至现有主流编辑器（如 VS Code、JetBrains 等），提供代码补全、智能对话及自主 Agent 模式。

| 工具 | 定价(2026-09) | 折扣 / 免费 | 适合 | 链接 |
|------|----------------|--------------|------|------|
| **GitHub Copilot** | 免费（每月 2000 次补全）<br>Pro: **$10/月（含 1500 AI credits）**<br>Pro+: $39/月（含 7000 credits）<br>Max: $100/月（含 20000 credits）<br>Business: $19/席/月（**1900** credits）<br>Enterprise: $39/席/月（**3900** credits） | ✅ 个人版 Pro/Pro+/Max 已自 **2026-06-17** 起逐步**重新开放注册**；Business/Enterprise 信用卡/PayPal 注册自 **2026-09-01** 起逐步重开。1 credit = $0.01；**行内补全与 Next Edit 在付费档保持免费/不限量**。学生可免费申请 Pro（详见学生福利）。<br>*（既有客户 Business/Enterprise 促销额度 3000 / 7000 已于 **2026-09-01** 结束，现恢复标准 1900 / 3900。）* | 深度依赖 GitHub 工作流的团队；企业级安全合规的首选方案 | [github.com/features/copilot](https://github.com/features/copilot) |
| **Continue.dev** | 核心功能**完全免费**（支持自带 Key 或本地 Ollama 部署）<br>Team: 约 $20/席/月 | 核心插件完全开源，支持零成本自托管 | 追求极致隐私合规、成本控制，且需要高度自定义模型接入的团队 | [continue.dev](https://www.continue.dev) |
| **Cline** | **完全免费且开源**（支持 BYOK 或本地模型）<br>**ClinePass：$9.99/月** — 含 **GLM 5.3 Flash / 5.3 / 5.2**、**Kimi K3**、Kimi K2.7 Code、DeepSeek V4 Pro/Flash、MiniMax M3、MiMo、Qwen3.7/3.8 等；支持 IDE 插件、CLI 与 Desktop | BYOK/本地模式仍为 $0；ClinePass 官方宣传额度约标准 API **2–5×**——以 [cline.bot/cline-pass](https://cline.bot/cline-pass) 为准 | 追求高自主性的 VS Code / Desktop 开发者；开源权重模型的低固定成本路径（国内免费试 K3 → 优先 WorkBuddy） | [cline.bot](https://cline.bot) |
| **Roo Code** | **完全免费且开源**（支持接入自定义 API Key） | 配合个人 API Key 即可实现按量付费，无固定订阅门槛 | 偏好 Cline 架构、但需要更丰富 Agent 工作模式的开发者 | [roocode.com](https://roocode.com) |
| **Augment Code** | 免费 Community 档位（受限）<br>试用期提供 3 万 credits（需绑定信用卡）<br>Business: **$100/月一口价**（涵盖最多 50 个席位，包含 $100等值用量）<br>Enterprise: 定制方案 | 提供 3 万 credits 免费评估额度；Business 档位采用一口价模式（50 席以内免收席位费） | 拥有大型复杂代码库、对全局上下文深度理解有强需求的团队 | [augmentcode.com](https://www.augmentcode.com) |
| **Amazon Q Developer** | ⚠️ **自 2026-05-15 起停止 IDE / 付费订阅新注册**；IDE 插件与付费订阅将于 **2027-04-30** 结束支持。既有用户过渡期内仍可使用；AWS 控制台内 Q 体验不受影响。新 Agent IDE 请迁移至 **Kiro** | 勿再规划基于 Q Developer IDE 插件的新项目 | 已在使用 Q Developer 的团队应规划迁移至 [kiro.dev](https://kiro.dev)；AWS 控制台 Q 不受影响 | [aws.amazon.com/q/developer](https://aws.amazon.com/q/developer/) |
| **Supermaven** | 免费档位（提供高速补全，支持大型代码库）<br>Pro: **$10/月**（含 1M 上下文窗口、编码风格自适应及 $5 智能对话额度）<br>Team: $10/席/月 | 免费层性能优异；Pro 档位提供 30 天免费试用 | 对代码补全响应延迟有极致要求、追求流畅编码体验的开发者 | [supermaven.com](https://supermaven.com) |
| **Qodo**（原 CodiumAI） | 免费 Developer 档位（每月包含 30 次组织级 PR 审查及 250 次 IDE/CLI 额度）<br>Teams: $30/席/月（年付）或 $38/席/月（月付） | 免费层在 PR 自动化审查与单元测试用例生成场景下极具实用价值 | 聚焦于单元测试自动生成及 PR 流程自动化审查的技术团队 | [qodo.ai](https://www.qodo.ai) |

### ⚠️ 历史免费方案变更说明（已转企业版）

以下工具曾为个人开发者社区中的热门免费方案，现已全面转型为企业级订阅模式（下线了免费层及个人计划）。保留此列表旨在帮助技术决策者规避过时评测信息的误导。

| 工具 | 现状 | 发生了什么 | 个人用户替代 |
|------|------|------------|--------------|
| **Sourcegraph Cody** | 仅限企业级订阅（约 $59/席/月，年付） | 个人免费版（Free）及专业版（Pro）已于 **2025-07 正式下线**；官方建议个人用户迁移至 Amp 平台 | [Amp](https://ampcode.com)（按量计费、零通道加价）或 [Continue.dev](https://www.continue.dev) |
| **Tabnine** | 仅限企业级订阅（$39 或 $59/席/月，年付） | 个人免费层及个人版计划已于 **2025-04 全面下线**；学术（学生）计划同步关闭 | [Cline](https://cline.bot) / [Continue.dev](https://www.continue.dev) / [Aider](https://aider.chat) |
| **Warp** | 终端基础功能免费；AI Agent 额度现需订阅 **Build 计划（$20/月）** 获得配额 | ⚠️ 免费版内置的 AI 额度已取消；免费用户目前仅支持通过 **BYOK（自带 OpenAI/Anthropic/Google API Key）** 方式调用 AI 功能，不再享有 Warp 提供的云端算力配额 | [Cursor](https://cursor.com) 或配合上述任意开源 CLI Agent 并接入自定义 Key |

## ⌨️ CLI 与终端 Agent

终端原生运行的 AI Agent——支持直接在命令行中进行代码编辑、自动化测试运行及 Git 工作流管理。

| 工具 | 定价(2026-09) | 折扣 / 免费 | 适合 | 链接 |
|------|----------------|--------------|------|------|
| **Freebuff** | **100% 免费**（广告支持；含 CLI / Web / Chat / Desktop）<br>CLI：`npm install -g freebuff` | 永久 $0，无需 API Key 或信用卡；DeepSeek Flash/Pro 路由（旧 V4 ID → **V4.1 Flash**）、Kimi、MiniMax 等；[Web 邀请链接](https://freebuff.com/web/?ref=ref-b3046190-1d77-44c1-915c-b71b4f36ae5e)。高级会话可能有每日上限 | **白嫖 DeepSeek V4.1 的首选**；零预算 CLI Agent / Web 构建 / Chat | [freebuff.com](https://freebuff.com/) |
| **Codebuff** | 订阅：**$100/月**（1× 用量）、**$200/月**（2.5×）、**$500/月**（7×）<br>按量计费：注册赠送 **500 credits**，之后 **$0.01/credit** | 注册 credits 约可支撑新项目数小时开发；随时可取消 | 深度代码库索引的高阶终端 Agent，输出质量更高；与 Freebuff 同公司，但是独立付费产品 | [codebuff.com](https://www.codebuff.com) |
| **Claude Code** | 免费版不包含 Claude Code<br>Pro: **$17/月（年付）** 或 $20/月（月付）<br>Max: 5x $100 或 20x $200<br>Team: $20–$100/席/月 | 年付方案约享 85 折优惠；使用配额基于 5 小时滚动窗口，与 Claude 网页端 Chat 共享；Max 档位设有双重周配额上限 | 追求顶尖推理能力、适用于大型复杂重构及百万级超长上下文分析的场景 | [claude.com/claude-code](https://www.claude.com/product/claude-code) |
| **Grok Build**（xAI） | Grok 对话免费层（有频次限制）<br>**SuperGrok：$30/月**<br>SuperGrok Heavy：更高档位 | ✅ **7 天 SuperGrok 免费试用**（[grok.com/plans](https://grok.com/plans)）——含 Grok 前沿模型与 Grok Build 正式额度；需绑信用卡；**试用结束前取消**以免 $30/月扣款。多半面向**从未订阅**账号；活动截止时间待定 | 基于 xAI 前沿模型的终端编程 Agent；可在不立即付费的前提下评估 | [grok.com/plans](https://grok.com/plans) |
| **Kimi**（月之暗面 / Kimi Code） | Adagio：**免费**<br>Andante：**¥49/月**<br>Moderato：¥99/月<br>Allegretto：¥199/月<br>Allegro：¥699/月<br>（年付更优惠；含 Kimi Code / Agent 共享额度池） | ⚠️ **「邀请有奖」一期抽奖已结束**（活动页公示）。正式套餐见[会员定价](https://www.kimi.com/membership/pricing)；旗舰 **Kimi K3** 已上线 Web / Code / API。**想免费摸清 K3 优先试 WorkBuddy**（邀请注册积分），或 ClinePass / OpenCode Go | 希望以会员方式使用 Kimi Code / Agent，或评估最新 **Kimi K3** | [kimi.com/membership/pricing](https://www.kimi.com/membership/pricing) |
| **OpenAI Codex** | **ChatGPT 免费版已包含 Codex 权益**（支持 Web、CLI 及桌面客户端，受限于 5 小时滚动窗口最低限额）<br>Go: $8/月<br>Plus: $20/月<br>Pro: $100–$200/月<br>Business/Enterprise: 定制方案 | 通过 ChatGPT 免费版即可实现零成本接入（无需绑定信用卡）；免费层的限时促销加量活动已结束；支持接入个人 **OpenAI API Key**（按 Token 计费，无窗口限制，但无法使用云端沙箱等高级特性） | 深度绑定 OpenAI 生态的开发者；**推荐使用官方桌面客户端（macOS/Windows）作为首选交互界面**；支持云端沙箱环境 | [openai.com/codex](https://openai.com/codex) |
| **Gemini CLI / Antigravity CLI** | **提供高额度免费层**（每日配额充足） | 极具诚意的免费额度政策 | 适合轻中度使用、且对超长上下文（Context Window）有强需求的场景 | [antigravity.google](https://antigravity.google) |
| **Ollama Cloud** | Free：$0<br>Pro：**$20/月**（或 $200/年）<br>Max：$100/月 | Pro 提供相对 Free **50×** 的云端用量，以及 **3 路云端模型并发**（Free：1；Max：10）。云端用量按 GPU 时间计量，并存在 **5 小时会话**与**7 天周度**重置窗口；本地运行模型始终无限制。 | 希望保持本地优先工作流，同时按订阅使用大模型云端算力，避免管理多家厂商 Key 的开发者 | [ollama.com/pricing](https://ollama.com/pricing) |
| **Aider** | **完全免费且开源**（仅需支付 LLM 厂商 API 费用，或配合本地模型实现 $0 运行） | 配合本地运行的开源模型可实现完全零成本 | 追求 Git 原生级结对编程（Pair Programming）体验的开发者；支持超过 75 种主流模型 | [aider.chat](https://aider.chat) |
| **Amp**（Sourcegraph） | **按量计费（Pay-As-You-Go）**，零加价直接转接原始 API 成本；首充仅需 $5 | 提供每日免费额度（约合 $10/天，按小时线性补充）——⚠️ **自 2026-05 起，该免费额度对部分用户已暂停或缩减**；目前已实现完全无广告体验 | 需要在多模型之间进行动态路由，且对上下文长度无限制要求的场景 | [ampcode.com](https://ampcode.com) |
| **Cline** | 开源版免费（支持 BYOK）<br>**ClinePass：$9.99/月** — GLM 5.3 Flash / 5.3 / 5.2、Kimi K3、DeepSeek V4、MiniMax、MiMo、Qwen3.7/3.8 等；CLI 安装：`npm i -g cline` | BYOK 仍为 $0；条款请以 [cline.bot/cline-pass](https://cline.bot/cline-pass) 为准 | 开源权重模型的低固定成本路径；国内免费试 K3 → 优先 WorkBuddy | [cline.bot](https://cline.bot) |
| **OpenCode** | 开源版免费（支持自带 Key）<br>**Go 计划：$10/月**（首月 **$5** 促销已于 **2026-08-24** 下线） | ✅ **邀请双方各得 $5 Go 用量额度**（[邀请链接](https://opencode.ai/go?ref=J9E8732NMP)）；**DeepSeek V4.1 Flash** 当前 **4×**（**$15 → $60**）至 **2026-09-20**；另含 GLM-5.3、Kimi K3、Qwen3.8、MiniMax M3、Hy3/Hy4 等 | **4× 窗口期内付费体验 V4.1 Flash 的主路径**；统一 Key 覆盖开源编程模型，可接已验证第三方 Agent | [opencode.ai](https://opencode.ai) |
| **Crush**（Charm） | **完全免费且开源**（支持接入自定义 API Key） | 配合个人 API Key 即可实现按量付费，无固定订阅门槛 | 追求极致终端交互美学（TUI）与多模型灵活切换的开发者 | [github.com/charmbracelet/crush](https://github.com/charmbracelet/crush) |
| **Goose**（Block） | **完全免费且开源**（支持接入自定义 API Key 或本地运行） | 配合个人 API Key 即可实现按量付费，无固定订阅门槛 | 需要高度可扩展本地 Agent、且深度依赖 MCP（Model Context Protocol）生态的场景 | [block.github.io/goose](https://block.github.io/goose) |
| **Qwen Code** | **完全免费且开源** | 配合本地或云端 Qwen 系列模型可实现零软件授权成本 | 深度信赖通义千问（Qwen）系列模型、追求极致成本控制的开发者 | [github.com/QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) |

## ⏳ 限时优惠与促销活动

以下为具备明确截止日期的限时优惠活动。**在进行任何决策前，请务必前往官网核实最新条款；若发现活动已过期，欢迎提交 Pull Request 进行更新。**

| 工具 | 优惠 | 截止 | 说明 |
|------|------|------|------|
| **OpenCode Go** | **DeepSeek V4.1 Flash 4× 额度**——月额度 **$15 → $60**（5 小时 / 周额度同步按 4× 放大），单价对齐官方高峰/非高峰价 | **2026-09-20** | 到期后 Flash 回到 **$15** 基础额度（除非官方延期）；Go 本体为 **$10/月** + 可选 **$5** 邀请额度——见 [OpenCode Go 文档](https://opencode.ai/docs/go/) |
| **Grok / SuperGrok**（xAI） | **7 天 SuperGrok 免费试用**——前沿 Grok + Grok Build 正式额度；入口 [grok.com/plans](https://grok.com/plans) | **待定**（活动下线时间未公布；2026-09 仍可见） | 需绑信用卡；试用结束前取消，否则按 **$30/月** 自动续费。多半仅限**从未开通过订阅**的账号 |

> 已过期的促销活动将从本节移除，相关工具仍将保留在上方对应分类中，并同步更新为常规价格信息。
>
> **近期已失效（已移出活跃列表）：** Kimi「邀请有奖」一期抽奖（**已结束——活动页公示**，**2026-09** 核实）；Cursor 邀请首月 5 折（**2026-07-23**）；WorkBuddy HY3 全员免费（**2026-07-22**）；Devin GLM-5.2 / Kimi K2.7 免费（**2026-07-05**）；ZCode / GLM Coding Plan 1.5× 加成（**2026-06-30**）；OpenCode Go 首月 $5（**2026-08-24**）；Copilot Business/Enterprise 促销额度加成（**2026-09-01**）。

## 🎓 学术与教育专属优惠

具备学术身份（如持有 `.edu` 邮箱或通过相关学术认证）的开发者，可申请免费或极高折扣的专属方案，其优惠力度通常远超常规商业促销。具体适用条款、准入门槛及支持的国家/地区请以各厂商官网为准。

| 工具 | 学生优惠 | 怎么领 |
|------|----------|--------|
| **Google Gemini** ✅ | **免费赠送 Google AI Pro 会员 1 年**——可升级为 **Gemini Pro** 权益，进而解锁 **Google Antigravity** 完整功能及更高额度的调用配额 | 需通过 Google 官方渠道完成学术身份认证（[gemini.google/students](https://gemini.google/students)） |
| **Zed** ✅ | **赠送 1 年免费会员资格**，每月包含约 **$10 AI 模型调用额度** | 需在 Zed 编辑器客户端内提交并完成学术身份认证（[zed.dev](https://zed.dev)） |
| **GitHub Copilot** ✅ | 申请成功后可作为 GitHub Student Developer Pack 的一部分，**免费使用 Copilot Pro** | 需前往 GitHub Education 官方页面提交学术认证申请（[education.github.com/pack](https://education.github.com/pack)） |
| **JetBrains 全家桶** ✅ | 在校就读期间可获得**全系 IDE 产品的免费个人授权**（包含内置的 AI 辅助功能） | 需前往 JetBrains 官网提交学术邮箱或相关证明进行申请（[jetbrains.com/student](https://www.jetbrains.com/student/)） |
| **Cursor** | 部分国家和地区提供学术免费或折扣 Pro 订阅，具体优惠状态请以当前官方政策为准 | 详情请前往官方网站查询（[cursor.com](https://cursor.com)） |

> 💡 **多重权益叠加建议：** 一名通过学术认证的学生，可同时申请并配置 **Gemini Pro（解锁 Antigravity） + Copilot Pro + JetBrains 全家桶 + Zed**，实现年度软件及算力授权成本 **$0**。

## 🎯 技术选型与决策矩阵

| 目标场景 / 需求画像 | 推荐方案 | 选型依据 |
|--------------------|----------|----------|
| **零预算 / 开源自建** | Freebuff + Aider/Cline + 本地开源模型 | 真正的零固定软件成本，完全无需订阅门槛 |
| **想用最新 DeepSeek V4.1 Flash** | **Freebuff**（$0）→ **OpenCode Go**（$10/月；抓紧 **4×** Flash 促销至 **2026-09-20**） | Freebuff 零成本摸清 Agent 能力；需要稳定额度与 API Key 时选 Go——尽快用掉 4× 窗口 |
| **个人开发者 / 成本敏感** | GitHub Copilot Pro（$10/月） | 基准订阅价格最低的成熟方案，提供无限量的行内代码补全 |
| **个人开发者 / 追求 Agentic IDE 体验** | Cursor Pro 或 Kiro Pro（$20/月） | Cursor 交互体验成熟；Kiro 适合规格驱动，也是 Amazon Q Developer 的迁移方向 |
| **高频重度用户 / 复杂工程重构** | Cursor Pro + Claude Code | 采用双轨制：日常编码与多文件编辑依赖 Cursor IDE，面对复杂架构重构与深度推理任务时调用 Claude Code 终端 Agent |
| **全栈 Web 开发** | Google Antigravity（AI Pro $19.99/月） | 原生支持多 Agent 并行协同，且内置浏览器沙箱，极大提升全栈开发与调试效率 |
| **已有 ChatGPT Plus 订阅** | OpenAI Codex | 权益复用，无需额外承担软件订阅支出 |
| **国内开发者 / 极致成本控制** | **Freebuff** / **OpenCode Go**（V4.1 Flash）/ **WorkBuddy**（邀请注册首月积分）/ 腾讯云 AI 模型广场 / ClinePass（$9.99/月）/ Aider + 国内主流模型（Qwen、DeepSeek、GLM、Kimi 等） | **想用最新 V4.1：Freebuff（免费）或 OpenCode Go（4× 至 9 月 20 日）**；想免费体验 Kimi K3 优先试 WorkBuddy——首月积分（最高约 3600）通常够用；模型广场新用户可各领 **100 万 Token**（**90 天**） |

## 💡 成本优化策略与技巧

1. **关注实际消耗，而非仅看名义订阅价。** 诸如 Copilot（按量 credits）、Antigravity（算力池）及 Codex（API Token）等主流工具目前均已引入按量计费或配额消耗机制，名义订阅费往往并非您的最终实际支出。
2. **优先选择年度订阅。** 绝大多数商业 AI 编程工具在选择年付方案时，可提供 **约 15%–20% 的预算减免**。
3. **按任务复杂度匹配模型算力。** 建立分级调用机制：常规代码修改、单文件重构或行内补全采用轻量且高响应速度的模型（如 Composer Standard、Gemini Flash、Haiku）；面对跨文件复杂重构或深层逻辑调试时，再调用高推理成本的旗舰模型。
4. **采用“开源客户端 + 自带 Key/本地运行”模式。** 通过 Aider、Cline 等开源 CLI/插件，配合本地运行的轻量模型（如 Ollama 部署）或国内低单价的 API 接口，可将运行成本控制在极低水平。
5. **DeepSeek V4.1 Flash 优先走低价渠道。** 日常编程可优先 **Freebuff（$0）**；需要稳定额度与可移植 API Key 时选 **OpenCode Go**——抓紧 **4× Flash 促销至 2026-09-20**。官方按量（`deepseek-flash`）适合要极致延迟/高并发、或 Go 额度不够时再补；灵活任务尽量排在**非高峰**时段，Token 单价可减半。
6. **合理叠加与组合免费额度。** 在考虑付费订阅前，建议优先将 Copilot 免费额度、开源 CLI 工具的免费层以及各厂商提供的基础免费配额进行组合使用，最大化榨取免费算力。
7. **建立季度复盘与评估机制。** AI 编程工具市场的竞争极度激烈，定价与配额政策几乎每月都在发生动态调整，上季度的最优选方案在当前季度未必依然适用。

## 🤝 参与贡献

本仓库的核心价值在于信息的**准确性与时效性**。我们非常欢迎并期待社区成员共同参与维护：

- **发现价格调整、全新折扣或新工具上线？** 欢迎随时 [提交 Issue](../../issues/new/choose) 或发起 Pull Request。
- **提交规范：** 请在提交时附带官方来源链接、您核实该信息的具体日期，以及（若有）折扣的有效截止时间。
- **格式指南：** 详细格式要求请参见 [CONTRIBUTING.md](CONTRIBUTING.md)。

> ⭐ 如果本项目对您的技术选型或成本优化有所帮助，欢迎点亮 Star 支持，让更多开发者受益。

## 📚 信息来源

本仓库收录的定价与产品功能信息均提炼自各厂商官方定价页面、官方更新日志（Changelog）及 2026 年度的行业对比评测；**2026 年 09 月**完成全量复核，对照 [DeepSeek API Docs](https://api-docs.deepseek.com/) / [定价页](https://api-docs.deepseek.com/quick_start/pricing) / [V4.1 Flash 公告](https://api-docs.deepseek.com/news/news260910)、[OpenCode Go 文档](https://opencode.ai/docs/go/)、[ClinePass](https://cline.bot/cline-pass)、[GitHub Copilot Changelog](https://github.blog/changelog/)、[Cursor 邀请计划下线说明](https://forum.cursor.com/t/is-the-cursor-referral-discount-program-over-will-there-be-future-referral-campaigns/166990) 与 [Amazon Q Developer 停服公告](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/)。每个工具条目中均已附带其官方网站链接。鉴于 AI 编程工具市场演进极快，**在进行任何付费决策前，请务必前往官网确认当前最新价格与服务条款**。

---

**声明：** 本项目为独立社区项目，与任何 AI 工具厂商均无商业隶属关系。部分链接为邀请/返利链接（其收益将全额用于本仓库的日常维护与运营，不会增加您的任何实际付费成本），已在对应位置明确标注。
