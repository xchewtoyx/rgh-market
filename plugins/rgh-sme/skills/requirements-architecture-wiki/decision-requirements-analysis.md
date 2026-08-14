---
type: concept
title: Decision Requirements Analysis
description: >
  For a system that exists to support a human making judgments under
  time pressure, eliciting the specific decisions the task demands — and
  the cues experts actually use to make them — surfaces interface
  requirements that "what should the system accomplish" never reaches.
sources:
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Gary Klein), ch. 7"
---

Conventional requirements elicitation for a decision-support system (a
dashboard, a monitoring console, a command-and-control display) typically
asks stakeholders what the system should *accomplish* — what data it
should show, what the screen should contain. That framing leaves the
designer to guess which of the displayed facts actually matter in the
moment and in what form, and the default response is to cram everything
potentially relevant onto the screen at equal visual weight.

**Decision requirements analysis** asks a different, prior question: what
are the specific, high-stakes judgments this task actually requires
someone to make, and what cues do the people who make them well actually
rely on? Eliciting this — through interviews structured around real past
incidents, not abstract task descriptions — surfaces requirements a
generic "what should it show" conversation misses entirely: which facts
are decision-relevant versus merely available, what implicit thresholds
or patterns an expert is watching for, and where the existing interface
buries or obscures the exact signal a decision hinges on.

The payoff is concrete, often small-looking interface changes with
outsized effect, because they target the specific perceptual bottleneck a
real decision depends on rather than improving the interface in general.
A worked example: redesigning a radar console so that the specific cues
experienced operators used to spot high-threat aircraft drove an
automatic visual highlight, rather than requiring the same identification
to be made manually from an undifferentiated display — a small, targeted
change traceable directly to one identified decision requirement.

This is the decision-focused counterpart to general [requirements
elicitation techniques](requirements-elicitation-techniques.md): where
those techniques surface what a system should do, decision requirements
analysis is specifically for systems whose job is to put the right
information in front of a person who then has to decide something,
narrowing "what to display" to "what does this specific judgment actually
need." A missing or poorly surfaced decision requirement is a
particularly consequential category of [architecturally significant
requirement](architecturally-significant-requirement.md), because the
system can pass every functional test and still fail the one judgment it
existed to support — the interface having technically presented the
needed fact without presenting it in a form usable under the time
pressure the decision actually occurs under.
