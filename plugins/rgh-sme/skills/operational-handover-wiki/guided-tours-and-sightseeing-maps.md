---
type: concept
title: Guided Tours and Sightseeing Maps
description: Two written onboarding formats — an orientation map and a narrated code route — that stay useful only if kept linked to and refreshed with the actual source.
sources:
  - title: "Living Documentation"
    resource: "Living Documentation (Martraire), ch. 5"
---

Two formats give a newcomer a way to build independent operating competence in a codebase without reading everything:

- **Sightseeing map**: points to the significant places in the system and how they relate to each other — an orientation device, not a full inventory. It tells a newcomer where the things worth knowing about are, so they can navigate on their own afterward.
- **Guided tour**: a purposeful route through the actual code, stopping at points chosen by someone who knows the system, explaining what to notice at each stop and why it matters. A tour through a transaction listener, its model, a monitoring service, and a downstream report is an interpretation laid over existing code — it does not restate the architecture in a separate document.

## Keeping Them Living

Both formats are interpretations over the real source, not descriptions that could drift from it silently — but they still decay unless deliberately kept current:

- Link tour stops directly to the actual source locations they describe, rather than to a paraphrase of them, so the reader is always looking at ground truth.
- Refresh the tour and map when the underlying code changes shape, the same as any other artifact in [Documentation Maintenance Workflows](documentation-maintenance-workflows.md) — a tour that still describes a component that was since removed or restructured is worse than no tour, because it actively misleads a reader who trusts it.

## Relationship to Live Walkthroughs

A guided tour here is a written, reusable artifact — distinct from the live, narrated walkthroughs described in [Live Knowledge Transfer Techniques](live-knowledge-transfer-techniques.md), which exist only in the moment they're given. The written tour scales to newcomers who arrive after the person who could give a live walkthrough is no longer available, which is exactly the situation a handover is meant to survive.
