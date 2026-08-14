---
type: concept
title: Release Team Protects User Experience
description: >
  Release engineering's role includes blocking a ship when developer
  urgency would harm existing users, because frequent trains make missing
  one feature cheap.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Release Team Protects User Experience

At scale, a single release can embody months of work from hundreds of
contributors, making "ship without confidence" vs "abandon a quarter's
features" an increasingly painful binary. **Release latency** grows with
scale — even daily binary cuts can take a week or more to roll out safely,
putting debugging a week behind the change.

A stated release-team responsibility is to **protect the product from its
developers**: a developer's passion and urgency about shipping a feature
must not override existing user experience. With [release train deadline
discipline](release-train-deadline-discipline.md) and frequent trains,
almost no single feature matters enough to hold a release — the pain of a
feature missing a train is small next to the pain users feel from a
rushed, not-quite-ready feature, or the pain the whole release feels from
delay.

This requires isolating new work behind strong interface contracts,
[feature flags](feature-flag-blast-radius-isolation.md), rigorous testing,
and clear acceptance conventions — so "not this train" is a routine outcome,
not a political fight.
