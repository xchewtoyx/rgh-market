---
type: concept
title: Known Failure Suppression in CI
description: >
  Tag failing tests with tracked bugs and suppress their failures to keep
  the suite green while retaining visibility into outstanding issues.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Known Failure Suppression in CI

Large integration suites integrating many teams or products are often
**nearly always broken**: failures can't all be fixed immediately — some
are outside the owning team's control, low priority, or test-code bugs.
Commenting out failing tests risks forgetting them; leaving them red erodes
trust in the suite and blocks [build cop rollback
discipline](build-cop-rollback-discipline.md).

**Bug-tag suppression:** associate a failing test with a filed bug; the
framework suppresses the failure while still recording that everything
*besides known issues* passes. Automate hygiene — when the bug closes, or
when a tagged test passes for longer than a configured limit, prompt cleanup
(and mark the bug fixed if needed). Tests tagged **flaky** may exempt from
pass-based cleanup prompts.

This keeps CI actionable: red means *new* breakage, not an accumulated
backlog. Track maintenance efficiency with **mean time to clean up (MTTCU)**
— time from fix submitted to tag removed — as a delivery-health metric
alongside [change failure rate](change-failure-rate.md).

For failures during upstream [version skew during
rollout](version-skew-during-rollout.md), pair suppression with
[feature-flag-aware integration tests](feature-flag-aware-integration-tests.md)
so tests expect different outputs when a plug-in feature is enabled in dev
but not prod.
