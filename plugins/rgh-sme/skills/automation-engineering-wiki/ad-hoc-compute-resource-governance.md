---
type: concept
title: Ad Hoc Compute Resource Governance
description: >
  Self-service distributed compute for one-off analyses needs quota guardrails
  because accidental over-consumption is easy, even when the engineering time
  saved almost always outweighs the compute cost.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 27"
---

# Ad Hoc Compute Resource Governance

Engineers need compute for prototypes and one-off analyses, not only for
production [cattle](pets-vs-cattle.md) jobs. A workstation suffices for
small tasks; at terabyte scale, waiting a day for a single-machine script
can block iteration entirely — a shared distributed service that finishes
in minutes across hundreds of cores is often the difference between
exploring an idea today and not exploring it at all.

The economic comparison usually favors running the job: a thousand core-hours
rarely costs as much as a day of engineering time — the same principle as
not hoarding cheap office supplies, except compute is **easy to over-consume
by accident** (a forgotten thousand-VM load test over vacation, a debug
session spawning thousands of full-machine workers). Governance therefore
targets accidental runaway, not stinginess.

Typical policy shape:

- **Quotas on general resource usage** — caps that stop one engineer or
  one forgotten job from monopolizing the fleet, aligned with [safeguards
  against runaway automation](safeguards-against-runaway-automation.md).
- **Near-unlimited quota for low-priority batch** — work that runs only on
  spare capacity and is preemptible, making most one-off analyses
  "effectively free" without risking production [serving
  jobs](pets-vs-cattle.md).

This sits at the platform layer of [reusable platforms over bespoke
scripts](reusable-platforms-over-bespoke-scripts.md): the scheduler and
quota system are shared infrastructure; the alternative is every team
building its own cluster or SSH-ing to pet machines for ad hoc work.
