---
type: concept
title: Pagination
description: >
  Cursor-based chunking of large collections or oversized single resources via
  pageToken, maxPageSize, and nextPageToken.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 21"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 7"
---

**Pagination** lets consumers retrieve large [list operations](list-operations.md)
or oversized single resources in bite-sized chunks. Three fields express
continuation:

- **`pageToken`** — opaque server-only cursor from a prior response (empty =
  first page)
- **`maxPageSize`** — client's **maximum** desired results per page (not exact —
  see [API wire naming](api-wire-naming.md))
- **`nextPageToken`** — server token for the next request; **empty means done**,
  even when `results` is empty (server may hit a time budget with no matches yet)

**Page size:** return *up to* `maxPageSize` — with uneven data distribution,
filling exactly N rows can require scanning billions of rows. Cut off at a time
budget and resume via token. Default consistently across the API (often **10**;
tune by resource size — 100 for tiny rows, 10–25 for multi-KB items). Reject
negative sizes; oversized requests may clamp to server limits.

**Tokens:** encrypt payload — Base64 alone leaks structure and constrains
evolution. Represent as **strings** (Base64 of encrypted UTF-8) for URLs and
JSON. Document **expiration** (minutes to hours; 60 minutes is generous) —
expired tokens retry from start. Prefer **last-seen cursor** over numeric offset;
offset pagination duplicates/skips rows when data changes mid-iteration. Snapshot
tokens when storage supports point-in-time reads.

**Total count:** omit `totalResults` unless UI truly needs "page X of Y" and the
count is cheap — at scale accurate totals are prohibitive.

**Inside one resource:** custom read method with `maxBytes`, `pageToken`,
`nextPageToken`, plus [field mask](field-mask.md) indicating which fields each
chunk populates — abort if the resource mutates mid-read (strong consistency).

**Anti-pattern:** exposing SQL `offset`/`limit` — leaks storage semantics and
inherits offset consistency problems.

No backward paging or arbitrary page jumps — programmatic clients iterate
forward; UIs cache locally for back navigation.

Pair with [wish list](wish-list.md) and [wish template](wish-template.md) to trim payloads.
Required for unbounded [atomic list fields](atomic-list-field.md) alternatives
and [operational data holders](operational-data-holder.md).
