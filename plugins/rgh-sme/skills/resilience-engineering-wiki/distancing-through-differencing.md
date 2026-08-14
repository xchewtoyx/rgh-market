---
type: concept
title: Distancing Through Differencing
description: >
  Reviewers discount a precursor incident's relevance by fixating on
  surface-level differences from their own context — location, personnel,
  equipment version — concluding "it couldn't happen here" while missing
  the deeper structural pattern the two events actually share.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 20"
---

Distancing through differencing is a cognitive and social discounting
process: confronted with a precursor incident, reviewers focus on how it
differs — real or imagined — from their own location, personnel,
organisation, or circumstances, and conclude the event "couldn't happen
here." Every incident is genuinely unique at the surface level, but this
mechanism mistakes surface uniqueness for the absence of a shared deeper
pattern, so the organisation extracts no lesson and rejects any systemic
change the precursor might have justified.

**Cross-site case**: a clean-room fire at an overseas plant, on the same
machine model later involved in a local fire months afterward, was
dismissed by safety managers as irrelevant because of the foreign location,
minor machine-version differences, and a different fire-suppression setup.
Workers and management attributed the overseas failure to national
stereotypes ("they weren't as careful") rather than extracting the
systemic hazard both events actually shared. Speeding up formal reporting
of the precursor did not help — the discounting happened after the report
arrived, not because it arrived too slowly, so faster dissemination alone
cannot fix a mechanism that operates on interpretation, not on latency.

**Within-plant case**: after the local fire, workers on *other shifts at the
same plant* discounted it the same way — attributing the event to the
involved workers being less careful, even though objective evidence showed
those workers were among the plant's most skilled. The differencing move
functions as a psychological defence (distancing the reviewer's own
vulnerability) as much as a factual appraisal, which is why it survives
contact with evidence that directly contradicts it.

The mirror-image bias is [false analogue
transfer](false-analogue-transfer.md): where distancing wrongly discounts a
genuinely relevant precursor because of a surface difference, false-analogue
transfer wrongly imports a precedent's track record because of a surface
similarity. Both errors come from judging relevance by surface features
instead of by the causally relevant dimension underneath them — one just
runs in the direction of dismissing a warning rather than trusting a false
reassurance.

**Countermeasure**: organisations must explicitly prohibit discarding a
precursor event on surface-difference grounds alone, and instead train
review to abstract from concrete details to the systemic contributors
underneath. Two examples of doing this well: a manager who noticed a
delivery-system safety rule (isolating chemicals in tanks and valves before
maintenance) and asked whether the same abstract principle should extend
into the process machinery itself, rather than treating it as specific to
delivery hardware; an engineer who used one instance of a missing machine
label as the occasion for a plant-wide labelling audit, rather than fixing
only the one label found. In both cases the move is the same: treat the
specific finding as an instance of a general pattern and ask where else the
pattern applies, instead of treating it as fully resolved once the specific
instance is fixed.
