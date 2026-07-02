# 📸 Metrics Snapshots — Channel Weekly + Video 24h/7d/30d

> **Purpose:** The time-series layer. Notion can't chart a number that gets overwritten; these two databases store dated rows so trends, comparisons, and "what works" analyses are real queries. This is the database your analytics automation writes to — and the one you'll pipe into a BI tool at scale.
> **Owner:** Founder 1 (analytics). Written by automation (AUT-002); hand-entry is the fallback, 15 min every Monday.
> **Related:** feeds Channels rollups, Videos rollups, KPI Scoreboard, Analytics Dashboard.

## 📅 Channel Snapshots (one row per channel per week)

| Property | Type | Notes |
|---|---|---|
| Snapshot | Title | `BIZ — 2026-W27` (automation-generated) |
| Channel / Week Of | Relation / Date | |
| Subscribers / Subs Δ | Numbers | Δ computed vs previous row |
| Views 28d / Watch Hours 28d | Numbers | |
| CTR 28d / Avg % Viewed / Avg View Duration | Numbers | |
| RPM / Revenue 28d | Numbers | |
| Videos Published (week) | Number | consistency check |
| Notes | Text | anomalies: spikes, strikes, algorithm shifts |

## 🎬 Video Snapshots (one row per video per checkpoint)

| Property | Type | Notes |
|---|---|---|
| Snapshot | Title | `[BIZ] Enron — 30d` |
| Video | Relation → Videos | |
| Checkpoint | Select | `24h / 7d / 30d / 90d / 365d` |
| Views / CTR / Impressions | Numbers | |
| Avg View Duration / Avg % Viewed | Numbers | |
| Retention @30s | Number | **the hook metric** — pairs with the video's Hook Type tag |
| Subs Gained / Revenue / RPM | Numbers | |

The 30d row feeds the video's Performance Review stage; the 24h row triggers the "underperforming — consider packaging swap" alert (AUT-005).

## Why checkpoints, not continuous data

Notion is not a data warehouse. Five checkpoints per video answer 95% of decisions (Did the hook hold? Did packaging deliver CTR? Is it evergreen?) at ~1% of the data volume. Continuous curves stay in YouTube Studio; **decisions** live here.

## Views

`By Channel by Week` · `30d Cohort` (all videos' 30d rows — the comparison table behind "best hooks / structures / thumbnails") · `24h Alerts` (CTR or retention below channel floor).

## AI table

| 🤖 AI does | 👁 Human reviews | 🚫 Never automated |
|---|---|---|
| Writes all rows via API; computes deltas; flags anomalies; drafts the weekly analytics narrative (PRM-008) | Anomaly explanations (AI sees *that*, humans determine *why*) | Strategy changes from single-video data |
