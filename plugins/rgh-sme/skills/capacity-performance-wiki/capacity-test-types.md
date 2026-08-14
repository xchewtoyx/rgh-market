---
type: concept
title: Capacity Test Types
description: The taxonomy of load-based tests — baseline, load, stress, soak, and spike — each designed to answer a different question about a system's capacity limits.
sources:
  - title: "Continuous Delivery"
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Jez Humble, David Farley), ch. 9"
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 17"
---

Capacity testing is not one test but a family of tests, each applying load differently to answer a different question. Picking the wrong type for the question at hand produces a result that looks like an answer but isn't.

## The Taxonomy

*   **Performance Baseline Testing:** Measures latency and resource consumption under normal, expected operational load. Establishes the reference numbers that every other test type is compared against — without a baseline, "did this get worse?" has no answer.
*   **Load Testing:** Drives the system at its maximum *expected* peak load and verifies throughput and response-time targets are met. Answers "does the system meet its SLA at the load we actually expect?"
*   **Stress Testing:** Pushes load beyond maximum expected capacity, deliberately past the point of failure, to find the breaking point, observe failure modes, and verify the system recovers cleanly once load subsides. Answers "what happens when we exceed capacity, and how does it fail?" **Breakpoint testing** is the specific goal within a stress test of locating the *exact* load threshold — the precise point where latency explodes or a resource (e.g. memory) is exhausted — rather than merely confirming that failure happens somewhere beyond expected capacity; it turns the stress test's qualitative "it breaks eventually" into a quantitative number that can feed directly into capacity headroom calculations.
*   **Endurance / Soak Testing:** Sustains load — not necessarily peak load — over an extended period (24-72 hours or longer) to surface failure modes that only manifest over time: slow memory leaks, thread pool exhaustion, database connection leakage, or log/disk space saturation. Answers "does the system stay healthy under sustained operation, not just in a short burst?" A sustained write rate outpacing background compaction is one concrete example — see [LSM-tree write amplification](lsm-tree-write-amplification.md).
*   **Spike Testing:** Applies a sudden, large jump in traffic to evaluate system stability and scaling response to abrupt demand changes, as opposed to load or stress testing's gradual or sustained ramps. Answers "can the system absorb a sudden surge without falling over?"

## Choosing a Test Type

The distinction that matters most operationally is between tests that stay within expected bounds (baseline, load) and tests that deliberately go beyond them (stress, soak, spike):

*   Load testing validates the system against *known* capacity requirements — it should pass cleanly before a release.
*   Stress, soak, and spike testing are exploratory: they exist to find the resource that becomes the bottleneck first, and to observe failure and recovery behavior under conditions the system wasn't explicitly sized for.

Whichever type is run, the results are only as trustworthy as the test harness generating the load and the representativeness of the environment it runs against — see [load generator bottlenecks](load-generator-bottlenecks.md) and [scaled capacity test environments](scaled-capacity-test-environment.md), and beware the measurement pitfalls in [benchmarking pitfalls](benchmarking-pitfalls.md), which apply to every type in this taxonomy.

All of the above uses synthetic load. Once synthetic testing has validated a system pre-launch, [live-traffic capacity validation](live-traffic-capacity-validation.md) — dark launches and staged rollouts — confirms those conclusions hold against genuine production traffic before it reaches full exposure.

How accessible any of these test types are to the engineers actually making a performance-sensitive change also matters: see [self-serve load-test tooling](self-serve-load-test-tooling.md) for why routing every test run through a separate team turns capacity validation into an escalation rather than a routine step.
