---
type: concept
title: Context Representation
description: >
  A payload-level grouping of metadata elements for invocation context that
  survives protocol translation and spans single requests or whole conversations.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 6"
---

A **context representation** bundles [metadata elements](metadata-element.md)
and [id elements](id-element.md) about the call — correlation id, locale,
[API key](api-key-as-message-element.md), session id, QoS properties, logical
clocks — in the **message payload** rather than scattered protocol headers.

**Why payload-level:** isolates client and provider from protocol churn and
gateway translation (HTTP↔gRPC) where header semantics may be dropped or altered.
End-to-end security tokens must reach the far end; intermediaries can break
header-only designs.

Structurally a [parameter tree](parameter-tree.md) (or [atomic parameter list](atomic-parameter-list.md)
for simple cases). Use the **same structure and location** across all operations
for discoverability; optional fields with defaults when per-operation needs
diverge (higher dev/test cost).

**Variants:**

- **Global context** — valid across a conversation or nested backend chain
  (auth token created once and propagated; business-transaction id for audit
  across calls). Often handled by gateways or shared libraries.
- **Local context** — single-request only (message id, username, TTL). Processed
  inside the API implementation.

Typical contents: priority classifiers, session/correlation identifiers, client
version, locale, location for routing (regulatory residency).

**Trade-offs vs protocol headers:** native headers are convenient when the API
commits to one protocol and infrastructure (load balancers, caches) understands
them; custom payload context pays design cost but maximizes control. **Risk:**
redundancy/inconsistency between transport status and payload
([error report](error-report-shape.md), success flags) — avoid verbatim HTTP
codes in payload ("404") for non-HTTP consumers; prefer semantic messages.

Pairs with [wish list](wish-list.md) (data requests may live inside context) and [pagination](pagination.md) blocks in responses.
[Request bundles](request-bundle.md) may need container-level and per-element
context, mirroring nested error reporting. [Version identifier](version-identifier.md)
may travel inside context.

Document placement in the [API description](api-description.md). Long-running
[state transition](state-transition-operation.md) conversations may require
explicit context propagation for logging.
