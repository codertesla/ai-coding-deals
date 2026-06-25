# AI 编程工具省钱指南 💰

> 一处查全 AI 编程工具的省钱信息：免费额度、新人折扣、邀请返利、开源平替。

**[English](README.md) · [简体中文](README.zh-CN.md)**

[![GitHub stars](https://img.shields.io/github/stars/codertesla/ai-coding-deals?style=social)](https://github.com/codertesla/ai-coding-deals/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/codertesla/ai-coding-deals)](https://github.com/codertesla/ai-coding-deals/commits)
[![Contributors](https://img.shields.io/github/contributors/codertesla/ai-coding-deals)](https://github.com/codertesla/ai-coding-deals/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/codertesla/ai-coding-deals)](https://github.com/codertesla/ai-coding-deals/issues)
![收录工具](https://img.shields.io/badge/收录工具-30+-blue)
![最后核实](https://img.shields.io/badge/最后核实-2026--06-brightgreen)
[![欢迎PR](https://img.shields.io/badge/PR-欢迎-orange)](CONTRIBUTING.md)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

AI 编程工具的定价变化**极快**。本仓库专门收集 **免费额度、折扣、邀请返利,以及每个工具最便宜的用法**,帮你不花冤枉钱。社区维护,对照官网核实。

> [!IMPORTANT]
> **免责声明:** 所有信息来自公开来源,可能已过时——**付费前请务必以官网最新信息为准。** 发现错误或过时?欢迎 [提交 Issue](../../issues/new/choose) 或 PR。**最近一次完整核实:2026-06。**

## 📑 目录

- [🔥 当前最值得薅的羊毛](#-当前最值得薅的羊毛)
- [💵 零成本用上 AI 编程](#-零成本用上-ai-编程)
- [🏗️ Agentic IDE(AI 原生 IDE)](#️-agentic-ideai-原生-ide)
- [🧩 助手 & IDE 扩展](#-助手--ide-扩展)
  - [⚠️ 已不再免费 / 仅企业版](#️-已不再免费--仅企业版)
- [⌨️ CLI / 终端 Agent](#️-cli--终端-agent)
- [⏳ 限时优惠](#-限时优惠)
- [🎓 学生福利](#-学生福利)
- [🎯 我该选哪个?](#-我该选哪个)
- [💡 省钱技巧](#-省钱技巧)
- [🤝 参与贡献](#-参与贡献)
- [📚 信息来源](#-信息来源)

## 🔥 当前最值得薅的羊毛

最值得马上薅的几个。(2026-06 核实,付费前再确认下官网。)

| 工具 | 优惠 | 为什么值 |
|------|------|----------|
| **Cursor** ✅ *已验证* | 新账号经**任意邀请链接首月 5 折**——Pro 首月 **$10**,更高档位也有对应折扣。每个邀请链接有使用次数上限,直接搜一个新鲜的即可(如 Google "Cursor 邀请链接 / referral link")。**支持支付宝**——记得取消自动续费。 | 2026-06 用全新账号实测有效;体验 Pro 最便宜的方式 |
| **Freebuff / Codebuff** | **100% 免费** 广告版 CLI agent,无需 API key、无订阅 | 真·零成本入门;适合在自己仓库里试免费开源模型 |
| **OpenCode** ✅ *已验证* | 经[邀请链接](https://opencode.ai/go?ref=J9E8732NMP)双方各得 **$5 额度** | 叠加低价中文模型(Qwen/DeepSeek/GLM/Kimi)更香 |
| **Devin Desktop** ✅ *已验证* | 新用户完成初始引导(连 Git)送 **$10 AI 额度**;Pro 及以上免费用 SWE 1.6 | 体验 Devin Cloud(委托出 PR 的云端 Agent)最便宜的方式 |
| **Zed**(学生)✅ | 通过学生认证可得 **一年免费会员**,每月约 $10 AI 额度 | 学生党最佳免费选项 |
| **ZCode**(智谱)✅ | 新用户 **5 天免费,每日 500 万 Token**(GLM-5.2 + GLM-5-turbo)——活动至 **2026-06-30** | 零成本体验当下热门开源模型 **GLM-5.2** |
| **GitHub Copilot** | **$10/月** Pro,sticker price 最低;**行内补全永久免费** | 即便改为按量计费仍是最便宜的能打选项 ⚠️ *2026-06-01 起新注册暂停* |
| **OpenAI Codex** | **ChatGPT 免费版即含 Codex**——Web + CLI + **桌面 App(macOS/Windows)**,无需绑卡 | $0 入门;桌面 App 是最佳入口 |
| **Google Antigravity / Gemini** | **慷慨免费层**;AI Pro 仅 **$19.99/月** | 想用多 Agent IDE + 快速 Gemini 模型,这是最便宜的入口 |
| **年付(多数工具)** | 年付省 **约 15–20%** | 如 Cursor Pro $240→$192/年,Copilot Pro $120→$100/年 |

> 有邀请链接或正在进行的促销?欢迎 PR 补充——见 [参与贡献](#-参与贡献)。

## 💵 零成本用上 AI 编程

不花一分钱也能认真做 AI 辅助开发:

- **完全免费、无需 API key:** [Freebuff](https://www.codebuff.com)(CLI,广告支持)——`npm install -g freebuff`
- **开源,自带 key 或本地模型(Ollama = $0):** [Aider](https://aider.chat)、[Continue.dev](https://www.continue.dev)、[Cline](https://cline.bot)、[OpenCode](https://opencode.ai)
- **随你可能已有的订阅附带:** [OpenAI Codex](https://openai.com/codex)(ChatGPT Plus)、[GitHub Copilot Free](https://github.com/features/copilot)(有限)
- **厂商慷慨免费层:** [Google Gemini / Antigravity](https://antigravity.google)、[Cursor Hobby](https://cursor.com)

💡 **中文用户提示:** 开源 CLI(Aider / OpenCode / Cline / Continue)可接入低价中文模型——**Qwen、DeepSeek、GLM、Kimi、MiniMax**——把成本压到接近零。

## 🏗️ Agentic IDE(AI 原生 IDE)

带深度 Agent 集成的完整 IDE——Agent 理解整个项目、跨文件编辑、在你的环境里运行。

| 工具 | 定价(2026-06) | 折扣 / 免费额度 | 适合 | 链接 |
|------|----------------|------------------|------|------|
| **Cursor** | Hobby 免费(有限)· Pro **$20/月(含 $20 用量)** · Pro+ **$60($70 用量)** · Ultra $200($400 用量)· Teams Standard $40/席(年付 $32)· Premium $120/席 | ✅ **新账号经任意邀请链接首月 5 折**(Pro 首月约 $10,更高档位同享;**支持支付宝**——记得取消自动续费,否则次月扣 $20)。链接有使用次数上限,搜一个新鲜的即可 · 年付约 8 折 · 💡 **Pro 省钱玩法:模型选 GLM-5.2 High,查看其调用记录免费、不消耗 $20 用量额度** | 重度用户;多模型 + 并行 Agent;社区最大 | [cursor.com](https://cursor.com) |
| **Devin Desktop**(原 Windsurf) | 免费(轻量 quota、无限 Tab/补全)· Pro **$20/月** · Max $200/月 · Teams $80/月起 + $40/全席位 | ✅ **新用户完成初始引导(连接 Git)送 $10 AI 额度**;**Pro 及以上免费用 SWE 1.6**;⏳ **GLM-5.2 与 Kimi K2.7 对 Pro/Max/Teams 免费至 2026-07-05** | 把重活交给 Devin Cloud 自动出 PR | [devin.ai](https://devin.ai) |
| **Google Antigravity** | 免费层 · 经 **Google AI Pro $19.99/月** · AI Plus $7.99 · AI Ultra **$99.99(5× Pro)** 与 **$200(20× Pro,原 $250 降价)** | 慷慨免费层;顶配 Ultra 由 $249.99 降至 $200(2026-05);$100 Ultra 奖励 credits 促销(已于 2026-05-25 结束);算力池每 5h 刷新至每周上限;Tab 补全免费 | 多 Agent 并行;内置浏览器;全栈 Web | [antigravity.google](https://antigravity.google) |
| **Kiro**(AWS,规格驱动) | 免费 50 credits · Pro **$20/月(1000)** · Pro+ $40(2000)· **Pro Max $100(5000)** · Power $200(10000) | 年付折扣;超量 $0.04/credit · 倍率:Auto 1.0× · Sonnet 1.3× · **Opus 4.8 2.2×** · Haiku 0.4× · GLM-5 0.5× · **Qwen3 Coder Next 0.05×** | 规格驱动、可维护的生产级代码;AWS 团队 | [kiro.dev](https://kiro.dev) |
| **Trae**(字节跳动) | 免费层(5000 补全/月,2 并发)· Lite **$3** · Pro **$10**(7 天试用)· Pro+ $30 · Ultra $100 | ✅ **国内版 trae.cn 个人完全免费**(用豆包/DeepSeek) | 想要 Cursor 式 IDE 的预算用户 | [trae.ai](https://trae.ai) |
| **ZCode**(智谱) | 活动免费额度 · 经 GLM Coding Plan 付费 | ✅ **新用户 5 天免费,每日 500 万 Token**(GLM-5.2 300万 + GLM-5-turbo 200万);GLM Coding Plan 订阅用户享 **1.5 倍配额**——活动至 **2026-06-30** | 想用智谱官方 GLM IDE 的开发者 | [zcode.z.ai](https://zcode.z.ai/cn/docs/welcome) |
| **CodeBuddy**(腾讯,国际站)| Free(250 credits / 2 周)· Pro **$9.95/月**(促销价,原 $19.90)/ $119.40/年(每月 1000 credits)· Team $40/人/月 | 免费 250 credits/2 周;加量包 $9.95/1000 credits 起 | 国际用户;腾讯云代码助手 | [codebuddy.ai](https://www.codebuddy.ai/) |
| **CodeBuddy**(腾讯,国内站)| 体验版 **免费:每月 500 credits**(对话有频次限制)· 专业版 ¥58/月(2000 credits)· 旗舰版 ¥198 · 专享版 ¥316 | 每月 500 credits 免费;⚠️ 订阅升级 **2026-07-01 生效** | 用腾讯云的中文开发者 | [codebuddy.cn](https://www.codebuddy.cn/pricing/) |
| **Qoder CN**(原通义灵码,阿里) | 个人社区版 **免费**(有限额度,含 2 周 Pro 试用 + 300 credits)· 个人专业版 ¥59/月(2000 credits)· 企业版 ¥99/¥199/席 | ⚠️ **2026-05-20 改名并改定价**,免费层实质削弱(补全有限 + 限额);旧"无限免费"时代结束 | 阿里云上的中文开发者;多模型(Qwen/GLM/Kimi) | [cn.aliyun.com/product/lingma](https://cn.aliyun.com/product/lingma) |
| **Zed** | 编辑器免费 · Pro 低价档 | 核心编辑器免费 · ✅ **学生认证后可得一年免费会员**,含每月约 $10 AI 模型额度 | 追求速度、本地优先、隐私友好 | [zed.dev](https://zed.dev) |

## 🧩 助手 & IDE 扩展

接入你现有编辑器(VS Code / JetBrains),提供补全、对话和 Agent 模式。

| 工具 | 定价(2026-06) | 折扣 / 免费 | 适合 | 链接 |
|------|----------------|--------------|------|------|
| **GitHub Copilot** | 免费(2000 补全/月)· Pro **$10/月 = 1500 AI credits** · Pro+ $39 = 7000 · Max $100 = 20000 · Business $19/人 · Enterprise $39/人 | ⚠️ **2026-06-01 起 Pro/Pro+/Max 新用户注册暂停**(Max 仅限现有用户升级)。1 credit = $0.01;**行内补全与 Next Edit 永久免费**。学生免费用 Pro(见学生福利)。 | GitHub 团队;最稳妥的企业选择 | [github.com/features/copilot](https://github.com/features/copilot) |
| **Continue.dev** | 核心 **免费**(自带 key 或本地 Ollama = $0)· Team 约 $20/席/月 | 完全可免费自托管 | 隐私 & 成本控制;任意模型 | [continue.dev](https://www.continue.dev) |
| **Cline** | **免费开源**(自带 key / 本地模型) | 用自己 key 即 $0 | 低成本的 VS Code 自主 Agent | [cline.bot](https://cline.bot) |
| **Roo Code** | **免费开源**(自带 key) | 用自己 key 即 $0 | Cline 分支,额外 Agent 模式 | [roocode.com](https://roocode.com) |
| **Augment Code** | 免费 Community(有限)· 试用 3 万 credits(需绑卡)· Business **$100/月一口价**(最多 50 席,含 $100 用量)· Enterprise 定制 | 3 万 credits 试用;Business 一口价(50 席内无按席收费) | 需要深度上下文的大型代码库 | [augmentcode.com](https://www.augmentcode.com) |
| **Amazon Q Developer** | **永久免费**(每月 50 次 agentic 请求 + 1000 行代码转换)· Pro **$19/人/月** | 慷慨的永久免费层(IDE + CLI),无需绑卡 | AWS 生态团队;Java/.NET 老项目改造 | [aws.amazon.com/q/developer](https://aws.amazon.com/q/developer/) |
| **Supermaven** | **免费**(快速补全,大代码库)· Pro **$10/月**(1M 上下文 + 风格适应 + $5 chat credits)· Team $10/席 | 免费层够用;Pro 30 天试用 | 追求"最快补全"的开发者 | [supermaven.com](https://supermaven.com) |
| **Qodo**(原 CodiumAI) | **免费 Developer**(每月 30 次 PR review/组织 + 250 IDE/CLI credits)· Teams $30/人/月(年付)/ $38(月付) | 免费层对 PR review + 测试生成很实用 | 主打测试生成 + PR review | [qodo.ai](https://www.qodo.ai) |

### ⚠️ 已不再免费 / 仅企业版

这几个以前都是热门免费选项,现在已经转成纯企业版,免费层和个人版都砍了。留着它们,是免得你被那些还在写"免费"的旧文章误导。

| 工具 | 现状 | 发生了什么 | 个人用户替代 |
|------|------|------------|--------------|
| **Sourcegraph Cody** | 仅企业版(约 $59/人/月,年付) | Free/Pro 已于 **2025-07 下线**;官方建议个人转用 Amp | [Amp](https://ampcode.com)(按量付费、零加价)或 [Continue.dev](https://www.continue.dev) |
| **Tabnine** | 仅企业版——$39 / $59 每人/月(年付) | 免费层与个人版已于 **2025-04 下线**;学生计划也已关闭 | [Cline](https://cline.bot) / [Continue.dev](https://www.continue.dev) / [Aider](https://aider.chat) |
| **Warp** | 终端免费;AI agent 用量现需 **Build $20/月** 才有 bundled 额度 | ⚠️ 免费 bundled AI 额度已取消;免费用户只能通过 **BYOK**(自带 OpenAI/Anthropic/Google key)用 AI,无 Warp 额度 | [Cursor](https://cursor.com) 或上方任意 CLI agent + 自带 key |

## ⌨️ CLI / 终端 Agent

在终端里直接运行 Agent——改代码、跑测试、管理 git。

| 工具 | 定价(2026-06) | 折扣 / 免费 | 适合 | 链接 |
|------|----------------|--------------|------|------|
| **Freebuff**(免费版 Codebuff) | **100% 免费**(广告支持,无需 API key) | 永久 $0;可选绑定 ChatGPT 订阅 | 零成本入门;试免费开源模型 | [codebuff.com](https://www.codebuff.com) |
| **Claude Code** | Free **不含 Claude Code** · Pro **$17/月(年付)/$20(月付)** · Max 5x $100 · Max 20x $200 · Team $20–$100/席 | 年付约 85 折;5h 滚动窗口(2026-05-06 已翻倍),与 Claude 聊天共享;Max 有两个周限额 | 最强推理(Opus 4.8);大型重构;1M 上下文 | [claude.com/claude-code](https://www.claude.com/product/claude-code) |
| **OpenAI Codex** | **ChatGPT Free 即含 Codex**(Web + CLI + 桌面 App,5h 窗口最低限额)· Go $8 · Plus $20 · Pro $100–$200 · Business/Enterprise | $0 经 ChatGPT 免费版(无需绑卡);免费层的促销加量已结束;也可用自带 **OpenAI API key**(按 token,无窗口限制但无云功能) | OpenAI 生态;**桌面 App(macOS/Windows)是官方推荐的主入口**;云沙箱 | [openai.com/codex](https://openai.com/codex) |
| **Gemini CLI / Antigravity CLI** | **免费层**(每日额度慷慨) | 非常慷慨的免费层 | 轻中度使用;超大上下文 | [antigravity.google](https://antigravity.google) |
| **Aider** | **免费开源**(仅付 LLM API,或本地 = $0) | 用本地模型即 $0 | Git 原生 pair programming;75+ 模型 | [aider.chat](https://aider.chat) |
| **Amp**(Sourcegraph) | **按量付费,零加价**转 API 成本;$5 起充 | 每日免费额度(约 $10/天,按小时补充)——⚠️ **2026-05 起对部分用户暂停/缩减**;现已无广告 | 多模型路由(GPT-5.5/Opus);上下文不受限 | [ampcode.com](https://ampcode.com) |
| **OpenCode** | 开源免费(自带 key)· **Go 计划:首月 $5,之后 $10/月**(约 $60/月用量:5h $12 · 周 $30) | ✅ **邀请双方各得 $5 额度**([邀请链接](https://opencode.ai/go?ref=J9E8732NMP)) | 一个 key 用 14 个开源模型(GLM-5.2、Kimi、Qwen、DeepSeek…);可配任意 agent | [opencode.ai](https://opencode.ai) |
| **Crush**(Charm) | **免费开源**(自带 key) | 用自己 key 即 $0 | 终端体验精美;多模型 | [github.com/charmbracelet/crush](https://github.com/charmbracelet/crush) |
| **Goose**(Block) | **免费开源**(自带 key / 本地) | 用自己 key 即 $0 | 可扩展的本地 Agent;MCP 原生 | [block.github.io/goose](https://block.github.io/goose) |
| **Qwen Code** | **免费开源** | $0(用 Qwen 模型) | 用 Qwen 模型的省钱用户 | [github.com/QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) |

## ⏳ 限时优惠

有截止日期的折扣——趁还在赶紧薅。**使用前请以官网为准;过期后欢迎 PR 更新。**

| 工具 | 优惠 | 截止 | 说明 |
|------|------|------|------|
| **Devin Desktop** | **GLM-5.2 与 Kimi K2.7 对 Pro/Max/Teams 免费**(前沿开源模型:GLM-5.2 43.0%、Kimi K2.7 39.5% FrontierCode Extended,对比 GPT-5.5 44.8% / Opus 4.8 51.8%) | **2026-07-05** | [devin.ai](https://devin.ai);另:新用户完成初始引导(连 Git)送 **$10 AI 额度** |
| **ZCode**(智谱) | 新用户 **5 天免费,每日 500 万 Token**(GLM-5.2 300万 + GLM-5-turbo 200万);GLM Coding Plan 订阅用户享 **1.5 倍配额** | 原公告 **2026-06-30**(截至 2026-06-25 官网仍列此项,以官网为准) | 零成本体验开源 **GLM-5.2**;[zcode.z.ai](https://zcode.z.ai/cn/docs/welcome) |

> 过期的优惠会从本节移除,工具仍保留在上方对应分类里,并更新为常规信息。

## 🎓 学生福利

有学生 / `.edu` 身份的话,不少工具能**免费或打折**用,有的比正价划算很多。具体条款和支持的国家/地区,以各厂商官网为准。

| 工具 | 学生优惠 | 怎么领 |
|------|----------|--------|
| **Google Gemini** ✅ | **免费 Google AI Pro 一年**——升级为 **Gemini Pro**,从而解锁 **Google Antigravity** 及更高用量额度 | 用 Google 完成学生认证([gemini.google/students](https://gemini.google/students)) |
| **Zed** ✅ | **一年免费会员**,含每月约 **$10 AI 模型额度** | 在 Zed 内完成学生认证([zed.dev](https://zed.dev)) |
| **GitHub Copilot** ✅ | 随 GitHub 学生开发包**免费用 Copilot Pro** | 申请 [education.github.com/pack](https://education.github.com/pack) |
| **JetBrains 全家桶** ✅ | 在校期间**全系 IDE 免费个人授权**(含 AI 功能) | 申请 [jetbrains.com/student](https://www.jetbrains.com/student/) |
| **Cursor** | 部分地区有学生免费/折扣 Pro,需自行确认当前状态 | 查看 [cursor.com](https://cursor.com) |

> 💡 叠加起来:一个认证学生可以 **Gemini Pro(→ Antigravity)+ Copilot Pro + JetBrains + Zed** 全部 **$0/年**。

## 🎯 我该选哪个?

| 你的情况 | 推荐 | 理由 |
|----------|------|------|
| **预算为 0** | Freebuff + Aider/Cline + 本地模型 | 真免费,无订阅 |
| **个人、预算敏感** | GitHub Copilot Pro($10/月) | 最便宜的能打选项,补全无限 |
| **个人、想要 Agentic IDE** | Cursor Pro 或 Kiro Pro($20/月) | Cursor 体验好,Kiro 更结构化 |
| **重度用户、复杂项目** | Cursor Pro + Claude Code | 日常用 IDE,硬骨头交给 Claude Code |
| **全栈 Web** | Google Antigravity(AI Pro $19.99/月) | 多 Agent + 内置浏览器 |
| **已付 ChatGPT** | OpenAI Codex | 不额外花钱 |
| **中文、极致省钱** | OpenCode/Aider + Qwen/DeepSeek/GLM/Kimi | 自带 key 用低价模型 |

## 💡 省钱技巧

1. **盯用量,别只看标价。** Copilot(按量 credits)、Antigravity(算力池)、Codex(API token)现在都按量计费,月费不等于真实成本。
2. **年付** 多数订阅工具省约 15–20%。
3. **模型对应任务。** 日常小改用便宜快模型(Composer Standard、Gemini Flash、Haiku),硬重构才上昂贵推理模型。
4. **自带 key + 本地模型。** 开源 CLI 配 Ollama 或低价 API,可把成本压到接近零。
5. **叠加免费层。** 先把 Copilot Free + 免费 CLI + 厂商免费层组合用满,再考虑付费。
6. **每季度复盘。** 这里的定价每月都在变,上季度的最优解这季度未必是。

## 🤝 参与贡献

这个仓库靠的就是**准确和及时**,欢迎一起来维护:

- **发现降价、新折扣或新工具?** [提交 Issue](../../issues/new/choose) 或发 PR。
- **请附上:** 官方来源链接、你核实的日期,以及(折扣)有效期。
- 格式见 [CONTRIBUTING.md](CONTRIBUTING.md)。

> ⭐ 如果帮你省了钱,点个 Star 让更多人看到。

## 📚 信息来源

定价和产品信息来自各厂商的官方定价页、更新日志,以及 2026 年的一些对比测评,核实时间为 **2026-06**。每个工具都链接了官网(见上)。这行变化太快,**付费前请在官网确认当前价格**。

---

*与任何厂商均无隶属关系。部分链接可能为邀请/返利链接(用于维护本仓库,对你不产生额外费用),使用处会标注。*
