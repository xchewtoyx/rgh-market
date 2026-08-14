---
type: concept
title: Automation Maturity Spectrum
description: >
  Operational automation progresses through recognizable stages — manual
  operation, playbook scripts, internal automation services, and autonomous
  self-healing systems — each trading operator control for consistency and
  scale.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 7"
---

# Automation Maturity Spectrum

Operational work does not jump straight from manual toil to full autonomy. It
moves through stages, each one changing who (or what) is directly executing
the operation:

1. **No automation** — operations performed manually, one CLI command at a
   time, by a human who understands the full context of what they're doing.
   Even at this stage, writing the procedure down as a well-designed
   [checklist](checklist-design-principles.md) buys real reliability before
   any code is written.
2. **Playbook automation** — shell scripts or runbooks that wrap the same
   manual commands so they execute consistently and faster, but still
   triggered and supervised by a human for each run.
3. **Internal service automation** — a centralized service executes
   scheduled or triggered tasks on its own; humans define policy and
   [reusable platform frameworks](reusable-platforms-over-bespoke-scripts.md)
   rather than running each operation by hand.
4. **Autonomous systems** — the system observes its own state and adjusts it
   without a human in the loop for each decision, up to and including
   [intent-based automation](intent-based-automation.md) that computes
   operational decisions from a stated goal rather than a stated procedure.
   [Self-healing overload response](self-healing-overload-response.md) is a
   common, narrower example: a component that detects its own degradation
   and corrects for it without waiting for the higher-level service that
   coordinates the rest of stage 4.

Moving up this spectrum increases leverage and consistency, but each step
also increases the damage a single bug can do and how fast it can do it —
see [failure domain amplification](failure-domain-amplification.md). Systems
that reach stage 3 or 4 need [idempotency](idempotency-in-automation.md) and
explicit [safeguards against runaway automation](safeguards-against-runaway-automation.md)
that weren't strictly necessary at stage 1 or 2, because there is no longer a
human re-checking every step before it happens. Heavy reliance on the upper
stages also creates [automation bias](automation-bias.md): the humans who
would need to intervene when the automation misbehaves progressively lose
the skill to do so.

The direction of travel is also worth more than the specific rung reached:
[risk reduction through repetition](risk-reduction-through-repetition.md)
is why moving a procedure up even one stage is usually worth it even before
it's fully autonomous — a script run daily gets more real-world validation,
faster, than the same procedure run by hand once a quarter, regardless of
which stage it eventually lands on.
