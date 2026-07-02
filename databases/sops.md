# 📖 SOP Library

> **Purpose:** Every repeatable process, written so a competent stranger can execute it. SOPs are what convert founder knowledge into company property — and what make hiring possible at all.
> **Owner:** Founder 1 approves; the person who *runs* the process writes and maintains it.
> **Instructions:** Rule of three — done it three times? Write the SOP. Every SOP is written from the `New SOP` template. Version bumps on every material change; old versions kept in the page's Version Log.
> **Related:** Tasks link to their SOP; Prompts embed in SOPs; Automations implement SOPs.

## Properties

| Property | Type | Notes |
|---|---|---|
| SOP | Title | `SOP-###: Name` |
| Version | Text | `v1.2` — bump minor for tweaks, major for process changes |
| Status | Select | `Draft / Active / Needs Update / Deprecated` |
| Category | Select | Research / Scripting / Editing / Thumbnail / QA / Publishing / Analytics / Hiring / Training / Sales / Ops |
| Owner | Relation → People | accountable for accuracy |
| Used In Stage | Select | pipeline stage(s) it governs |
| Prompts Used | Relation → Prompts | |
| Automations | Relation → Automations | |
| Last Reviewed | Date | quarterly review cadence; `Needs Update` auto-flag if > 90 days |
| Time to Execute | Number (min) | feeds capacity planning |

## `New SOP` template (page body)

1. **📘 About** — purpose, when to use, owner
2. **🤖 AI table** — AI does / human reviews / never automated (mandatory)
3. **Prerequisites** — access, tools, inputs required
4. **Steps** — numbered, one action each, with screenshots/embeds
5. **Quality bar** — what "done correctly" looks like; link 1–2 gold examples
6. **Common mistakes**
7. **Version log** — date, version, what changed, who

## The 10 starter SOPs (full text in [`/sops`](../sops/))

SOP-001 Research · SOP-002 Script · SOP-003 Editing · SOP-004 Packaging (Thumbnail+Title) · SOP-005 QA & Review · SOP-006 Publishing · SOP-007 Analytics Review · SOP-008 Hiring · SOP-009 Training/Onboarding · SOP-010 Sponsorships. (SOP-011 New Channel Launch follows once channel #2 is real.)

## Views

`By Category` · `⚠️ Stale` (Last Reviewed > 90d) · `By Owner` · `By Pipeline Stage`.

## AI table

| 🤖 AI does | 👁 Human reviews | 🚫 Never automated |
|---|---|---|
| Drafts SOP v1 from a Loom transcript of someone doing the task; flags SOPs contradicted by recent process changes | The process owner validates every step by running it | Approving an SOP as Active (Founder 1 signs) |
