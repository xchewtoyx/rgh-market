---
type: concept
title: The Organizational Stress-Strain Model
description: >
  Woods and Wreathall's analogy from ductile-metal mechanics — an
  organisation absorbs and recovers from stress up to a yield point, beyond
  which cognitive overload produces spiking errors and permanent
  (non-recoverable) capability loss, not just slower recovery.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 7"
---

Woods and Wreathall (2008) model an organisation's response to operational
stress on the stress-strain curve of a ductile metal, giving [buffering
capacity, margin, and tolerance](buffering-margin-and-tolerance.md) a
specific mechanical shape rather than leaving "tolerance" abstract:

- **Elastic region**: up to a threshold (the **yield point**), the
  organisation absorbs added workload or stress and returns fully to
  baseline performance once the load is removed — the deformation is
  temporary, exactly like a metal spring flexing and springing back.
- **Plastic deformation and fracture**: past the yield point, cognitive load
  exceeds what the people carrying it can sustain. Mental functioning
  degrades, error rates spike, and individuals lose coping capability —
  and, matching the metal analogy exactly, this deformation does *not*
  reverse itself when the load is later removed. A workforce that has
  yielded does not simply bounce back to baseline once the outage or crisis
  ends; some capability is permanently spent.

This gives [tolerance](buffering-margin-and-tolerance.md) a sharp,
falsifiable prediction the abstract version does not: below the yield point,
degradation as load rises should be gradual and recoverable; at and past it,
degradation should be sudden, non-linear, and the recovery incomplete even
after the load is removed. The practical imperative this creates for a
highly resilient organisation is not to keep everyone permanently inside the
elastic region regardless of cost — real operations routinely need to run
people near their limits — but to actively **detect when workers are
approaching their yield point** and execute an adaptive intervention (adding
capacity, removing stressors, or removing load) before the crossing happens,
because the option to simply undo the damage once crossed does not exist the
way it does inside the elastic region. See [pinging](pinging-proactive-risk-probing.md)
for one concrete mechanism used to detect the approach to that point before
it is crossed.
