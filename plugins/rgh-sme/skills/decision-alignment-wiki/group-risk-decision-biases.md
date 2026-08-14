---
type: concept
title: Group Risk-Decision Biases
description: >
  Three named failure modes — group polarization, risk
  transfer, and decision transfer — by which a group's risk
  call diverges from what any individual member would
  actually choose.
sources:
  - title: "Database Reliability Engineering"
    resource: "Database Reliability Engineering (Laine Campbell, Charity Majors), ch. 3"
---

Group settings distort risk decisions in three specific,
nameable ways, beyond generic groupthink:

- **Group polarization** (the "risky shift"): group
  discussion pushes the eventual consensus toward a more
  extreme position than the average of what individual
  members held going in — not toward the middle. A group can
  end up more risk-tolerant, or more risk-averse, than any one
  person in the room actually believed on their own.
- **Risk transfer**: a team accepts more risk than it would
  in isolation when it can offload the consequences onto
  another team — the decision-makers and the consequence-bearers
  are not the same people, so the group underweights the risk
  relative to what a team that would itself bear the fallout
  would choose.
- **Decision transfer**: a team overestimates a risk
  specifically to justify escalating the decision upward,
  avoiding ownership of the call rather than making it —
  inflating the stated risk is a way of routing around
  accountability, not a genuine assessment.

All three distort the group's stated risk assessment away
from what an accountable individual would conclude, in
opposite directions (polarization can push either way; risk
transfer pushes toward more risk-taking; decision transfer
pushes toward more risk-aversion, or at least toward avoiding
the decision). Naming which one is in play is itself useful
diagnostic information when a group's risk call feels off:
ask whether the people deciding are also the people who will
bear the consequences (risk transfer), whether the stated
risk level is being used to justify passing the decision
elsewhere (decision transfer), or whether the group's position
has drifted further from the median individual view than the
discussion actually warranted (polarization).

This complements
[consensus-driven-paralysis](consensus-driven-paralysis.md)
(mutually exclusive options producing no decision at all) with
the opposite failure: a group reaching a confident consensus
that is systematically distorted rather than genuinely
representative of its members' judgment.

Before diagnosing polarization or transfer, rule out the simpler
explanation that the "group" position was never really a group
position at all — see
[decision-influence-concentration](decision-influence-concentration.md)
for measuring whether one voice quietly dominated the call.
