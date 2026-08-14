---
type: concept
title: Custom Method
description: >
  Non-standard RPC-style operations that may perform side effects and break
  standard-method guarantees when CRUD semantics would bend the interface.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 9"
---

**Custom methods** sit outside the [standard method contract](standard-method-contract.md)
— they are not bound to standard idempotency and side-effect rules and can do
whatever fits the scenario. Trade-off: clients assume less unless the API
documents conventions **consistently**.

**When to use:** standard methods technically cover most actions, but forcing
some behaviors into update/replace produces surprising interfaces. Example:
marking email `sent` via `UpdateEmail({state: 'sent'})` conflates field update
with [state transition](state-transition-operation.md) and pulls in SMTP side
effects — turning a storage update into a multi-system chain. Prefer
`CreateEmail` (pure draft save) plus a separate `SendEmail` custom method for
delivery and state change on success.

Resource reshuffles (splitting `Email` and `EmailDraft`) can preserve standard
methods but need not be dogma — adjust tools when purity blocks clarity.

**HTTP format:** almost always **POST** (GET only when idempotent and safe —
often a [singleton sub-resource](singleton-sub-resource.md) is better; DELETE
is rare). Append the action after **`:`** on the resource path:
`POST /rockets/1234567:launch` → `LaunchRocket`. Avoid slash-only action paths
that blur where the resource path ends. Name `<Verb><Noun>` like standard
methods; skip prepositions (`CreateRocketForMars`).

**Side effects** — email send, background jobs, multi-resource updates — are
expected and permitted; document thoroughly and use sparingly.

**Misuse:** custom methods as duct tape on a bad resource layout — masks design
debt and blocks real fixes. Before adding one, verify the action is not really
a standard-method operation in disguise.

See [custom method targeting](custom-method-targeting.md) and
[stateless custom method](stateless-custom-method.md). Many-to-many shortcuts:
[add-remove custom methods](add-remove-custom-methods.md); bulk atomic work:
[batch operations](batch-operations.md); filtered bulk delete:
[purge custom method](purge-custom-method.md).
