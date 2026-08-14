---
type: concept
title: Reuse Existing Authoritative Sources Before Writing New Documentation
description: Locating and publishing knowledge that already exists in an authoritative form — standard vocabulary, public references, or tool histories — instead of transcribing it into a new, separately-maintained document.
sources:
  - title: "Living Documentation"
    resource: "Living Documentation (Martraire), ch. 3"
---

Before writing a new document, check whether the knowledge it would contain already exists somewhere authoritative. Transcribing an existing fact into a new document creates a second copy that can drift from the original, and duplicates maintenance effort that a link would have avoided entirely.

## Where Authoritative Knowledge Already Lives

- **Standard vocabulary and patterns**: Naming something with an established term (a design pattern, a bounded context, an architectural style) imports the whole body of reasoning, alternatives, and constraints that term carries — it is compressed, ready-made documentation. Learn standard terminology primarily to recognize and communicate what's already happening in a system, not just to force an implementation to match the pattern.
- **Public references and standards**: Most generic domain or technical knowledge (protocols, regulatory definitions, industry-standard processes) is already documented publicly and better than a team could write it internally. Link to the authoritative external source rather than re-explaining it in-house.
- **Tool histories**: Source control, chat logs, issue trackers, service registries, and console histories already record a great deal of project knowledge as a byproduct of normal work. Treat these as legitimate sources rather than re-entering the same facts manually into a separate document, which both wastes effort and creates a second record that can contradict the first.

## Consolidating Dispersed Facts

When the same authoritative fact is genuinely needed in multiple places, don't just let copies accumulate — install reconciliation: consistency tests that fail when copies diverge, verification of assumptions embedded in tests, or a single published contract that other locations reference. Where facts are scattered across many places with no single source, consolidate them into one usable view while preserving traceability back to where each fact originally came from, so a reader can still verify it.

## Relationship to Other Practices

This is the search-before-you-write complement to [Self-Documenting Declarative Systems](self-documenting-declarative-systems.md): that note is about making the system itself the source of truth going forward; this one is about recognizing that a source of truth already exists elsewhere before duplicating it. Once a fact's authoritative source is chosen, publishing a snapshot of it (e.g. a generated reference page) should carry a version marker so readers know exactly what state it reflects.
