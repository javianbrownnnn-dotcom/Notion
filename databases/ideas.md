# 💡 Ideas Database

> **Purpose:** The fuel tank. Every video concept is captured, researched, scored, and ranked here. Nothing enters production without passing the score gate. Packaging (title + thumbnail concept) is validated HERE, before a script exists.
> **Owner:** Founder 1 (CEO) — owns the scoring model. Everyone contributes ideas.
> **Instructions:** Capture in 30 seconds (Title, Channel, one-line Topic). Enrich later during weekly Idea Review. An idea moves to `Approved` only with score ≥ 70 AND a thumbnail concept + 3 title options attached.
> **Linked SOPs:** SOP-001 Research. **Related:** feeds Videos; fed by Competitor Videos, Knowledge Base.

## Properties

| Property | Type | Config / Notes |
|---|---|---|
| Idea | Title | working title |
| Channel | Relation → Channels | required |
| Status | Select | `Inbox` / `Researching` / `Scored` / `Approved` / `In Production` / `Rejected` / `Icebox` |
| Topic | Text | one-line subject |
| Niche / Sub-niche | Select + Text | within the channel's vertical |
| Source | Select | Team / Competitor / Comment mining / Trend / AI suggestion / Audience request |
| Submitted By | Relation → People | |
| **— Scoring inputs (1–10 each) —** | | scored during Idea Review, definitions in SOP-001 |
| Audience Demand | Number | search volume + comment demand + proven-competitor evidence |
| Curiosity Gap | Number | strength of the open question the packaging can pose |
| Evergreen Score | Number | 10 = evergreen forever, 1 = dead in a week |
| Trend Potential | Number | timeliness upside |
| Competition Gap | Number | 10 = proven demand + weak execution to beat |
| CTR Potential | Number | how thumbnailable is the core image/promise |
| RPM Potential | Number | advertiser-friendliness of the niche |
| Production Ease | Number | 10 = cheap/fast (inverse of difficulty) |
| **Score** | Formula | `Demand*2 + Curiosity*1.5 + Evergreen + CompetitionGap*1.5 + CTR*2 + RPM + Ease` → 0–100. Weights are v1 — recalibrate quarterly against actual performance (that's SOP-007 Analytics). |
| Priority | Formula | `Score ≥ 85 → "🔥 P1"; ≥ 70 → "P2"; ≥ 55 → "P3"; else "❄️"` |
| Estimated Views 30d | Number | analyst's estimate; later compared to actuals to calibrate the estimator |
| Search Volume | Number | monthly, from keyword tool |
| Hooks | Text | 2–3 candidate opening hooks |
| Audience Emotion | Multi-select | Curiosity / Fear / Awe / Outrage / Greed / Nostalgia / Justice |
| Thumbnail Ideas | Files + Text | rough concepts/sketches — REQUIRED before approval |
| Title Options | Text | ≥ 3 — REQUIRED before approval |
| Inspired By | Relation → Competitor Videos | the proof-of-demand links |
| References | URL/Text | sources, docs, articles |
| AI Research Notes | Page content | AI-drafted brief (PRM-001), clearly labeled, human-verified before use |
| Related Videos | Relation → Videos (self-portfolio) | our own adjacent videos (series potential) |
| Promoted To | Relation → Videos | filled when approved → production |
| Rejection Reason | Select | Low score / Rights risk / Off-brand / Duplicate / Cost |

## Views

- `Inbox` (Status = Inbox — process weekly to zero)
- `Ranked` (Status = Scored/Approved, sorted by Score desc) — the pull queue for production
- `By Channel` (board)
- `Icebox` / `Rejected` (kept forever — rejected ideas are data)

## The gate (non-negotiable)

Production pulls **only** from `Approved`, top score first. If Approved runs dry, production pauses and everyone does idea work. A starving idea pipeline is a company emergency, not a production problem.

## AI table

| 🤖 AI does | 👁 Human reviews | 🚫 Never automated |
|---|---|---|
| Comment-mining & trend suggestions into Inbox; drafts research briefs (PRM-001); proposes preliminary scores with reasoning; generates title/hook candidates (PRM-004/005) | Every score before `Scored`; every fact in the research brief; title/thumbnail selection | Final approval to production; rejection of ideas (humans kill ideas, AI never does) |
