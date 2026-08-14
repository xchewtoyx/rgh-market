---
type: concept
title: Proxy-Validation Failure Pattern
description: >
  An agent closes a task on a self-invented or shallow check that resembles
  success — row counts, file existence, a help flag — instead of reproducing
  the actual evaluator's exact contract.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), App. C.1, C.2.3"
---

A cross-cutting failure family in long-horizon agent tasks: the agent reaches
a state that *feels* done and stops there, using a check it invented itself
rather than the one that will actually grade it. The check is plausible-looking
but structurally weaker than the real evaluator, so the task fails even though
the agent believed — and could point to evidence suggesting — it had
succeeded. A catalog of concrete shapes this takes:

1. **Shallow validation** — confirming a command runs (`--help`, `py_compile`,
   or existence-only checks) instead of exercising the actual feature the task
   requires.
2. **Localhost-only service validation** — checking a service responds on
   `localhost` when the task's real contract names an externally reachable
   endpoint; the two can diverge (binding to `127.0.0.1` instead of `0.0.0.0`
   passes the local check and fails the external one).
3. **Inline or self-written proxy validators** — computing an independent
   estimate or writing a custom checker instead of running the named
   evaluator, then trusting the proxy's agreement with itself as if it were
   agreement with ground truth.
4. **Raw/low-level API calls bypassing an official wrapper** — when a task
   names a specific tool or library as the required mechanism, calling a
   lower-level primitive that produces superficially similar output but skips
   behavior the wrapper is responsible for.
5. **No golden or threshold comparator** — running a benchmark or computation
   and treating "it produced a number" as passing, with no comparison against
   an expected value or tolerance.
6. **Repeated long timeouts on the same command shape**, and **repeated
   retries hitting the same error signature** — cross-step patterns invisible
   from any single step in isolation, only visible across the run's history.

Patterns 1, 3, and 5 are the same underlying mistake at different specificity:
mistaking "a check passed" for "the task's actual evaluator would pass." A
[publish-state protection guard](publish-state-protection-guard.md) stops the
agent from *destroying* verified state but does nothing if the state was never
correctly verified in the first place — these two guardrails are
complementary, not substitutes.

**Countermeasures at two component levels.** A prompt-level rule — "mirror the
evaluator before finishing: run an end-state acceptance sweep that asserts the
same fields the hidden verifier asserts, and trust a failing check over your
own theory of why it should be passing" — catches this when the agent is
willing to re-derive the real contract, but only if it remembers to apply the
rule. The patterns that depend on **cross-step history** (5 and 6 above)
cannot be caught by a static prompt rule at all, because no single step
reveals them — they need a middleware hook that accumulates state across the
whole run and only fires when the pattern actually appears in the live
command history; see
[next-turn salience promotion](next-turn-salience-promotion.md) for how to
make that middleware's warning land somewhere the agent actually acts on it,
rather than trailing after tool output where it gets ignored.
