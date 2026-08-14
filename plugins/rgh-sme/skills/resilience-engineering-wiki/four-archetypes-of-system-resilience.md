---
type: concept
title: Amalberti's Four Archetypes of System Resilience
description: >
  Human activities settle into one of four governance archetypes — each with
  its own primary safety tool and its own diminishing-returns limit — so the
  safety tool that works for one archetype does nothing, or actively harms,
  in another.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 16"
---

Amalberti classifies activities into four archetypes by how risk is
governed, not by how dangerous the activity happens to be — each archetype
defaults to a different primary safety tool, and each tool has a point past
which adding more of it stops helping:

1. **Ultra-performing systems** — extreme sports, audacious surgical
   grafts. Centred on maximum individual or small-team performance; the
   absolute number of fatalities is small and failure is accepted as
   inherent to peak performance. Safety is an *individual* concern, governed
   by a winner/loser logic where failure is attributed to the individual's
   own performance rather than the system around them. No dominant safety
   tool applies at this stage — the archetype predates systematic tooling.
2. **Egoistic systems** — road driving, patient/doctor selection in private
   medicine: a governed market open to individual customers, combining
   global infrastructure governance with local operational anarchy. Risk
   decisions are localised to the individual user, and accidents read as
   isolated events (worker error, customer misfortune) that generate little
   systemic pressure for change. Primary tool: **standardisation** —
   competence (training), work (procedures), technology (ergonomics and
   guidelines).
3. **Systems of collective expectation** — public utilities and services
   (food supply, energy grids, postal services, banking): users do not
   choose an individual provider, and failures threaten public order and
   political leadership rather than just the individual affected. High
   public visibility forces active risk communication, formal safety
   bureaus, and public reporting to *demonstrate* safety commitment, often
   without altering core operations. Primary tool: **audit** — in-service
   reporting, sentinel-event tracking, morbidity/mortality conferences,
   Crew Resource Management, macro-ergonomics.
4. **Ultra-safe systems** — nuclear power, chemical manufacturing,
   commercial aviation: a single major accident is unacceptable and
   business-threatening. Ultimate safety authority shifts away from local
   operators to national or international regulators. Primary tool:
   **supervision** — mandatory traceability (black boxes, datalinks),
   automated process controls, strict error accountability, reduced
   operational autonomy for sharp-end workers.

**Each tool follows an inverted-U efficiency curve.** Standardisation
genuinely moves an egoistic-archetype system; pushed past its useful range
it produces the same [safety-clutter](safety-clutter.md) plateau [the
ultra-safe continuum](amalberti-safety-continuum.md) describes for rules.
Audit and supervision have their own thresholds past which the training or
compliance cost outweighs the operational return, at which point systems
resist further mandates rather than adopt them — the French *loi
Bachelot-Narquin*, passed after the 2001 AZF chemical-plant explosion,
mandated citizen consultation committees rather than the costlier plant
retrofits regulators initially sought, because the fireworks and chemical
sectors it targeted defended their economic viability by rejecting the more
expensive safety tool outright.

**The point is diagnostic, not just descriptive.** Forcing an archetype's
tool onto a system still operating a different archetype doesn't just fail
to help — it can destabilise the system it is meant to protect. **Concorde**
is the clean case: designed in the late 1960s as evolving civil-aviation
rules (speed limits below FL100, baggage-weight limits) accumulated around
it, full compliance would have grounded the fleet or made transatlantic
routes fuel-infeasible. Operators instead ran under **Borderline Tolerated
Conditions of Use** rather than either full compliance or ungoverned
non-compliance — see [borderline tolerated conditions of
use](borderline-tolerated-conditions-of-use.md) for how that differs from
ordinary [normalisation of deviance](normalization-of-deviance.md). The
same logic runs in reverse in the fireworks industry, whose safety
performance sits two orders of magnitude below the chemical industry it
otherwise resembles: reliance on manual crafting and continuous low-margin
chemical innovation means the industry actively resists the standardised
and audited tools that would apply to a more mature archetype, on the
explicit warning (voiced by industry representatives after AZF) that strict
enforcement would displace or destroy the industry rather than make it
safer within its current economics.
