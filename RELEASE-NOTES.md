# pfQuest-CoA v1.0.15 — Stable

Current stable release for Conquest Reborn. This release publishes the latest pfQuest v1.0.15-dev build with stable **1.0.15** version labels.

- Includes `pfQuest/` and `pfQuest-ascension/` side by side with upstream license notices and attribution.
- Uses the shared **CoASync** channel and PFQ6 protocol for bounded multi-category quest discovery reconciliation.
- Waits 20 seconds after login before attempting to join, checks existing channel slots, and hides the channel from visible chat frames without leaving it.
- Preserves existing quest data, map features, and SavedVariables.
- An optional status panel can be opened with `/pfqsyncui`.

Known limitation: sharing and cross-client synchronization still need in-game validation with compatible peers. The status panel is optional and does not open automatically.

Maintainer: Uncle Bone
