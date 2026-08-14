---
type: concept
title: Continuous Fuzzing
description: >
  Running fuzzers automatically against every build, rather than as a one-off
  activity, so crashes and vulnerabilities surface within hours of the
  change that introduced them instead of being discovered later or not at all.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 13"
---

# Continuous Fuzzing

Fuzzing — feeding a program automatically generated or mutated inputs to
find inputs that crash it or trigger undefined behavior — finds a different
class of defect than either [automated acceptance testing](automated-acceptance-testing.md)
or a [nonfunctional test gate](nonfunctional-test-gate.md): it doesn't check
a known expected behavior, it searches for inputs the developer never
anticipated. Run once, a fuzzer only reflects what it found in that one
run. Run continuously — a pipeline stage that builds the fuzz targets from
every change and feeds them to a fuzzing service on an ongoing basis — the
same input corpus keeps mutating and expanding coverage over time, so a bug
introduced today can be caught within hours rather than sitting undetected
until an unrelated fuzzing pass eventually reaches that code path.

Making this practical at scale requires the fuzzing service itself to
manage: which crashing inputs have already been filed as bugs (crash
deduplication, based on program state at the time of the crash), periodic
retesting of previously filed crashes so a bug can be closed automatically
once a fix makes it stop reproducing, and code-coverage reporting so gaps in
the fuzz driver's input corpus are visible and can be targeted. This turns
fuzzing from a point-in-time security audit activity into an ongoing
[commit-stage](commit-stage.md)-adjacent feedback loop feeding the same
issue tracker regular bug reports come from.
