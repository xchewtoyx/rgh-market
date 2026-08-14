---
type: concept
title: Central File for Cross-Module Design Notes
description: A single named file collecting explanations for concerns that span multiple modules with no natural single home, referenced by short pointer comments at every touch point.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (Ousterhout), ch. 13"
---

Some design decisions inherently span several modules with no single obvious anchor point — a distributed system's handling of a node the cluster believes is dead but that is actually still running touches every module that makes decisions based on liveness, and none of them is uniquely "the" place that concern belongs. Two default options both fail here: duplicating the explanation at every touch point is awkward and drifts out of sync as the system evolves, and parking the full explanation at just one touch site means developers working through any of the other sites have no reason to know it exists.

## The Pattern

Maintain one central file, organized into clearly labeled topic sections, each explaining one cross-cutting concern in full — what the hazard is, and how the system as a whole neutralizes it. Every piece of code that touches that concern carries only a short pointer comment back to the relevant section (e.g. "see 'Zombies' in designNotes") rather than repeating the explanation locally.

- **Best case first**: before reaching for a separate file, check whether a genuine anchor point already exists — a shared enum, a single required registration site, a schema definition — and attach the full explanation there instead. A central design-notes file is the fallback for when no such anchor exists at all, not the default choice.
- **Acknowledge the tradeoff explicitly**: a central file gives every reader one authoritative, non-duplicated place to look, but it is physically distant from the code that depends on it, which is exactly the condition under which documentation silently drifts out of sync as the system changes around it. This is worth pairing with the same [documentation maintenance workflows](documentation-maintenance-workflows.md) used for other stand-alone documentation, and the pointer comments themselves need occasional auditing to confirm they still point at a section that still exists and still matches reality.

## Why This Matters for Handover

This is a targeted technique for exactly the kind of "here be dragons" knowledge a handover is meant to transfer: the cross-cutting hazard that no single file's local context reveals, and that a new maintainer working on any one of the affected modules would otherwise have no way to discover short of already knowing to look for it. It complements [External Annotations for Fragile Legacy Systems](external-annotations-for-fragile-legacy-systems.md) — that technique documents a single fragile component from the outside; this one documents a concern that was never local to any one component in the first place.
