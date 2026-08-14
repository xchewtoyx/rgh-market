---
type: concept
title: Failing Test Bug Tagging
description: >
  Suppressing known failing tests by linking each failure to a tracked bug so
  the suite stays green while failures remain visible and stale tags auto-expire.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Failing Test Bug Tagging

Large integration suites at scale are rarely all green at once — failures may
live in dependent teams' code, low-priority product bugs, or flaky tests.
Commenting out failures loses visibility; leaving them red blocks everyone.

**Bug tagging** associates a failing test with a tracked bug; the framework
suppresses the failure while still recording that the test is known-broken.
Automated cleanup checks whether the bug is closed; if a tagged test passes
for longer than a configured window, prompt cleanup (and mark the bug fixed if
not already). Tests tagged **flaky** skip auto-cleanup on pass — flakes need
separate quarantine policy per [CI as alerting](ci-as-alerting.md).

For rollouts where behavior differs by environment (feature enabled in dev
months before prod), tests can query feature status and assert expected output
for each state rather than manual per-environment disabling.

Related metric: **mean time to clean up (MTTCU)** — time from fix submitted to
bug tag removed. Automating bug filing and tagging reduces Build Cop toil; see
[build cop](build-cop.md).

This implements the pragmatic side of [CI as alerting](ci-as-alerting.md) —
not every red test warrants blocking all commits.
