---
type: concept
title: Output Metrics vs. Outcome Metrics
description: >
  Common productivity metrics like lines of code, story-point velocity, and
  resource utilization measure local output and invite gaming; delivery
  performance should be measured with global, outcome-based metrics instead.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 2"
---

# Output Metrics vs. Outcome Metrics

Three common metrics fail as delivery-performance measures because they
optimize local output rather than the system's actual outcome:

- **Lines of code**: rewards code bloat; the best engineering solution to a
  problem often involves minimal or negative code change, which this metric
  penalizes.
- **Velocity (story points)**: relative and team-specific, so it can't be
  compared across teams. Using it as a management metric invites gaming —
  inflated estimates, hoarded work, refusal to help other teams — because
  anything that looks bad on a team's own velocity gets avoided regardless of
  whether it helps the organization.
- **Capacity utilization**: borrowed from manufacturing, where maximizing
  machine utilization makes sense. In a knowledge-work pipeline, queuing
  theory says the opposite: as utilization approaches 100%, lead time
  approaches infinity. High utilization eliminates the slack capacity a team
  needs to absorb unplanned work, handle incidents, or invest in process
  improvement — see
  [capacity utilization and lead time](capacity-utilization-antipattern.md).

The alternative is measuring global, outcome-based results — see
[the DORA four key metrics](dora-four-key-metrics.md) — which measure
whether the whole delivery system produced value, not whether any one team's
local numbers look good.

## Measuring in a low-trust environment

Any metric, output- or outcome-based, produces distorted numbers if measured
punitively. As Deming put it: "Whenever there is fear, you get the wrong
numbers." Metrics have to serve continuous improvement in a genuinely
generative, blameless learning culture — used as a top-down control lever,
they get gamed regardless of which metric was chosen.
