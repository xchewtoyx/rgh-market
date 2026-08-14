---
type: concept
title: Contract Tests for Fakes
description: >
  A shared test suite run against both the real implementation and a fake
  keeps the fake's behavior aligned with the API contract as the real code
  evolves.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 13"
---

A [fake](fake-objects.md) must track the real implementation's evolving
behavior. Without verification, fake behavior can silently drift, producing
passing tests that wouldn't hold in production.

**Contract tests**: a shared test suite written against the API's public
interface, executed against both the real implementation and the fake. The
real-implementation run is slower; typically only the fake's owning team needs
to run it regularly.

**Fake fidelity**: preserve the API contract (same outputs/state changes for
given inputs from the test's perspective), not every physical property (an
in-memory database needn't replicate disk behavior). Where the contract doesn't
guarantee exact values (hash output), the fake needn't replicate them. Latency
and resource consumption fidelity is usually unnecessary — but then those
constraints can't be tested with the fake alone.

A fake may implement only the subset of the API your tests need; fail fast on
unsupported paths rather than silently returning wrong results.

**Ownership**: the team owning the real implementation should write and maintain
the fake when usage justifies the investment (handful of users may not;
hundreds usually do). Fake at the root of the untestable dependency (the
database API, not every caller).

If no fake exists, ask the API owner first; otherwise wrap the API in your own
class and fake the wrapper — often simpler since you need only a subset.

See [prefer real implementations in tests](prefer-real-implementations-in-tests.md)
and [test doubles overview](test-doubles-overview.md).
