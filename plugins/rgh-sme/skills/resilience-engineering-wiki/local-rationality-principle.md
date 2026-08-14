---
type: concept
title: The Local Rationality Principle
description: >
  What people did made sense to them at the time given their goals, attention,
  knowledge, and constraints — so the investigative question is why it made
  sense, not what they failed to do.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Dekker), ch. 1"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 19"
---

Grounded in cognitive science (Rasmussen, Woods, Cook): people do what makes
sense to them at the time, given their goals, attentional focus, knowledge,
and operational constraints — otherwise they would not be doing it. Nobody
comes to work to have an accident.

The principle forces an investigative shift. Replace the retrospective
question *"What did they fail to do? What should they have done?"* with the
internal question *"Why did it make sense for them to do what they did?"* The
first question compares behaviour against knowledge only the outcome
provides; the second reconstructs the world as the person actually had it.

Dekker's **tunnel metaphor** captures the required perspective: the operator
moves through a tunnel with a limited field of view and no knowledge of the
outcome. An investigation must reconstruct the situation *inside-out* — what
was visible, what mattered, what competed for attention at each moment —
rather than *outside-in*, where the investigator hovers above the tunnel with
the ending in hand. The outside-in position is precisely what produces
[hindsight bias](hindsight-bias.md).

The concrete conditions that make local rationality the right frame — time
pressure, ill-defined goals, missing information, a shifting situation — are
catalogued as [naturalistic decision-making
conditions](naturalistic-decision-making-conditions.md). The cognitive
mechanism experienced practitioners actually use under those conditions is
the [recognition-primed decision model](recognition-primed-decision-model.md):
recognising a situation as a familiar pattern, not comparing options.

Operators always act within a **discretionary space** — a zone where action
or inaction can only be judged in hindsight. The principle translates
directly into software operations; Etsy's Ian Malpass on the moment after
taking the site down: "we get this 'ice-water down the spine' feeling, and
likely the first thought through our head is, 'I suck and I have no idea
what I'm doing.' … The better question to focus on is, 'Why did it make
sense to me when I took that action?'"

Local rationality is what makes systemic accounts explanatory rather than
exculpatory: if a reasonable practitioner in that situation would have acted
similarly, the situation — the tools, tasks, [goal
conflicts](goal-conflicts-and-production-pressure.md), and training the
organisation supplied — is where the fix lives. It also explains why
[deviance normalises](normalization-of-deviance.md) without anyone choosing
risk, and why [drift](drift-into-failure.md) is invisible from inside: every
step passes the local-rationality test.

The same idea generalises from investigating one past action to designing
for future ones: [bounded rationality and role
perspective](bounded-rationality-and-role-perspective.md) argues that
anyone occupying a given position in a system will reason from that
position's characteristically restricted view, so replacing the person
without changing the position reliably reproduces the same behaviour.
