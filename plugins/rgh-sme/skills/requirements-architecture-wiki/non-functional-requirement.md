---
type: concept
title: Non-Functional Requirement
description: >
  A non-functional requirement specifies a quality or operational
  property a product must have — how well it does what it does — and is
  as decisive for acceptance as any functional capability, despite
  lacking a clean 1:1 trace to a single feature.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 11"
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Jez Humble, David Farley), ch. 9"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 4"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 3, ch. 20"
---

A non-functional requirement (NFR) specifies a quality or property the
product must possess — *how well* it performs its
[functional](functional-requirement.md) behavior, not what that behavior
is. The Volere categorization groups these into look-and-feel; usability
and accessibility; performance (response time, throughput, capacity,
reliability, precision); operational/environmental conditions;
maintainability and support; security; cultural fit; and legal/regulatory
compliance. A complementary, engineering-facing vocabulary for the same
territory names capacity, throughput, latency (stated as percentiles, e.g.
p95/p99), concurrency, availability, scalability, security, usability, and
operational maintainability — precise enough to state an NFR without
resorting to words like "fast" or "scalable" that
[fit criteria](fit-criterion.md) exist to eliminate. A third taxonomy
(FURPS+) sorts the same territory into Reliability, Performance, and
Supportability, plus a separate "design constraints" category for choices
imposed on the solution rather than qualities of it — different vocabulary
over the same underlying territory, not a competing definition of it.

NFRs are structurally different from functional requirements in one
important way: a feature requirement traces cleanly from a user story to
specific code and an integration test, but a reliability or security NFR
usually applies horizontally across the whole system, isn't tied to any
one story, and has no equivalent of "flip this flag to turn it on." That
makes them easy to state once, centrally, and easy to leave implicit — and
correspondingly easy to under-elicit relative to functional requirements.
Conventional requirements practice systematically favors the
functional side: systems get built and tested against what they *should*
do, while operational qualities — what a system must *not* do (crash,
hang, leak data, lose money) — go undiscovered until they fail in
production, because nobody treated them as first-class requirements to
elicit and specify in the first place. See [feature-complete vs.
production-ready](feature-complete-vs-production-ready.md) for this
failure mode in full. A countermeasure some organizations adopt is a
standing checklist of operational NFRs — telemetry, dependency tracking,
graceful degradation, version compatibility, log searchability,
distributed tracing, centralized runtime config — applied to every service
by default, on the reasoning that the team building a service is not its
only customer: the team that has to operate it downstream is too, and its
needs deserve the same priority as a user-facing feature. See [operational
requirements as first-class requirements](operational-requirements-as-first-class.md)
for the stronger version of this argument: that the "non-functional" label
itself is part of why these needs get under-elicited.

Because an NFR has no single story to live inside, a backlog-centric
process needs a deliberate home for it — a dedicated NFR backlog inside
the same tracking tool used for stories, a wiki page valued for being
continuously visible to the whole program, or a standalone [NFR
specification document](nonfunctional-requirements-specification-template.md) —
rather than leaving it to be remembered informally, which is how NFRs
quietly get forgotten between the interview where they were elicited and
the point where they should have been tested.

NFRs also don't trace to verification the same way functional
requirements do: not every NFR is practically testable beyond a one-time
inspection (a mandated programming language, say), most warrant at least
one objective test, and some need an entire test suite — but every
system-qualities test should map back to at least one NFR, since a test
with nothing it's verifying against gives no way to judge pass or fail.
This many-to-many, not-always-required mapping is the NFR-specific case of
the general discipline in [requirements
traceability](requirements-traceability.md).

See [SLO as documented requirement](slo-as-documented-requirement.md) for
a fully worked example of specifying a reliability NFR with the same
rigor — fit criterion, rationale, ownership — that Volere expects of any
requirement. See [quality attribute scenario](quality-attribute-scenario.md)
for a complementary six-part format specialized for architecturally
significant NFRs.

Not every quality concern a stakeholder raises is the software
architecture's to satisfy: a system that is physically isolated and
guarded, for instance, may legitimately have no software security
requirement at all, because the concern is being handled by non-software
means. Treating every quality concern as automatically a software NFR,
without checking whether some other control already covers it, produces
requirements that are technically satisfiable but pointless to build.
