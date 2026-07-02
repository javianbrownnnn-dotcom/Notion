# ⚙️ Automations Registry

> **Purpose:** One row per automation. An automation nobody understands is an outage waiting to happen; at 50 people, undocumented automations are how data silently rots. Every scenario has an owner, a trigger, a documented failure mode, and a health check.
> **Owner:** Founder 1 (AI & systems).
> **Instructions:** No automation ships without a row here + a linked runbook page (what it does, how to pause it, how to re-run missed items). Review health monthly.

## Properties

| Property | Type | Notes |
|---|---|---|
| Automation | Title | `AUT-###: Name` |
| Status | Select | `Live / Paused / Broken / Planned / Deprecated` |
| Trigger | Text | schedule / webhook / button |
| Tool | Select | Notion native / Make / n8n / Zapier / Custom script / Slack workflow |
| Reads From / Writes To | Relations → (databases as pages) + text | the data-flow map |
| Owner | Relation → People | who gets paged when it breaks |
| SOP Implemented | Relation → SOPs | |
| Failure Mode | Text | REQUIRED: what breaks downstream if this silently stops? how would we notice? |
| Last Verified | Date | monthly check |
| Runbook | Page | setup, credentials location (reference, never secrets), pause/re-run steps |

## Starter automation roadmap (build in this order)

| ID | Automation | What it does | Phase |
|---|---|---|---|
| AUT-001 | Video task spawner | New Video from template → 15 stage tasks, relative dates, dependency links (native Notion template + button) | 1 |
| AUT-002 | Analytics import | YouTube API → weekly Channel Snapshots + video 24h/7d/30d rows | 1 |
| AUT-003 | Slack pipeline alerts | task overdue / stage Blocked / video at-risk → channel ping | 2 |
| AUT-004 | Idea intake | form / Slack emoji / trend feed → Ideas Inbox | 2 |
| AUT-005 | 24h underperformance alert | 24h snapshot below channel floor → packaging-review task | 2 |
| AUT-006 | Sponsor CRM hygiene | stale `Next Follow-up` → Slack nudge; deal Won → invoice task + Revenue stub | 2 |
| AUT-007 | Publishing checklist gate | Stage → Scheduled blocked unless QA task Done (button + validation) | 3 |
| AUT-008 | Scoreboard writer | Monday: compile KPI Weekly row from Snapshots/Finance/Tasks | 3 |
| AUT-009 | SOP staleness flagger | Last Reviewed > 90d → Needs Update + owner ping | 3 |
| AUT-010 | Applicant intake | job-form submission → Applicants row + screening task | 3 |

## Views

`Live` (by tool) · `🔥 Broken` · `Verification Due` · `Data-flow` (grouped by Writes To).

## AI table

| 🤖 AI does | 👁 Human reviews | 🚫 Never automated |
|---|---|---|
| The automations themselves; monthly health-summary draft | Failure-mode docs; monthly verification | Automations that publish content, send external email unsupervised, or move money |
