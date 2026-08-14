---
type: concept
title: Eval-Driven Development
description: >
  Define evaluation criteria before building (or before a capability exists),
  so shipped features stay measurable and future-model bets become trackable
  instead of wishful.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), Going from zero to one: a roadmap to great evals for agents"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 4"
---

An application that is deployed but can't be evaluated is worse than one
never deployed — it costs to maintain and costs even more to take down.
**Eval-driven development** is the TDD analogue for foundation-model systems:
write the evaluation contract *before* (or as) you build, rather than
shipping first and hoping usage metrics somehow reveal quality later.
Enterprise AI features that survive in production tend to be the ones with
clear criteria already — recommenders (engagement/purchase-through), fraud
detection (money saved), coding (functional correctness), close-ended
classification — while game-changing but hard-to-evaluate applications get
under-invested in because teams cannot tell whether they work. Reliable
evaluation pipelines are therefore the bottleneck that unlocks new
applications, not a late polish step.

Structure that early contract with
[application evaluation criteria](application-evaluation-criteria.md) (domain,
generation, instruction-following, cost/latency) and implement it as
[offline prompt evaluation](offline-prompt-evaluation.md) /
[offline evaluation proxies](offline-evaluation-proxies.md) the harness can
re-run on every prompt, model, or loop change. Prefer measurable oracles
where they exist ([functional testing eval](functional-testing-eval.md),
[gold-standard matching](gold-standard-matching.md)), and treat open-ended
judges as calibrated proxies under
[agent grader types](agent-grader-types.md) — not as a reason to skip the
contract.

A specialized form of the same discipline is the *capability bet*: write a
[capability eval](capability-vs-regression-evals.md) for a feature the
current model can't reliably clear yet, ship the feature "well enough"
today as a wager on near-future models, and let the suite reveal when the
bet pays off. A low starting pass rate is expected and informative, not a
sign the eval is broken. Every time a new model version ships, rerunning
the same suite quickly shows which bets landed — a jump confirms the
capability arrived; a flat suite says the bet hasn't, without a human
re-reviewing the feature by hand.

This is the harness-maintenance discipline that pairs with
[harness drift awareness](harness-drift-awareness.md)'s point that silent
model swaps change behavior without a code diff: eval-driven development
turns that otherwise-silent change into a specific, anticipated, and
measured event for the exact capabilities the product is waiting on. It also
supplies the natural pipeline that keeps
[eval saturation](eval-saturation.md) from leaving a gap: as one capability
eval's pass rate climbs and it graduates into the regression suite, the next
eval-driven bet is already in place to take over as the thing being climbed
toward.
