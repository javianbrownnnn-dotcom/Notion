# 👥 People Database (Team Directory)

> **Purpose:** One row per human who works here — founders, employees, freelancers. The reason task assignees are relations: skills, rates, workload, and performance all live here and roll up everywhere.
> **Owner:** Founder 1 (→ Head of Ops when hired). **Pay fields move to a restricted teamspace at first external hire.**
> **Instructions:** Rows are created by the Hiring pipeline on conversion (or manually for founders). Every person gets an onboarding checklist from the role template.
> **Linked SOPs:** SOP-009 Training/Onboarding. **Related:** fed by Applicants; feeds Tasks, SOPs, Expenses.

## Properties

| Property | Type | Notes |
|---|---|---|
| Name | Title | |
| Type | Select | `Founder / Employee / Freelancer / Agency` |
| Role | Multi-select | Editor / Scriptwriter / Researcher / Thumbnail Designer / Voice Actor / Motion GFX / Analyst / Sales / Ops |
| Status | Select | `Onboarding / Active / Bench / Offboarded` |
| Channels | Relation → Channels | who they work on (VO artists especially) |
| Skills | Multi-select | tools & specialties (Premiere, AE, documentary pacing, …) |
| Timezone / Email / Portfolio | Text/URL | |
| Rate | Number + Select | $/video or $/hr — restricted view |
| Total Paid | Rollup | Expenses → sum — restricted |
| Open Tasks | Rollup | Tasks → count not Done — the capacity signal |
| Est. Hours This Week | Rollup | Tasks (due this week) → sum Effort |
| Performance | Select | ⭐1–5, reviewed after every 3 deliverables (rubric in SOP-009) |
| Performance Notes | Page | dated entries: what was strong/weak, turnaround reliability |
| SOPs Owned | Relation → SOPs | |
| Source | Relation → Applicants | hiring provenance |
| Start Date / NDA & Contract | Date / Files | |

## `New Team Member` template (page body)

📘 About block → Onboarding checklist (role-specific: accounts, SOPs to read, first trial-scope task) → 30/60/90 expectations → Performance log.

## Views

- `Active Roster` (by Role) · `Capacity` (sorted by Est. Hours This Week — who can take work) · `Bench` (trusted freelancers between projects — your surge capacity for channel #4) · `⭐ Review Due`.

## AI table

| 🤖 AI does | 👁 Human reviews | 🚫 Never automated |
|---|---|---|
| Drafts onboarding checklists per role; flags overload (est. hours > capacity) in weekly meeting doc | Performance ratings | Hiring/firing/rate decisions; performance conversations |
