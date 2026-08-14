---
type: concept
title: Canary Request Pattern
description: >
  Sending a fanned-out query to one or two backends first and only fanning out to the rest if those replies succeed, so a single malformed or malicious query can't crash an entire fleet at once.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 6"
---

A **query of death** is a specific request that triggers an untested code
path, causing the backend that handles it to crash, hang, or run away —
dangerous on its own, but catastrophic in a fan-out architecture where one
query is dispatched to many backends (or shards) simultaneously: a single
bad query can crash the entire fleet in one shot, not just one machine.

The **canary request pattern** defends against this at the request level:
rather than fanning a query straight out to every backend, the frontend
sends it first to just one or two "canary" backends and waits for a
healthy reply within a reasonable time before fanning out to the rest. If a
canary crashes, hangs, or errors, the query is flagged as dangerous and
never reaches the remaining backends — limiting the blast radius to the one
or two canaries instead of the whole fleet. This is the request-shaped
sibling of a canary deployment (progressive-delivery territory): where a
deployment canary limits exposure of a *new build* to a small slice of
traffic before a full rollout, a request canary limits exposure of a single
*query* to a small slice of backends before full fan-out.

The pattern is a cheap, generic complement to a manually maintained banned
query list (an explicit, easily-updated deny list of known-dangerous
queries pushed to all frontends) — a deny list only blocks queries someone
has already noticed and added, whereas canarying catches novel dangerous
queries automatically, including both unpredictable bugs and deliberate
denial-of-service-style queries crafted to exploit a fan-out architecture's
blast radius. It trades a small amount of added latency (the canary
round-trip before full fan-out) for containment of a specific,
high-severity failure mode.
