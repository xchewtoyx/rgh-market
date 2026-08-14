---
type: concept
title: After Action Review (AAR)
description: A post-incident review methodology that evaluates both what broke and how the people responded, run as a critique rather than a search for a culprit.
sources:
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 6"
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Gary Klein), ch. 11"
---

An **After Action Review (AAR)** evaluates two separate things after every
incident: what broke (the technology failure and its contributing factors)
and how the people responded to it. The source deliberately avoids the term
"post mortem" — associated with death, and in practice too often turned into
"searching for the guilty" — and treats root-cause analysis (RCA) alone as
insufficient, since RCA tends to overfocus on a single technical cause and
skip evaluating the human/process side (a delayed dispatch, a commander who
didn't lead effectively) entirely. The diagnostic question the AAR is built
to answer: if a problem took two hours to resolve, was that because the
problem itself was genuinely that hard, or because there was no process
managing the human response to it? This complements, rather than replaces,
[blameless postmortems](blameless-postmortems.md) and [learning
reviews](learning-reviews.md) — different named methodologies converging on
the same goal of learning without blame.

An AAR is framed as **critique, not criticism**: constructive and grounded
in context, rather than perceived as an attack. Getting the questions right
matters as much as the intent — starting with "why" tends to produce
defensive explanations, while starting with "how," "what," or "when"
produces more usable, descriptive data. There is no single objective account
of an incident, only an amalgam of perspectives, so an AAR is structured to
collect and triangulate multiple viewpoints rather than converge
prematurely on one simplified narrative.

**Data collection** for every incident should capture, as a baseline: a
description of the problem (symptoms); a description of the cause or
contributing factors; who responded and their dispatch/arrival timestamps
(feeding [mean time to assemble](mean-time-to-assemble.md)); what solution
was implemented; and the overall time to resolve. From this, someone —
ideally not limited to people who worked the incident — builds a full
timeline including decision points and *why* each decision made sense given
the information available at the time, since hindsight always knows more
than the responders did in the moment. Timeliness matters: the longer the
gap between incident and review, the harder it is to convene people and the
less relevant the findings — a target of completing the review within a
week is offered as already too slow.

A useful interview structure for drawing out what actually happened, adapted
from expertise-elicitation research: take a first quick pass through the
incident just to see where the real judgment calls were, then a full
retelling pinned to an explicit timeline, then a pass specifically probing
what each person noticed at each shift in their understanding and what
alternatives they considered (or didn't, and why) — and, if time allows,
a pass asking what a *less experienced* responder would likely have gotten
wrong at each choice point, which reliably surfaces expertise the
responder themselves wouldn't think to mention unprompted. A review is
also, whether or not anyone intends it, a **permission story**: it
implicitly teaches everyone who hears it what the organization actually
tolerates — how much pushback on a plan is acceptable, how loud someone is
allowed to get before being heard, when it's socially safe to escalate
past a hesitant peer. A review that only reconstructs the technical
timeline while ignoring this teaches the culture something too, just by
omission.

The suggested five-step process: determine what caused the problem;
evaluate each part of the response (the [incident command
system](incident-command-system.md), the commander's performance, the
subject-matter experts' problem-solving); compile findings into a report
promptly; convene the team to review it; and — the step most often
skipped — ensure identified changes actually get implemented and followed
up on. The [TALENT diagnostic framework](talent-diagnostic-framework.md)
gives a structured way to locate *where* on the people side a failure
occurred once the timeline is built.
