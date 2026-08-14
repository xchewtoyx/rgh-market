---
type: concept
title: Measuring Many Things by Measuring Only a Few
description: >
  A well-chosen, small set of SLIs can implicitly validate many underlying
  concerns at once, because one check tends to subsume several others.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 3, ch. 12"
---

For a simple request/response API, a practitioner might in principle want to
know: is the service up? is it available? is it responsive? is it returning
an acceptable ratio of good:bad responses? is the response correctly
formatted? is the correct data being returned? Instrumenting the last
question — "is the correct data being returned" — tends to subsume most of
the others: if a service produced correct, correctly-formatted, timely data,
it was necessarily up, available, and responsive enough to produce it.

Concrete example: a successful product search on an e-commerce site
implicitly validates the catalog database, the cache, the inventory service,
and the network all at once — a single well-chosen SLI stands in for the
health of several components without needing to instrument each one
separately.

This is why a small number of well-chosen SLIs (see
[SLO count and scope](slo-count-and-scope.md)) usually outperforms a large
number of narrow ones: the goal isn't exhaustive coverage of every internal
signal, it's finding the few signals whose health implies the rest.

This principle underlies [end-to-end vs per-component SLI measurement](end-to-end-vs-per-component-sli-measurement.md):
often the practical compromise of measuring each component well, rather than
capturing the full user journey end to end, is "more than good enough"
precisely because of this subsumption effect.
