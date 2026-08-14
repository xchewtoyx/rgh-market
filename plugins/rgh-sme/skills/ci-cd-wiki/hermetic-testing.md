---
type: concept
title: Hermetic Testing
description: >
  Tests run against a self-contained environment with no live production
  backends, improving determinism and presubmit stability at the cost of setup
  and fidelity trade-offs.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 13"
---

# Hermetic Testing

**Hermetic tests** run against an environment (application servers and
resources) that is entirely self-contained — no external dependencies such as
production backends. This is distinct from [hermetic builds](hermetic-builds.md),
which pins build inputs; hermetic **testing** pins the runtime under test.

Hermeticity applies at every [test size](test-size-constraints.md): a test
should contain all information needed to set up, execute, and tear down its
environment without assuming execution order, shared databases, or other
ambient state. Harder to achieve as tests grow larger, but still worth
pursuing — see [tests obvious upon inspection](test-obvious-upon-inspection.md).

Two properties:

- **Greater determinism** — inputs don't change because an upstream service
  changed; rerunning the same code should reproduce results. Failures point to
  application or test changes, not ambient environment drift.
- **Isolation** — production incidents don't break hermetic tests; hermetic
  runs don't affect production. Tests don't depend on who runs them or network
  path to shared staging.

Hermetic backends may be **fakes** (cheap, limited fidelity) or a **full stack
started sandboxed** (higher cost; feasible for smaller systems). At larger
scale, **record/replay** caches live backend responses and replays them in a
hermetic environment — cheaper than full stack startup but brittle when
cache invalidation is wrong (false positives from over-caching, false negatives
from under-caching).

Hermetic testing is especially valuable on **presubmit**, where instability
blocks every developer — see [presubmit vs. postsubmit testing](presubmit-vs-postsubmit-testing.md).
Nonhermetic end-to-end tests often move to postsubmit; teams need failure
management (hotlists, temporary disablement) so releases aren't permanently
blocked. Google Assistant's move to hermetic presubmit cut runtime ~14× and
eliminated routine bypass of test results.

For distributed systems, **hotswapping** — routing a request to a head-version
backend while other services stay at production versions — supports O(N)
postsubmit isolation instead of O(N²) full environment matrices.

Pair with [independent testability](independent-testability.md) and
[ephemeral test environments](ephemeral-test-environments.md) when hermetic
fakes aren't enough fidelity for late pipeline stages.
