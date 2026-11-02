# pfQuest-CoA

> **[Download](https://github.com/uncle-bone/pfQuest-CoA/releases/latest)**

Quest helper and Conquest Reborn database addon for Ascension: Conquest of Azeroth / Conquest Reborn (WoW 3.3.5a, Interface 30300).

Maintainer: **Uncle Bone**

## Current release: v1.0.15

This release updates pfQuest-CoA sharing to the shared **CoASync** channel and adds bounded multi-category discovery reconciliation. Both addon folders, `pfQuest/` and `pfQuest-ascension/`, are included side by side with upstream license notices and attribution.

### v1.0.15 changes

- Uses the **CoASync** channel and a dedicated `PFQ6` discovery protocol.
- Waits 20 seconds after login before attempting to join, checks for existing channels, and hides CoASync from visible chat frames without leaving the channel.
- Adds bounded indexing and reconciliation for quest discoveries, plus sharing status and controls.
- Preserves existing quest data, map features, and SavedVariables.
- The optional status panel opens only when requested with `/pfqsyncui`; it does not open automatically.

Sharing and cross-client synchronization still need in-game validation with compatible peers. The release ZIP is based on the v1.0.15-dev chat build; the included addon version labels are set to stable **1.0.15**.

## v1.0.16 maintenance status

The v1.0.16 development package fixes a WoW 3.3.5a Lua runtime error in `coa_sync.lua` caused by passing the multiple return values of `GetNumQuestLogEntries()` into `tonumber()`. It retains the CoASync sharing diagnostics and command buttons. **This fix has not yet been published as a verified GitHub release; the current verified release remains v1.0.15.**

For the in-game sharing panel, open pfQuest settings and select **Open Sharing & Diagnostics**. The panel includes buttons for status, statistics, channel information, and refresh. CoASync should be joined after a delayed startup and hidden from ordinary chat windows. For troubleshooting, use `/pfqsync status`.

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
