---
type: concept
title: Checklist Design Principles
description: >
  A documented procedure only earns the reliability it promises if it is
  built to specific design rules — short, tested, and focused on the steps
  people actually forget — not just written down.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Gawande), ch. 6-7"
---

# Checklist Design Principles

Writing a procedure down is the first rung of the [automation maturity
spectrum](automation-maturity-spectrum.md), but a badly designed checklist
does not deliver the reliability that rung is supposed to buy — it gets
skipped, resented, or followed so mechanically that it stops catching the
failures it was built for. Design rules that separate a checklist that
gets used from one that doesn't:

- **Target killer items, not every step.** A checklist that tries to spell
  out the entire procedure turns human judgment off instead of
  reinforcing it. Keep it to the handful of steps that are easy to skip
  under pressure and expensive when skipped, and trust the operator's
  competence for the rest.
- **Stay within working memory — 5 to 9 items per pause point.** Beyond
  that, completion time creeps up, people start skipping items to save
  time, and the checklist itself becomes the thing under pressure to cut.
- **Choose DO-CONFIRM or READ-DO deliberately.** DO-CONFIRM — operators
  execute from memory, then pause to verify — preserves workflow speed for
  practiced operators. READ-DO — operators execute each step as it's read
  — suits procedures with rarely-practiced steps or high consequences for
  sequencing errors. Picking the wrong mode for the situation is why some
  checklists get treated as bureaucratic overhead rather than a tool.
- **Time-box the pause.** A verification pause that runs past roughly a
  minute stops feeling like a check and starts feeling like a delay,
  which is when people begin shortcutting it.
- **First drafts fail — test before deploying.** A checklist written by
  experts without frontline field testing routinely turns out ambiguous,
  wrongly scoped, or disruptive to the actual workflow once used for
  real. Iterating in the real operating environment (not just on paper)
  is what catches this before rollout.
- **Treat it as a living document.** A checklist that never changes has
  usually stopped being checked against how the work actually happens.
  Revise it as procedures, tooling, and failure modes change, rather than
  treating the first version as final.

These rules matter most exactly where a fleeting note or ad hoc runbook is
tempting to skip them: any operational procedure precise and repeatable
enough to hand to another engineer is also precise enough to become the
next rung up — a [playbook automation script](automation-maturity-spectrum.md).
A checklist that hasn't been through this design discipline will encode
its own ambiguity and skipped steps straight into that script.
