---
type: concept
title: Probabilistic Confidence in Recommendations
description: >
  State a recommendation's confidence as a number or range
  instead of a flat assertion, so updating it later feels like
  new information rather than admitting to having been wrong.
sources:
  - title: "Thinking in Bets: Making Smarter Decisions When You Don't Have All the Facts"
    resource: "Thinking in Bets (Annie Duke), ch. 2"
---

A flat assertion ("this vendor will meet our SLA") and a
probabilistic one ("I'm about 70% confident this vendor will meet
our SLA") can be based on identical underlying evidence, but they
behave completely differently once new information arrives or the
minority outcome occurs. A prediction that was never claimed to be
certain cannot be "wrong" just because the less likely branch came
in — a sincerely-estimated 30% risk that materializes is not a
forecasting failure, the way a favored election or referendum
forecast is not "wrong" when the underdog wins (see
[decision-quality-independent-of-outcome](decision-quality-independent-of-outcome.md)
for the same principle applied to grading the decision itself).

Stating confidence numerically, or as a range ("sometime between
Q2 and Q4," not "Q3"), earns four benefits a binary claim
does not:

- **Updating stops being ego-threatening.** Moving from "I was
  60% confident" to "I'm now 40% confident" is processing new
  information; moving from "I said this would work" to "I was
  wrong" is admitting failure — the second framing makes people
  cling to a stated position long after the evidence has turned
  against it, purely to avoid the all-or-nothing status hit.
- **It reads as more credible, not less.** A stated degree of
  uncertainty signals that the claim was actually weighed, where
  false certainty signals either overconfidence or an unexamined
  assumption.
- **It invites correction.** A stakeholder who hears "I'm not
  fully sure" is far more willing to volunteer the piece of
  information that would move the estimate than one who hears a
  confident, closed assertion — asking someone to contradict a flat
  claim carries social cost that asking them to help refine an
  already-uncertain one does not.
- **It protects the audience from over-absorbing an unvetted
  claim.** People tend to believe a stated claim by default and
  only sometimes get around to checking it — an explicit confidence
  level is a built-in prompt to check rather than simply accept.

This is a natural companion to
[hyperrationality](hyperrationality.md)'s caution against demanding
full analytical certainty before acting: expressing calibrated
confidence is how a recommendation stays actionable without
overclaiming precision it doesn't have, and it gives
[fair-treatment-of-objections](fair-treatment-of-objections.md) an
honest starting point — an objection to a 65%-confidence claim is a
request to help move a number, not a challenge to a fact.
