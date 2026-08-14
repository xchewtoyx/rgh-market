---
type: concept
title: Large Test Ownership
description: >
  Every large test needs documented owners with ability and incentive to
  maintain it — project leads for in-project integration, feature owners for
  cross-service scenarios.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# Large Test Ownership

Unit tests inherit ownership from the module under test. **Large tests** span
multiple components — without explicit ownership they rot: contributors can't
safely change them, failures linger, and suites get skipped during large-scale
refactors.

Ownership models:

- **Project integration tests** — owned by the project lead.
- **Feature-spanning tests** — owned by a feature owner (end-to-end engineer,
  product manager, or test engineer with business-scenario responsibility).

Record ownership via code-location OWNERS files or per-test annotations when
multiple methods in one artifact have different owners — failures route to the
right contact automatically.

Pairs with [developer-owned test maintenance](developer-owned-test-maintenance.md)
and [build cop](build-cop.md). Nonhermetic or resource-heavy large tests often
run on separate postsubmit continuous builds outside TAP; presubmit is encouraged
when friction is acceptable.

See [large test SUT forms](large-test-sut-forms.md) for scope trade-offs.
