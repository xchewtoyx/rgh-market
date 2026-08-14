---
type: concept
title: Capacity Yield Point
description: >
  Demand on a person can increase with manageable compensation up to a
  yield point, beyond which functioning degrades permanently for that
  episode until load is removed and recovery completes.
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel et al., Eds.), Chapter 7 (Siemens Turbine Maintenance Case Study)"
---

Woods and Wreathall's ductile-metal analogy maps cleanly onto personal
capacity: under increasing load, a person copes and recovers when the
load is removed — up to a **yield point**. Beyond yield, the system does
not spring back: mental functioning degrades, errors become more likely,
and risk of loss rises until load is actively reduced and recovery runs
its course. Further load can push past fracture — complete inability to
cope.

The analogy is not merely metaphorical in maintenance field service:
extreme weather did not directly cause turbine losses, but cold-weather
gear, discomfort, and stacked emergent work raised stress, degraded
functioning, and correlated with high-loss outages. Difficult situations
stack without a one-to-one link to any single failure: each one consumes
capacity and stress further reduces what remains.

Highly resilient planning therefore includes **noticing** when people are
approaching yield — multiple minor safety incidents, progress stalling,
fatigue signs, communication dropping off, common tasks performed late —
not only responding after a breakdown. Near-limit behavioral signs
include forgetfulness, missed steps, anger outbursts, and visible
fatigue/stress.

The design question that matters at yield approach: where were people
relative to their limits *before* the new stressor arrived — already
highly loaded and close to the limit, or with headroom to absorb it? See
[capacity load triage menu](capacity-load-triage-menu.md) for the three
response categories once overload is noticed.

Resilience engineering maps four behaviors onto this curve: anticipate
disruptions before they arrive, notice when risk profile changes, plan
responses, and adapt work when yield approaches. Loss prevention treats
safety, quality, and inefficiency as one family because overload degrades
all three through the same capacity mechanism — mental functioning under
stacked demand, not separate failure modes requiring separate remedies.
