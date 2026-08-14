---
type: concept
title: Effect Propagation Analysis for Verification Scope
description: Tracing every path by which a change's effects can become observable, so verification neither misses silently-affected areas nor wastes effort on unaffected ones.
sources:
  - title: "Working Effectively with Legacy Code"
    resource: "Working Effectively with Legacy Code (Michael C. Feathers), ch. 11"
---

# Effect Propagation Analysis for Verification Scope

Checking only the thing you directly changed is not enough evidence that a change is safe: a change can silently affect behavior somewhere else entirely, and unless something is checked there too, that effect goes unverified. **Effect propagation analysis** is the discipline of tracing forward from a change point through every mechanism by which its effects could become observable, to determine the actual — often larger, sometimes smaller — surface that verification needs to cover.

## The three propagation mechanisms to trace

1. **Return values used by a caller** — the most visible path, and the one reviewers check by habit.
2. **Mutation of an object passed by reference**, later read by other code holding the same reference — easy to miss because nothing in a mutating call's own signature or return value announces that this happened.
3. **Mutation of global or shared state**, read by code with no visible connection to the change at all — the least visible path, since it leaves no trace in either the changed function's signature or its caller's code.

Trace recursively: once you know what a change modifies, ask what reads that modified state, and what reads *that* in turn, until you reach the actual externally observable endpoints (a return value a real caller uses, a display, a persisted record). Those endpoints are candidate places to verify from — see [verification checkpoint proximity](verification-checkpoint-proximity.md) for how to choose among them once the graph is known.

## Where to stop tracing

Tracing should terminate at a genuine boundary: private state with no external accessor, or a value with a type/immutability guarantee that forecloses further mutation. But treat apparent boundaries with suspicion until confirmed — a guarantee that looks absolute in the language's syntax (a `const`-qualified parameter, a `final` field, package-private visibility) can be locally circumvented (a class marking a field `mutable`, a subclass in the same package, reflection) and no longer actually blocks propagation. A boundary is only load-bearing once you've checked it holds in this specific case, not because the keyword is present.

## Why this differs from prioritizing which claims to check

[Claim verification triage](claim-verification-triage.md) is about the order and priority of checking claims you've already identified. Effect propagation analysis is about discovering which claims exist to check in the first place — it expands or contracts the verification surface before triage ever runs. Skipping this step produces a verification plan that looks complete (every identified claim gets checked) while silently missing effects that were never identified as needing verification at all.

## A design signal, not just a testing one

A change whose effects fan out through many independent paths to many endpoints is inherently harder to verify completely than one whose effects converge on a single path. Discovering a wide, tangled propagation surface during this analysis is itself evidence that the surrounding structure would benefit from consolidation — not only a testing inconvenience to work around.
