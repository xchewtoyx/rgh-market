---
type: concept
title: Invariant Assertion Placement
description: Stating an assumed invariant explicitly as a checkable assertion at the point it is established, not merely wherever it is relied upon.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring: Improving the Design of Existing Code (2nd ed.) (Martin Fowler), ch. 10, Simplifying Conditional Logic — Introduce Assertion"
---

# Invariant Assertion Placement

Systems routinely depend on conditions that are never stated anywhere — "this value is never negative," "at least one of these fields is populated" — leaving the assumption invisible until something violates it far from where the violation actually originated. An **assertion** makes such an assumption an explicit, checkable claim about program state: a condition asserted to always be true, whose failure signals that the assumption itself was wrong, not something the surrounding logic should have to handle.

## Where to place it

Place the assertion at the point the invariant is **established**, not at every point it is later relied upon. A value's non-negativity should be asserted where it is set, not re-checked at each of its many call sites — asserting only at points of use makes a violation surface far from its actual cause, turning a one-step trace into a hunt. Asserting at the point of origin means a violation is caught adjacent to whatever produced it.

## Two properties that distinguish an assertion from validation logic

- **Behavior neutrality**: a correct assertion must leave program behavior unchanged if deleted entirely — some runtimes can even compile assertions out, which is only safe if this holds. An assertion checks a claim; it must never be the mechanism that makes the claim true (e.g., clamping or defaulting a value is normalization, not assertion).
- **Scope discipline**: assertions are for claims that must hold by construction — internal invariants the surrounding code already guarantees, not data arriving from outside the system's control. Validating externally-sourced input is real program logic with real handling paths, not a candidate for an assertion; conflating the two either lets bad external data silently corrupt state (if wrongly asserted) or duplicates first-class validation as an afterthought (if wrongly treated as internal-only).

## Communication value independent of failure

An assertion's value does not stop at catching bugs — it also documents, in a form a reader cannot skim past, exactly what state the surrounding code assumes. This is why an assertion is often worth leaving in place even after the specific defect that prompted adding it is fixed: it keeps the assumption visible to whoever next changes the code nearby. This is the runtime, single-invariant analogue of [defining checkable claims](defining-checkable-claims.md) in a document — both convert an assumption that would otherwise stay implicit into something a later reader or a later execution can actually check.

## A related but separate technique

Placing an assertion once and trusting it is different from confirming a check can actually detect a violation — see [test oracle self-validation](test-oracle-self-validation.md) — and different again from running an assertion against real traffic before relying on the invariant it encodes, see [assumption verification via runtime instrumentation](assumption-verification-via-runtime-instrumentation.md).
