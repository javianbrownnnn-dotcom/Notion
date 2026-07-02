# ✅ Tasks Database

> **Purpose:** The universal unit of work for the whole company — video stage tasks, growth/outreach tasks, hiring tasks, meeting action items. One owner, one due date, per task. This is what makes workload visible and delegation real.
> **Owner:** Founder 3 (operationally); every founder owns their own hygiene.
> **Instructions:** Video tasks are auto-spawned by the `🎬 New Video` template — don't hand-create them. Ad-hoc tasks: title as a verb phrase, always set Assignee + Due. A task without an owner and a date is a wish.
> **Related:** child of Videos/Meetings/Deals/Applicants; feeds People (workload rollup).

## Properties

| Property | Type | Notes |
|---|---|---|
| Task | Title | `Stage — [CODE] Video name` for pipeline tasks |
| Status | Status | `Not Started / In Progress / In Review / Blocked / Done` |
| Assignee | Relation → People | **relation, not Notion person property** — so freelancers, rates, and workload roll up |
| Due | Date | video templates set relative offsets from Publish Date |
| Video | Relation → Videos | if a pipeline task |
| Stage | Select | mirrors the 15 pipeline stages (for cross-video views like "all Scripts this week") |
| Blocked By / Blocks | Relation → Tasks (self, two-way) | dependency chain; a task with an unfinished `Blocked By` shows 🔒 |
| Ready | Formula | ✅ when all `Blocked By` rollup = Done — "what can I start right now" |
| SOP | Relation → SOPs | the how-to; template pre-fills per stage |
| Effort (hrs) | Number | estimate; template pre-fills stage defaults |
| Actual (hrs) | Number | filled on Done — feeds cost-per-video truth & capacity planning |
| Channel | Rollup | via Video |
| Parent (other) | Relation → Meetings / Deals / Applicants | for non-video tasks |
| Priority | Select | P1 / P2 / P3 |

## Dependency chain spawned per video

`Research → Outline → Script → Review → Voiceover → Editing → (Thumbnail ∥ Title ∥ Description — parallel) → SEO → QA → Schedule → Publish → Perf Review`. Thumbnail/Title/Description run in parallel after Script Review — packaging never waits on editing.

## Views

- `My Plate` (Assignee = Me, not Done, sorted by Due) — everyone's daily home
- `🔓 Ready to Start` (Ready ✅, unassigned or mine)
- `⚠️ Overdue` / `🔒 Blocked` (grouped by Blocked By)
- `By Stage This Week` (board by Stage) — batch view: an editor sees all edits, a writer all scripts
- `Workload` (board by Assignee, not Done) — the capacity view used in the weekly meeting

## AI table

| 🤖 AI does | 👁 Human reviews | 🚫 Never automated |
|---|---|---|
| Drafts subtask checklists from the SOP; flags at-risk tasks (due soon + not started) to Slack | Effort estimates; priority calls | Reassigning humans' work; marking Done |
