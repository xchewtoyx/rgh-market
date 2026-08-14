---
type: concept
title: Swiss Cheese (Barrier) Model
description: >
  Reason's model of accidents as a hazard trajectory passing through holes in
  layered defences, distinguishing sharp-end active failures from dormant
  latent conditions — useful, but with known limitations.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Dekker), ch. 5"
---

James Reason's barrier model (1990) pictures an organisation as a stack of
defensive layers, each with holes; an accident is a hazard trajectory that
finds aligned holes through every layer. Its key contribution over the
[chain-of-events model](chain-of-events-model.md) is the distinction between:

- **Active failures** — unsafe acts committed by operators at the [sharp
  end](sharp-end-and-blunt-end.md), close in time and space to the outcome.
- **Latent conditions** — dormant vulnerabilities embedded long before by the
  blunt end: design choices, policy, staffing, maintenance, procurement.

Bhopal (1984) is the archetype: escaping MIC gas killed thousands because
latent failures were stacked — uncalibrated gauges, untrained staff, disabled
refrigeration, undersized scrubbers, a disconnected flare tower. No single
sharp-end act explains it.

The model moved attention from the frontline to the organisation, but it has
three known limitations:

1. **It re-invokes human error**: a sharp-end "unsafe act" is still typically
   cast as the necessary final trigger, so the operator remains the last hole.
2. **Unbounded pathogen search**: with no stopping criteria, everything can be
   labelled a latent pathogen (one ATC study catalogued over 837), which turns
   investigation into inventory rather than explanation.
3. **The fallacy of social redundancy**: layers made of people do not stack
   independently — see [social redundancy fallacy](social-redundancy-fallacy.md).

Because the layers are analysed one by one, the model also struggles with
accidents that emerge from *interactions* between intact components — the gap
filled by the [systems-theoretic accident
model](systems-theoretic-accident-model.md). Adding new layers to plug holes
is also not a free improvement: each new layer is a new component with new
relationships to the rest of the system, so the barrier strategy can [increase
overall complexity risk](redundancy-can-increase-complexity-risk.md) even as
it makes each individual layer more robust — one root of the model's
unbounded-pathogen-search limitation above. The model's framing of risk as
hazardous energy to be contained behind layers is itself inherited from
[Newtonian-Cartesian accident
thinking](newtonian-cartesian-accident-thinking.md).

Because latent conditions are the only half of this picture that is
predictable and controllable *before* an event, they are also the direct
target of proactive auditing methods such as [Tripod's basic risk
factors](tripod-basic-risk-factors.md).
