# 🎨 Asset Library

> **Purpose:** Registry of every reusable creative asset — AND the rights-management system that keeps documentary channels alive. Files live in Drive/Frame.io; Notion holds the link + **license metadata**, which is the part that saves you in a copyright dispute.
> **Owner:** Founder 3.
> **Instructions:** No asset enters a video unless it has a row here with License Type filled and Proof attached. The QA stage audits this via the Video's `Assets Used` relation.
> **Linked SOPs:** SOP-003 Editing, SOP-005 QA. **Related:** Videos (used-in), Channels (brand kits).

## Properties

| Property | Type | Notes |
|---|---|---|
| Asset | Title | |
| Type | Select | Logo / Font / Music / SFX / B-roll / Archival footage / Animation / Template / Brand Guideline / Stock image |
| Channel | Relation → Channels | blank = company-wide |
| File Link | URL | Drive/Frame.io — never upload heavy media to Notion |
| Preview | Files | thumbnail/low-res only |
| **License Type** | Select | `Owned / Commissioned (WFH) / Royalty-free sub / Licensed (paid) / Creative Commons / Public Domain / Fair-use claim ⚠️` |
| **License Proof** | Files/URL | receipt, license PDF, subscription record, CC page archive |
| Source / Attribution Required | URL / Checkbox | |
| License Expiry | Date | subscriptions & term licenses — expiry view prevents silent lapses |
| Fair-use Rationale | Text | REQUIRED if license type is fair-use: transformation argument, portion used |
| Used In | Relation → Videos | the audit trail, populated during editing |
| Tags | Multi-select | searchability: era, mood, subject |

## Views

`By Type` · `By Channel` (brand kits) · `⚠️ Expiring 60d` · `⚠️ Fair-use claims` (Founder 1 reviews monthly — these are your risk register) · `Music` (gallery w/ mood tags).

## AI table

| 🤖 AI does | 👁 Human reviews | 🚫 Never automated |
|---|---|---|
| Auto-tags assets; drafts fair-use rationales for review; flags videos whose Assets Used contain expiring/unproven licenses | Every fair-use rationale (human legal judgment) | Clearing an asset for publish |
