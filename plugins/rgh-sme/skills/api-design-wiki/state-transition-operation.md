---
type: concept
title: State Transition Operation
description: >
  An operation that reads current provider state and writes a new state,
  modeling business activities, entity updates, or process steps with visible
  execution state.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 5"
---

A **state transition operation** `sto: (in, S) -> (out, S')` initiates work
that changes provider application state — incremental entity updates,
long-running claim processing, checkout and payment. Validates allowed
transitions at runtime; pairs command input with result/ack output.

Forces: service granularity (single attribute vs whole process); audit and
time windows; conflicts with concurrent clients or batch jobs; long-running or
heavy work; incremental diffs vs full replacement payloads.

**Update types:**

- **Full replacement** — often processable without reading current state;
  behaves like creation; HTTP PUT.
- **Partial/incremental** — requires read; HTTP PATCH; harder to make
  idempotent ("set x to y" beats "increment x by y" under retries).
- **Upsert** — replace on missing id creates the entity with client-supplied
  id.

Transaction boundary usually matches the operation (ACID, saga, or TCC).
Prefer idempotent absolute updates. Expose on [processing resources](processing-resource.md)
or [information holder resources](information-holder-resource.md).

**Business activity processor variant** — generic state-machine primitives:
prepare, start, suspend, resume, complete, fail, cancel, undo, restart,
cleanup. Frontend BPM keeps process state on the client; BPM services keep it
on the provider. Identifiers typically appear as id elements in the URI;
[link elements](link-element.md) can advance state.

Differs from siblings per [operation responsibility patterns](operation-responsibility-patterns.md).
