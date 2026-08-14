---
type: concept
title: Canary Metric Selection
description: >
  Choosing which signals decide whether a canary passes is a trade-off
  between false positives that discard good releases and false negatives
  that let bad ones through, and should reuse existing SLI instrumentation.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 16"
---

# Canary Metric Selection

The metrics a [canary](canary-release.md) is evaluated against decide what
it can and can't catch. Base metric choice on existing SLIs where
possible, reusing instrumentation already built for SLO measurement rather
than inventing canary-specific signals (the choice of *which* telemetry
signals are trustworthy indicators is `observability`'s territory; this is
about which of those signals belong in a release-go/no-go decision).

Acceptance-criteria tuning is a direct trade-off:

- Too strict → false positives, throwing away good releases.
- Too loose → false negatives, missing bad ones.

Practical guidance:

- Stack-rank candidate metrics and cap the set (roughly a dozen) — an
  unmaintained pile of canary metrics costs more upkeep than it returns
  and erodes trust in the whole canary process once it starts giving noisy
  verdicts.
- Prefer metrics with a strong, direct link to user impact: HTTP error
  codes and latency are strong signals for a frontend service. CPU and
  memory usage are usually weak signals — noisy, and don't map cleanly to
  user impact.
- Watch for metrics that need special handling: HTTP 404s conflate real
  regressions with unrelated causes (a bad link shared externally), so
  exclude them or add dedicated black-box URL monitoring rather than
  trusting the raw count.

See [canary measurement validity](canary-measurement-validity.md) for how
the canary/control comparison itself can be undermined even with
well-chosen metrics.
