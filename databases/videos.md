# 🎞 Videos Database (Production Pipeline)

> **Purpose:** One row per video, from approved idea to archived performance review. The factory floor. The row tracks the *product*; the work is done in 15 auto-spawned stage [Tasks](tasks.md) with owners, due dates, and dependencies.
> **Owner:** Founder 3 (Production).
> **Instructions:** Created ONLY by promoting an `Approved` Idea, using the `🎬 New Video` template (spawns all stage tasks). Stage advances only when its task is Done and the stage's exit criteria (in the SOP) are met.
> **Linked SOPs:** SOP-002 Script … SOP-006 Publishing (each stage names its SOP). **Related:** fed by Ideas; feeds Snapshots, Expenses, Deals.

## Pipeline stages (Status property, grouped board = the factory)

| # | Stage | Default Owner (today) | Exit criteria | SOP |
|---|-------|------------------------|---------------|-----|
| 1 | 💡 Idea | F1 | promoted from Ideas with score ≥ 70 | SOP-001 |
| 2 | 🔍 Research | F1 | fact-checked research doc + source list | SOP-001 |
| 3 | 🧱 Outline | F3 | beat-by-beat outline w/ hook + open loops | SOP-002 |
| 4 | ✍️ Script | F3 | full script, target length, reading-level pass | SOP-002 |
| 5 | 👁 Review | **F1 (never the writer)** | facts verified, rights flags cleared, voice check | SOP-005 |
| 6 | 🎙 Voiceover | VO artist / F3 | recorded, matches channel voice spec | SOP-002 |
| 7 | ✂️ Editing | F3 | full cut, pacing pass, licensed assets only | SOP-003 |
| 8 | 🖼 Thumbnail | F3 | 2–3 variants produced for testing | SOP-004 |
| 9 | 🏷 Title | F1 | final + 2 alternates for A/B | SOP-004 |
| 10 | 📝 Description | F2/F1 | description, chapters, sponsor copy per deal | SOP-006 |
| 11 | 🔎 SEO | F1 | tags, metadata checklist done | SOP-006 |
| 12 | ✅ QA | **F2 (never the editor)** | full QA checklist incl. asset-clearance audit | SOP-005 |
| 13 | 📅 Scheduled | F3 | uploaded, scheduled, end screens/cards set | SOP-006 |
| 14 | 🚀 Published | auto | live | SOP-006 |
| 15 | 📈 Performance Review | F1 | 30-day retro logged (below) | SOP-007 |
| 16 | 🗄 Archived | — | learnings extracted to Knowledge Base | — |

Review (5) and QA (12) are assigned to someone **other than** the person who made the work. This rule survives every reorg.

## Properties

| Property | Type | Notes |
|---|---|---|
| Name | Title | `[CODE] Title` |
| Channel | Relation → Channels | required |
| Idea | Relation → Ideas | origin; carries the score |
| Stage | Status | the 16 stages above |
| Publish Date | Date | target; drives the content calendar |
| Stage Tasks | Relation → Tasks | the 15 spawned tasks |
| Progress | Rollup | Tasks → % Done |
| Next Blocker | Rollup | Tasks → filter Blocked → show titles |
| Sponsor Deal | Relation → Deals | if integrated |
| Assets Used | Relation → Assets | populated during editing — this is the rights audit trail |
| Script / VO / Edit / Thumbnail links | URL | Drive/Frame.io links |
| Final Title / Thumbnail | Text / Files | as published |
| Video URL | URL | |
| Length (min) | Number | |
| Production Cost | Rollup | Expenses → sum (freelancer payments + assets) |
| Views 30d · CTR 30d · AVD · Retention % · Revenue 30d | Rollups | from Video Snapshots (30d row) |
| Performance vs Channel Avg | Formula | Views 30d ÷ channel trailing avg — the hit-rate metric |
| Hook Type · Story Structure · Thumbnail Style | Selects | tagged at publish; this is what makes "what works" queryable later |

## `🎬 New Video` template

Page body: 📘 About block → Research brief → Outline → Script → Packaging (title options, thumbnail variants) → QA checklist → **Performance Review** section (filled at day 30: what we predicted vs got, hook/retention analysis, one lesson → Knowledge Base). Template spawns the 15 stage tasks with relative due dates and dependency links (see [Tasks](tasks.md)).

## Views

- `Factory` (board by Stage) — the main view
- `📅 Content Calendar` (calendar by Publish Date, all channels; also filtered per channel hub)
- `⚠️ At Risk` (Publish Date < 7 days away AND Stage before QA, or any task Blocked/overdue)
- `By Channel` / `Published — by Performance` (sorted by Performance vs Avg)

## AI table

| 🤖 AI does | 👁 Human reviews | 🚫 Never automated |
|---|---|---|
| Drafts outline & script v1 from research brief (PRM-002/003); generates description/tags/chapters; drafts the 30-day performance review from snapshot data | Script accuracy & voice (line-by-line on Review); all packaging choices; QA checklist | Clicking Publish; asset-clearance sign-off; anything in the QA gate |
