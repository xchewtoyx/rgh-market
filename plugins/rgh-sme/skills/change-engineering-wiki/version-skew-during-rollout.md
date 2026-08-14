---
type: concept
title: Version Skew During Rollout
description: >
  Progressive delivery leaves a distributed system running incompatible
  code, data, and configuration versions simultaneously until rollout
  completes.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Version Skew During Rollout

**Version skew** is a state where a distributed system simultaneously
contains multiple incompatible versions of code, data, and/or configuration.

[Canary release](canary-release.md) and any partial rollout introduce
skew by design: some production instances run the new version while others
run the old one, and dependencies may lag either side. Skew is caught
during release-candidate promotion when configuration and code are assembled
and tested together — a large fraction of production bugs stem from
configuration mismatches, which is why static configuration should be
promoted as part of the same [release candidate](build-once-promote-artifact.md)
as its corresponding code.

Safe rollout requires [backward and forward compatibility during
rollout](backward-and-forward-compatibility-during-rollout.md) for any
shared data or wire formats touched by the change, because old and new
instances read each other's output for the whole deploy window.

Experiments and [feature flags](feature-flag-blast-radius-isolation.md)
reduce deployment risk by isolating behavioral change within toggled
modules — a common strategy when continuously pushing entire large
binaries to production is infeasible but continuous feedback from
production is still desired.
