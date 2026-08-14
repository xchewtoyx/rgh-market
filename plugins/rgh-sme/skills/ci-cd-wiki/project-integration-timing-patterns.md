---
type: concept
title: Project Integration Timing Patterns
description: >
  Three points at which a multi-project codebase can integrate versions of
  its dependent projects — at build time, at a dedicated delivery-pipeline
  stage, or at apply time — each trading consistency for team autonomy
  differently.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code, 2nd ed. (Kief Morris), ch. 19"
---

# Project Integration Timing Patterns

When one project's code depends on another's (an application on a shared
library, an infrastructure stack on a shared network, a service on another
service), there's a choice about *when* the versions of those two projects
get locked together — not just whether they're integrated via
[source or binary](source-vs-binary-component-integration.md). Three points
along the pipeline are available, each a different trade-off between
consistency and team autonomy:

- **Build-time integration**: the projects are built and tested together,
  producing one artifact (or a group of artifacts versioned and promoted as
  a unit) from the start of the pipeline. This is what a
  [monorepo](source-vs-binary-component-integration.md) building everything
  together amounts to in practice. Gives the fastest feedback on
  cross-project conflicts and the strongest consistency guarantee — the same
  combination of versions is what gets tested and what ships — at the cost
  of tighter coupling and build complexity that grows with project count.
- **Delivery-time integration**: each project builds and tests
  independently first; a dedicated **fan-in stage** later in the pipeline
  combines specific passing versions of each project, and that combination
  travels together through the rest of the pipeline. This is the general
  form behind [downstream pipeline triggering](component-pipeline-triggering.md):
  a new published version becomes the input to an integration stage that
  locks in a version pairing before promoting it further.
- **Apply-time integration**: each project's pipeline delivers all the way
  to every environment independently, and the actual version pairing is
  decided only when the artifact is applied to a live environment —
  whichever version of the dependency currently happens to be there. This
  is what [independent deployability](independent-deployability.md)
  requires in practice: no coordinated release step exists at all, so teams
  never block on each other, but there's no guarantee production runs the
  same version combination that was tested. This gap has to be closed by
  treating the dependency's interface as a contract and testing against it
  directly — see [independent testability](independent-testability.md)'s
  consumer-driven contract testing — rather than by testing the exact
  version combination that will run in production, since that combination
  isn't known in advance.

## Choosing among them

The three sit on a single spectrum: build-time integration maximizes
consistency and minimizes team autonomy; apply-time integration maximizes
autonomy and minimizes consistency; delivery-time integration sits between
them, adding an explicit integration stage without going as far as either
extreme. Organizations with a few tightly related projects and a small team
often prefer build-time integration's stronger guarantees; organizations
with many autonomous teams and hundreds of services generally need
apply-time integration's decoupling, accepting contract testing as the
price for it.
