---
type: concept
title: Progressive Compute Automation
description: >
  Operating compute at organizational scale forces a recognizable ladder of
  automation — deployment, monitoring, process self-healing, then central
  scheduling — because manual SSH-and-deploy workflows collapse long before
  the fleet does.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 27"
---

# Progressive Compute Automation

At one machine, SFTP-ing code in, SSH-ing to compile, and running by hand
is tolerable. At hundreds or thousands of machines, the same workflow
becomes the [toil](toil.md) that blocks everything else: no automatic
migration when a machine dies, ad hoc progress monitoring, and a
human-maintained "sign up" file to throttle who may use which machines —
each failure mode visible only because someone is watching.

The usual escape path climbs the [automation maturity
spectrum](automation-maturity-spectrum.md) in a compute-specific order:

1. **Deployment automation** — a shell script at first, then a robust
   parallel-deploy tool so the same rollout runs consistently across many
   hosts without a human repeating steps.
2. **Monitoring automation** — export liveness and throughput signals
   (process alive, work completed) to a dashboard so progress is visible
   without SSH-ing to ask.
3. **Process self-healing** — an agent on each machine detects anomalies
   (no heartbeat for five minutes, no progress for ten) and kills and
   restarts the process locally. At cloud scale the same idea appears as
   an autohealing policy that recreates a VM or container on failed health
   checks — see [autoscaling safety
   practices](autoscaling-safety-practices.md) for pairing that with
   capacity automation.
4. **Central automated scheduling** — the turning point: a service that
   knows the full machine list, picks unoccupied machines, and deploys
   without a hand-maintained sign-up file. Combined with machine-log
   scanning for bad-health signals (mass disk read errors, and similar),
   it can avoid scheduling onto broken machines, attempt automated
   remediation (reboot, disk scan) before paging a human, and — once a
   machine is known broken — reallocate its work elsewhere without manual
   migration.

Step 4 is what makes the fleet start to resemble earlier time-sharing
architectures: a central allocator, not a spreadsheet of who borrowed
which box. It also exemplifies why [reusable platforms over bespoke
scripts](reusable-platforms-over-bespoke-scripts.md) pay off here — the
scheduler is infrastructure every team shares, not a per-job workaround.

The same progression applies to *new* operational requirements as the
organization grows: GPU/TPU scheduling, heterogeneous hardware, and even
whole-datacenter turn-up were once manual, specialist, multi-week
processes and became fully automated as the number of datacenters made
manual operation impossible. Automation must keep absorbing new classes
of [toil](toil.md) along three growth axes at once: more distinct
applications, more replicas per application, and larger largest
applications.
