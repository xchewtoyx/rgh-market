---
type: concept
title: Error Event Schema
description: >
  A centralized dimensional schema recording every error a pipeline's
  quality screens throw, at two grains, so error volume can be measured and
  traced over time.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

Rather than logging [quality screen](quality-screens.md) failures wherever is
convenient at the point they occur, centralize them in a dedicated
dimensional schema built for exactly this purpose — it applies equally to
generic system-to-system data integration, not just warehouse pipelines. Two
tables, at two grains:

- **Error event fact table** — one row per error thrown by any screen,
  anywhere in the pipeline. Dimensioned by calendar date (so errors can be
  sliced by weekday or fiscal period), the batch job or processing step that
  was running, and the screen that fired (identifying the specific criterion,
  its code location, and which response it took: halt, suspense, or tag).
  Also carries a precise error timestamp as a fact, for interval math, and a
  surrogate error-event key, needed because a single error burst can insert
  many rows in the same instant.
- **Error event detail fact table** — one row per individual field within a
  record that participated in an error, at a lower grain than the event
  table and tied back to it via the error-event key. A single structural or
  business-rule error touching several fields at once fans out into several
  detail rows from one parent event.

Every quality screen is responsible for populating both tables at the moment
it fires, which is what makes the schema a genuine audit trail rather than a
best-effort log: querying it answers "how many errors of this type fired last
month, and on which fields" without reconstructing the answer from scattered
job logs.
