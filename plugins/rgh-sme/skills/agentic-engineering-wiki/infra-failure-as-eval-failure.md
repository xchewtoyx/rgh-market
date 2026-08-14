---
type: concept
title: Count Infrastructure Failures As Task Failures
description: >
  When computing an eval's pass rate, score a trial that dies on an
  infrastructure exception as a failure rather than discarding it, so the
  metric can't be inflated by silently dropping hard trials.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), App. A"
---

A rollout can fail two different ways: the agent genuinely fails the task, or
the surrounding infrastructure fails it first — a sandbox crash, an API
timeout, some fault that has nothing to do with the agent's competence. The
tempting convention is to discard the second kind and compute
[pass@1](pass-at-k-and-pass-hat-k.md) only over trials that ran to
completion. That convention is a hidden metric-inflation risk: harder tasks
are disproportionately likely to hit timeouts and resource exhaustion, so
discarding infra failures selectively removes the trials most likely to have
failed anyway, quietly raising the reported pass rate.

The harsher, more defensible convention: count every infrastructure exception
as a failed trial (reward 0) in the numerator and denominator of the pass
rate, exactly like a genuine task failure. This keeps the metric comparable
across runs and across leaderboards that use the same convention, and it
removes any incentive — deliberate or accidental — to make a configuration
*look* more reliable by making its failures crash instead of complete.
Token-cost figures are a legitimate exception to this rule: excluding
infra-aborted trials from a mean-tokens-per-trial figure (used in
[Succ/Mtok](successes-per-million-tokens.md)) is fine, since a truncated
trial's token count doesn't represent what a completed trial actually costs
— the harsher-counting rule applies to the success/failure tally, not to
every downstream statistic computed from completed trials.
