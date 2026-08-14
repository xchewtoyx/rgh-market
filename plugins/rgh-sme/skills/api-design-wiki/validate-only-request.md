---
type: concept
title: Validate-Only Request
description: >
  A request flag that runs server-side validation and dependency checks without
  committing changes, defaulting to normal execution when omitted.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 27"
---

Unsafe methods offer no low-risk "try it" path — a mistaken delete or create can
cause real damage. Add **`validateOnly?: boolean`** on request interfaces (default
**false**) so callers preview outcomes without mutating state.

When `validateOnly` is true, the method exercises real validation paths — permissions,
referential integrity, uniqueness, format checks — but rolls back before persisting,
like a transaction that never commits. Rule of thumb: **if execution would throw,
validation should throw the same error** (403, 409, 400, …).

## Response shape

Mirror a successful execution response where possible. Server-generated ids may be
blank or placeholder values — the goal is confirming the request would succeed, not
supplying final data. For nondeterministic outcomes (lottery, random winner), return
any **plausible** success shape; exact odds need not match production.

## External dependencies

Validation must stay **safe, idempotent, and side-effect free**. If an external
service has no validation mode (test email on deliverability check), skip that check
rather than send real side effects. Partial validation (format-only on email) beats
breaking the no-side-effects guarantee.

Read-only but expensive operations (warehouse query syntax check) still benefit —
catch invalid input without running costly work.

## Contrast with purge

[Purge custom method](purge-custom-method.md) inverts the default: validation-only
unless `force` is set, because accidental execution is catastrophic. `validateOnly`
defaults to normal execution — forgetting the flag must not block real work.

Support per method as needed; not every endpoint requires validation mode.
