# pfQuest-CoA v1.0.16 — Prerelease

- Correct SmartSync CoASync receive handling for WoW 3.3.5a: accept the event's plain or decorated channel name only when its numeric local channel index matches the joined CoASync slot.
- Fix quest-log scanning so the second return value from GetNumQuestLogEntries cannot be misinterpreted as a tonumber base.
- Add a Lua 5.1 regression test confirming valid messages increase received/peer counts and invalid channel identities are ignored.
- Preserve PFQ6 protocol framing, quest data, settings, diagnostics, and the v1.0.15 stable release.

Built from the checksum-verified v1.0.15 source archive. Automated Lua syntax, regression, TOC, and ZIP integrity checks are required. In-game multi-client verification remains pending.
