---
type: concept
title: External Annotations for Fragile Legacy Systems
description: Using annotations, sidecar files, or metadata registries to document a system without modifying it, for cases where touching the code directly is too risky.
sources:
  - title: "Living Documentation"
    resource: "Living Documentation (Martraire), ch. 4"
---

When code can't be made to express enough on its own, and it's too fragile or high-risk to change directly, documentation can still be attached to it externally: annotations, structured comments or tags, naming conventions, sidecar files, or a separate metadata registry. The goal is to make this augmentation intrinsic to the system and machine-accessible — something tooling can publish, verify, or search — rather than a static aside that only benefits a human reading it firsthand.

## When to Prefer This Over Modifying the Code

- **The system is too fragile to touch**: a legacy component with no tests, unclear ownership, or a history of breaking under small changes is exactly the case where invasive edits (even "just adding a comment") carry real risk. An external annotation, sidecar file, or registry entry can document it without touching the component itself.
- **Conventions can substitute for invasive change**: a naming or structural convention (e.g., a consistent suffix or file layout) can document intent across a legacy codebase without editing individual files — but only if the convention is itself documented somewhere discoverable and consistently checked, otherwise it just becomes another unwritten rule a newcomer has to rediscover.

## Failure Modes to Watch For

Conventions and external annotations both degrade in the same three ways if left unmanaged: **discoverability** (a newcomer has no way to find that the convention or registry exists at all), **drift** (the annotation stops matching what the code actually does, and nothing catches the mismatch), and **ambiguity** (the convention is inconsistently applied, so its meaning can't be trusted). Treat an external annotation scheme as a piece of infrastructure that itself needs a documented definition and an enforcement check — not a one-time fix.

This is a targeted alternative to touching the code, not a substitute for the safer alternative of designing the system to need less explanation in the first place — see [Reducing Documentation Need Through System Design](reducing-documentation-need-through-system-design.md). For migrating a legacy system toward better documentation coverage over time rather than all at once, see [Marginal Documentation Migration](marginal-documentation-migration.md). When the risk is specifically that a change might alter undocumented existing behavior, [characterization tests](characterization-tests-for-undocumented-behavior.md) pin that behavior down mechanically instead of describing it in prose. When the concern isn't tied to one fragile component but genuinely spans several modules with no natural home in any of them, see [Central File for Cross-Module Design Notes](central-file-for-cross-module-design-notes.md).
