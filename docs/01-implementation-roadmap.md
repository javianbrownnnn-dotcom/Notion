# 01 — Implementation Roadmap

Build order matters in Notion: relations require target databases to exist, templates require relations, dashboards require everything. Follow the sequence. Total: ~4 weeks part-time alongside normal production; the OS starts paying for itself in week 2.

## Phase 1 (Week 1): The spine — capture and production never wait

**Day 1–2: Skeleton + hub**
1. Create the `DATABASES` page; create **Channels**, **People** (3 founder rows), **Ideas**, **Videos**, **Tasks** with all properties per spec. Wire relations in this order: People ← everything's owners; Channels ← Ideas/Videos; Videos ↔ Tasks; Tasks ↔ Tasks (Blocked By/Blocks); Ideas → Videos.
2. Build the Ideas scoring formula + Priority formula. Test with 5 real ideas.

**Day 3–4: Templates (the standardization payload)**
3. Build the `🎬 New Video` template with all 15 stage tasks, relative dates, dependency links, SOP relations (AUT-001). Test end-to-end with one real video.
4. Build `New Channel` template (full hub layout) and instantiate channel #1.
5. **Migrate current work in flight** into Videos/Tasks. From this day forward, nothing lives outside the system.

**Day 5: Operating rhythm**
6. Create **Meetings** DB + Weekly Sync template; **OKRs** + this quarter's objectives (max 3); the KPI Weekly database with week-1 row (manual is fine).
7. Assemble **Company HQ** and the three role dashboards from linked views (they'll grow as later DBs land).

*Exit criteria: a video was created from the template, its 15 tasks exist with owners, and Monday's meeting ran off the scoreboard.*

## Phase 2 (Week 2): Intelligence + knowledge

8. **Competitors + Competitor Videos**; log your 10 nearest competitors and 20 outlier videos; convert 5 into scored Ideas (proves the loop).
9. **SOP Library** + write SOP-001/002/003 first (the daily-use trio) from [starter-sops](../sops/starter-sops.md); others within 2 weeks, each written by whoever runs the process.
10. **Prompt Library** + seed PRM-001…010 from [the starter set](../ai/prompt-library-starter.md).
11. **Knowledge Base**; backfill 5 ⭐Canon entries; **Assets** with license fields; backfill every asset currently used in production (yes, all — this is the rights audit).

## Phase 3 (Week 3): Money + metrics

12. **Metrics Snapshots** (both DBs). Set up AUT-002 (YouTube API → snapshots via Make/n8n); manual Monday entry as interim fallback.
13. **Finance** (Revenue + Expenses); backfill this quarter; wire Video cost rollups and Channel profit/Health formulas.
14. **Sponsor CRM** (Companies/Contacts/Deals); import every past and current conversation; Growth dashboard goes fully live.

## Phase 4 (Week 4): People + automation hardening

15. **Hiring** DB + role scorecard for the first hire (editor). Post the role. This is not optional — see [Strategic Analysis §1.1](00-strategic-analysis.md).
16. **Automations Registry**; document AUT-001/002 already live; build AUT-003 (Slack alerts) and AUT-004 (idea intake).
17. Documentation audit: every database has its 📘 About block. Analytics Dashboard assembled.

## Operating cadence from Week 5

- **Daily:** everyone works from `My Plate`; factory board is truth.
- **Weekly (Mon):** scoreboard → pipeline walk → priorities. Idea inbox to zero.
- **Monthly:** analytics deep-dive (SOP-007), P&L per channel, automation health, SOP staleness.
- **Quarterly:** OKR grading + setting, SWOT refresh, scoring-model recalibration, AI policy review.

## Definition of "the OS is working" (check at day 60)

1. Zero work exists outside Videos/Tasks. 2. A stranger could produce a thumbnail from SOP-004 alone. 3. The Monday meeting starts from a scoreboard nobody compiled by hand. 4. You know cost-per-video for the trailing five videos. 5. The first hire is executing pipeline stages.
