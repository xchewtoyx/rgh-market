---
type: concept
title: Business-Goal-Driven Requirements
description: >
  Some architectural decisions trace to a business goal with no
  quality-attribute requirement in between at all, so eliciting business
  goals explicitly — not just quality scenarios — catches requirements a
  stakeholder workshop focused on quality attributes would miss.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 19"
---

A business goal can drive an architectural decision through three
different paths, and only one of them is visible to elicitation that
starts from quality attributes: it can drive a quality-attribute
requirement (a market-differentiation goal driving an unusually fast
response-time target — knowing the underlying goal also lets the
architect meaningfully push back on or justify how stringent that target
should be); it can drive an architectural decision **directly, with no
quality-attribute requirement in between** (a manager insisting on
including a particular database not for any technical reason but to keep
an existing team employed — no requirements document will ever capture
this, yet omitting it is exactly as much a failure from that
stakeholder's perspective as missing a real functional or quality
requirement); or it can have no architectural relevance at all (a
cost-reduction goal met by lowering office thermostats). Architects often
absorb the first and last kind by osmosis; the middle kind is the one
routinely missed, because nothing about it looks like a testable
requirement.

**PALM** is a workshop method for surfacing this middle kind
systematically, run with the architect and key business stakeholders in
two steps: first, elicit business goals using a prompting checklist —
organizational growth and continuity, financial objectives, personal
objectives, responsibility to employees/society/the state/shareholders,
market position, business-process improvement, product quality and
reputation, and managing change in the environment — then express each
goal as a structured scenario, consolidate near-duplicates, and
prioritize, the same discipline a [quality attribute
scenario](quality-attribute-scenario.md) applies to a quality requirement.
Second, for each important goal scenario, participants propose a
candidate quality attribute and a response-measure value that would help
achieve it, feeding directly into an [architecturally significant
requirement](architecturally-significant-requirement.md) set.

The checklist's value is the same as any [checklist used against
taxonomy](quality-attribute-checklist-vs-catalog.md): it prompts a
question a stakeholder might not think to volunteer unprompted, not a
classification to argue over. See [quality attribute
workshop](quality-attribute-workshop.md) for the parallel method that
starts from stakeholder-proposed quality scenarios directly rather than
from business goals.
