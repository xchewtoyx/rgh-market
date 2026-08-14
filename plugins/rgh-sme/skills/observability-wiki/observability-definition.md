---
type: concept
title: Observability Definition
description: Observability, borrowed from control theory, is the degree to which a system's internal state can be inferred purely from its external outputs — in software this is operationalized as the ability to understand or debug any given system state without shipping new code.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 1"
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 3"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 15"
---

The term originates with Rudolf Kálmán (1960, control theory): observability is whether a system's internal state can be inferred purely from its external outputs. (Its dual, controllability, has no real software equivalent and isn't part of the software usage.) A simpler, equivalent framing used elsewhere: observability is the property of being able to determine what your system is doing by examining its outputs.

In software, this is treated as a **property of software dependability**, not a category of tooling — proposed as a 7th attribute alongside Jean-Claude Laprie's dependability framework (availability, reliability, maintainability, safety, confidentiality, integrity), defined operationally as *"the ability to understand or debug any given system state."*

**Six functional requirements**, derived by working backward from the control-theory definition, describe what a genuinely observable system needs: (1) high-dimensionality wide events, ideally hundreds of attributes; (2) high-cardinality data preserved, not discarded; (3) raw events stored, aggregated at read time with flexible schemas; (4) the ability to zoom continuously between an individual request and a whole-system view, visualized as a trace; (5) an exploratory, open-ended query interface instead of only static dashboards; (6) sub-second-to-seconds query latency. See [cardinality](cardinality.md) and [dimensionality](dimensionality.md) for (1)–(2), [pre-aggregation is irreversible](pre-aggregation-is-irreversible.md) for (3), and [structured events as the observability substrate](structured-events-as-observability-substrate.md) for how (4) is achieved in practice.

A **qualitative test** for how observable a system actually is: can you understand any novel system state without shipping new code; compare arbitrary attribute combinations with no cardinality limits; trace by transaction/session to see real usage; select the exact events violating an SLO and see the pattern instantly; find any kind of outlier, easily?

The most common failure mode in the market is treating "observability" as a rebrand of conventional monitoring/APM tooling rather than engaging with what it actually requires — traditional tooling is good at [known-unknowns](known-unknowns-vs-unknown-unknowns.md) (you know the failure mode, just not whether it's occurring right now); real observability is what's needed for unknown-unknowns, novel failure modes nobody wrote a check for in advance.
