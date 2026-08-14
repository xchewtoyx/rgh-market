---
type: concept
title: Documentation Version Boundaries
description: Preserving distinct documentation for different supported versions of a system to avoid user confusion.
sources:
  - title: "Docs for Developers: An Engineer’s Field Guide to Technical Writing"
    resource: "Docs for Developers (Jared Bhatti et al.), ch. 11"
---

When a system undergoes significant changes, maintaining a clear version boundary in documentation is necessary to ensure operators and users do not refer to instructions that do not apply to their environment.

## Key Versioning Principles

- **Differentiate Behavior Visibly**: Clearly distinguish current, legacy, and future behavior on pages where multiple system versions are documented. Ensure that readers on supported older versions can easily locate instructions that match their environment.
- **Maintain a Single Source of Truth**: Remove misleading or redundant duplicate content. Conflicting advice across different pages leads to confusion; it is safer to merge information into one place or delete obsolete pages.
- **Durable Linking and Redirects**: Avoid breaking links that operators rely on (e.g., links bookmarked in runbooks or automated alerts). If a page must be moved, configure appropriate redirects to guide the user to the correct location.

For more details on managing the complete lifecycle of documentation, see [Documentation Maintenance Workflows](documentation-maintenance-workflows.md) and [Documentation Deprecation as User Migration](documentation-deprecation-migration.md).
