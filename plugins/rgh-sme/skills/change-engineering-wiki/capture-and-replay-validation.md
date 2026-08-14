---
type: concept
title: Capture-and-Replay Validation
description: >
  Record real production traffic once, then replay it repeatedly against a
  candidate change to validate behavior offline, without needing a live
  mirror or touching production during the test.
sources:
  - title: "Observability Engineering, 2nd Edition"
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), Part I"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# Capture-and-Replay Validation

Capture a snapshot of real production traffic — requests, or the write
operations hitting a datastore — and save it, so a candidate change can be
validated by replaying that exact recorded traffic against it offline,
repeatedly, on demand.

This differs from [traffic teeing](traffic-teeing.md) in one important way:
teeing mirrors *live* traffic in real time to a parallel system, so each
test run needs its own window of real production activity, and a rare
condition might not recur during the test. A capture is recorded once and
can be replayed against any number of candidate changes, deterministically,
including conditions that were expensive or rare to encounter live —
making it well suited to validating a risky data or schema change (see
[schema migration production risk categories](schema-migration-production-risk-categories.md))
before it ever touches real data.

The trade-off is staleness: a capture reflects traffic patterns and data
shapes from the moment it was taken, and stops being representative as
production's real usage drifts away from what was recorded — a live tee
doesn't have this problem, at the cost of not being repeatable.

A related but distinct use of representative (rather than strictly
captured) data is a [self-serve staging load test](self-serve-staging-load-test.md),
built to validate performance under a realistic input mix rather than to
reproduce a specific recorded moment of production traffic.

For dependency servers rather than inbound request traffic, see [record
replay dependency isolation](record-replay-dependency-isolation.md) — record
mode on post-submit against live externals, replay mode hermetically on
presubmit.
