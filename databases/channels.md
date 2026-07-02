# 📺 Channels Database

> **Purpose:** One row per YouTube channel. The hub of the entire OS — every idea, video, competitor, deal, dollar, and metric relates back to a channel. Each row's page IS that channel's hub (see [Channel Hub Template](../dashboards/channel-hub-template.md)).
> **Owner:** Founder 1 (CEO).
> **Instructions:** A channel is created *only* from the `New Channel` template, which spawns the full hub. Strategy fields are reviewed quarterly; metric fields are rollups/automation-fed — never hand-edit them.
> **Linked SOPs:** SOP-011 New Channel Launch. **Related:** feeds everything; fed by Snapshots, Finance, Videos.

## Properties

| Property | Type | Config / Notes |
|---|---|---|
| Name | Title | Channel name |
| Code | Text | 2–3 letter code used in all video names, e.g. `BIZ` |
| Status | Select | `Research` / `Pre-launch` / `Active` / `Paused` / `Sunset` |
| Vertical | Select | Business / History / Crime / Religion / Science / Psychology / Health / Finance |
| Channel URL | URL | |
| Launch Date | Date | |
| Channel Lead | Relation → People | accountable human (a founder today) |
| Upload Schedule | Select | e.g. `Weekly – Tue`, `2×/week – Tue+Fri` |
| Target Frequency /mo | Number | drives the consistency KPI |
| **Strategy (page content, from template — see below)** | | Mission, audience, value prop, voice, monetization, SWOT |
| Ideas | Relation → Ideas | |
| Videos | Relation → Videos | |
| Competitors | Relation → Competitors | |
| Deals | Relation → Deals | |
| Snapshots | Relation → Metrics Snapshots | |
| Subscribers (latest) | Rollup | Snapshots → Subscribers → latest ¹ |
| Views 30d | Rollup | Snapshots → Views 28d → latest |
| Revenue 30d | Rollup | Revenue entries this month → sum |
| RPM (latest) | Rollup | Snapshots → RPM → latest |
| Avg CTR (latest) | Rollup | Snapshots → CTR → latest |
| Avg Retention (latest) | Rollup | Snapshots → Avg % viewed → latest |
| Videos Published 30d | Rollup | Videos → filtered count (automation-maintained number is fine) |
| Cost 30d | Rollup | Expenses this month → sum |
| Profit 30d | Formula | `Revenue 30d − Cost 30d` |
| Health | Formula | 🟢 if consistency ≥ target AND profit ≥ 0; 🟡 if one fails; 🔴 if both — surfaces on Company Scoreboard |

¹ Notion rollups can't do "latest" directly on all plans: sort the relation by date and use "Show original / limit 1", or let the snapshot automation write latest values back to the channel row. Either way, snapshots remain the source of truth.

## `New Channel` template — page body

Identical for every channel (this is the "same production system" guarantee):

1. **📘 About** (documentation block per standard)
2. **🎯 Mission** — one paragraph
3. **👤 Target Audience** — persona: who, age, what they watch at 11pm, why they'd subscribe
4. **💎 Value Proposition** — why us over the 5 nearest competitors
5. **🗣 Brand Voice** — tone, vocabulary, pacing, narrator persona, banned clichés; VO artist relation
6. **📖 Story Structures** — the 2–3 narrative frameworks this channel uses (linked to Knowledge Base entries)
7. **⚔️ Competitors** — linked view of Competitors filtered to this channel
8. **💰 Monetization Strategy** — AdSense assumptions, sponsor categories that fit, affiliate/product roadmap
9. **🔭 Future Opportunities** — spin-offs, languages, shorts strategy, licensing
10. **📊 SWOT** — 4-column table, reviewed quarterly (dated entries, don't overwrite)
11. **📈 Growth** — linked Snapshots view (this channel, by week) + linked Videos view (published, by 30-day views)
12. **🚦 Pipeline** — linked Videos board (by stage, this channel) and Ideas table (by score, this channel)

## Views

- `All Channels` (table, sorted by Profit 30d)
- `Portfolio Board` (board by Status)
- `🔴 Needs Attention` (Health ≠ 🟢)

## AI table

| 🤖 AI does | 👁 Human reviews | 🚫 Never automated |
|---|---|---|
| Drafts SWOT refresh from competitor + snapshot data; drafts niche research for `Research`-status channels | Founder 1 approves strategy changes | Mission, brand voice, kill/scale decisions |
