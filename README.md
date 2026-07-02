# AI Coding Cost Optimization & Selection Guide 💰

> A comprehensive guide to AI coding tool selection and cost optimization — tracking free tiers, commercial discounts, referral credits, and open-source alternatives in one place.

**[English](README.md) · [简体中文](README.zh-CN.md)**

[![GitHub stars](https://img.shields.io/github/stars/codertesla/ai-coding-deals?style=social)](https://github.com/codertesla/ai-coding-deals/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/codertesla/ai-coding-deals)](https://github.com/codertesla/ai-coding-deals/commits)
[![Contributors](https://img.shields.io/github/contributors/codertesla/ai-coding-deals)](https://github.com/codertesla/ai-coding-deals/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/codertesla/ai-coding-deals)](https://github.com/codertesla/ai-coding-deals/issues)
![Tools tracked](https://img.shields.io/badge/tools_tracked-30+-blue)
![Last verified](https://img.shields.io/badge/last_verified-2026--06-brightgreen)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-orange)](CONTRIBUTING.md)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

AI coding tool pricing and quotas evolve rapidly. This repository tracks **free tiers, commercial discounts, referral credits, and highly cost-effective deployment strategies** to help developers and technical teams optimize their AI spend. Maintained by the community and verified against official vendor documentation.

> [!IMPORTANT]
> **Disclaimer:** All information is aggregated from public sources and is subject to change. **Always verify pricing, quotas, and terms on the vendor's official website before making purchasing decisions.** Spot an error or outdated entry? Please [open an issue](../../issues/new/choose) or submit a Pull Request. **Last comprehensive verification: June 2026.**

## 📑 Contents

- [🔥 Featured Deals & Cost-Savers](#-featured-deals--cost-savers)
- [💵 Zero-Budget AI Coding Strategies](#-zero-budget-ai-coding-strategies)
- [🏗️ Agentic IDEs (AI-Native Integrated Development Environments)](#️-agentic-ides-ai-native-integrated-development-environments)
- [🧩 Assistants & IDE Extensions](#-assistants--ide-extensions)
  - [⚠️ Legacy Free Tier Changes (Enterprise Transition)](#️-legacy-free-tier-changes-enterprise-transition)
- [⌨️ CLI & Terminal Agents](#️-cli--terminal-agents)
- [⏳ Time-Limited Promos](#-time-limited-promos)
- [🎓 Academic & Student Benefits](#-academic--student-benefits)
- [🎯 Decision Matrix & Scenario-Based Recommendations](#-decision-matrix--scenario-based-recommendations)
- [💡 Strategic Cost-Optimization Advice](#-strategic-cost-optimization-advice)
- [🤝 Contributing](#-contributing)
- [📚 Sources](#-sources)

## 🔥 Featured Deals & Cost-Savers

High-value promotions and cost-saving opportunities currently active. (Verified June 2026 — please confirm on the official vendor page before purchasing.)

| Tool | The deal | Why it's worth it |
|------|----------|-------------------|
| **Cursor** ✅ *verified* | **50% off your first month** for new accounts via any referral link — Pro for **$10** (first month), with proportional discounts on higher tiers. Referral links have usage limits; search for a fresh link (e.g., search "Cursor referral link"). **Alipay accepted** — remember to cancel auto-renew if you do not plan to continue. | Verified June 2026 on a new account; the lowest-cost entry point to evaluate Pro features |
| **Freebuff** | **100% free** ad-supported coding agent (CLI / Web / Chat) at [freebuff.com](https://freebuff.com/) — requires no API key or subscription; [Web referral link](https://freebuff.com/web/?ref=ref-b3046190-1d77-44c1-915c-b71b4f36ae5e) | Genuinely $0; CLI via `npm install -g freebuff`; open-source models (DeepSeek, Kimi, MiniMax, etc.) — a separate free product from the same company as [Codebuff](https://www.codebuff.com) |
| **Cline (ClinePass)** | **$1.99/month launch promo** (standard **$9.99/month**) when signing up via `npm i -g cline` — bundled access to 10+ open-weight models (GLM-5.2, Kimi K2.7 Code, DeepSeek V4, Qwen3.7, MiniMax, MiMo, etc.) at **2–5× API rate limits**; available on Cline CLI & IDE | One of the lowest fixed-cost paths to GLM-5.2 and Kimi K2.7 Code; promo end date not yet announced — verify at [cline.bot](https://cline.bot) or [x.com/cline](https://x.com/cline) |
| **OpenCode** ✅ *verified* | **$5 free credit** for both parties when signing up via [referral link](https://opencode.ai/go?ref=J9E8732NMP) | Highly cost-effective when paired with low-cost regional models (e.g., Qwen, DeepSeek, GLM, Kimi) |
| **Devin Desktop** ✅ *verified* | New users receive **$10 AI credit** upon completing onboarding (connecting a Git repository); Pro and above tiers include free access to the SWE 1.6 model | The lowest-cost path to evaluate Devin Cloud (autonomous PR-creation agent) |
| **Zed** *(students)* ✅ | **Free 1-year membership** including ~$10/month in AI model credits upon academic verification | The premier free option for verified students and academic developers |
| **ZCode** *(Zhipu)* ✅ | New users receive a **5-day free trial with 5M free tokens/day** (GLM-5.2 and GLM-5-turbo allocation) — promotion active through **2026-06-30** | The most accessible way to evaluate the capabilities of the open **GLM-5.2** model |
| **GitHub Copilot** | **$10/month** Pro tier — lowest nominal subscription price; **inline completions remain free** | Highly cost-effective baseline option even with usage-based metrics ⚠️ *New sign-ups paused since 2026-06-01* |
| **OpenAI Codex** | **Included in ChatGPT Free** — accessible via Web, CLI, and **desktop applications (macOS/Windows)** with no credit card required | Zero-budget entry point; utilizing the official desktop application provides the optimal workflow |
| **Google Antigravity / Gemini** | Generous **free tier**; AI Pro subscription available at **$19.99/month** | Cost-effective entry point for evaluating multi-agent workflows and high-speed Gemini models |

> 💡 **Tip:** Most subscription-based AI coding tools offer **~15%–20% savings** when billed annually.

> Have an active referral link or a new promotion to share? Please submit a Pull Request — see [Contributing](#-contributing).

## 💵 Zero-Budget AI Coding Strategies

High-quality AI-assisted development is entirely feasible without direct software budget allocation:

- **Fully Free & No API Key Required:** [Freebuff](https://freebuff.com/) — ad-supported CLI (`npm install -g freebuff`), Web app builder, and Chat; powered by open-source models. *(Same company as [Codebuff](https://www.codebuff.com), but a separate free product line.)*
- **Open-Source Self-Hosted (Bring-Your-Own-Key or Local Models, e.g., Ollama = $0):** [Aider](https://aider.chat), [Continue.dev](https://www.continue.dev), [Cline](https://cline.bot), [OpenCode](https://opencode.ai).
- **Leveraging Existing Subscriptions:** [OpenAI Codex](https://openai.com/codex) (included with ChatGPT Plus), [GitHub Copilot Free](https://github.com/features/copilot) (limited baseline quota).
- **Generous Vendor Free Tiers:** [Google Gemini / Antigravity](https://antigravity.google), [Cursor Hobby](https://cursor.com).
- **Free OpenAI-Compatible Inference Endpoint (BYOK):** **NVIDIA NIM Free Tier** — one API key across a large model catalog (incl. popular Chinese models), compatible with the OpenAI SDK via `base_url="https://integrate.api.nvidia.com/v1"`. Best for prototyping and model comparisons (rate-limited; no SLA; terms/logging policies apply). Signup may require phone OTP; rate limits vary (e.g. dashboard may show “up to 40 RPM”). **Suggested first model to try (community-tested):** `nvidia/nemotron-3-super-120b-a12b` (fast + returned normal `message.content`); some other models may require tuning (e.g. higher `max_tokens`). See [build.nvidia.com](https://build.nvidia.com/) and the [model catalog](https://build.nvidia.com/models).

💡 **Deployment Tip for Regional Developers:** Utilizing open-source CLI agents or extensions (such as Aider, OpenCode, Cline, or Continue) allows you to integrate highly cost-effective regional APIs (e.g., **Qwen, DeepSeek, GLM, Kimi, MiniMax**), reducing ongoing operational costs to near-zero.

## 🏗️ Agentic IDEs (AI-Native Integrated Development Environments)

Complete integrated development environments featuring deep agentic workflows — allowing the AI agent to understand global project context, perform cross-file edits, and execute or debug code in local or sandboxed environments.

| Tool | Pricing (2026-06) | Discounts / free credits | Best for | Link |
|------|-------------------|--------------------------|----------|------|
| **Cursor** | Hobby: Free (limited)<br>Pro: **$20/mo (includes $20 quota)**<br>Pro+: **$60 (includes $70 quota)**<br>Ultra: $200 (includes $400 quota)<br>Teams Standard: $40/seat (annual $32)<br>Premium: $120/seat | ✅ **New accounts receive 50% off the first month via any referral link** (Pro tier ≈ $10 first month; higher tiers eligible; **Alipay accepted** — remember to cancel auto-renew to avoid the standard $20 billing in the second month). Referral links have usage caps; search for active links.<br>· Annual plans offer ~20% savings.<br>· ⚠️ **GLM-5.2 free usage ended on 2026-06-26** (verified); calls now deduct from your subscription quota like other models. | Power users; multi-model flexibility and parallel agentic workflows; largest developer community | [cursor.com](https://cursor.com) |
| **Devin Desktop**（formerly Windsurf） | Free (light quota, unlimited Tab completions)<br>Pro: **$20/mo**<br>Max: $200/mo<br>Teams: $80/mo base + $40/full seat | ✅ **New users receive $10 AI credit** upon completing onboarding (connecting a Git repository); Pro and above tiers include free access to the SWE 1.6 model;<br>⏳ **Limited-Time Promo: GLM-5.2 and Kimi K2.7 models are free for Pro/Max/Teams users until 2026-07-05** | Delegating complex, long-running engineering tasks to Devin Cloud for automated PR creation | [devin.ai](https://devin.ai) |
| **Google Antigravity** | Free tier available<br>or via **Google AI Pro ($19.99/mo)**<br>AI Plus: $7.99/mo<br>AI Ultra: **$99.99** / **$200 (reduced from $250)** | Includes a generous free tier; top-tier Ultra pricing reduced from $249.99 to $200 in May 2026; compute pools reset every 5 hours (subject to a weekly cap); inline Tab completion is entirely free. | Multi-agent parallel workflows, built-in browser interaction, and full-stack web development | [antigravity.google](https://antigravity.google) |
| **Kiro**（AWS, spec-driven） | Free: 50 credits<br>Pro: **$20/mo (includes 1,000 credits)**<br>Pro+: $40 (includes 2,000 credits）<br>Pro Max: **$100 (includes 5,000 credits)**<br>Power: $200 (includes 10,000 credits) | Annual billing discounts available; overage billed at $0.04/credit.<br>· Model consumption multipliers: Auto 1.0×, Sonnet 1.3×, **Opus 4.8 2.2×**, Haiku 0.4×, GLM-5 0.5×, **Qwen3 Coder Next 0.05×** | Spec-driven development emphasizing highly maintainable production-grade code; AWS-centric engineering teams | [kiro.dev](https://kiro.dev) |
| **Trae**（ByteDance） | Free tier (5K autocompletions/month, 2 concurrent tasks)<br>Lite: **$3/mo**<br>Pro: **$10/mo** (includes 7-day trial)<br>Pro+: $30/mo<br>Ultra: $100/mo | ✅ **The regional version (trae.cn) is completely free** for individual developers (utilizing Doubao and DeepSeek models) | Budget-conscious developers seeking a Cursor-like user experience | [trae.ai](https://trae.ai) |
| **ZCode**（Zhipu） | Promotional free credits<br>or paid via GLM Coding Plan | ✅ **New users receive a 5-day free trial with 5M tokens/day** (GLM-5.2 3M and GLM-5-turbo 2M allocation); GLM Coding Plan subscribers receive a **1.5× quota multiplier** — active through **2026-06-30** | Developers seeking an official, deeply integrated IDE for the GLM model ecosystem | [zcode.z.ai](https://zcode.z.ai/cn/docs/welcome) |
| **CodeBuddy**（Tencent, international） | Free: 250 credits / 2 weeks<br>Pro: **$9.95/mo** (promo price, originally $19.90) or $119.40/year (1,000 credits/month)<br>Team: $40/seat/month | Provides 250 credits per 2 weeks; additional credit packs start at $9.95 per 1,000 credits | Global developers; standardized coding assistance within the Tencent Cloud ecosystem | [codebuddy.ai](https://www.codebuddy.ai/) |
| **CodeBuddy**（Tencent, regional） | Trial: **Free (500 credits/month)** (rate-limited chat)<br>Professional: ¥58/month (2,000 credits)<br>Flagship: ¥198/month<br>Exclusive: ¥316/month | Provides 500 credits/month free; ⚠️ subscription restructuring takes effect **2026-07-01** | Regional developers operating primarily within the Tencent Cloud ecosystem | [codebuddy.cn](https://www.codebuddy.cn/pricing/) |
| **Qoder CN**（formerly Tongyi Lingma, Alibaba） | Community: **Free** (restricted quota, includes 2-week Pro trial and 300 credits)<br>Professional: ¥59/month (2,000 credits)<br>Enterprise: ¥99 or ¥199/seat/month | ⚠️ **Rebranded and repriced on 2026-05-20**; the free tier has been significantly restricted (limited completions and quotas), ending the previous unlimited-free era | Developers within the Alibaba Cloud ecosystem requiring flexible switching between regional models (Qwen, GLM, Kimi) | [cn.aliyun.com/product/lingma](https://cn.aliyun.com/product/lingma) |
| **Zed** | Editor core features free<br>Low-cost Pro subscription tier available | Core editor is open-source and free;<br>✅ **Verified students receive a free 1-year membership** including ~$10/month in AI model credits | Developers prioritizing extreme speed, local-first workflows, and strong privacy compliance | [zed.dev](https://zed.dev) |

## 🧩 Assistants & IDE Extensions

Integrate seamlessly into your existing editor (such as VS Code or JetBrains) to provide inline code completions, interactive chat, and autonomous agent modes.

| Tool | Pricing (2026-06) | Discounts / free | Best for | Link |
|------|-------------------|------------------|----------|------|
| **GitHub Copilot** | Free (2,000 completions/month)<br>Pro: **$10/mo (includes 1,500 AI credits)**<br>Pro+: $39/mo (includes 7,000 credits)<br>Max: $100/mo (includes 20,000 credits)<br>Business: $19/user/month<br>Enterprise: $39/user/month | ⚠️ **New sign-ups for Pro/Pro+/Max paused since 2026-06-01** (Max is upgrade-only for existing users). 1 credit equals $0.01; **inline completions and Next Edit features remain free**. Students can access Copilot Pro for free (see Academic & Student Benefits). | GitHub-centric workflows; the standard choice for enterprise-grade compliance | [github.com/features/copilot](https://github.com/features/copilot) |
| **Continue.dev** | Core features **completely free** (supports BYOK or local Ollama deployments)<br>Team: ~$20/seat/month | Completely open-source and free to self-host | Teams prioritizing strict privacy compliance, cost control, and custom model integration | [continue.dev](https://www.continue.dev) |
| **Cline** | **Free and open-source** (supports BYOK or local models)<br>**ClinePass: $9.99/mo** — bundled access to 10+ open-weight models (GLM-5.2, Kimi K2.7 Code, DeepSeek V4, Qwen3.7, MiniMax, MiMo, etc.) at 2–5× API rate limits; works on IDE extension & CLI | ⏳ **ClinePass launch promo: $1.99/mo** when signing up via `npm i -g cline` (end date TBD — verify at [cline.bot](https://cline.bot)); BYOK/local mode remains $0 | Developers seeking a highly autonomous VS Code agent; ClinePass is a low fixed-cost alternative to assembling regional API keys individually | [cline.bot](https://cline.bot) |
| **Roo Code** | **Free and open-source** (supports custom API keys) | $0 software cost when paired with your own API key for pay-as-you-go billing | Developers preferring the Cline architecture but requiring additional specialized agent modes | [roocode.com](https://roocode.com) |
| **Augment Code** | Free Community tier (restricted)<br>Trial: 30K credits (requires credit card)<br>Business: **$100/month flat rate** (covers up to 50 seats, includes $100 usage)<br>Enterprise: Custom pricing | Provides a 30K-credit trial; flat-rate Business pricing (no per-seat fees up to 50 seats) | Teams working with large, complex codebases requiring deep, global context | [augmentcode.com](https://www.augmentcode.com) |
| **Amazon Q Developer** | **Perpetual free tier** (includes 50 agentic requests/month and 1,000 lines of code transformation/month)<br>Pro: **$19/user/month** | Generous free tier covering both IDE and CLI with no credit card required | AWS-centric engineering teams; ideal for Java and .NET legacy codebase modernization | [aws.amazon.com/q/developer](https://aws.amazon.com/q/developer/) |
| **Supermaven** | Free tier (high-speed completions, supports large repositories)<br>Pro: **$10/month** (includes 1M context window, coding style adaptation, and $5 chat credits)<br>Team: $10/seat/month | Highly capable free tier; Pro plan offers a 30-day trial | Developers prioritizing near-zero latency and high-speed autocomplete performance | [supermaven.com](https://supermaven.com) |
| **Qodo**（formerly CodiumAI） | Free Developer tier (includes 30 organization-level PR reviews/month and 250 IDE/CLI credits)<br>Teams: $30/user/month (annual) or $38/user/month (monthly) | Highly practical free tier focusing on automated PR reviews and unit test generation | Technical teams focusing on automated test suite generation and PR workflow auditing | [qodo.ai](https://www.qodo.ai) |

### ⚠️ Legacy Free Tier Changes (Enterprise Transition)

The following tools previously offered popular free or individual tiers but have since transitioned exclusively to enterprise-only models (discontinuing all free and individual plans). They are preserved here to prevent confusion from outdated articles or reviews.

| Tool | Status | What happened | For individuals, use instead |
|------|--------|---------------|------------------------------|
| **Sourcegraph Cody** | Enterprise-only subscription (~$59/user/month, annual) | Free and Pro plans were **discontinued in July 2025**; official documentation recommends individual developers migrate to Amp | [Amp](https://ampcode.com) (pay-as-you-go, zero-markup API pricing) or [Continue.dev](https://www.continue.dev) |
| **Tabnine** | Enterprise-only subscription ($39 or $59/user/month, annual) | The free tier and all individual plans were **discontinued in April 2025**; the academic student program has been closed | [Cline](https://cline.bot) / [Continue.dev](https://www.continue.dev) / [Aider](https://aider.chat) |
| **Warp** | Terminal core features free; AI Agent capabilities now require the **Build plan ($20/month)** for bundled credits | ⚠️ Free bundled AI credits have been removed; free-tier users are restricted to **BYOK (Bring-Your-Own-Key)** mode for OpenAI, Anthropic, or Google APIs with no Warp-provided compute allocation | [Cursor](https://cursor.com) or any of the open-source CLI agents listed above with your own API key |

## ⌨️ CLI & Terminal Agents

AI agents running natively in the terminal — capable of direct codebase editing, automated test execution, and Git workflow management.

| Tool | Pricing (2026-06) | Discounts / free | Best for | Link |
|------|-------------------|------------------|----------|------|
| **Freebuff** | **100% free** (ad-supported; CLI / Web / Chat)<br>CLI: `npm install -g freebuff` | $0 forever — no API key or credit card; [Web referral link](https://freebuff.com/web/?ref=ref-b3046190-1d77-44c1-915c-b71b4f36ae5e) | Zero-budget CLI agent, web app builder, or AI chat; open-source models (DeepSeek, Kimi, MiniMax, etc.) | [freebuff.com](https://freebuff.com/) |
| **Codebuff** | Subscriptions: **$100/mo** (1× usage), **$200/mo** (2.5×), **$500/mo** (7×)<br>Pay-as-you-go: **500 free credits** on signup, then **$0.01/credit** | Signup credits (~few hours on a new project); cancel anytime | Premium terminal agent with deep codebase indexing and higher output quality; same company as Freebuff, but a paid product | [codebuff.com](https://www.codebuff.com) |
| **Claude Code** | Free tier does not include Claude Code<br>Pro: **$17/mo (annual)** or $20/mo (monthly)<br>Max: 5x $100 or 20x $200<br>Team: $20–$100/seat/month | Annual plans offer ~15% savings; usage limits are based on a rolling 5-hour window (quota doubled on 2026-05-06) shared with Claude Web Chat; Max tier features dual weekly limits | Advanced reasoning (Opus 4.8), large-scale architectural refactoring, and million-token context analysis | [claude.com/claude-code](https://www.claude.com/product/claude-code) |
| **OpenAI Codex** | **Included in ChatGPT Free** (Web, CLI, and desktop applications, subject to the lowest 5-hour rolling window limits)<br>Go: $8/mo<br>Plus: $20/mo<br>Pro: $100–$200/mo<br>Business/Enterprise: Custom pricing | $0 cost via ChatGPT Free with no credit card required; promotional limit boosts have concluded; supports integration with your personal **OpenAI API Key** (billed per-token, bypasses window limits, but excludes cloud sandbox features) | Deep integration with the OpenAI ecosystem; **desktop applications (macOS/Windows) are the recommended interface**; supports cloud sandboxing | [openai.com/codex](https://openai.com/codex) |
| **Gemini CLI / Antigravity CLI** | **Free tier** (provides high daily quotas) | Highly generous free-tier allocation | Light-to-moderate usage requiring massive context windows | [antigravity.google](https://antigravity.google) |
| **Ollama Cloud** | Free: $0<br>Pro: **$20/mo** (or $200/yr)<br>Max: $100/mo | Pro includes **50×** more cloud usage than Free and **3 concurrent cloud models** (Free: 1; Max: 10). Cloud usage is GPU-time based with **5-hour session** and **7-day weekly** reset windows. Local models remain unlimited. | Developers who want a single local-first workflow while running large cloud models (e.g. `glm-5.2:cloud`) without managing multiple vendor keys | [ollama.com/pricing](https://ollama.com/pricing) |
| **Aider** | **Free and open-source** (pay only for LLM API consumption, or $0 when running local models) | Completely free when paired with local open-source models | Git-native pair programming workflows; supports over 75+ commercial and open-source models | [aider.chat](https://aider.chat) |
| **Amp**（Sourcegraph） | **Pay-as-you-go, zero-markup** on raw API costs; $5 minimum initial deposit | Provides a free daily credit allocation (~$10/day, replenished hourly) — ⚠️ **this allocation has been paused or reduced for some users since May 2026**; fully ad-free since 2026 | Dynamic routing across multiple models (e.g., GPT-5.5, Claude Opus) with unconstrained context windows | [ampcode.com](https://ampcode.com) |
| **Cline** | Open-source version is free (BYOK)<br>**ClinePass: $9.99/mo** — bundled 2–5× API rate limits on GLM-5.2, Kimi K2.7 Code, DeepSeek V4, Qwen3.7, MiniMax, MiMo, and more; CLI via `npm i -g cline` | ⏳ **ClinePass launch promo: $1.99/mo** when signing up via CLI (end date TBD — verify at [cline.bot](https://cline.bot)) | Unified ClinePass subscription for 10+ open-weight models on Cline CLI & IDE; strong alternative to OpenCode for fixed monthly pricing | [cline.bot](https://cline.bot) |
| **OpenCode** | Open-source version is free (BYOK)<br>**Go Plan: $5 for the first month, then $10/mo** (provides ~$60/month in equivalent usage: $12/5-hour limit, $30/week limit) | ✅ **Referral Promo: $5 credit for both parties** when signing up via [referral link](https://opencode.ai/go?ref=J9E8732NMP) | Accessing 14+ open models (including GLM-5.2, Kimi, Qwen, DeepSeek) through a single unified key; compatible with any third-party agent client | [opencode.ai](https://opencode.ai) |
| **Crush**（Charm） | **Free and open-source** (supports custom API keys) | $0 software cost when paired with your own API key for pay-as-you-go billing | Developers seeking an elegant Terminal User Interface (TUI) and flexible multi-model routing | [github.com/charmbracelet/crush](https://github.com/charmbracelet/crush) |
| **Goose**（Block） | **Free and open-source** (supports custom API keys or local execution) | $0 software cost when paired with your own API key for pay-as-you-go billing | Highly extensible local agents with native support for the Model Context Protocol (MCP) | [block.github.io/goose](https://block.github.io/goose) |
| **Qwen Code** | **Free and open-source** | $0 software licensing cost when running Qwen-series models | Developers relying on the Qwen model ecosystem who require maximum cost efficiency | [github.com/QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) |

## ⏳ Time-Limited Promos

Active discounts and promotional offers with explicit deadlines. **Please verify these on the official vendor page before making decisions, and submit a Pull Request if you notice an expiration date has changed.**

| Tool | Promo | Expires | Notes |
|------|-------|---------|-------|
| **Cline (ClinePass)** | **$1.99/month launch promo** (standard $9.99/month) for bundled access to 10+ open-weight models — sign up via `npm i -g cline` | **TBD** (new product launch; end date not yet announced) | Includes GLM-5.2, Kimi K2.7 Code, DeepSeek V4, Qwen3.7, MiniMax, MiMo, and more at 2–5× API rate limits; available on Cline CLI & IDE — verify current terms at [cline.bot](https://cline.bot) |
| **Devin Desktop** | **GLM-5.2 and Kimi K2.7 models are free** on Pro / Max / Teams tiers (frontier-tier open models scoring GLM-5.2 43.0% and Kimi K2.7 39.5% on the FrontierCode Extended benchmark, compared to GPT-5.5 at 44.8% and Opus 4.8 at 51.8%) | **2026-07-05** | Details at [devin.ai](https://devin.ai); additionally, new users receive **$10 AI credit** upon completing onboarding (connecting a Git repository) |
| **ZCode**（Zhipu） | New users receive a **5-day free trial with 5M free tokens/day** (GLM-5.2 3M and GLM-5-turbo 2M allocation); GLM Coding Plan subscribers receive a **1.5× quota multiplier** | Originally scheduled to expire **2026-06-30** (still listed on the official page as of 2026-06-25; please confirm on-site) | The most accessible way to evaluate the open **GLM-5.2** model; details at [zcode.z.ai](https://zcode.z.ai/cn/docs/welcome) |

> Expired promotions are removed from this section; the respective tools remain in their standard categories above with updated pricing information.

## 🎓 Academic & Student Benefits

Developers with verified academic status (such as a `.edu` email address or enrollment verification) can access **free or heavily discounted** plans. These academic offers often provide significantly better terms than standard commercial promotions. Please check each vendor's official page for current eligibility criteria and regional availability.

| Tool | Student offer | How to get it |
|------|---------------|---------------|
| **Google Gemini** ✅ | **Free Google AI Pro membership for 1 year** — upgrading your account to **Gemini Pro**, which unlocks **Google Antigravity** and higher usage limits | Complete academic verification through Google's student portal ([gemini.google/students](https://gemini.google/students)) |
| **Zed** ✅ | **Free 1-year membership** including ~**$10/month in AI model credits** | Complete student verification directly within the Zed editor client ([zed.dev](https://zed.dev)) |
| **GitHub Copilot** ✅ | **Free Copilot Pro subscription** included as part of the GitHub Student Developer Pack | Apply via GitHub Education ([education.github.com/pack](https://education.github.com/pack)) |
| **JetBrains IDEs** ✅ | **Free individual licenses** for all JetBrains IDEs (including integrated AI assistance features) for the duration of your studies | Apply via JetBrains Academic Program ([jetbrains.com/student](https://www.jetbrains.com/student/)) |
| **Cursor** | Academic discounts or free Pro access reported in select regions; verify current availability on the official site | Details available on the official website ([cursor.com](https://cursor.com)) |

> 💡 **Academic Stack Strategy:** A verified student can simultaneously configure **Gemini Pro (unlocking Antigravity) + Copilot Pro + JetBrains IDEs + Zed** to achieve a comprehensive development and AI compute stack for **$0/year**.

## 🎯 Decision Matrix & Scenario-Based Recommendations

| Target Scenario / Developer Profile | Recommended Solution | Key Rationale |
|-------------------------------------|----------------------|---------------|
| **Zero Budget / Open Source Self-Host** | Freebuff + Aider/Cline + local open-source models | Genuinely free; eliminates recurring software licensing costs |
| **Solo Developer / Cost-Sensitive** | GitHub Copilot Pro ($10/month) | The lowest nominal subscription price for a mature, highly capable tool offering unlimited inline completions |
| **Solo Developer / Seeking Agentic IDE** | Cursor Pro or Kiro Pro ($20/month) | Cursor provides exceptional user experience polish and fluid interactions; Kiro excels in spec-driven development and structured code generation |
| **Power User / Complex System Refactoring** | Cursor Pro + Claude Code | A dual-track workflow: Cursor IDE for daily development and multi-file edits, paired with Claude Code in the terminal for complex reasoning and deep architecture refactoring |
| **Full-Stack Web Development** | Google Antigravity (AI Pro $19.99/month) | Native support for multi-agent parallel workflows combined with an integrated browser sandboxed environment for efficient debugging |
| **Existing ChatGPT Plus Subscriber** | OpenAI Codex | Leverages your existing subscription benefits with no additional software cost |
| **Regional Developer / Maximum Cost Efficiency** | ClinePass ($9.99/mo) / OpenCode / Aider + regional APIs (Qwen, DeepSeek, GLM, Kimi) | ClinePass offers a flat monthly rate for 10+ open-weight models; BYOK clients with regional APIs enable pay-as-you-go billing and near-zero running costs |

## 💡 Strategic Cost-Optimization Advice

1. **Monitor active consumption, not just the base subscription.** Tools like Copilot (usage credits), Antigravity (compute pools), and Codex (API tokens) increasingly bill based on active consumption. The base monthly subscription fee is often not your sole cost driver.
2. **Commit to annual billing.** Choosing annual payment terms on commercial AI tools typically yields **savings of ~15%–20% on your overall software budget**.
3. **Align model capability with task complexity.** Implement a tiered usage strategy: leverage highly responsive, low-cost models (e.g., Composer Standard, Gemini Flash, Haiku) for routine code generation and inline completions. Reserve premium reasoning models exclusively for complex architectural refactoring.
4. **Leverage "Open-Source Client + BYOK/Local" architectures.** Utilizing open-source CLI agents or extensions (like Aider or Cline) paired with local models (via Ollama) or low-cost API endpoints can reduce active operating costs to near-zero.
5. **Optimize and combine free-tier allocations.** Before committing to paid subscriptions, combine Copilot's free tier with open-source CLI tools and vendor-provided free quotas to maximize your complimentary compute allocation.
6. **Establish a quarterly evaluation cycle.** The AI developer tool market is highly competitive, with pricing, quotas, and model capabilities changing monthly. The optimal selection from last quarter may no longer represent the best value today.

## 🤝 Contributing

The value of this repository relies entirely on the **accuracy and timeliness** of its information. Community contributions are highly encouraged:

- **Discovered a price change, a new discount, or a newly launched tool?** Please [open an issue](../../issues/new/choose) or submit a Pull Request.
- **Submission Requirements:** Please include the official source link, the date you verified the information, and (for discounts) the applicable expiration date.
- **Formatting Guidelines:** Detailed formatting instructions are available in [CONTRIBUTING.md](CONTRIBUTING.md).

> ⭐ If this project has helped optimize your development costs or guide your technical selection, please consider starring the repository to increase its visibility for other developers.

## 📚 Sources

Pricing and product capability information are aggregated directly from official vendor pricing pages, official product changelogs, and 2026 industry comparison reviews, with comprehensive verification completed as of **June 2026**. Each tool entry includes a direct link to its official website. Because the AI developer tool ecosystem evolves rapidly, **always verify current pricing and terms on the official vendor website before making purchasing decisions.**

---

**Declaration:** This repository is an independent community project and is not affiliated with any AI tool vendor. Some links may contain referral codes (which support the ongoing maintenance and hosting of this project at no additional cost to you), marked clearly where applicable.
