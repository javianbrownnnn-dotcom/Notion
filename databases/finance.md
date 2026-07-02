# 💵 Finance — Revenue & Expense Ledgers

> **Purpose:** The unit-economics layer your original spec was missing. Every dollar in and out, tagged to channel (and video where possible). Produces the three numbers that decide strategy: **cost per video, revenue per video, per-channel P&L**.
> **Owner:** Founder 1 (until a finance hire; move to restricted teamspace at first external hire).
> **Instructions:** Log expenses when incurred, revenue when received. This complements (does not replace) real accounting software — it exists to tie money to *content*, which QuickBooks can't do.

## 📈 Revenue

| Property | Type | Notes |
|---|---|---|
| Entry | Title | `Channel — Stream — Month` |
| Channel | Relation → Channels | |
| Stream | Select | `AdSense / Sponsorship / Affiliate / Licensing / Course / Merch / Other` — the concentration-risk view depends on this |
| Deal | Relation → Deals | if sponsorship |
| Amount / Month | Number / Date | |

**Views:** `By Stream This Quarter` (board, sum) — watch concentration · `By Channel` · `Monthly` (timeline).

## 📉 Expenses

| Property | Type | Notes |
|---|---|---|
| Entry | Title | |
| Category | Select | `Freelancer / Software / Music & Assets / Ads / Legal / Equipment / Other` |
| Channel | Relation → Channels | required |
| Video | Relation → Videos | **fill whenever attributable — this powers cost-per-video** |
| Paid To | Relation → People | freelancer payment history rolls up on their profile |
| Amount / Date / Recurring? | Number / Date / Checkbox | |

## Rollups this enables

- **Videos.Production Cost** = sum of linked expenses → compare to Revenue 30d/90d per video
- **Channels.Profit 30d** = revenue − expenses → the Health flag on the Company Scoreboard
- **People.Total Paid** = freelancer spend history → rate negotiations with data

## AI table

| 🤖 AI does | 👁 Human reviews | 🚫 Never automated |
|---|---|---|
| Drafts monthly P&L summary per channel; flags cost-per-video outliers vs channel norm | All entries monthly (reconcile vs bank) | Payments; anything money actually moves on |
