---
type: concept
title: The Core Analysis Loop
description: A repeatable, four-step investigative loop — start from the trigger, verify the signal is real, search for dimensions disproportionately present in the anomalous region versus baseline, and narrow or stop — that only works on data with enough dimensionality and cardinality to search, which metrics and raw logs generally lack.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 8"
---

A repeatable loop for investigating an anomaly from telemetry, independent of prior familiarity with the system:

1. Start from whatever triggered the investigation (customer report, anomaly, alert).
2. Verify the signal is real — is there a genuine change in behavior visible somewhere (a curve shift in a visualization), or is this noise/a red herring?
3. Within the anomalous region, search for dimensions that are disproportionately present versus the baseline: inspect sample rows for outlier columns, try experimental `GROUP BY`s on likely fields, filter to isolate candidates. See [high-cardinality querying for outlier isolation](high-cardinality-outlier-isolation.md) for the concrete technique this step relies on.
4. If you now understand enough, stop; if not, narrow the filtered view and return to step 3.

This loop is explicitly brute-force-capable: cycling through every dimension comparing anomaly against baseline is impractical by hand at real scale, but is exactly the kind of thing that can be automated — diff every dimension's value distribution inside vs. outside the anomaly and rank by how strongly it differs.

Crucially, this loop is only possible on data with enough [cardinality](cardinality.md) and [dimensionality](dimensionality.md) to search freely: [metrics](metric-anatomy.md) lack the dimensionality to support step 3 at all, and raw logs require costly ID-stitching and reconstruction to approximate it — [arbitrarily wide structured events](structured-events-as-observability-substrate.md) are what make the loop practical. It's the concrete investigative technique underlying [debugging from first principles](debugging-from-first-principles-vs-tacit-knowledge.md), and it directly answers the "why" that a [symptom-based alert](symptom-based-vs-cause-based-alerting.md) or [helpful alert](helpful-alert-criteria.md) deliberately leaves open.
