# 🎬 Media OS — The Operating System for a Multi-Channel YouTube Documentary Company

This repository is the **canonical specification** for our Notion-based company operating system. It is designed to scale from 3 founders to a 50–100 person media company running 10+ faceless documentary channels — with the discipline of an ERP, not the looseness of a note-taking app.

> **Why a spec repo?** Notion has no version control. This repo is the versioned source of truth for the OS itself. Every structural change to the workspace (new database, new property, changed pipeline stage) is made **here first**, reviewed, then applied in Notion. The workspace is the running instance; this repo is the schema.

---

## Reading order

| # | Document | Read this if you want… |
|---|----------|------------------------|
| 0 | [Strategic Analysis](docs/00-strategic-analysis.md) | Why the OS is shaped this way, bottlenecks and blind spots in the business model |
| 1 | [Implementation Roadmap](docs/01-implementation-roadmap.md) | The build order (what to create in Notion, week by week) |
| 2 | [Workspace Architecture](docs/02-workspace-architecture.md) | Teamspaces, the relational map (ERD), naming conventions, permissions, documentation standards |
| 3 | [`databases/`](databases/) | Full schema for every database: properties, relations, rollups, views, page templates |
| 4 | [`dashboards/`](dashboards/) | Block-by-block layouts for Company HQ and every role dashboard |
| 5 | [`sops/`](sops/) | The 10 starter SOPs |
| 6 | [`ai/`](ai/) | AI integration policy + starter prompt library |
| 7 | [Scaling Playbook](docs/03-scaling-playbook.md) | How the OS absorbs 10 channels, 100 people, and new revenue streams |

---

## The 17 databases (the "tables" of the ERP)

**Content engine**
1. [Channels](databases/channels.md) — one row per channel; the hub everything hangs off
2. [Ideas](databases/ideas.md) — scored, ranked idea backlog (the fuel tank)
3. [Videos](databases/videos.md) — the production pipeline, Idea → Archive
4. [Tasks](databases/tasks.md) — the universal unit of work, with owners, due dates, dependencies
5. [Competitors + Competitor Videos](databases/competitors.md) — intelligence + swipe file

**Commercial engine**
6. [Sponsor CRM](databases/sponsors-crm.md) — Companies, Contacts, Deals (deliverables link to Videos)
7. [Finance](databases/finance.md) — Revenue + Expense ledgers → cost-per-video, per-channel P&L

**People engine**
8. [People](databases/people.md) — team directory: skills, rates, capacity, performance
9. [Hiring](databases/hiring.md) — applicant pipeline; winners convert into People

**Knowledge engine**
10. [SOP Library](databases/sops.md) — version-controlled processes
11. [AI Prompt Library](databases/prompts.md) — version-controlled prompts
12. [Asset Library](databases/assets.md) — logos, music, b-roll, **with license tracking**
13. [Knowledge Base](databases/knowledge-base.md) — books, courses, lessons learned, searchable

**Management engine**
14. [OKRs & KPIs](databases/okrs.md) — Objectives → Key Results → KPI scoreboard
15. [Metrics Snapshots](databases/metrics-snapshots.md) — weekly channel stats + per-video 24h/7d/30d snapshots (this is what makes trends chartable)
16. [Meetings](databases/meetings.md) — weekly/monthly/quarterly rituals with action items
17. [Automations](databases/automations.md) — registry of every automation, its owner, and its failure mode

## The dashboards (views, never data)

- [Company HQ](dashboards/company-hq.md) — mission, quarterly objectives, scoreboard, announcements
- [CEO Dashboard](dashboards/ceo-dashboard.md) — Founder 1
- [Growth Dashboard](dashboards/growth-dashboard.md) — Founder 2
- [Production Dashboard](dashboards/production-dashboard.md) — Founder 3
- [Analytics Dashboard](dashboards/analytics-dashboard.md) — the data brain
- [Channel Hub Template](dashboards/channel-hub-template.md) — cloned for every new channel; identical for all

---

## Non-negotiable principles

1. **One entity, one database, one row.** A video exists in exactly one place. Dashboards are *filtered views*, never copies.
2. **Relations over text.** If a field names a thing that has its own database (a person, a channel, a sponsor), it is a relation, not text.
3. **Templates are the standardization mechanism.** Every recurring artifact (video, meeting, SOP, channel) is born from a database template. Changing the template changes the company.
4. **If it happened twice, it gets an SOP. If it has an SOP, it can be delegated. If it can be delegated, it can be hired for.**
5. **Numbers get snapshotted.** "Current subscribers" is a fact that dies weekly. Time-series rows are what enable decisions.
6. **Every database carries its own documentation** (Purpose, Owner, Instructions, Examples, Linked SOPs, Related Databases) — see [Documentation Standards](docs/02-workspace-architecture.md#documentation-standards).
7. **AI drafts, humans decide.** Every workflow states what AI does, what humans review, and what is never automated — see [AI Policy](ai/ai-integration-policy.md).
