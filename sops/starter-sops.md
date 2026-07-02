# The 10 Starter SOPs

Each of these becomes a row in the [SOP Library](../databases/sops.md), created from the `New SOP` template. Written to be executable by a competent stranger — that's the test (the first freelancer trial project doubles as the SOP's QA). All start at v1.0; the person who runs the process maintains it.

---

## SOP-001: Research (v1.0) — Owner: F1 · ~4h/video · Stages: Idea, Research

**Purpose:** turn an approved idea into a fact-checked research brief a scriptwriter can trust blindly.

1. Open the Idea row; read score rationale, references, and `Inspired By` competitor videos.
2. Run **PRM-001** with the topic + angle → AI research brief draft into the Idea's `AI Research Notes`.
3. **Verify every load-bearing claim against a primary source.** Minimum 5 independent sources; each claim in the brief gets an inline source link. AI text without a verified source is deleted, not kept "for flavor."
4. Build the source list: primary docs, books, reputable journalism. Flag paywalled/disputed items.
5. Rights pre-scan: list archival footage/imagery the story will need; check availability & license path (feeds Assets).
6. ⚠️ Crime/Health/Religion: complete the claims-verification checklist (named individuals, medical claims, doctrinal claims) — legal-risk flags go to F1.
7. Deliverable: research brief in the Video page — narrative summary, verified claim list w/ sources, characters/timeline, open questions, rights notes.

**Quality bar:** a scriptwriter never needs to re-Google a fact. **Common mistake:** trusting AI citations without opening them.
🤖 drafts brief, suggests sources · 👁 every claim verified by human · 🚫 crime/health claims are never AI-verified only.

---

## SOP-002: Script (v1.0) — Owner: F3 · ~6h/video · Stages: Outline, Script, Voiceover

