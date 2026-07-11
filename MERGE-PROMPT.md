# Merge Prompt — Integrate the Media OS + CI research into THE-BIG-3

Paste the block below into a Claude Code session that has **both** repositories in scope:
`javianbrownnnn-dotcom/notion` and `javianbrownnnn-dotcom/THE-BIG-3`.

> **How to give a session both repos:** On Claude Code for web, create/configure the environment so both repos are added as sources (same settings area as the network policy). Locally, `git clone` both repos side by side and run Claude Code from a directory that can see both.

---

## THE PROMPT (copy everything below this line)

You have access to two repositories:

- **SOURCE:** `javianbrownnnn-dotcom/notion`, branch `claude/youtube-media-os-notion-kovjm5`. It contains a complete Notion "Media OS" specification (17 database schemas in `databases/`, dashboards in `dashboards/`, SOPs in `sops/`, AI prompt library in `ai/`, strategy/roadmap/scaling docs in `docs/`, a build script `build_media_os.py`) **plus two** completed competitive-intelligence reports: the **business/modern-ambition** niche (`docs/05-competitive-intelligence-report.md` + `research/modern-ambition-2026-07/`) and the **Christianity/faith** niche (`docs/06-competitive-intelligence-christianity.md` + `research/christianity-2026-07/`). Both use the identical structure and both include a "How to Load This Into Notion" section mapping their data to the databases.
- **TARGET:** `javianbrownnnn-dotcom/THE-BIG-3` — the main workspace repo for our 3-founder YouTube media company. The "business" niche work already lives here.

**Your job:** integrate the SOURCE content into TARGET so everything connects cleanly. This is a careful content merge, not a blind copy.

### Hard requirements (do not violate)
1. **Audit TARGET FIRST.** Before writing anything, read TARGET's full structure and list what already exists (databases, docs, any business-niche CI content, any Ideas/Competitors/Channels material). Produce a short reconciliation table: "already in TARGET" vs "new from SOURCE" vs "conflicts/overlaps." Show it before making changes.
2. **No duplicate ideas.** Merge the CI report's 20 "opportunities" and 20 "video ideas" into a **single deduplicated Ideas list** — channel/niche-level concepts tagged as niches, individual videos as scored Ideas, overlaps collapsed into one entry each. If TARGET already has any of these ideas, update in place; never create a second copy.
3. **Don't overcrowd the app.** Keep one source of truth per entity. Databases live in one place; everything else references them. Do not create parallel/near-duplicate databases or docs. If TARGET already has a database that matches a SOURCE one, extend it — don't add a second.
4. **Seamless connections.** Preserve the relational design: Ideas→Channels, Competitors→Channels, Videos→Ideas, Knowledge Base entries → supporting evidence. Keep the evidence chain intact (every recommendation links to the competitor/video that inspired it).
5. **Full load for BOTH niches' CI data:** bring in all competitor rows (business ~35 + Christianity ~35), the pattern insights (→ Knowledge Base), the deduplicated Ideas set per niche, and each flagship channel as a Channels entry (business "Founder Reality"; Christianity "the Bible and its world") with strategy + 12-month projection. **Keep the two niches distinct** — Competitors tagged by Vertical (Business vs Religion/Christianity), Ideas scoped to their channel — so they don't cross-contaminate, and dedupe *within* each niche (each report's own opportunities vs video ideas overlap).
6. **Carry the Christianity sensitivity protocol** (report §10) into the QA SOP and AI policy for that channel — it is not optional metadata.

### Suggested structure in TARGET (adapt to what's already there)
- Media OS spec (`databases/`, `dashboards/`, `sops/`, `ai/`, `docs/`) — merge only what TARGET is missing.
- A `research/` area with one subfolder per niche: `research/business-modern-ambition/` (from SOURCE) and, later, `research/christianity/`.
- A single consolidated CI report doc per niche under `docs/` (mirror `docs/05-competitive-intelligence-report.md`).

### Process
1. Clone/read both repos. Confirm branch `claude/youtube-media-os-notion-kovjm5` on SOURCE.
2. Do the audit + reconciliation table (requirement 1). **Ask me to confirm the table before proceeding.**
3. Apply the merge on a new branch in TARGET (e.g. `integrate/media-os-and-ci`). Commit in logical chunks with clear messages.
4. Deduplicate ideas per requirement 2; show me the final merged Ideas list and flag anything you collapsed.
5. Push the branch and open a PR into TARGET's default branch summarizing: what was added, what was merged/updated, what was deduped, and any conflicts you resolved.
6. Do NOT delete or overwrite existing TARGET content without showing me first.

Work carefully and ask me a question whenever a merge decision is ambiguous (naming, where something should live, whether two ideas are truly duplicates). I would rather answer a question than have you guess.

---

*(End of prompt.)*

## After the merge
Both niche reports (business + Christianity) are already complete in SOURCE. Future niches (History, Crime, Science, Psychology, Health, Finance) follow the same pattern: run the CI agent per `docs/04-competitive-intelligence-agent.md`, drop raw output in `research/<niche>-<date>/`, write a consolidated `docs/0N-competitive-intelligence-<niche>.md`, then load into the databases with the same dedup + vertical-tagging rules above.
