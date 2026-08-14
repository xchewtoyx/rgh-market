---
type: concept
title: "Code Smell: Mutable Data"
description: >
  Unexpected updates to shared data from elsewhere in a system cause
  hard-to-spot, condition-dependent bugs — the core motivation behind
  functional programming's immutable-update discipline, with mitigations
  available even outside a functional language.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

Unexpected updates to data from elsewhere in a system produce hard-to-spot,
condition-dependent bugs. Even without a functional language's enforced
immutability, several mitigations apply:
[Encapsulate Variable](encapsulate-variable.md) funnels updates through
narrow, monitorable functions; [Split Variable](split-variable.md) separates
a variable that's been repurposed for two different things;
[Slide Statements](slide-statements.md) plus
[Extract Function](extract-function.md) separate side-effect-free code from
code that performs updates; [Command/Query Separation](command-query-separation.md)
in an API keeps callers from being forced into side effects just to read a
value; and [Remove Setting Method](remove-setting-method.md) eliminates a
setter as early as possible — looking for a setter's remaining clients
often itself reveals scope-reduction opportunities. Derived or calculable mutable data is
especially bad, since it can drift out of sync with what it's derived from;
the cure is [Replace Derived Variable with Query](replace-derived-variable-with-query.md).
As mutable-data scope grows, [Combine Functions into
Class](combine-functions-into-class.md) or [Combine Functions into
Transform](combine-functions-into-transform.md) limit how much code can
touch it; for structured data specifically, prefer replacing the whole
structure over in-place mutation
([Change Reference to Value](change-reference-value.md)).

The first move for [global data](global-state-opacity.md) specifically is
always Encapsulate Variable, since global mutable data combines this smell
with the opacity problem of not being able to trace who touched it from
anywhere in the call graph.
