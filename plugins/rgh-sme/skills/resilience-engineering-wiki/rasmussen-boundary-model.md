---
type: concept
title: Rasmussen's Three-Boundary Model
description: >
  Every operation is squeezed between an economic boundary, a workload
  boundary, and a safety boundary, and management/competitive pressure
  systematically pushes it toward the latter two.
sources:
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Dekker), ch. 2"
  - title: Observability Engineering
    resource: "Observability Engineering, 2nd ed. (Majors, Fong-Jones, Miranda), ch. 22"
---

Jens Rasmussen modelled a complex operation as manoeuvring inside a space
bounded by three edges:

- **Economic boundary**: beyond which the operation can no longer sustain
  itself financially.
- **Workload boundary**: beyond which people or technology can no longer
  perform the required tasks.
- **Safety boundary**: beyond which the system functionally fails.

Competitive and cost pressure gives management no way out of this space
except manoeuvring within it — and the pressure is asymmetric: it pushes
continuously toward the workload and safety boundaries while pulling away
from the economic one, because economic failure is immediate and legible
while workload and safety erosion are gradual and only visible after the
fact. An organisation squeezed by [scarcity and
competition](goal-conflicts-and-production-pressure.md) does not choose to
approach the safety boundary; it drifts there as the only remaining slack in
the system gets consumed.

The boundary is not directly observable while operating inside it — there is
no alarm at the edge, only a trend. This is why [drift into
failure](drift-into-failure.md) is best understood as *migration toward* a
boundary rather than a single crossing: an internal oversight-capacity memo
can warn explicitly that "diminished surveillance is imminent" and the
warning can still not stop the eventual failure, because the warning itself
is just one more data point being interpreted through the same [local
rationality](local-rationality-principle.md) that is producing the
migration. [Feedback delay](feedback-delay-masks-accumulating-risk.md) is
part of the structural reason the boundary stays invisible for so long: the
gap between an approach and its consequence is exactly what keeps a trend
from registering as a trend.

The model generalises past aviation and process industries to any
sociotechnical system under sustained delivery pressure, including software
organisations. One AI customer-service product found itself drifting toward
all three edges simultaneously and invisibly: added model capability was
purchased with creeping response latency (toward the boundary of acceptable
performance), an unmonitored cost leak in a speculative-execution
optimisation went undetected because it happened to fire on interactions with
no user-facing telemetry at all (toward the economic boundary), and dozens of
uncoordinated daily changes across many teams accumulated risk no individual
team could see (toward the workload boundary). The team's diagnosis of its
own near-miss was explicit: the boundaries are invisible by default, and an
organisation's monitoring is only as good as its ability to make each
boundary legible in real time through a dedicated signal — a customer-facing
latency metric and a per-interaction cost metric, in this case — rather than
inferring proximity to the edge only after crossing it.
