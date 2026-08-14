---
type: concept
title: Normalization of Deviance
description: >
  Normalization of deviance is the organizational phenomenon where engineers become accustomed to persistent anomalies or minor failures, treating them as normal behavior rather than signals of system degradation.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 15"
---

**Normalization of deviance** occurs when a team repeatedly tolerates minor deviations from standard, healthy operating procedures or system states. Over time, these anomalies are accepted as the new baseline, creating dangerous blind spots that mask critical failures.

### Drivers of Normalized Deviance

In reliability engineering, deviance is commonly normalized due to:
1. **Operational Overload and Alert Fatigue**: A high volume of non-actionable warnings or noise causes engineers to tune out warnings. This is mitigated by establishing a strict [actionable alert philosophy](actionable-alert-philosophy.md) and managing [pager fatigue](sustainable-on-call-and-burnout.md).
2. **Untracked Tech Debt**: When a work-around or a minor bug remains in the system for years, it is eventually assumed to be expected behavior. New team members may spend hours debugging what is actually normalized system behavior, degrading overall [system understandability](system-understandability.md).
3. **Miscalibrated Baselines**: Without analyzing historical logs to establish a healthy baseline, teams may assume a high background level of errors or restarts is normal (e.g., assuming a high rate of container out-of-memory events is typical for a cluster rather than addressing the memory leak).

### Mitigating Normalized Deviance

Teams can actively counter normalized deviance through:
* **Fresh Perspectives**: Rotating engineers in and out of on-call shifts, and actively soliciting feedback from new team members who have not yet normalized the system's quirks.
* **Blameless System Reviews**: Conducting regular reliability reviews to audit persistent anomalies.
* **Historical Baseline Calibration**: Analyzing logs and telemetry during stable periods to differentiate normal system noise from true operational degradation.
