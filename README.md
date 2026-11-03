# pfQuest-CoA

> **[Download Here!](https://coa-research.unclebone.workers.dev/download/pfQuest-CoA)**

Quest helper and Conquest Reborn database addon for Ascension: Conquest of Azeroth / Conquest Reborn (WoW 3.3.5a, Interface 30300).

Maintainer: **Uncle Bone**

## **Current stable release: v1.0.15.**

This release updates pfQuest-CoA sharing to the shared **CoASync** channel and adds bounded multi-category discovery reconciliation. Both addon folders, `pfQuest/` and `pfQuest-ascension/`, are included side by side with upstream license notices and attribution.

### v1.0.15 changes

- Uses the **CoASync** channel and a dedicated `PFQ6` discovery protocol.
- Waits 20 seconds after login before attempting to join, checks for existing channels, and hides CoASync from visible chat frames without leaving the channel.
- Adds bounded indexing and reconciliation for quest discoveries, plus sharing status and controls.
- Preserves existing quest data, map features, and SavedVariables.
- The optional status panel opens only when requested with `/pfqsyncui`; it does not open automatically.

Sharing and cross-client synchronization still need in-game validation with compatible peers. The release ZIP is based on the v1.0.15-dev chat build; the included addon version labels are set to stable **1.0.15**.

## v1.0.16 — CoASync receive and quest-log fixes (prerelease)

- Fix WoW 3.3.5a channel event parsing: accept plain or decorated CoASync names only when the local channel number also matches.
- Fix quest-log polling by capturing the first return from GetNumQuestLogEntries before converting it.
- Preserve PFQ6 framing, quest sharing, diagnostics, SavedVariables, and the v1.0.15 stable package.

[Download the v1.0.16 prerelease ZIP](https://github.com/uncle-bone/pfQuest-CoA/releases/download/v1.0.16/pfQuest-CoA-v1.0.16.zip)

This build is based on the verified v1.0.15 release archive with source checksum validation. Automated Lua 5.1 and ZIP checks pass before publication. Multi-client behavior still needs in-game confirmation.

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
