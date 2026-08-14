---
type: concept
title: Blameless Postmortems
description: A post-incident analysis culture that assumes operators act with good intentions, aiming to identify systemic gaps rather than individual failure.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 15"
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook (Gene Kim, Jez Humble, Patrick Debois, John Willis, Nicole Forsgren), ch. 19"
  - title: "The Site Reliability Workbook"
    resource:
      "The Site Reliability Workbook: Practical Ways to Implement SRE (Betsy
      Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen
      Thorne), ch. 10, ch. 19"
  - title: "Building Secure and Reliable Systems"
    resource:
      "Building Secure and Reliable Systems (Heather Adkins, Betsy Beyer,
      Paul Blankinship, Piotr Lewandowski, Ana Oprea, Adam Stubblefield),
      ch. 21"
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook (Gene Kim, Jez Humble, Patrick Debois, John Willis, Nicole Forsgren), Appendix 8"
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 6"
  - title: "Thinking in Bets"
    resource: "Thinking in Bets: Making Smarter Decisions When You Don't Have All the Facts (Annie Duke), ch. 3, 5"
---

**Blameless Postmortems** reinforce psychological safety by assuming that engineers act with good intentions based on the information available to them at the time. This depends on an organization whose broader information-flow culture supports it — see the [Westrum organizational culture typology](westrum-organizational-culture-typology.md) for why a blameless template alone doesn't guarantee blameless outcomes. If an engineer makes a mistake, the postmortem focuses on why the system allowed that mistake to happen (e.g., poor tooling, lack of safeguards, or confusing interfaces) rather than blaming the individual. Etsy's Bethany Macri gave the precise, oft-quoted definition: "Blamelessness in a post-mortem does not mean that no one takes responsibility. It means that we want to find out what the circumstances were that allowed the person making the change... to do this... By removing blame, you remove fear, and by removing fear, you get honesty." Blameless does not mean consequence-free — it means the inquiry targets the system, not the person, as the object of change.

The meeting itself needs active facilitation to stay blameless in practice, not just in template: the facilitator should open by restating the blameless norm explicitly, and should resist the group's pull toward a single tidy "root cause" — asking "how" repeatedly, rather than stopping at the first plausible explanatory factor, surfaces the multiple contributing conditions that a linear narrative hides. See the [root cause fallacy](root-cause-fallacy.md) for why that pull toward one cause is itself worth guarding against.

Key components of a blameless postmortem:
* **Clear Triggers**: Defined criteria for when a postmortem is required (e.g., SLO breach, data loss, manual intervention > X minutes).
* **High-Resolution Timeline**: Chronological sequence of events (detection, escalation, mitigation, resolution) built using evidence-based telemetry and chat logs rather than subjective memory.
* **Objective Analysis**: Identifying what went well, what went poorly, and — as a distinct third category — **where luck played a role**: near misses that succeeded by chance rather than by design. Recording luck separately from "what went poorly" matters because a lack of skill isn't the same failure as an absence of bad luck; a step that happened to work only because a secondary system was healthy that day is a latent risk even though nothing went wrong, and it gets lost if it's folded into "what went well."
* **Action Items**: Concrete engineering tasks with assigned owners and bug tracking IDs.

