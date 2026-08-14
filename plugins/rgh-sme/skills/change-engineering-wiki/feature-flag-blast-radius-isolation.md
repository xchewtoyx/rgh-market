---
type: concept
title: Feature Flag Blast Radius Isolation
description: >
  Gating individual features behind their own flags lets a broken feature
  be disabled in isolation, without forcing a rollback of the whole release
  it shipped in.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 8"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Feature Flag Blast Radius Isolation

Reliable continuous releases require **flag-guarding** every in-flight
change: flags control whether feature code runs, can differ between
development and release builds, and should let build tooling strip disabled
features entirely where the language permits. New code lives alongside the
old path behind a flag; once validated, the old path is removed in a later
release. Flag values can be updated independently of a binary release via
dynamic configuration — but configuration changes themselves need safe
rollout (flipping a flag to 100% at once is risky), so a configuration
service that manages staged flag ramping is worth investing in.

Flag-guarding also enables press-release timing: the binary can ship early
while the flag stays off until announcement, minimizing leak risk — though
it is not a perfect safety net for sensitive features (code can still be
analyzed if not obfuscated, and not every feature can hide behind a flag
without excessive complexity).

When a release bundles several features behind independent feature flags,
a single broken feature can be disabled by flipping its flag off, without
[rolling back](rollback-vs-roll-forward.md) the entire release and losing
every other feature that shipped alongside it. This decouples the
granularity of mitigation from the granularity of deployment: the release
is the unit of *what got deployed*, the flag is the unit of *what's turned
on*, and they don't have to match.

This makes feature flags a finer-grained blast-radius control than
rollback — the cost of disabling a single flag is much lower than the cost
of reverting a whole deployment, and it can usually be done faster too
(a config change vs. a redeploy).

Feature flags used this way are a mitigation tool at the moment something
goes wrong; the same mechanism, used to progressively enable a flag for a
growing population before turning it on for everyone, is
[canary release](canary-release.md) applied at the feature level instead of
the binary/deployment level. Flag lifecycle management (naming, cleanup,
avoiding stale flags) is out of scope here.
