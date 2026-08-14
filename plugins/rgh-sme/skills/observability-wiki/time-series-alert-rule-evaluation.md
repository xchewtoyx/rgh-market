---
type: concept
title: Time-Series Alert Rule Evaluation and SLO Alerting
description: Time-series alerting rules evaluate mathematical expressions over metric streams at regular intervals; for service reliability, alerting should be based on the consumption rate of the service's error budget (burn rate) using multiwindow multi-burn-rate checks to balance precision, recall, and reset time.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 10"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 5"
  - title: "Implementing Service Level Objectives"
    resource: "Implementing Service Level Objectives (Alex Hidalgo), ch. 8"
---

A time-series alerting engine (e.g., Borgmon, Prometheus) evaluates algebraic expressions over ingested metrics at a fixed cadence — for example, calculating error ratios over a rolling window. When applying alerts to [Service Level Objectives (SLOs)](symptom-based-vs-cause-based-alerting.md), alerting rules must be evaluated against four primary performance criteria:

* **Precision**: The proportion of triggered alerts that represent active, significant incidents (minimizing false positives to combat [alert fatigue](alert-fatigue-and-normalized-deviance.md)).
* **Recall**: The proportion of significant incidents that successfully trigger an alert (minimizing false negatives).
* **Detection Time**: How quickly the alerting rule fires after a system begins degrading.
* **Reset Time**: How quickly the alert stops firing once the underlying issue is mitigated.

## Evolution of SLO Alerting Strategies

The Site Reliability Workbook identifies six progressively sophisticated approaches to time-series alert rule evaluation for service-level monitoring:

1. **Target Error Rate ≥ SLO Threshold (Short Window)**: Checking if the error rate over a short window (e.g., 10 minutes) exceeds the SLO target. While detection time is fast, precision is extremely poor; small spikes that do not threaten the error budget trigger unnecessary pages.
2. **Increased Alert Window**: Evaluating errors over a longer window (e.g., 36 hours). This improves precision but results in terrible reset times: the alert continues to fire for hours after the incident ends because the historical errors remain in the evaluation window.
3. **Incrementing Alert Duration (`FOR` Clauses)**: Requiring the error threshold to hold for a minimum duration (e.g., `FOR 1h`) before paging. This is discouraged because detection time does not scale with severity — a 100% outage takes just as long to page as a minor 1% degradation — and a flapping metric resets the duration timer, failing to alert at all.
4. **Alerting on Burn Rate**: Paging when the rate of error-budget consumption (the burn rate) exceeds a threshold. A burn rate of 1.0 consumes 100% of the budget in exactly the target period (e.g., 30 days). Paging on a burn rate of 14.4 (which consumes 2% of the budget in 1 hour) ensures rapid detection of severe outages.
5. **Multiple Burn-Rate Alerts**: Layering multiple burn-rate and window pairs (e.g., paging immediately on high burn rates and ticketing on slower, long-term burns) to catch both fast and slow-burning incidents.
6. **Multiwindow, Multi-Burn-Rate Alerts (Recommended)**: Adding a short window (typically $1/12$ the size of the long window) that must *also* exceed the burn-rate threshold for the alert to fire. The alert triggers quickly due to the long window's stability, but resets within minutes of mitigation because the short window quickly falls below the threshold.

## Recommended Multiwindow Multi-Burn-Rate Configuration

To implement this recommended approach, alerting engines evaluate two parallel queries for a given threshold: a long window for precision and a short window for quick reset. The page or ticket is only active if `long_window_burn_rate > threshold AND short_window_burn_rate > threshold`.

Google's standard recommended starting parameters for a 30-day (720-hour) rolling window are:

| Alert Severity | Long Window | Short Window | Burn Rate | Budget Consumed | Trigger Condition |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Critical (Page)** | 1 hour | 5 minutes | 14.4 | 2% | Both windows exceed threshold |
| **Critical (Page)** | 6 hours | 30 minutes | 6.0 | 5% | Both windows exceed threshold |
| **Warning (Ticket)** | 3 days (72h) | 6 hours | 1.0 | 10% | Both windows exceed threshold |

Once a rule fires, routing and deduplication of the resulting alert is managed downstream — see [alert routing and notification management](alert-routing-and-notification-management.md). For low-traffic services, time-series evaluations become noisy; operators should mitigate this by generating synthetic traffic, combining service groups, or lengthening the evaluation windows.

## Equivalent Framing: Baseline/Lookahead Extrapolation

The same multiwindow burn-rate math can be built as an **extrapolation** rather than a fixed-threshold comparison: measure the burn rate over a recent **baseline** window, then project it forward across a **lookahead** window to estimate when the error budget will hit zero — visualized as extending a downward-trending line to where it crosses the axis. This framing surfaces two refinements worth layering onto the table above:

- **Forecast budget gain and loss as two separate rates** (successful requests replenishing headroom vs. errors consuming it) rather than one net rate — this makes the alert naturally less sensitive during predictable low-traffic periods (e.g. nighttime) instead of needing that handled as a special case.
- **Require a sustain duration before firing**, on top of the short/long dual-window requirement: short-lived blips (route reconvergence, VM migration) are common and often self-heal within 30–60 seconds. Calibrate the sustain window either by computing what effective loss rate a shorter sustain period would imply and comparing it against the declared burn-rate thresholds, or empirically, by observing how long the bulk of historically inactionable blips actually last and setting the sustain window a bit longer than that.

As with the baseline/lookahead ratio generally, extrapolating too little history too far forward (e.g. 15 minutes of data used to predict 3 days out) reproduces the same over-alerting failure mode as an unstable short window in the multiwindow table above.
