---
type: concept
title: Build Cop Rollback Discipline
description: >
  A designated owner keeps CI green by rolling back breaking changes
  quickly rather than fixing forward on top of a broken mainline.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Build Cop Rollback Discipline

When continuous integration allows changes to land before every slow test
finishes — trading exhaustive presubmit for throughput — someone must
own recovery when post-submit tests fail. Each team typically assigns a
**Build Cop** responsible for keeping all tests passing in their project
regardless of who broke them: drop current work, identify the offending
change, and **roll back** (preferred) or fix forward (riskier).

Rollback is the fastest route to a known-good state; failing tests erode
confidence in the whole suite if they linger. At scale, CI may **automatically
roll back** when it has high confidence in the culprit. The pairing matters:
"Tests give us confidence to change; rollbacks give us confidence to undo.
Without tests, rollbacks can't be done safely. Without rollbacks, broken
tests can't be fixed quickly, thereby reducing confidence in the system."

See [roll back vs. roll forward](rollback-vs-roll-forward.md) for why
rollback is the default mitigation during delivery, and [CI culprit
finding](ci-culprit-finding.md) for locating the change in batched runs.
