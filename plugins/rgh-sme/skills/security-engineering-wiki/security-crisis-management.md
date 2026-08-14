---
type: concept
title: Security Crisis Management
description: >
  Triage decides whether an escalation is playbook work or a crisis;
  security response differs from reliability response in that you
  investigate fully before fixing, under incident command with explicit
  roles.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 17"
---

# Security Crisis Management

"There are only two types of companies: those that know they've been
compromised, and those that don't know." Not every incident is a crisis —
in a healthy organization few are. **Triage** first, EMT-style: from the
facts available, is this a false positive, an easily corrected
opportunistic compromise, or a complex targeted one? Preplan the criteria.
The same ransomware is a single-engineer playbook item for an org with
execution allowlisting, a non-event for one that auto-wipes compromised
demo instances, and an existential crisis for one with few layers and
little visibility — severity is a function of *your* defenses, not the
threat. Useful triage questions: what data could someone on that system
reach, and how valuable is it? What trust relationships does the system
have? Which compensating controls would the attacker still have to beat?
Commodity malware or something crafted for you? Vulnerabilities usually
aren't incidents (good [defense in depth](defense-in-depth.md) absorbs
them), but extreme-risk bugs (Heartbleed, Shellshock class) are worth
managing *as* incidents, especially under coordinated-disclosure
confidentiality (see
[zero-day response](zero-day-vulnerability-response.md)).

**The defining difference from reliability response**: an outage doesn't
resist being fixed; an attacker does. SRE instinct is fix-first (revert
the CL), investigate after. In a suspected compromise, premature fixing
or cleanup can tip off the adversary and be catastrophic — **complete
the investigation before correcting**, under
[operational security](incident-operational-security.md). And don't
panic: take five minutes to breathe and plan; postmortems essentially
never say the response should have started five minutes sooner.

**Command, control, communications** (IMAG, modeled on the Incident
Command System — one framework shared with SRE so teams interoperate
under stress; full treatment belongs to incident management, security
specifics here):

- Declare explicitly ("we are declaring an incident involving X; I am
  incident commander") and have the IC explicitly accept. Notify
  executives that normal processes may be bypassed until containment.
- The IC manages, full-time — an IC doing log analysis means no one is
  steering. Deputize staff who know the affected systems; appoint an
  *operations lead* to execute the strategy the IC sets. Other leads as
  needed: *management liaison* (empowered to shut down revenue services
  or revoke engineers' credentials), *legal* (privacy expectations,
  evidence handling), *communications lead* (below), and — early —
  a *remediation lead* who builds the cleanup plan in parallel with the
  [investigation](digital-forensics.md), so remediation starts the moment
  investigation ends. Parallelize everything you can, including redacted
  shareable indicator lists and the postmortem.
- The IC runs a loop over leads (status, new info others need,
  roadblocks, resources, fatigue), status dashboards, stakeholder
  updates, and the question "do we know enough to remediate yet?" —
  OODA (observe, orient, decide, act) as the decision discipline.
- **Handovers and fatigue**: cap shifts (including IC) at ~12 hours; the
  law of diminishing returns turns tired responders into error sources.
  Follow-the-sun or two-team rotation where staffing allows; handover =
  updated documentation plus the outgoing IC answering "what would I do
  in the next 12 hours if I weren't handing off?" Morale is an IC
  responsibility: food, sleep, destressing, burnout watch, leading by
  example.

**Communications discipline**: be explicit and overcommunicate —
"mitigated" means different things to product and security teams; the
communicator owns being understood. Ban hedging ("we're pretty sure" →
"sure about servers, NAS, email, file shares; low confidence in hosted
systems due to log visibility"). Keep sync meetings small (leads only,
IC-planned agenda, an assigned note taker — notes feed the postmortem
and legal). A **communications lead** manages who learns what:
executives get succinct progress/roadblocks/consequences; the response
team gets full detail; uninvolved staff get a deliberate decision
(informed helpers vs. rumor mill — the vaguely aware fill gaps with
fiction); customers may be legally entitled to notification on a clock
(24-hour expectations are now common); law enforcement will ask for more
than you planned to share.

**The imminent-risk exception**: executives (advised by the IC) may
trade availability for security outright — Apple turned FaceTime off for
a day rather than leave an easily exploited privacy bug live, a decision
the industry applauded. Crisis decisions are rarely about the *right*
call, but the best of a range of suboptimal ones.
