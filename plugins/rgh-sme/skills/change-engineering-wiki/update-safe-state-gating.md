---
type: concept
title: Update Safe-State Gating
description: >
  An embedded or mobile system should only apply an update while it is in
  an operational state where an update-induced glitch or restart cannot
  cause physical harm, not merely when connectivity allows it.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 18"
---

# Update Safe-State Gating

For software controlling a physical system (a vehicle, an aircraft, an
industrial controller), the question "can we push this update now?" is not
just about connectivity or a maintenance window — it is about whether the
device is currently in a state where an update-induced glitch, restart, or
transient loss of control authority is survivable. The canonical example:
never update engine control software while the vehicle is driving, even if
a network connection is available and the fleet-wide rollout is otherwise
ready to proceed. The system must be **update-safety-state-aware**:
capable of identifying which of its own operational states are safe to
interrupt, and refusing (or queuing) an update outside those states.

This is a per-device, physical-state gate, distinct from
[change freeze triggers](change-freeze-triggers.md), which halt releases
fleet-wide based on an incident or error-budget signal — safe-state gating
instead asks, for one specific device, "is *this instance*, right now, in
a condition where it's acceptable to disrupt it," independent of what the
rest of the fleet is doing.

It compounds with two other constraints specific to this class of system:
many consumer-device update mechanisms are one-way and not
rollback-capable once applied, which pushes mutable state toward the cloud
rather than the device itself (data that must survive a bad update is
safer kept where [rollback](rollback-vs-roll-forward.md) is still
possible); and [partial system deployment](independent-deployability.md) —
updating only the changed subsystem rather than the whole application —
matters even more here, since minimizing what's touched during a
necessarily narrow safe-state window reduces both the update's duration
and its blast radius.