1. Read research brief + the channel's Brand Voice spec and Story Structures.
2. Outline first (PRM-002 assist): hook (first 30s promise), 3–5 acts, open loops at act breaks, payoff. **Outline approved before drafting** — rework is 10× cheaper here.
3. Draft with PRM-003 per act, then rewrite in channel voice. Target length per channel spec (words ≈ minutes × 140 for docs pacing).
4. Hook pass: write 3 hook variants (PRM-005); read aloud; pick with F1.
5. Self-check: reading-level, no unexplained jargon, every claim traceable to the brief (add nothing the research doesn't support).
6. Submit to Review stage (SOP-005). After approval → VO: record per channel voice spec, or generate + human-QA if the channel uses AI voice (see AI policy §4).

**Quality bar:** first 30 seconds make skipping feel expensive; no claim beyond the brief.
🤖 outline + draft v1 · 👁 line-by-line rewrite, voice, facts · 🚫 publishing an unedited AI script.

---

## SOP-003: Editing (v1.0) — Owner: F3 · ~20h/video · Stage: Editing

1. Assemble: VO on timeline, rough visual pass matching script beats.
2. **Every asset placed must exist in the Asset Library with License Type + Proof.** Add new assets to the DB before using them. Link all to the Video's `Assets Used`.
3. Visual rhythm: change something on screen every 3–6s in the first minute; no static shot > 8s without motion/zoom.
4. Sound pass: music beds per channel kit, ducked under VO; SFX at transitions.
5. Retention pass: rewatch the first 60s cold — cut anything before the promise lands.
6. Export per platform spec; upload to Drive/Frame.io; link on Video row; move to parallel packaging stages.

**Quality bar:** `Assets Used` complete = QA won't bounce it; first minute survives a bored viewer.
🤖 rough-cut assembly tools, auto-captions, b-roll search · 👁 pacing, story, all asset clearances · 🚫 publish-without-human-watch; fair-use calls.

---

## SOP-004: Packaging — Thumbnail + Title (v1.0) — Owner: F3 produce / F1 approve · ~3h · Stages: Thumbnail, Title

1. Start from the Idea's validated thumbnail concept + title options (they existed *before* production — the gate guarantees it).
2. Thumbnails: 2–3 distinct variants (different visual ideas, not color tweaks). Rules: one focal object, ≤ 4 words, legible at 120px, channel style guide respected.
3. Titles: 5+ candidates via PRM-004; test each against: curiosity gap? honest? < 60 chars? matches thumbnail promise without repeating it?
4. F1 approves the pair (thumbnail + title are ONE promise; approve together).
5. Record `Thumbnail Style` and `Hook Type` tags on the Video row (this powers the "what works" analytics).
6. Losing variants saved to the Video page for A/B swap if 24h CTR is below floor (AUT-005).

**Quality bar:** you'd click it in a sidebar of the channel's actual competitors.
🤖 concept brainstorms (PRM-006), draft imagery, title candidates · 👁 selection, honesty check · 🚫 clickbait that the video can't cash.

---

## SOP-005: QA & Review (v1.0) — Owner: reviewer ≠ maker · ~2h · Stages: Review, QA

**Script Review (stage 5, F1):** facts vs brief (spot-check 10 claims) · voice vs channel spec · rights flags cleared · legal checklist for sensitive niches · hook approved. Verdict: approve / revise-with-notes.

**Final QA (stage 12, F2 today):**
1. Watch the full video at 1× like a viewer. (No skipping. Yes, really.)
2. Checklist: audio levels · typos in on-screen text · **asset-clearance audit** (`Assets Used` complete, no ⚠️ fair-use unreviewed, no expiring licenses) · sponsor deliverables per Deal spec · title/thumbnail/description match · end screen + cards set.
3. Any failure → back to owning stage with notes. QA does not fix; QA bounces.
4. Pass → sign QA task Done (this is what unlocks Scheduling — AUT-007).

**Quality bar:** zero copyright surprises, zero "we said we'd fix that" repeats.
🤖 typo/loudness scans, checklist pre-fill · 👁 the entire watch-through, every clearance · 🚫 the QA sign-off itself. Never the maker.

---

## SOP-006: Publishing (v1.0) — Owner: F3 · ~1h · Stages: Description, SEO, Scheduled, Published

1. Description (PRM-007 assist): 2-line hook, chapters, sponsor copy exactly per Deal, source credits (documentary trust signal), newsletter link (always).
2. SEO: tags, end screens to best adjacent video, cards at retention dips, playlist placement.
3. Upload → schedule at channel's slot (consistency beats "optimal hour"). Verify monetization checks pass pre-publish.
4. On publish: confirm live, pin a comment with a question (engagement seed), Slack notify (AUT-003).
5. Set the 24h/7d/30d snapshot expectations (AUT-002 handles rows).

🤖 drafts everything in step 1–2 · 👁 sponsor copy vs contract, all metadata · 🚫 the publish click; sponsor copy edits without F2 sign-off.

---

## SOP-007: Analytics Review (v1.0) — Owner: F1 · weekly 30min / monthly 2h

**Weekly:** verify AUT-002 ran → scan 24h alerts → scoreboard row commentary (PRM-008 draft, human-verified) → flag anomalies for Monday.
**Monthly:** 30d cohort vs predictions (calibration view) · update "what works" reads (only n≥5 groups) · pick 1–2 packaging/story experiments for next month (each = a Knowledge Base hypothesis entry) · 3 lessons → Knowledge Base with "what we do differently" lines.
**Quarterly:** reweight the Idea scoring formula against actuals; document the change in the Ideas DB version log.

🤖 ingestion, drafts, anomaly flags · 👁 every causal claim · 🚫 strategy pivots from single-video data.

---

## SOP-008: Hiring (v1.0) — Owner: F2 source / F1 decide · per role rubric

1. Role scorecard first: outcomes (not duties), quality rubric 1–5 with examples, rate band. Store in the Applicants page template.
2. Source (freelance markets, communities, referrals) → every candidate a row.
3. Screen portfolio vs rubric (AI pre-flags, human decides) → 20-min call: communication, availability, rate, red flags → notes in row.
4. **Trial project: real, paid, small** — one pipeline task with the real SOP. Score 1–5 vs rubric. SOP unclear to them? That's an SOP bug — log it.
5. Trial ≥ 4 → offer (rate, terms, NDA/contract templates) → convert to People row → SOP-009 onboarding. Trial 3 = Talent Pool. ≤ 2 = reject kindly, tag reason.

🤖 sourcing lists, screening flags, outreach drafts · 👁 every screen, every interview · 🚫 offers and rejections.

---

## SOP-009: Training & Onboarding (v1.0) — Owner: F1 → role manager

Day 1: accounts (Notion member-level, Slack, Drive scoped) · People row + onboarding checklist from role template · read: HQ principles, their SOPs, ⭐ Canon knowledge entries.
Video 1: shadow — watch a gold-standard example of their deliverable, annotate differences vs their trial.
Videos 1–2: full SOP execution with review-every-step; feedback logged in Performance Notes.
Video 3: normal pipeline, normal QA. Target: full speed by video 3, not video 10.
Every onboarding ends with: "which SOP step was unclear?" → SOP edit. New hires are your best documentation auditors.

🤖 drafts role checklists, answers "how do we X" from SOPs/KB · 👁 all feedback human · 🚫 performance judgments.

---

## SOP-010: Sponsorships (v1.0) — Owner: F2

1. Prospect: mine Competitor `Sponsor Types` + niche-fit brands → Companies rows with Fit Channels.
2. Outreach (PRM-010 drafts, F2 edits every send): lead with audience fit + retention stats from Snapshots, not just subs. Log every touch; set Next Follow-up (3-touch cadence: D0, D4, D10).
3. Qualify → pitch: one-pager auto-fed by channel stats. Price from rate card (CPM-based floor; F1 approves discounts > 15%).
4. Close: Deal row through stages; contract + insertion order attached; deliverables spelled out.
5. Deliver: Deal → Video relation; integration copy into the Description stage task; F2 verifies in QA.
6. Post-air: performance recap to sponsor within 7 days (retention on the integration slot — renewals are sold here) → invoice → Revenue row on payment.

🤖 prospect lists, outreach/recap drafts, pitch stats · 👁 every external email, all pricing · 🚫 unsupervised sending; contract terms.
