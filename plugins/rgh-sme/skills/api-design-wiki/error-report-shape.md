---
type: concept
title: Error Report Shape
description: >
  The contract-level structure for reporting failures — machine-readable code,
  human message, and optional structured details.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 10, ch. 24"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 6"
---

An **error report** returns failure outside successful response bodies — HTTP
status plus a structured payload. Structure as an [atomic parameter list](atomic-parameter-list.md):
machine-readable **code** (may be an [id element](id-element.md)) plus human
**text**; optionally reuse transport codes (HTTP 4xx) but do not rely on them
alone — preserves protocol/format autonomy.

Include:

- **`code`** — stable, machine-readable, specific (clients branch on this).
- **`message`** — human explanation; never required for client logic.
- **`details`** — structured extras (field violations, retry hints).
- **Correlation id** — for provider-side fault analysis; may live in
  [context representation](context-representation.md).

**Forces:** audience spans developers, operators, and help desk — balance detail
against jargon and length. Must not leak implementation (SQL stack traces aid
attackers and enable DoS). Support i18n for end-user-facing text but **always**
ship a machine-readable code so non-human consumers never parse prose.

**Security:** failed-login errors must not reveal whether a user id exists —
blunt enumeration attacks. Verbose text raises leakage risk.

Distinguish transport errors (could not execute method) from domain errors
(operation ran but business rules failed). Avoid **redundancy/inconsistency**
between HTTP status and payload status (HTTP 200 with failure body or the
reverse) — handle deliberately if both appear.

For [request bundles](request-bundle.md), report status **per entry** and for
the whole bundle (bundle-level report plus per-request-id map of reports).

[Long-running operations](long-running-operation.md) put work failures in
`OperationError.result`, not as get-status HTTP errors.

Incompatible [version identifiers](version-identifier.md) should error explicitly
rather than silently misparse. New error codes from [rate limits](rate-limit.md)
often imply a breaking [semantic versioning](semantic-versioning-api.md) major.

Returned from [state creation operations](state-creation-operation.md) and
[state transition operations](state-transition-operation.md) as atomic flags or
structured reports. May nest inside response [context representation](context-representation.md).
