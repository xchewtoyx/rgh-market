---
type: concept
title: Summarization and Exception Reporting
description: >
  Condense dashboard content by reducing large sets of numbers to summaries
  and by showing detail only when something falls outside normal range —
  without going so far that the viewer loses all ongoing awareness.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 5 §5.1.1, ch. 5 §5.2.2.1"
---

A [dashboard](dashboard-definition.md) cannot show everything needed to fully
act on a problem — trying to would make it unreadable, more like a full
report than something monitorable at a glance. Two complementary condensing
techniques:

- **Summarization**: representing a large set of numbers as one number. Sums
  and averages are the most common dashboard summaries; distribution and
  correlation measures are rare, and usually need a purpose-built chart (see
  [box plot](box-plot.md), [scatter plot for correlation](scatter-plot-for-correlation.md))
  rather than a single summary statistic.
- **Exceptions**: since a dashboard exists to monitor what's going on, most
  of its content is only actionable when something is outside normal — "why
  make someone wade through hundreds of values when only one or two require
  attention?" This is the same logic behind
  [evaluative state banding](evaluative-state-banding.md) and
  [static/dynamic highlighting](static-vs-dynamic-highlighting.md).

Choosing the summarization level is itself a design decision, not a
mechanical step — transaction-level detail almost never belongs on a
dashboard; some level (per-quarter, per-region, per-month) must be chosen,
and picking the right one is the designer's job.

Exceptions should be used carefully, not maximized. Few explicitly warns
against reducing a dashboard to only a single alert indicator, drilling down
solely when something's wrong — this risks running things in "ignorant
bliss," entirely dependent on pre-built thresholds to know anything at all.
Anyone with a job to do needs a basic ongoing picture of what's going on, even
when everything is fine, not just a notification when it isn't. This is a
real tension with condensation, not a contradiction to resolve mechanically:
condense aggressively, but keep enough always-visible signal that the viewer
isn't flying blind between alerts.
