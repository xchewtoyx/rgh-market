---
type: concept
title: Exception Slugs for Error Attribution
description: Attaching a stable, unique, greppable identifier to every distinct throw site lets an investigator jump directly from a dashboard spike to the exact line of code that produced it, instead of re-deriving the mapping from a free-text error message.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 6"
---

When an error occurs, capture more than just the exception type or message — attach a stable, unique, greppable identifier (an "exception slug") tied to the specific throw site in the code. A free-text error message can be reused across multiple call sites, or can vary slightly between similar failures, making it unreliable as a key for grouping or attribution; a dedicated per-throw-site slug doesn't have this ambiguity.

The payoff is direct: seeing a spike for one slug on a dashboard, an investigator can grep the codebase for that exact string and land on the responsible line immediately, instead of having to reverse-engineer which of several similar-looking error paths actually produced it. This is one instance of a broader instrumentation habit — see the [wide-event attribute checklist](wide-event-attribute-checklist.md) for the fuller set of error-attribute conventions this fits into.
