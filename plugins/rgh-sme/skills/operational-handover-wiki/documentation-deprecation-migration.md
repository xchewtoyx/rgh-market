---
type: concept
title: Documentation Deprecation as User Migration
description: Managing the deprecation of documentation as a structured migration process to guide users safely to supported alternatives.
sources:
  - title: "Docs for Developers: An Engineer’s Field Guide to Technical Writing"
    resource: "Docs for Developers (Jared Bhatti et al.), ch. 11"
---

Deprecating documentation is not just about deleting files; it must be managed as a structured migration process. If documentation is removed prematurely, operators and users may find themselves without a clear path forward during a system transition.

## The Deprecation Process

- **Clear Communication**: Announce deprecations with the following critical details:
  - What is changing and why
  - Who is affected
  - The timeline for deprecation and retirement
  - Supported alternatives or replacements
  - Concrete, step-by-step migration instructions
  - Where to seek help or report issues
- **Proactive Warnings**: Place warnings early and repeatedly. These warnings should reside inside the relevant documentation pages themselves, within the product or system outputs (e.g., CLI warnings), and in release communications.
- **Grace Period**: Keep deprecated documentation available long enough for users to complete their transition. Ensure the deprecated pages are marked unmistakably (e.g., with a deprecation banner).
- **Retirement Criteria**: Do not retire deprecated pages until a viable replacement and migration path have been fully established and verified.
- **Feedback Loop**: Monitor and measure friction during the migration process. Refine documentation and migration guidance dynamically as operators encounter real-world issues.

To manage the ongoing lifecycle of operational documents, refer to [Documentation Maintenance Workflows](documentation-maintenance-workflows.md) and [Documentation Version Boundaries](documentation-version-boundaries.md).
