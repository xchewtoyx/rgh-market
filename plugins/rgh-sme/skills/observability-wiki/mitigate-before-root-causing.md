---
type: concept
title: Mitigate Before Root-Causing
description: During an active incident, restoring service (rollback, failover) should take priority over fully understanding the root cause, since a mitigated outage buys time for careful investigation while an unmitigated one keeps costing users.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 12"
---

Once a problem is demonstrated, the immediate priority is mitigating user impact — traffic failover, rolling back a release — rather than beginning deep root-cause analysis. Deep investigation can happen afterward, once the bleeding has stopped.

The corresponding pitfall is **fixating on causes over mitigation**: spending hours identifying a complex code bug during an active outage instead of simply rolling back the deployment that introduced it. If a recent change is a plausible cause (see [change correlation in debugging](change-correlation-in-debugging.md)), reverting it is usually cheaper and faster than understanding it in the moment.

This is a debugging-process principle about ordering investigation after mitigation; coordinating *who* handles mitigation vs. investigation during a live incident is an incident-response concern, not an observability one.
