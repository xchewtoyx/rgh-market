---
type: concept
title: Plan Continuation Bias
description: The cognitive bias where operators continue with an original plan of action despite changing conditions that suggest the plan is no longer viable.
sources:
  - title: "The Field Guide to Understanding 'Human Error'"
    resource: "The Field Guide to Understanding 'Human Error' (Sidney Dekker), ch. 4"
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Gary Klein), ch. 5-6"
---

**Plan Continuation Bias** occurs when practitioners stick to an initial operational plan in the face of deteriorating conditions. Rather than assessing options side-by-side, operator cognition is focused on continuous *situation assessment*—asking "is this still doable?" 

This bias is driven by **cue asymmetry**:
* **Early Cues**: Highly visible, strong, and unambiguous signals that support the initial plan.
* **Later Cues**: Weak, ambiguous, and arriving incrementally. As a result, they struggle to dislodge the established momentum of the plan.

Under this bias, operators interpret rules not as rigid boundaries, but as negotiable parameters. Telling operators to simply "follow the rules" is ineffective because they assess continued viability in real time based on their [local rationality principle](local-rationality-principle.md). Addressing this bias requires systemic safeguards, such as non-punitive, positive incentives to abort operations (e.g., "no-questions-asked" go-around rewards).

### The garden path fallacy and snap-back

The same cue-asymmetry mechanism explains why a responder's running
interpretation of an incident — not just a plan of action — can drift far
from correct without anyone noticing. Because [mental
simulation](mental-simulation-as-evaluation-tool.md) is flexible, it can
explain away almost any single piece of disconfirming evidence: a
denial gets read as suspicious, an inconsistency gets attributed to a
data error, a contradiction gets folded into an ever more complicated
version of the original theory. Each individual explaining-away step is
often reasonable on its own — evidence genuinely is unreliable sometimes —
which is exactly what makes the pattern dangerous: a series of
individually-sensible steps can cumulatively stray far from the correct
interpretation with no single step feeling like a red flag. This is the
**garden path fallacy** (Marvin Cohen).

The self-correction mechanism is **snap-back**: once the pile of
explained-away evidence gets large enough, the accumulated strain
collapses confidence in the running theory all at once, prompting a
re-examination of everything previously dismissed. The catch is that
snap-back is unreliable exactly when it matters most — the "usual alarms"
(the early, strong, unambiguous cues this note describes) have often
already fired and been satisfied long before the weak disconfirming
evidence has piled up enough to trigger a snap-back. A real-world case
where this ran the other way — two ships' captains each reading the
other's evasive maneuver as a temporary, self-correcting error rather than
a genuine change in intent, until they collided — shows the same mechanism
in a live coordination failure, not just a solo misjudgment. Structurally,
the fix is the same one used against ordinary plan-continuation bias: don't
rely on a threshold that has to build up unassisted, build in an explicit,
scheduled prompt (a periodic [CAN report](can-report.md) or status check)
that forces a fresh look at the running interpretation before the
explained-away pile gets too large to question.
