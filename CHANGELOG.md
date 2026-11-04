# Changelog

Current stable release: **v1.0.17** · [Direct ZIP download](https://github.com/uncle-bone/pfQuest-CoA/releases/download/v1.0.17/pfQuest-CoA-v1.0.17.zip)

## v1.0.18 — Tested development candidate (release pending)

- Add `/pfqsync simulate` PFQ6 local diagnostic with reported no-channel-traffic result.
- Preserve real peer-to-peer PFQ6 synchronization and existing SavedVariables compatibility intent.
- Live in-game result: simulation PASS; after simulation, two more messages received and one new record imported from real peers.
- Remaining verification: Lua 5.1 automated regression execution, relog persistence, and remote-client confirmation of outgoing record receipt.
- Not yet published as a stable GitHub release; do not use an unverified v1.0.18 asset URL.

## v1.0.17 — CoASync bootstrap and identity fixes

- Allow HELLO packets to bootstrap peer discovery when no peer is known; keep record traffic gated until discovery.
- Add Lua 5.1 regression coverage for peerless HELLO, category-specific quest IDs, and incoming channel validation.
- Set both in-game CoASync pane headers from the packaged v1.0.17 version.
- Preserve PFQ6 framing, existing quest data, settings, and SavedVariables. In-game multi-client verification remains pending.

## v1.0.16 — CoASync receive and quest-log fixes

- Validate local CoASync channel index and plain/decorated channel name.
- Fix quest-log scanning with the multi-value GetNumQuestLogEntries API.
- Preserve PFQ6 protocol framing and SavedVariables.

## v1.0.15 — Previous stable

- Publish the latest v1.0.15-dev CoASync build with stable 1.0.15 version labels.
- Add bounded multi-category quest discovery reconciliation over CoASync using the PFQ6 protocol.
- Delay channel join by 20 seconds, check channel availability, and hide CoASync from visible chat frames without leaving it.
- Preserve existing quest data, map features, and SavedVariables.
- Cross-client sharing still requires in-game validation with compatible peers.

## v1.0.4

- Add **Prefer Stock Quest Giver/Turn-in Icons** to CoA Map & Minimap Styles.
- Enable by default to prevent overlapping pfQuest and Blizzard quest-giver markers.
- Preserve objective markers, routes, and the existing Save, Cancel, and Reset controls.
- Runtime behavior still needs in-game confirmation.

## v1.0.1

- Throttle periodic minimap refresh from approximately 20 Hz to 5 Hz.
- Preserve world-map animation, pin positioning and existing SavedVariables.
- Package complete pfQuest and pfQuest-ascension addon folders with upstream license notices.
- Runtime validation pending.

## v1.0.0

- Establish independent project version numbering.
- Baseline from user-supplied pfQuest and pfQuest-ascension archive.
- Update Wrath 3.3.5a addon metadata.
- Preserve character settings, database extension, and upstream licensing.
- Disable the extension's upstream version-broadcast messaging.
- Initial package delivered in project chat; runtime testing pending.
