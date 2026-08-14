---
type: concept
title: Quality Attribute Scenario
description: >
  A six-part scenario format — stimulus, source, environment, artifact,
  response, and response measure — that turns an untestable quality claim
  like "the system must be secure" into a specific, checkable requirement.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 3"
---

A quality attribute — performance, security, modifiability, availability,
and the rest — is only useful as a requirement if it is stated concretely
enough to test. "The system will be modifiable" is meaningless, because
every system is modifiable with respect to some changes and brittle with
respect to others. The quality attribute scenario fixes this by forcing
six parts to be considered, uniformly across every quality attribute:

1. **Stimulus** — the triggering event or condition (a load spike, a user
   action, a security attack, a change request, a completed unit of
   development).
2. **Source** — where the stimulus originates, because that changes the
   required response (a request from a trusted internal service is not
   treated the same as one from an untrusted external caller).
3. **Environment** — the circumstances the scenario occurs in (normal
   operation vs. overload; before vs. after a release freeze; the first
   failure vs. the Nth in a row).
4. **Artifact** — the specific part of the system the stimulus hits (the
   whole system, or one particular element — a failure in the primary
   data store may warrant a different response than one in a metadata
   cache).
5. **Response** — what the system (for runtime attributes) or the
   development organization (for attributes like modifiability or
   testability) must do about the stimulus.
6. **Response measure** — how the response is measured, so the scenario
   can actually pass or fail (a latency or throughput figure; the
   labor-hours or wall-clock time to make, test, and deploy a change).

It's common to leave a part out, especially early in elicitation, but
working through all six is what forces a check on whether each one
matters for this particular requirement — omitting a part by oversight is
different from omitting it by informed judgment. This is the same
discipline a [fit criterion](fit-criterion.md) applies to an ordinary
requirement, specialized for quality attributes and split into enough
parts to make the requirement precise instead of just measurable.

A **general scenario** is a quality-attribute-specific but
system-independent template — one per quality attribute, meant to jump
start elicitation. A **concrete scenario** instantiates a general
scenario for the actual system under design. Handing a stakeholder a
general scenario to tailor is far more productive than asking them to
invent a scenario from nothing, for the same reason a starting template
generally beats a blank page in any elicitation exercise — see
[requirements elicitation techniques](requirements-elicitation-techniques.md).

Quality attribute scenarios are the elicitation-and-specification half of
the discipline; [quality-attribute scenario
testing](quality-attribute-scenario-testing.md) is the verification half —
actually checking a concrete scenario's response measure against built or
running behavior, rather than letting it sit as an assertion in a design
document. Scenarios collected and prioritized across all the quality
attributes that matter for a system feed directly into
[architecturally significant requirements](architecturally-significant-decision.md)
and into the trade-offs an architecture has to make between them — see
[documenting trade-offs](documenting-trade-offs.md).
