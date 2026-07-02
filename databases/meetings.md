# 🤝 Meetings Database

> **Purpose:** Every recurring ritual, with agendas born from templates and action items that become real Tasks (not bullet points that die in the notes).
> **Owner:** Founder 1 runs weekly; rotate the scribe.
> **Instructions:** Create from the matching template BEFORE the meeting; agenda items added async. A decision isn't made until it's written in the Decisions block; an action isn't real until it's a Task with owner + date.

## Properties

| Property | Type | Notes |
|---|---|---|
| Meeting | Title | `Weekly Sync — 2026-07-06` |
| Type | Select | `Weekly Sync / Monthly Review / Quarterly Planning / Retro / 1:1 / Ad-hoc` |
| Date / Attendees | Date / Relation → People | |
| Action Items | Relation → Tasks | created live in the meeting |
| Decisions | Text | one line each — the searchable decision log |
| Related Objective | Relation → Objectives | |

## Templates

**Weekly Sync (30–45 min, Mondays)**
1. Scoreboard review (5') — KPI row, red items only
2. Last week's action items — done or explained
3. Pipeline walk (10') — Videos board: blocked & at-risk only
4. Idea queue level + this week's priorities per founder (3 max each)
5. Wins / Losses (5') — logged, not just spoken
6. New action items → Tasks

**Monthly Review (90 min)** — per-channel P&L + snapshot trends · published cohort review (predicted vs actual vs Idea scores — recalibrate the scoring weights) · hiring pipeline · automation health · top 3 lessons → Knowledge Base.

**Quarterly Planning (half day)** — grade last quarter's OKRs (0–1.0) · SWOT refresh per channel · set ≤3 objectives · kill/scale decisions per channel · SOP audit (stale list to zero).

**Retrospective (after every channel launch, big hit, or big miss)** — what happened vs plan · keep / stop / start · SOP + scoring-model changes (linked).

## Views

`Upcoming` · `Decision Log` (all Decisions, searchable — settle "didn't we decide X?" in 10 seconds) · `By Type`.

## AI table

| 🤖 AI does | 👁 Human reviews | 🚫 Never automated |
|---|---|---|
| Pre-fills scoreboard & pipeline summaries into the agenda; transcribes & drafts minutes; extracts action-item candidates | Minutes & decisions before saving; action items confirmed by owners | Making decisions; grading OKRs |
