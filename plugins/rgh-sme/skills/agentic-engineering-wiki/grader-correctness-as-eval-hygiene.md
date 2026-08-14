---
type: concept
title: Grader Correctness as Eval Hygiene
description: >
  A low agent score can mean the grader is broken, not the agent — check the
  grader before concluding capability is lacking, and design it so passing
  requires actually solving the task rather than exploiting a loophole.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), Going from zero to one: a roadmap to great evals for agents"
---

A surprisingly low score is not automatically evidence of a capability gap —
it can just as easily be evidence the grader itself is broken, and sophisticated
teams miss this regularly. **Reading transcripts is the primary way to find
out which**: a suspicious score is a *starting point*, but the underlying
practice is reading transcripts and grades across many trials routinely, not
only when a result looks wrong — it's how you build confidence that a flat
or falling score reflects agent performance and not the eval, and it
regularly surfaces eval problems that wouldn't otherwise look suspicious from
the aggregate score alone. Invest in tooling that makes transcripts easy to
browse; a failure should be legible enough, on reading, that it's clear what
the agent got wrong and why — a failure that doesn't explain itself on
inspection is itself a signal to look harder at the grader before trusting
the score. Concrete failure shapes worth actively checking for before
trusting a low score:

- **Overly rigid matching.** A grader expecting the exact string `"96.124991…"`
  and rejecting `"96.12"` as wrong penalizes correct-to-the-precision-that-
  matters answers for not matching an arbitrary level of decimal precision.
- **Ambiguous task specs.** A task description underspecified enough that
  multiple reasonable readings exist, graded against only one of them. A
  practical authoring test: would two domain experts, working independently,
  reach the same pass/fail verdict on a given attempt? Could they pass the
  task themselves, given only the description a grader sees? If either
  answer is no, the spec needs tightening before it's trustworthy — and the
  same test applies to a model-based grader's rubric, since a vague rubric
  produces inconsistent judgments the same way a vague task description
  does. A specific way underspecification bites: a task that asks for a
  script without naming a filepath while the grading tests assume one
  particular path fails an agent that read and followed the instructions
  correctly — everything the grader checks needs to be stated in the task,
  not left implicit.
- **Stochastic tasks with no reproducible target.** A task whose "correct"
  outcome depends on randomness the grader didn't pin down, so the same good
  solution can score differently on different runs.
- **Inverted or misconfigured thresholds.** A grader that checks for
  "optimize to below X" when the task actually asked to optimize to
  *above* X — or any threshold direction that silently disagrees with the
  stated task — penalizes agents that correctly followed the stated
  instructions and rewards agents that ignored them.

**A reference solution is the cheapest proof a task/grader pair is even
valid.** Before trusting any score from a task, produce one known-working
output that passes every grader attached to it — this both proves the task
is solvable as specified and verifies the graders are wired up correctly,
catching the rigid-matching and inverted-threshold bugs above before a real
agent ever runs against the task. A related diagnostic, specific to
frontier models: a task that scores **0% across many trials** (see
[pass@k](pass-at-k-and-pass-hat-k.md) at k=100) is, more often than not,
evidence of a broken task or grader rather than a genuinely incapable agent —
a strong prior worth checking before accepting the zero at face value.

One documented case: a coding-agent eval scored 42% until an engineer found
several of these bugs stacked together (rigid numeric matching, ambiguous
specs, irreproducible stochastic tasks); after fixing the grader and loosening
an over-constrained scaffold, the same agent scored 95% on the same
underlying task. A benchmark's own task configuration can carry the same class
of bug — a time-horizon eval was found asking agents to optimize toward a
stated threshold while the actual grading silently required *exceeding* that
threshold, penalizing models for following the instructions as given.
Carefully double-checking both tasks and graders, especially after an
unexpectedly low or a suspiciously easy result, catches these before they're
mistaken for a real capability finding.

**A low score can also mean the agent outperformed the eval's imagination,
not the grader's implementation.** Distinct from a grader bug: a frontier
model can find a genuinely better solution than any the task designer
anticipated, one that falls outside the static eval's checked solution
space entirely. One documented case had Opus 4.5 solve a flight-booking
benchmark task by discovering a loophole in the stated policy — the eval
scored it a failure, but the agent's solution was arguably better for the
end user than any path the eval was written to recognize. The fix isn't
"more bypass resistance" (the solution wasn't gaming the check, it was
legitimately outside it) — it's periodically reviewing failing trials for
this shape before writing them off as capability gaps.

**Bypass resistance is the complementary design requirement, not a separate
concern.** A grader that would pass a shortcut solution not because the
shortcut solves the task, but because the shortcut satisfies the letter of
the check, has the same practical effect as a rigid or miscalibrated grader —
it makes the score stop measuring what it claims to measure. Design tasks and
graders so that passing genuinely requires solving the underlying problem,
the same discipline
[eval observation anti-leakage](eval-observation-anti-leakage.md) and
[eval environment isolation](eval-environment-isolation.md) apply to the
task's inputs and environment, applied here to the grading logic itself.
