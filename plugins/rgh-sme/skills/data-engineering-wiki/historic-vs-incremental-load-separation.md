---
type: concept
title: Historic vs. Incremental Load as Separate Processes
description: >
  Why a one-time historic backfill and the ongoing incremental load usually
  need separate implementations even though they apply the same
  transformation rules, and what each can afford that the other can't.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 20"
---

Standing up a pipeline against an existing, populated source involves two
distinct loading processes that apply the same business-rule transformations
but differ sharply in their operating constraints, and are usually built as
separate code paths rather than one:

- **Historic (backfill) load**: a one-time pass loading all pre-existing
  source history. Its defining characteristic is volume — potentially
  thousands of times a single incremental cycle's size — offset by the
  luxury of loading into a non-production table, so a multi-day runtime is
  often tolerable, and a human can pause it mid-run to manually resolve a
  data problem (a missing dimension member, an unexpected referential
  integrity gap) before continuing.
- **Incremental load**: the ongoing, recurring load applying only what's
  changed since the last cycle. It must be fully automated end to end — there
  is no equivalent of pausing a nightly job to have someone manually patch a
  bad row, since the next cycle is already queued up behind it.

The two share transformation logic and often share code for genuinely common
steps, but the automation and volume constraints diverge enough that
treating them as one undifferentiated "load" process tends to produce a
pipeline optimized for neither: over-engineered for the rare historic
backfill, or too fragile for the unattended incremental cadence it has to
run under every day. This is a specific case of the more general
[incremental vs. full extraction](incremental-vs-full-extraction.md)
trade-off, but at the load side rather than the extract side — a pipeline
typically needs both a working full-history load path and a working
incremental path, not a choice between them.
