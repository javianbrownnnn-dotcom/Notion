# 📊 Analytics Dashboard

The data brain. Every module is a view over [Metrics Snapshots](../databases/metrics-snapshots.md), [Videos](../databases/videos.md), and [Finance](../databases/finance.md). Reviewed in depth monthly; skimmed weekly via the Scoreboard.

## Layout

**1. 📅 Weekly pulse** — Channel Snapshots, last 8 weeks, grouped by channel: Subs Δ, Views 28d, Watch hours, CTR, Retention, RPM, Revenue. (Notion shows the table; real charts come from the BI layer at scale — the rows are already shaped for it.)

**2. 🚨 24h alerts** — Video Snapshots: 24h checkpoint below channel floor (CTR or retention) → each should have a packaging-review task (AUT-005).

**3. 🏆 What works** (the queries that justify the whole tagging discipline)
- *Most successful topics*: published Videos grouped by Niche, avg `Performance vs Channel Avg`
- *Most successful hooks*: grouped by `Hook Type`, avg Retention @30s
- *Best thumbnails*: gallery of top-decile CTR videos, grouped by `Thumbnail Style`
- *Best story structures*: grouped by `Story Structure`, avg % viewed
- Each group needs n ≥ 5 before anyone acts on it — small-sample "insights" are noise (rule lives in SOP-007).

**4. 🎯 Prediction calibration** — 30d cohort: Idea Score & Estimated Views vs actuals. Miss badly for two months in a row → reweight the scoring formula in Quarterly Planning.

**5. ⚙️ Operational metrics** — Upload consistency per channel (published vs target) · Publishing speed (Idea-approved → Published, days; from task timestamps) · Founder hours per video (Actual hrs rollup) · Cost per video trailing 5.

**6. 💵 Money view** — Revenue by stream (concentration %) · per-channel Profit 30d · RPM by channel by week.

**7. 📝 Monthly analytics narrative** — AI-drafted (PRM-008) from the month's snapshots, human-verified, decisions extracted to Meetings → the "why", archived so future you can read what past you believed.

## AI table

| 🤖 AI does | 👁 Human reviews | 🚫 Never automated |
|---|---|---|
| All ingestion; anomaly flags; narrative drafts; pattern clustering across tags | Every causal claim; the n≥5 discipline | Strategy pivots from one video's data; publishing/packaging changes without human sign-off |
