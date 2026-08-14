---
type: concept
title: Change Scope Classification (Local, Nonlocal, Architectural)
description: Classifying a prospective change by how many elements it touches predicts how risky and how staged a maintainer's rollout needs to be.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 2"
---

Every architecture partitions the changes a future maintainer might want to make into three categories, and which category a given change falls into is itself a fact worth documenting for the maintainer who inherits the system:

- **Local**: confined to a single element (e.g. adding a pricing rule inside one module). Lowest risk, safe for an unfamiliar operator to attempt without wide coordination.
- **Nonlocal**: touches multiple elements but the system's fundamental interaction pattern stays intact (e.g. a new business rule that also needs new database fields and a new UI display). Higher risk than local, but still stageable and incremental — each affected element can be changed and verified in turn.
- **Architectural**: changes the fundamental interaction pattern itself (e.g. converting a single-threaded component to multi-threaded). Likely to touch the whole system, and not something a maintainer should attempt piecemeal or without going back through design authority.

## Why This Matters for Handover

Determining which category a prospective change actually falls into requires being able to trace what depends on the piece about to change — a "uses" or dependency view maintained specifically for this purpose lets a maintainer check, before touching anything, whether a change they assume is local is actually going to ripple further than they think.

A well-designed system keeps the changes its maintainers will actually need to make in the "local" category — that's what "effective architecture" means in change terms. When a handover document or [runbook](runbook-checklist-design.md) tells a new operator "here's what's safe to touch," it is implicitly making a claim about which of these three categories a given change falls into. Making that classification explicit — rather than leaving the new maintainer to discover the hard way that a change they thought was local actually rippled system-wide — is itself a piece of tacit knowledge worth capturing. This is the conceptual complement to [Infrastructure-as-Code Properties for Safe Change](iac-properties-for-safe-change.md)'s composability property: composability is what keeps a module boundary and a "local change" boundary the same thing.

Failing to keep common changes local, or failing to warn a maintainer when a change is nonlocal or architectural rather than local, is one of the ways a system quietly accumulates the kind of unmanaged risk that [Automated Guardrails for Safe Changes](automated-guardrails-for-safe-changes.md) exist to catch before it reaches production.
