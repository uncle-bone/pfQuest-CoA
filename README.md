# pfQuest-CoA

> **[⬇ Download v1.0.1 — Current stable release](https://github.com/uncle-bone/pfQuest-CoA/releases/download/v1.0.1/pfQuest-CoA-v1.0.1.zip)** — install-ready package for WoW 3.3.5a / Conquest Reborn.

Quest helper and Conquest Reborn database addon for Ascension Conquest of Azeroth / Conquest Reborn (WoW 3.3.5a).

Maintainer: **Uncle Bone**

## Current release: v1.0.1 (2026-11-01)

The current release establishes a conservative performance baseline while keeping pfQuest's zone-based map architecture. It includes both required addon folders: `pfQuest/` and `pfQuest-ascension/`.

### v1.0.1 changes

- Throttles periodic minimap refresh from approximately 20 Hz to 5 Hz.
- Preserves world-map animation, pin positioning, quest databases, custom content patches, and SavedVariables.
- Includes the upstream license notices and attribution.

Runtime behavior still needs in-game verification on Conquest Reborn.

## v1.0.0 baseline (2026-11-01)

The initial package is based on the supplied pfQuest and pfQuest-ascension source archive. Both addon directories are required:

- `pfQuest/`
- `pfQuest-ascension/`

Install both in `Interface/AddOns`. Enable both at the AddOns selection screen.

### Initial changes

- Start independent CoA version numbering at `1.0.0` for standard Wrath TOCs and the CR database extension.
- Enable the default 3.3.5a TOC files.
- Preserve the existing SavedVariables and Conquest Reborn database patches.
- Disable the extension's old Conquest Reborn client-update announcements and related addon version broadcasts.
- Preserve original upstream attribution and license notices.

**Status:** Source package integrity checked; in-game operation still needs testing on Conquest Reborn.

### Upstream acknowledgments

Original pfQuest by Shagu / Eric Mauser. See each bundled `LICENSE` file for upstream license terms.

The addon remains a community fork and is not an official Ascension product.
