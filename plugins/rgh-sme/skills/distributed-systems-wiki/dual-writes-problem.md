---
type: concept
title: The Dual Writes Problem
description: >
  Application code writing the same change to two systems (database plus
  cache/index) inevitably drifts via race conditions and partial failure —
  the motivation for log-based integration.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 11"
---

# The Dual Writes Problem

The naive way to keep a search index, cache, or warehouse in sync with the
database is for application code to write to both. This fails in two
independent ways:

1. **Race conditions.** Two concurrent writers update value X: the database
   receives A-then-B while the index receives B-then-A (network
   interleaving). Both systems complete "successfully" and disagree
   *permanently* — silent drift with no error ever raised.
2. **Partial failure.** One write succeeds and the other fails
   ([which you cannot always even detect](unreliable-networks.md)), and the
   two systems diverge. Preventing this atomically would need
   [2PC](two-phase-commit.md) across heterogeneous systems, with all its
   costs.

The structural fix is to stop having two independent write paths: designate
one system the **system of record** (leader) and make every other
representation a **derived follower** consuming an ordered change log —
via [change data capture](change-data-capture.md) or
[event sourcing](event-sourcing.md). When the two things needing to stay in
sync are a service's own state and an event it must publish about that
state, the same fix takes a specific shape: the
[transactional outbox pattern](transactional-outbox.md) writes both in one
local transaction and lets CDC relay the event. A single ordered
[log](log-based-messaging.md) removes the race (everyone applies the same
order) and turns partial failure into mere lag: a derived system that
crashed resumes from its log position instead of diverging. This is the same
principle as [state machine replication](state-machine-replication.md)
applied across heterogeneous systems.
