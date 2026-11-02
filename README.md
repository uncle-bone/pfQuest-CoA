# pfQuest-CoA

> **[⬇ Download v1.0.5 — Current stable release](https://github.com/uncle-bone/pfQuest-CoA/releases/download/v1.0.5/pfQuest-CoA-v1.0.5.zip)** — [release notes](https://github.com/uncle-bone/pfQuest-CoA/releases/tag/v1.0.5).

Quest helper and Conquest Reborn database addon for Ascension: Conquest of Azeroth / Conquest Reborn (WoW 3.3.5a).

Maintainer: **Uncle Bone**

## Current release: v1.0.5

This release contains the latest available pfQuest-CoA channel-hotfix package. Both addon folders, `pfQuest/` and `pfQuest-ascension/`, are included side by side with upstream license notices and attribution.

### v1.0.5 changes

- Adds an experimental, bounded journal for confirmed quest-ID discoveries.
- The SmartSync component attaches only to an already existing **BBLC25C** channel. It does not create, reorder, leave, or otherwise modify chat channels.
- Preserves existing quest data, world-map/minimap features, and SavedVariables.
- Uses the package's stable addon metadata version **1.0.5**.

This build does **not** implement the later proposed CoASync channel migration. SmartSync and cross-player behavior still need in-game validation with another compatible client online.

## v1.0.4

- Adds **Prefer Stock Quest Giver/Turn-in Icons** to CoA Map & Minimap Styles.
- Enabled by default to avoid overlapping pfQuest and Blizzard quest-giver markers while preserving objective markers and routes.

## v1.0.1

- Throttles periodic minimap refresh from approximately 20 Hz to 5 Hz.
- Preserves world-map animation, pin positioning, quest databases, custom content patches, and SavedVariables.

## Installation

Extract both addon folders side by side into `Interface/AddOns/` and enable both in Conquest Reborn. Do not remove SavedVariables when updating.

### Upstream acknowledgments

Original pfQuest by Shagu / Eric Mauser. See the included `LICENSE` files for upstream license terms.

The addon remains a community fork and is not an official Ascension product.
