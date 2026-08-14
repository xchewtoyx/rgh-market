---
type: concept
title: Responsibility-Based Extraction (vs. Mirroring an API)
description: >
  Instead of wrapping an API 1:1, Extract Method the responsibilities
  buried inside API-heavy code and give them higher-level, API-agnostic
  names — lighter weight than skinning the API, but the extracted methods
  may still carry some API code along with them.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 15"
---

Rather than mirroring a library's API 1:1 with [wrapper interfaces](skin-and-wrap-the-api.md),
directly identify the responsibilities buried inside API-heavy code (see
[finding responsibilities hidden in API calls](find-responsibilities-hidden-in-api-calls.md))
and [Extract Method](splitting-and-joining-methods.md) each one under a
higher-level, non-API-flavored name — worked example: pulling scattered
session/transport/connect/send calls into a single `sendMessage(Message)`
method on a new collaborator, named for what it accomplishes rather than
which API calls it happens to make.

Best suited when the API is complex enough that mirroring it entirely would
be heavy work, and when you have either a safe automated Extract Method tool
or enough confidence to do the extraction correctly by hand.

**Trade-off against skinning the API**: Skin and Wrap is more upfront work
but yields cleaner, more complete isolation from the third-party library —
directly reusable for the lock-in concern in
[library lock-in from scattered calls](library-lock-in-from-scattered-calls.md).
Responsibility-Based Extraction is lighter-weight but risks extracting
methods that still can't be independently tested, since some API code
inevitably rides along inside them. Many teams end up using both: a thin
wrapper purely for testability, plus a separate higher-level extraction that
presents a better-shaped interface to the rest of the application.
