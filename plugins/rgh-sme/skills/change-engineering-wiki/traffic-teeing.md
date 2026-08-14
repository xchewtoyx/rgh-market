---
type: concept
title: Traffic Teeing
description: >
  Copy live production traffic to a test or canary system and discard its
  responses, giving more realistic coverage than synthetic load at the
  cost of complexity and risk on stateful systems.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 16"
---

# Traffic Teeing

Traffic teeing duplicates live production traffic to both the real
production system and a separate test or canary system, discarding the
copy's responses. It is a way to evaluate a change against real request
patterns without actually serving the change's output to users — related
to but distinct from [canary release](canary-release.md), which serves
real responses to a real, if small, subset of traffic.

It's more representative of real usage than artificial/synthetic load
generation, which maximizes code coverage but not *state* coverage — poor
for systems with mutable state (caches, cookies, session affinity) and
dangerous on systems with real side effects, since synthetic load can
accidentally trigger production-affecting actions (e.g. a billing system
that would actually charge a card).

Traffic teeing has its own failure mode on stateful systems: a shared
cache between the real and teed paths inflates the teed system's
measured cache hit rate, invalidating whatever performance signal the tee
was meant to produce.

For a full system replacement (not just a code change), the bar teeing is
validated against can be stricter than "produces a correct result": some
domains (e.g. financial reconciliation) require **bug-for-bug parity** —
the replacement must match the legacy system's actual output exactly,
including any known quirks or bugs in that legacy system, before cutover
is safe. In that case the right sequence is to deliberately reproduce the
legacy bug in the replacement, confirm teed outputs match byte-for-byte,
cut over, and only then remove the emulated bug as a normal fixed-forward
change against the new system of record — rather than trying to fix the
bug as part of the migration itself, which would make a parity comparison
meaningless.
