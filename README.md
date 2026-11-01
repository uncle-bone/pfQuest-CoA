# pfQuest-CoA

> **[⬇ Download v1.0.4 — Current stable release](https://github.com/uncle-bone/pfQuest-CoA/releases/download/v1.0.4/pfQuest-CoA-v1.0.4.zip)** — install-ready package for WoW 3.3.5a / Conquest Reborn.

Quest helper and Conquest Reborn database addon for Ascension: Conquest of Azeroth / Conquest Reborn (WoW 3.3.5a).

Maintainer: **Uncle Bone**

## Current release: v1.0.4

Adds an option to use stock Blizzard quest-giver and turn-in icons alongside pfQuest's map features. Both required addon folders are included: `pfQuest/` and `pfQuest-ascension/`.

### v1.0.4 changes

- Adds **Prefer Stock Quest Giver/Turn-in Icons** to CoA Map & Minimap Styles.
- Enabled by default to avoid overlapping pfQuest and Blizzard quest-giver markers.
- Preserves quest objective markers and routes.
- Can be disabled to compare pfQuest's own marker styles; existing Save, Cancel, and Reset controls remain available.
- Keeps upstream license notices and attribution.

Install both addon folders side by side in `Interface/AddOns/`. Runtime behavior of the new style option still needs in-game testing on Conquest Reborn. The previous v1.0.1 release established the minimap refresh performance baseline.

## v1.0.1

- Throttles periodic minimap refresh from approximately 20 Hz to 5 Hz.
- Preserves world-map animation, pin positioning, quest databases, custom content patches, and SavedVariables.

## v1.0.0 baseline

The initial package is based on the supplied pfQuest and pfQuest-ascension source archive. Both addon directories are required. It established independent CoA version numbering, enabled the default 3.3.5a TOCs, preserved SavedVariables and Conquest Reborn patches, and retained upstream license notices and attribution.

### Upstream acknowledgments

Original pfQuest by Shagu / Eric Mauser. See each bundled `LICENSE` file for upstream license terms.

The addon remains a community fork and is not an official Ascension product.