### Tooling and Sharing
Standardizing postmortems using specialized tooling (such as Etsy's **Morgue** tool) simplifies timeline creation, timezone handling, and chat log imports. Easy tooling significantly increases postmortem completion rates, especially for lower-severity incidents. Retrospectives must be searchable and published widely (sometimes publicly to build trust) so that lessons are distributed throughout the organization. Mature setups auto-populate postmortem metadata (roles, timeline, severity, detection mechanism) from incident-management tooling and store postmortems centrally, enabling trend analysis over time using consistent [outage tracking metrics](outage-tracking-metrics.md) — rather than treating each postmortem as a one-off document.

A postmortem that omits background context (undefined jargon, no glossary),
quantitative impact data, or a populated recovery-efforts section fails
readers outside the immediate team and undermines the org-wide learning that
justifies writing one at all — publishing narrowly, to just the owning team,
wastes most of the document's value. Publish promptly, ideally within about
a week: accuracy degrades with delay, and silence in the meantime invites
people to fill the gap with their own assumptions, sometimes letting the
same failure recur before the lessons are captured.

### Sustaining the culture, not just the template

A blameless template alone doesn't guarantee a blameless culture. Reinforcing
mechanisms matter: reward the *closing* of action items, not just the
writing of the postmortem, and publicize the reliability improvements that
result. When someone with authority — including senior leadership — slips
into blameful language ("who should have known"), it undermines the whole
culture and needs active, tactful correction, redirected toward systemic
questions ("what warning signs did we miss"). Teams too overloaded to write
a careful postmortem produce a weak one that seeds a future recurrence of
the same failure — protecting writing time is itself a reliability
investment. As Google VP Ben Treynor Sloss put it: "a postmortem without
subsequent action is indistinguishable from no postmortem" — every
outage-causing postmortem should produce at least one tracked bug.

When an incident spans an organizational boundary — a platform and the
customers building on it — run a **joint postmortem** with the affected
party rather than a one-way postmortem handed to them afterward. A joint
session surfaces mutual lessons (what the platform could have made safer,
what the customer's own architecture should change) and builds the kind of
trust that a unilateral document can't.

Learning need not be limited to an organization's own incidents. Public
after-action reports from other organizations — the Columbia Disaster
Investigation Board's report on NASA's organizational culture is a widely
cited example — apply the same blameless, systemic-factor lens to failures
an organization never experienced directly, broadening what it learns from
beyond its own incident history.

By removing blame, organizations ensure that engineers feel safe to report mistakes. To maximize learning, postmortems should be coupled with [action-item quality](action-item-quality.md) guidelines and grounded in the [local rationality principle](local-rationality-principle.md).

### Self-serving bias distorts who gets credited with what

A specific, well-documented distortion worth watching for explicitly: people
routinely attribute their own bad outcomes to bad luck and their own good
outcomes to skill — and do the reverse for other people, crediting others'
successes to luck and their failures to lack of skill. Left unchecked, this
means a blameless postmortem's nominal target (avoid blaming the
individual) can still get quietly undermined by a room that unconsciously
sorts outcomes into "their fault" and "just unlucky" along exactly these
lines. The corrective habit is symmetrical: when reviewing your own
decision, ask what you'd conclude if a respected peer had made the
identical call; when reviewing someone else's, ask what you'd conclude if
you had made it yourself. Consciously separating "was this outcome driven
by the decision, or by something nobody in the room controlled" — the same
discipline behind [action item quality](action-item-quality.md)'s
distinction between explanatory and change factors — is what a blameless
process is actually trying to institutionalize, not just a rule against
naming names.

### A CUDOS-style charter for the review itself

Sociologist Robert Merton's four norms for how a scientific community
should treat evidence transfer cleanly onto how a postmortem group should
treat an incident's evidence:

- **Share everything relevant**, including the detail that feels most
  uncomfortable to admit — discomfort is itself a signal the detail matters,
  not a reason to omit it. A single person's account of what happened is
  reliably incomplete or shaped by their own vantage point, so the group
  has to actively ask for what's missing rather than assume one telling is
  the whole story.
- **Judge the claim, not the messenger.** A finding shouldn't get more or
  less scrutiny depending on who raised it — dismissing an unconventional
  read of the incident because it came from the newest team member, or
  waving through a senior engineer's account unchallenged, both defeat the
  point of the exercise.
- **Watch for the room's own conflicts of interest.** People are motivated
  to defend their own prior decisions, avoid admitting error, and read the
  evidence in whatever way protects that. Describing what happened without
  immediately revealing who made which call, or what the ultimate outcome
  was, before asking for an assessment strips out some of this bias — an
  evaluator who doesn't yet know how the story ends is less likely to
  reverse-engineer a judgment to fit it.
- **Make dissent an expected, structured part of the process**, not an
  interruption. Reframing disagreement as "how do we know this, and what
  would tell us we're wrong" rather than "you're wrong" keeps the exchange
  civil while still surfacing the challenge — and having a designated
  person raise the counterargument (echoing the [Plans
  group](incident-command-system.md)'s function during live response) makes
  it a legitimate role instead of a personal confrontation.

### The blame game as the primary failure mode

Playing the blame game is described as the primary "deal killer" for a
postmortem process — easy to fall into, especially for whoever wasn't in
the hot seat, and it takes only one high-profile witch-hunt-style review to
teach an organization that future incidents should be handled defensively
rather than openly. The useful distinction to hold onto in the room itself
is **critique versus criticism**: critique is constructive and grounded in
the context a responder actually had; criticism reads as an attack and gets
rejected by the person receiving it, shutting down the honesty the whole
exercise depends on. A facilitator's job includes noticing when the
conversation has drifted from one into the other and redirecting it back —
see [After Action Review](after-action-review.md) for a review format built
around this same critique framing, extended to also evaluate the incident
command and response structure itself, not only the technical timeline.
