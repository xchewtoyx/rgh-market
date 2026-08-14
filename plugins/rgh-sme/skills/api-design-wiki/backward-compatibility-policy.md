---
type: concept
title: Backward Compatibility Policy
description: >
  Explicit categories of server-side change — new functionality, bug fixes,
  mandated compliance, performance, semantics — and how each can break clients.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 24"
---

**Compatibility** means client and server can communicate successfully. With
multiple client and server versions in flight, focus on whether **server changes**
leave existing client code working — ideally in "blissful ignorance" via
[backward-compatible](backward-forward-compatibility.md) injection into the
current version rather than forcing immediate migration.

There is no universal test — expectations differ (data warehouse vs IoT fleet).
Publish an explicit **policy** covering:

**Adding functionality**

- Whether in-version augmentation is allowed at all (banks freeze; startups ship).
- New fields on existing resources can exhaust memory on constrained clients,
  especially on list responses.
- New resources/methods rarely break callers directly but enumeration tools may
  miss them.
- New resources with dependencies on existing ones (for example a required
  `MessagePolicy` on `ChatRoom`) force clients to learn new concepts.

**Fixing bugs**

- HTTP 500 fixes are usually safe. Fixing silent "success" with wrong results
  may break dependents (floating-point `0.1 + 0.2` semantics).

**Mandatory changes**

- GDPR, security patches — minimize disruption with notice; may require new
  [version identifiers](version-identifier.md) or blocking old traffic.

**Under-the-hood changes**

- Small latency shifts usually fine; large shifts can force async redesign.
- ML model swaps can change outputs — breaking for users needing reproducibility.

**Changing semantics**

- Broadest category — permission models, list ordering, rate limits. Defaults
  matter: apply only to new resources vs all. Silent throttling can break tests
  expecting immediate consistency even when errors are avoided.

Judgment: could a reasonable client expect the old behavior for the version's
lifetime? See [semantic versioning](semantic-versioning-api.md) and
[lifecycle guarantees](limited-lifetime-guarantee.md) for governance.
