---
type: concept
title: Monitoring Mode Selection
description: >
  Choose among continuous, probe, proactive, and reactive monitoring modes
  depending on whether the system is steady-state, under investigation,
  facing a planned change, or showing a drift signal.
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Woods, Wreathall, eds.), ch. 6 (Philippe Cabon et al.)"
---

Controls need feedback loops, but not every loop runs the same way:

- **Continuous** — routine telemetry and incident logs continuously feed a
  [factor combination risk matrix](factor-combination-risk-matrix.md) or
  [running decision log](running-decision-log.md). Default steady-state
  mode.
- **Probe** — focused measurement over a limited window (e.g. a one-month
  sleep and fatigue diary) to refresh estimates when continuous data are
  thin.
- **Proactive** — intensified monitoring before a known change (new job
  schedule, travel, medication change) to baseline and adjust controls
  ahead of failure.
- **Reactive** — triggered when a continuous indicator drifts (rising
  missed deadlines, more [automated proofreading
  scaffold](automated-proofreading-scaffold.md) catches, partner flags
  overload via [designated external state
  monitor](designated-external-state-monitor.md)).

Match mode to cost: continuous light logging is cheap; probe and proactive
bursts cost more attention but prevent mis-calibrated controls. Results
should feed back to everyone who must sustain the controls — not only the
person designing them — so engagement does not decay after setup.
