---
type: concept
title: Biodegradable Documentation
description: Designing documentation for temporary system states (like migrations or parallel run phases) to decay and be removed once the transition is complete.
sources:
  - title: "Living Documentation"
    resource: "Living Documentation (Martraire), ch. 14"
---

During system transformations, migrations, or architectural refactorings (such as implementing a strangler pattern), teams must write extensive documentation to guide operators through the transition state. However, this documentation becomes clutter and technical debt once the transition is complete. To prevent this, temporary operational procedures must be designed to be **biodegradable**.

## Characteristics of Biodegradable Documentation

- **Explicit Expiration Triggers**: Every document explaining a temporary state must state its sunset criteria upfront (e.g., "Retire this guide once all traffic is cut over to Service B and the legacy VM is destroyed").
- **Visual Isolation**: Separate transition guides from the evergreen wiki. Mark them with prominent headers or warning banners indicating that the document details a transient state.
- **Proximity to the Transition Code**: Store migration-specific runbooks inside the migration branches or near the code handling the transition, rather than in the main operations wiki. When the transition branch is merged or deleted, the temporary documentation is deleted with it.
- **Clean-up in Definition of Done**: Make the removal of transition documentation a required step in the project's final rollout checklist. The migration is not "done" until its temporary instructions are retired.

By ensuring transition instructions are deleted post-migration, teams maintain the overall health of their long-term [Documentation Maintenance Workflows](documentation-maintenance-workflows.md).
