# 🤖 AI Prompt Library

> **Purpose:** Version-controlled registry of every production prompt. When 5 scriptwriters use "the script prompt," they must all use the *same, current* one — and when output quality shifts, you can trace it to a prompt version.
> **Owner:** Founder 1 (AI systems).
> **Instructions:** Prompts are used by copy-pasting from the current version only. Edits = new version with changelog entry and before/after example. Test on 2–3 real inputs before bumping to Active.
> **Related:** embedded in SOPs; referenced by Automations.

## Properties

| Property | Type | Notes |
|---|---|---|
| Prompt | Title | `PRM-###: Name` |
| Version | Text | `v1.3` |
| Status | Select | `Draft / Testing / Active / Deprecated` |
| Category | Select | Research / Script / Storytelling / Hooks / Thumbnails / Titles / SEO / Analytics / Competitor Analysis / Outreach / Automation |
| Model | Select | which model + settings it's tuned for |
| Used In SOPs | Relation → SOPs | |
| Owner | Relation → People | |
| Quality Rating | Select | ⭐1–5 from users; < 3 triggers rework |
| Variables | Text | the `{{placeholders}}` the user must fill |

## Page template

1. **📘 About** — what it produces, when to use, what to check in the output
2. **The prompt** (code block, `{{variables}}` marked)
3. **Example input → gold-standard output**
4. **Known failure modes** — where this prompt hallucinates or drifts
5. **Version log**

## Starter prompts (full text in [`/ai/prompt-library-starter.md`](../ai/prompt-library-starter.md))

PRM-001 Research Brief · PRM-002 Outline · PRM-003 Script Draft · PRM-004 Title Generator · PRM-005 Hook Writer · PRM-006 Thumbnail Concepts · PRM-007 SEO Package · PRM-008 Analytics Narrative · PRM-009 Competitor Breakdown · PRM-010 Sponsor Outreach.

## Views

`By Category` · `Active Only` (what the team copies from) · `⭐ Low-Rated` (rework queue).

## AI table

| 🤖 AI does | 👁 Human reviews | 🚫 Never automated |
|---|---|---|
| Suggests prompt improvements from rated outputs | Every version bump tested on real inputs | Marking a prompt Active for factual/research categories without a hallucination check |
