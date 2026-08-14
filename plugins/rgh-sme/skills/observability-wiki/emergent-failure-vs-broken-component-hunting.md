---
type: concept
title: Emergent Failure vs. Broken-Component Hunting
description: In complex distributed systems, an outage is often an emergent property of many components behaving normally and interacting unexpectedly, not the traceable effect of one broken part — so debugging that only searches for "the" root cause can fail even when every individual finding is correct.
sources:
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Sidney Dekker), ch. 3, 4, 6"
---

Classic fault-tracing assumes a system's behavior decomposes cleanly into its components' behavior: if the system failed, some component must have failed, and finding that component explains the failure. This works for genuinely simple systems, but complex sociotechnical and distributed systems routinely produce **system accidents** — outages that emerge from the interaction of components that each performed exactly as designed, with no single part ever leaving spec. Investigators who only know how to search "down and in" (decompose the system, find the broken piece) will, in these cases, either force-fit a real-but-non-explanatory finding into the role of "root cause," or spend disproportionate effort chasing a broken part that never existed — a version of a [eureka part search](change-correlation-in-debugging.md) that comes up empty because there was nothing broken to find.

Two practical symptoms of this trap in production debugging:

- **A component list of "OK" and "not OK" items doesn't add up to an explanation.** A postmortem that catalogs every subsystem as broken/not-broken (à la a checklist) leaves the reader to supply, unaided, the causal story connecting them — that connection only exists if the system really is a simple sum of its parts. When it isn't, the checklist is a description of what was true, not of why the failure happened.
- **The absence of a broken part is not evidence the investigation failed.** Long, expensive investigations sometimes never find a "eureka" cause because none exists — the failure was a joint product of many normally-functioning components crossing paths in a way nobody anticipated, which is exactly the case an [unknown-unknown](known-unknowns-vs-unknown-unknowns.md) is: there is no pre-existing broken-component signature to discover, only a novel combination to characterize after the fact.

The corrective move is to trace relationships and interactions ("up and out") rather than only decomposing components ("down and in") — asking how normally-behaving parts combined, not only which part deviated from spec. This is the deeper justification for [the core analysis loop](core-analysis-loop.md)'s dimension-by-dimension search for what's disproportionately present in the anomalous population, rather than a search for a single faulty component: in a system where failure is emergent, the "cause" is a combination of conditions across dimensions, not a component to be located. It also reinforces why [correlation is not causation](correlation-vs-causation-in-debugging.md) in this setting: a correlated component may be functioning correctly and still be part of the story, while a single "broken" component, once found, may still not explain the outage on its own.
