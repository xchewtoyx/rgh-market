---
type: concept
title: Safe Configuration Change Properties
description: >
  Configuration changes carry the same production risk as code changes and
  need the same three safety properties: gradual deployability, rollback
  capability, and automatic rollback when operator control is lost.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 14"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Safe Configuration Change Properties

Configuration is a fast, low-overhead lever for changing system behavior
without a full code rebuild — which is exactly why it's dangerous: config
changes are often made without the review or testing rigor applied to code,
sometimes under incident-response pressure, and can have outsized,
immediate blast radius (a single bad firewall rule can lock operators out
of the system they need to fix it). A config change should be treated as a
release and given the same safety properties as one:

Static configuration at organizations like Google lives in version control
with code, passes the same review, and is promoted as part of the [release
candidate](build-once-promote-artifact.md) so it is tested alongside the
code it configures — not applied ad hoc per environment after the binary
ships.

1. **Gradual deployability** — avoid all-or-nothing global pushes; roll
   out incrementally (the config equivalent of [rolling deployment](rolling-deployment.md)
   or [canary release](canary-release.md)) so a bad value is caught before
   it reaches 100% of the blast radius.
2. **Rollback capability** — rolling back to the last known-good
   configuration is faster and higher-confidence than attempting a live
   patch; see [roll back vs. roll forward](rollback-vs-roll-forward.md) for
   why rollback is the safer default response.
3. **Automatic rollback / stop-progress on loss of operator control** — a
   config change that locks operators out of the system it controls (the
   firewall-rule scenario) is a worst-case failure mode that needs a
   specific guard: if the system can detect it has lost reachability to its
   own operators, it should revert itself rather than wait for a human who
   may no longer be able to reach it.

A prerequisite for properties 2 and 3 is that configuration evaluation be
**hermetic** — it must not depend on external, independently-mutable state
(e.g. a live value read from a network filesystem at evaluation time). If
config isn't hermetic, replaying an old version doesn't actually reproduce
the old behavior, which breaks reliable rollback and roll-forward alike.
