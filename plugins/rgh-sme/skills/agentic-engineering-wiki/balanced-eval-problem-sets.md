---
type: concept
title: Balanced Eval Problem Sets
description: >
  Test both cases where a behavior should occur and cases where it shouldn't
  — a one-sided eval only rewards one-sided optimization.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), Going from zero to one: a roadmap to great evals for agents"
---

An eval suite that only checks whether a behavior fires when it *should*
gives a harness change nowhere to fail except by under-triggering — so
optimizing against it can only ever push toward triggering the behavior
*more*, since there's no case in the suite that would catch it firing too
often. The result is a class-imbalanced eval producing exactly the one-sided
optimization its imbalance invites: an agent tuned only against
"does it search when it should" evals can end up searching for nearly
everything, because nothing in the suite ever penalized an unnecessary
search.

The fix is building both directions into the same suite deliberately:
positive cases where the behavior is the right call, and negative cases
where withholding it is the right call. Concretely, for a model deciding
whether to invoke a search tool: pair queries that genuinely need a search
("what's the weather") with queries the model should answer from its own
knowledge without one ("who founded Apple?"). Balancing under-triggering
against over-triggering this way typically takes several rounds of
refinement to both the prompt and the eval itself, and the negative side of
the set is exactly as important to keep growing as the positive side — new
example problems continue to be added on both sides to improve coverage as
edge cases surface.

This generalizes past tool-triggering to any harness decision with a "do it"
and a "don't do it" branch — [human approval gate](human-approval-gates.md)
escalation, [intent classification for routing](intent-classification-for-routing.md),
or any binary policy an agent applies per turn. Wherever a
[grader](agent-grader-types.md) checks a should-fire behavior, ask whether
the same suite also contains a should-not-fire counterpart before trusting
that a high pass rate reflects good judgment rather than a policy that
always says yes.
