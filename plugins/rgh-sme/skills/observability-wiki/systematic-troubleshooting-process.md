---
type: concept
title: Systematic Troubleshooting Process
description: Effective troubleshooting follows a repeatable sequence — demonstrate, mitigate, characterize, test, and fix — while actively avoiding common diagnostic anti-methodologies like streetlight searches or random changes.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 12"
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 2"
---

A systematic troubleshooting process follows five main operational stages:

1. **Problem demonstration** — Replicate or verify the failure state using metrics, logs, or reproduction tests, verifying that the issue is real and measurable.
2. **Mitigation before root-causing** — Stop user pain immediately by draining traffic, rolling back changes, or increasing capacity before attempting to diagnose the deep cause. See [mitigate before root-causing](mitigate-before-root-causing.md).
3. **Workload Characterization** — Characterize the current system load across five dimensions to define the problem space:
   * *Who*: Client identity, user account, API key, or process owner.
   * *Why*: The purpose or type of operation (e.g., read, write, complex search).
   * *What*: Request payload size, query parameters, or transaction complexity.
   * *When*: Arrival pattern, burstiness, concurrency level, and timing.
   * *How*: Communication protocol, transport security, and connection pool behavior.
4. **Hypothesis generation and testing** — Formulate testable hypotheses based on system topology and recent changes, then systematically isolate variables (via binary search, log analysis, or tracing) to validate or invalidate them. See [change correlation in debugging](change-correlation-in-debugging.md), [binary search isolation](binary-search-isolation.md), and [testing hypotheses with real data](hypothesis-testing-with-real-data.md).
5. **Fix** — Apply a permanent code, configuration, or architectural fix, followed by a postmortem review to prevent recurrence.

## Diagnostic Tools and Profiling

During hypothesis testing, two complementary profiling techniques help isolate bottlenecks:

* **CPU Profile Analysis**: Sampling thread stack traces at a fixed frequency (e.g., 99 Hz) to identify which functions and execution paths are consuming CPU time. Synthesized via [CPU Flame Graphs](cpu-flame-graphs.md).
* **Off-CPU Analysis**: Measuring the time threads spend blocked *off* the CPU waiting for external events (e.g., lock acquisition, disk I/O, network socket responses, or page faults). Off-CPU time is computed as:
  $$\text{Off-CPU Time} = \text{Total Elapsed Time} - \text{On-CPU Time}$$

## Debugging Anti-Methodologies to Avoid

Responders under pressure often fall into cognitive traps that prolong outages. A systematic process must actively guard against these anti-methodologies:

* **The Streetlight Anti-Methodology**: Searching for performance issues or bugs only in areas where metrics are convenient, familiar, or easy to read, regardless of whether they correlate with the problem.
* **The Random Change Anti-Methodology**: Modifying configuration parameters, kernel settings, or code paths at random in the hope that performance improves. This introduces secondary bugs and destroys baseline comparisons.
* **The Blame Someone Else Anti-Methodology**: Attributing the failure to an external dependency, network provider, or database tier without empirical, quantitative telemetry verifying the claim.
* **Ad Hoc Checklist Tuning**: Blindly applying a static checklist of tuning recommendations without first verifying if the target system actually exhibits the specific bottleneck addressed by the check.
