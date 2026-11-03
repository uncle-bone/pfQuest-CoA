# pfQuest-CoA

> **[Download Here!](https://coa-research.unclebone.workers.dev/download/pfQuest-CoA)** · [Release notes](https://github.com/uncle-bone/pfQuest-CoA/releases/tag/v1.0.17)
> **Current stable release: v1.0.17.**

Quest helper and Conquest Reborn database addon for Ascension: Conquest of Azeroth / Conquest Reborn (WoW 3.3.5a, Interface 30300).

Maintainer: **Uncle Bone**

## v1.0.17 — CoASync bootstrap and identity fixes

- Send the PFQ6 HELLO when sharing is enabled even if no peers are known yet, allowing two fresh clients to discover each other.
- Keep record and bucket traffic gated until a peer is known.
- Test peerless startup HELLO, category-specific quest IDs, channel validation, and peer counting.
- Show v1.0.17 in both in-game CoASync pane headers and keep addon metadata aligned.
- Preserve PFQ6 framing, existing quest records, settings, and SavedVariables.

In-game multi-client verification remains pending.

## Previous stable v1.0.16 — CoASync receive and quest-log fixes

- Correct SmartSync CoASync receive handling for WoW 3.3.5a: accept plain or decorated channel names only when the local channel number also matches the joined CoASync slot.
- Fix quest-log scanning so the second return value from GetNumQuestLogEntries cannot be misinterpreted as a tonumber base.
- Add a Lua 5.1 regression test confirming valid messages increase received/peer counts and invalid channel identities are ignored.
- Preserve PFQ6 protocol framing, quest data, settings, diagnostics, and existing SavedVariables.

Automated Lua syntax, regression, TOC, and ZIP integrity checks passed. In-game multi-client verification remains pending.

## Previous stable release: v1.0.15

This release moved pfQuest-CoA sharing to the shared **CoASync** channel and added bounded multi-category discovery reconciliation. Both addon folders, `pfQuest/` and `pfQuest-ascension/`, are included side by side with upstream license notices and attribution.

- Uses the **CoASync** channel and a dedicated `PFQ6` discovery protocol.
- Waits 20 seconds after login before attempting to join, checks for existing channels, and hides CoASync from visible chat frames without leaving the channel.
- Adds bounded indexing and reconciliation for quest discoveries, plus sharing status and controls.
- Preserves existing quest data, map features, and SavedVariables.
- The optional status panel opens only when requested with `/pfqsyncui`; it does not open automatically.

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
