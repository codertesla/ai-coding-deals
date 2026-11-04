# Contributing / 参与贡献

This directory stays useful because developers report price shifts, quota updates, and expired promos as soon as they happen. Even a one-line correction helps keep the reference accurate.

本指南的价值取决于每一条价格与配额数据的准确与实时。哪怕只修正一行过期价格或补充一条新折扣，都能帮其他开发者少走弯路。

## What to Contribute / 贡献范围

- **Update pricing or quotas / 修正价格与配额：** Report changed subscription tiers, credit multipliers, or free-tier limits.
- **Add a new tool / 新增工具：** Submit a verified Agentic IDE, IDE extension, or CLI coding agent.
- **Share a promo or referral / 补充限时促销或邀请权益：** Add active trial windows, student perks, or bilateral referral credits.
- **Flag discontinued tiers / 标记停服或转企业版：** Report free tiers that have shut down or pivoted to enterprise-only licensing.

## Submission Checklist / 提交规范

1. [Open an issue](../../issues/new/choose) for quick reports, or submit a Pull Request to update the tables directly.
   快速反馈可直接提 Issue；直接修改表格请发起 Pull Request。
2. **Every update must include / 每次提交需包含：**
   - **Official source URL / 官方来源链接：** Direct link to the vendor's pricing page, documentation, or changelog.
   - **Verification date / 核实日期：** Exact date (`YYYY-MM-DD`) you confirmed the live terms.
   - **Expiration date / 截止日期：** Required for any time-limited promo or trial window.

## Copy & Formatting Rules / 文案与排版准则

- **Preserve table structure / 保持表格字段一致：** Match the exact columns in `README.md` and `README.zh-CN.md`.
- **Precision over hype / 克制直给，拒绝套话：** State concrete prices, token multipliers, and rate limits. Avoid generic marketing adjectives ("seamless", "revolutionary", "赋能", "极致丝滑") or decorative emojis in headings and table cells.
- **Verified numbers only / 仅填已核实数字：** Write exact prices only after checking the live vendor page. If a tier is unconfirmed, write `See official site` / `见官网`.
- **Bilingual sync / 中英双语同步：** Update both `README.md` and `README.zh-CN.md` when possible. If you only edit one language, note it in your PR and a maintainer will sync the other.

## Referral & Affiliate Policy / 邀请与返利链接规范

Referral links are accepted **only when they grant equal or better terms** (such as bilateral signup credits) compared to the public URL, and must be explicitly labeled in the table cell.

仅当邀请链接对受邀用户确实有利（如双方获赠额外额度、且不劣于官网公开价）时才予收录，并须在单元格内明确标注。劣于公开价或纯引流链接将被拒绝。

## Out of Scope / 不予收录

- Unverified claims without an official vendor source / 无官方出处、无法核实的传闻
- Abandoned or unmaintained wrappers / 已停止维护的套壳工具
- Promotional links without user benefit / 无实际额度优惠的纯推广链接
- Content sites, price-comparison aggregators, and directories that are not themselves a coding tool or inference endpoint / 内容站、比价聚合站与非工具型目录
- Submissions that withhold a vendor employment or affiliate relationship / 未披露厂商任职或返利关系的投稿
