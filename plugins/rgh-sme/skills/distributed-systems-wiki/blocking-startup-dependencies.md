---
type: concept
title: Blocking Startup Dependencies
description: >
  A process that blocks its own initialization on a synchronous remote call
  turns an unresponsive dependency into a deployment-wide restart loop, not
  just one slow request.
sources:
  - title: "Release It! (2nd ed.)"
    resource: "Release It!, 2nd ed. (Nygard), ch. 12, Case Study: Waiting for Godot"
---

# Blocking Startup Dependencies

An unbounded wait on a remote call is dangerous anywhere in a running
process (see [timeouts and failure detection](timeouts-and-failure-detection.md)'s
warning about default infinite socket timeouts), but a wait during
**process startup** is a sharper version of the same bug: it doesn't just
hang one request or one worker thread, it prevents the instance from
becoming available *at all*.

## The failure shape

1. On startup, the process makes a synchronous RPC to fetch some reference
   or configuration data it believes it needs before it can serve traffic.
2. The remote dependency isn't down — it's unresponsive (undergoing
   maintenance, dropping connections silently). Because the calling client
   has no connect timeout, the startup thread blocks indefinitely.
3. The process never finishes initializing, so it never binds its service
   port and never becomes ready.
4. A container/deployment orchestrator's readiness probe — which is only
   checking "did this instance finish starting and start answering" —
   reports failure. The orchestrator kills the instance and starts a fresh
   one, which hits the same unresponsive dependency and hangs the same way.

The result is an infinite restart loop, not a single failed instance: every
replacement instance re-runs the same blocking startup path and re-hangs on
the same unavailable dependency. Because the orchestrator's health signal
*is* the readiness probe, and the readiness probe can never pass, this can
stall an entire rolling deployment — the orchestrator will not promote new
instances or proceed with a rollout while replacements keep failing their
health checks, which is a materially worse outcome than the plain
"cascading failure" case in [cascading failures](cascading-failures.md): the
blast radius here is the whole deployment pipeline, not just the load on
surviving nodes.

## The fix: never let readiness depend on a synchronous remote call

- **Bind the local port and pass health checks immediately.** Startup should
  reach a servable state on local state alone — a bundled default dataset or
  the last cached copy from a previous run — before it ever calls out to any
  remote dependency.
- **Fetch remote configuration asynchronously, in the background**, after
  the process is already accepting traffic, and keep retrying/refreshing it
  on its own schedule rather than gating readiness on the fetch completing.
- **Give every bootstrap network call an explicit, aggressive connect
  timeout**, exactly the discipline [retry design](retry-design.md) and
  [timeouts and failure detection](timeouts-and-failure-detection.md)
  already require for calls made after startup — a client library's default
  of "no timeout" is exactly as dangerous on the startup path as anywhere
  else, just with a larger blast radius when it fires there.

The general principle this instantiates: readiness should reflect whether an
instance can serve *degraded but useful* traffic, not whether every
dependency it would like to have is currently reachable — the same
distinction [partial failure](partial-failure.md) draws between a fault in
one component and a failure of the system as a whole, applied to the
startup path specifically.
