---
type: concept
title: Incident Response Process Framework (PROCESS)
description: A seven-attribute checklist — Predictable, Repeatable, Optimized, Clear, Evaluated, Scalable, Sustainable — for auditing whether an organization's incident response is mature rather than ad hoc.
sources:
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 1"
---

**PROCESS** evaluates an organization's incident response maturity as seven
interdependent attributes, each building on the last:

- **Predictable** — the *who*: are roles and on-call expectations
  unambiguous before an incident starts, and is "you're on-call" treated as
  non-optional?
- **Repeatable** — the *how*: does a given incident type get handled the
  same way regardless of time of day or day of week? Repeatability doesn't
  require 24x7 staffing, only that on-call responders are genuinely
  available and respond consistently — it is described as "the natural
  enemy of [spray and pray](dispatch-vs-notification.md)."
- **Optimized** — are responders actually trained and equipped for the job,
  including third-party vendors who need to share the same sense of
  urgency? People who "don't get it" are usually people who were never
  briefed, not people who don't care.
- **Clear** — are programmatic and incident-specific goals communicated to
  everyone who might participate, starting at the executive level? Clarity
  failures show up as SMEs joining a bridge and asking "why am I here."
- **Evaluated** — is there a **quality assurance** loop (checking behavior
  against an established standard) and a **quality improvement** loop
  (finding and fixing gaps), feeding into the [after action
  review](after-action-review.md)? Unaddressed poor performance becomes
  the accepted norm if it's never surfaced.
- **Scalable** — can the same framework flex from a two-person incident to
  a company-wide one? This depends on having **bench strength** — a wide
  pool of comparably skilled responders to rotate through coverage, rather
  than depending on a few irreplaceable people.
- **Sustainable** — does incident response get the same organizational
  investment (budget, leadership attention, career respect) as any other
  business function, rather than being treated as a necessary evil bolted
  onto otherwise-strong engineers?

The framework is meant as a discussion and audit tool: if [mean time to
assemble](mean-time-to-assemble.md) or resolution time is a problem, walking
through each PROCESS attribute in order locates which part of the response
system is actually broken, rather than treating "our incidents take too
long" as one undifferentiated complaint.
