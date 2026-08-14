---
type: concept
title: Lame-Duck Mode (Queue Draining)
description: >
  A replica that needs to be taken out of service intentionally fails its
  own health checks so a load balancer stops routing new traffic to it,
  letting automation retire or replace it without losing in-flight work.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 2"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 27"
---

# Lame-Duck Mode (Queue Draining)

Killing a live replica outright loses whatever requests it was in the
middle of serving. Lame-duck mode avoids this: the replica intentionally
starts failing its load balancer health check while it keeps running,
so the load balancer stops sending it *new* requests but the replica
finishes the ones already in flight before anything terminates it. Once
its request queue is empty, it's safe to kill, upgrade, or reclaim without
any request loss.

This is a small building block that most automated remediation and
maintenance depends on: an [autoscaler](autoscaling-safety-practices.md)
scaling down, a [self-healing](self-healing-overload-response.md) process
replacing an unhealthy instance, or a rolling upgrade cycling replicas one
at a time all need a safe way to stop routing to a target *before* removing
it, rather than removing it and dealing with the dropped requests after the
fact. Without it, automation is forced to choose between two bad options:
kill-and-lose-in-flight-work, or leave the old instance running
indefinitely out of caution — neither of which is acceptable at the speed
and frequency automation is expected to operate.

The same mechanism works symmetrically for bringing a replica *into*
service under test: starting it already in drained mode lets automation
(or an operator) route synthetic or canary traffic to it directly,
bypassing the load balancer, and only "undrain" it into normal rotation
once it's confirmed healthy — a cheap way to validate a freshly
provisioned or freshly upgraded instance before it can affect real users.

Managed schedulers can improve on blind kill-and-replace by **signaling
intent to reschedule** before terminating a [cattle](pets-vs-cattle.md)
replica — giving the container time to refuse new requests while finishing
in-flight ones, which requires the load balancer to honor an "cannot
accept new requests" response and redirect elsewhere. That advance notice
turns lame-duck draining from something the replica invents under duress
into a coordinated step in [progressive compute
automation](progressive-compute-automation.md), but only for services
built to participate; without it, automatic recovery still works while
users see errors during moderate failure rates.
