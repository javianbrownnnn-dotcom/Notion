# 🤝 Sponsor CRM — Companies, Contacts, Deals

Founder 2's engine. Three related databases (a flat "sponsors" list stops working the first time one company sponsors three videos across two channels through two different contacts).

---

## 🏢 Companies

> **Purpose:** every brand we could ever sell to. **Owner:** Founder 2.

| Property | Type | Notes |
|---|---|---|
| Company | Title + URL | |
| Category | Select | VPN / SaaS / Finance app / Education / DTC / Gaming / Health … |
| Fit Channels | Relation → Channels | where their audience overlaps ours |
| Sponsors Competitors? | Relation → Competitors | warm signal — they already buy this niche |
| Status | Select | `Prospect / Contacted / In Conversation / Active Sponsor / Churned / Dead` |
| Contacts / Deals | Relations | |
| Lifetime Value | Rollup | Deals → sum of Value (Won) |
| Notes | Page | call notes, preferences, history |

## 👤 Contacts

| Property | Type | Notes |
|---|---|---|
| Name | Title | |
| Company | Relation → Companies | |
| Role / Email / LinkedIn | Text/URL | |
| Relationship Owner | Relation → People | |
| Last Touch | Date | automation-updated from email if possible |
| Next Follow-up | Date | drives the follow-up view — nothing falls through |

## 💰 Deals

> The pipeline. One row per negotiation, not per company.

| Property | Type | Notes |
|---|---|---|
| Deal | Title | `Company — Channel — Month` |
| Company / Contact | Relations | |
| Channel | Relation → Channels | |
| Stage | Status | `Lead → Pitched → Negotiating → Verbal → Contract Sent → Won → Delivered → Paid` / `Lost` |
| Value | Number ($) | |
| Weighted Value | Formula | Value × stage probability (Pitched .1, Negotiating .3, Verbal .6, Contract .8, Won 1) — the forecast number |
| Deliverables | Text | integration length, placement, exclusivity |
| Videos | Relation → Videos | **the integration lands in the production pipeline as a real dependency** — sponsor copy becomes part of the Description stage task |
| Contract / Insertion Order | Files | |
| Invoice Status | Select | `Not Sent / Sent / Paid / Overdue` |
| Revenue Entries | Relation → Revenue | when paid |
| Close Date / Air Date | Dates | |
| Lost Reason | Select | Price / Timing / Metrics too small / Ghosted |

**Views:** `Pipeline` (board by Stage — Founder 2's main screen) · `Forecast This Quarter` (sum Weighted Value) · `⚠️ Overdue Invoices` · `Delivered, Unpaid` · `Follow-ups Due` (on Contacts).

## AI table

| 🤖 AI does | 👁 Human reviews | 🚫 Never automated |
|---|---|---|
| Builds prospect lists from Competitor sponsor data; drafts outreach & follow-up emails (PRM-010); drafts pitch-deck stats from Snapshots; summarizes call notes | Every email before send; pricing | Sending outreach unsupervised; negotiating terms; signing anything |
