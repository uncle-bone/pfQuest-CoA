# pfQuest-CoA v1.0.17 — CoASync bootstrap and identity fixes

- Send HELLO while no peers are known so fresh clients can discover each other; hold record sharing until a peer is established.
- Add Lua 5.1 regression coverage for peerless HELLO, distinct Q/C quest keys, and valid/invalid channel identities.
- Preserve PFQ6 framing, existing quest records, settings, and SavedVariables.

Stable release. Automated Lua syntax, regression, TOC and ZIP checks run before publication. In-game multi-client verification remains pending.

# pfQuest-CoA v1.0.16 — CoASync receive and quest-log fixes

- Correct SmartSync CoASync receive handling for WoW 3.3.5a: accept the event's plain or decorated channel name only when its numeric local channel index matches the joined CoASync slot.
- Fix quest-log scanning so the second return value from GetNumQuestLogEntries cannot be misinterpreted as a tonumber base.
- Add a Lua 5.1 regression test confirming valid messages increase received/peer counts and invalid channel identities are ignored.
- Preserve PFQ6 protocol framing, quest data, settings, diagnostics, and the v1.0.15 stable release.

Built from the checksum-verified v1.0.15 source archive. Automated Lua syntax, regression, TOC, and ZIP integrity checks are required. In-game multi-client verification remains pending.
