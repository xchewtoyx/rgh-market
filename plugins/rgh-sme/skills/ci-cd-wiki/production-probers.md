---
type: concept
title: Production Probers
description: >
  Automated functional checks running continuously against production with
  deterministic read-only actions, acting as live smoke tests and canary inputs.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Production Probers

**Probers** are functional tests with encoded assertions against **production** —
typically well-known, deterministic, **read-only** actions (e.g. issue a query
and verify a non-empty response without asserting exact content). They provide
early detection of major outages and validate that tests still reflect reality.

During [canary release](canary-release.md), **canary analysis** runs prober
assertions against the canary cohort and compares health metrics to baseline.

Limitations: issues caught here already affect users; **mutable (write) probers**
risk nondeterminism, assertion failure on later reads, or user-visible side
effects — avoid unless carefully designed.

The same suite run against production and against CI supports
[production vs. CI test comparison](production-vs-ci-test-comparison.md).
Probers belong in the [defense in depth](swiss-cheese-testing-model.md) layer
after presubmit and RC testing — not a substitute for earlier gates per
[canary release](canary-release.md)'s "failing canary is a process failure" framing.
