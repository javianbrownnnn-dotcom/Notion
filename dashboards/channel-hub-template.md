# 📺 Channel Hub Template

Every channel's row page in the Channels database IS its hub, born from the `New Channel` template — which is how "every channel uses the exact same production system" is enforced structurally rather than by promise. Full field list in [channels.md](../databases/channels.md); this file describes the page experience.

## Page layout

**Header** — banner in channel brand style · Code, Status, Lead, Upload schedule (properties).

**1. 🧭 Strategy block** (the identity — the ONLY part that differs between channels)
- Mission · Target audience persona · Value proposition
- Brand voice spec (narrator persona, pacing, vocabulary, banned clichés) + VO artist
- Story structures used (linked Knowledge entries)
- Monetization strategy & future opportunities
- SWOT (dated quarterly entries)

**2. 🚦 Pipeline block** (identical for every channel)
- Ideas: `Ranked` view filtered to this channel + fuel-gauge callout
- Videos: Factory board filtered to this channel
- Content calendar (this channel)
- `⚠️ At Risk` list

**3. 📈 Performance block**
- Channel Snapshots (this channel, by week)
- Published videos by `Performance vs Channel Avg`
- 24h alerts (this channel)

**4. 💰 Commercial block**
- Deals (this channel) by stage
- Revenue by stream (this channel) · Profit 30d
- Sponsor-fit companies (Companies where Fit Channels contains this channel)

**5. ⚔️ Intelligence block**
- Competitors (this channel) · their outlier videos not yet converted to Ideas

**6. 🎨 Brand kit** — Assets filtered to this channel (logo, fonts, music beds, templates, guidelines).

## Scaling behavior

- **Channel #2**: duplicate nothing — create one row from the template; every view auto-filters. Launch day is SOP-011.
- **At ~10 channels**: each channel becomes a Notion teamspace whose homepage is this hub; a Channel Lead owns it; the databases behind it never change.
- A founder can compare any two channels field-by-field because the hubs are isomorphic. Deviation from the template requires Founder 1 sign-off (that's a company-wide process change, not a channel preference).
