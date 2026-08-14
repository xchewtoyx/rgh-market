---
type: concept
title: Standard Method Contract
description: >
  The predictable get, list, create, update, delete, and replace methods with
  defined idempotency, side-effect, and error semantics for resource-oriented APIs.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 7"
---

Resource-oriented APIs expose a **standard method contract**:

| Method | Typical HTTP | Idempotent | Side effects |
| --- | --- | --- | --- |
| Get | GET | Yes | None |
| List | GET collection | Yes | None |
| Create | POST | No | Creates resource |
| Update | PATCH | Often | Mutates resource |
| Replace | PUT | Yes | Replaces resource |
| Delete | DELETE | **No** | Removes resource |

\*Create is not idempotent unless deduplicated via
[request deduplication and idempotency keys](request-deduplication-and-idempotency-keys.md).

**Delete is intentionally non-idempotent:** resource-oriented APIs are imperative —
deleting a nonexistent resource should **fail**, not succeed silently. The caller
must know this delete invocation removed the resource, not that absence predates
the call. That choice drives [batch operations](batch-operations.md) all-or-nothing
semantics and makes retries on delete unsafe without deduplication keys.

## Method availability

Not every resource supports every standard method. Distinguish:

- **405 Method Not Allowed** — the method does not apply to this resource type
  (for example [singleton sub-resource](singleton-sub-resource.md) may only get/update).
- **403 Forbidden** — the method applies but this instance forbids it (immutable
  archive, write-protected row).

Never omit a route and return **404** for an unsupported method — that implies the
resource does not exist.

## Side effects and idempotency

Standard methods must do what they claim — no hidden work. Blatant side effects
(third-party calls, multi-system chains that can partially fail) belong in
[custom methods](custom-method.md). Subtle effects (a get that increments a hit
counter) are judgment calls weighed against performance and failure modes.

**Security:** return **404** for both "not found" and "no access" on get/delete so
callers cannot probe existence via status-code differences.

## Get

Strict key-value lookup by identifier; input is the id; response is the resource.

## List

Targets a collection — top-level (`GET /chatRooms`) or subcollection under a parent
(`GET /{parent=chatRooms/*}/messages`).

- **Access control:** return only resources the caller may see — not a uniform 403
  for the whole list.
- **Result counts:** avoid exact totals in list responses — expensive at scale. If
  needed, use an estimate field (for example `resultCountEstimate`) even when currently
  exact, preserving freedom to switch later.
- **Sorting:** generally discouraged — global sort across distributed shards is costly
  with limited consumer value.
- **Filtering:** encouraged — see [list filter](list-filter.md). Client-side filter
  after full list wastes bandwidth and server work.

## Create

Given resource data, persist so get and list can find it. Prefer server-generated
[resource identifiers](resource-identifier.md); client-chosen ids are acceptable for
sync scenarios. Response is always the created resource.

**Strong consistency:** once create succeeds, get, list, update, and delete must see
the resource immediately ("read your writes"). If storage is only eventually
consistent, use a [custom method](custom-method.md) or
[long-running operation](long-running-operation.md) instead — custom methods carry no
such guarantee.

## Update

Partial modification via PATCH — only fields the client sends change. Distinguish
"leave alone" from "set blank" via [field mask](field-mask.md). State transitions
(archive, send) often fit [custom methods](custom-method.md) better than status
fields on update.

## Replace

PUT sets the resource to **exactly** the request body — fields omitted are removed,
including fields the client does not know about. Solves stale-client clobbering when
the API adds fields the library lacks. Do not use replace as a substitute for create —
create-only-if-absent semantics are not expressible. Replace can create when the id
is client-chosen but that path is generally best avoided.

## Trade-off

Standard methods sacrifice perfect fit for learn-once-apply-everywhere predictability.
They cover roughly ninety percent of cases; reach for custom methods only when
standard semantics genuinely bend.

Related: [long-running operations](long-running-operation.md),
[list revisions](list-revisions.md), [delete revision](delete-revision.md),
[state transition operation](state-transition-operation.md).
