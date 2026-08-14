---
type: concept
title: Hitless In-Service Software Upgrade (ISSU)
description: >
  Patch a running process's code or data in place — without stopping,
  restarting, or replacing it — for deployments where even a rolling
  restart's brief per-instance gap is unacceptable.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 4"
---

# Hitless In-Service Software Upgrade (ISSU)

Hitless ISSU updates a live process's running code without stopping it,
rather than replacing the process itself. This is a different mechanism
from [rolling deployment](rolling-deployment.md) or
[blue-green deployment](blue-green-deployment.md): those achieve
zero-downtime by shifting traffic away from an instance before it is
touched, so the instance itself can be crudely replaced. ISSU instead
leaves the process serving traffic throughout and mutates it in place —
used where even a rolling deployment's momentary per-instance gap (drain,
restart, reintroduce) is unacceptable, historically telecom and networking
gear that must not drop an active session.

Two patching mechanisms:

- **Function patch** (procedural code): an incremental linker/loader
  stores the updated function body in pre-allocated memory and rewires the
  old function's entry/exit points to it. Used for narrow bug fixes.
- **Class patch** (object-oriented code): a backdoor mechanism adds member
  data or functions to a live object at runtime. Also used for fixes
  rather than large-scale change.

Because these mechanisms only reach small, targeted edits, hitless ISSU is
suited to patching a fielded defect, not a substitute for redeploying an
architecturally different version — the general-purpose replace-the-whole-instance
strategies ([rolling](rolling-deployment.md), [blue-green](blue-green-deployment.md),
[canary release](canary-release.md)) remain the default for feature-level
changes precisely because they don't require this kind of invasive,
upgrade-specific tooling.

A related reintroduction tactic worth reusing outside the ISSU context:
after a component is patched or repaired, run it in **shadow mode** —
receiving real traffic and being monitored for correct behavior, with its
state repopulated incrementally — before promoting it back to fully active
duty, rather than trusting the patch and cutting back over immediately.
