---
type: concept
title: Remote API Domain Model
description: >
  Platform-neutral vocabulary — provider, client, endpoint, operation, message,
  and contract — that anchors API pattern decisions and coupling analysis.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 1"
---

The pattern language rests on a **domain model** independent of HTTP, SOAP, or
queue technology. Unless stated otherwise, **API** means **remote API**: a set of
well-documented network endpoints letting internal and external components offer
services to each other — activating provider logic, exchanging data, or notifying
events toward domain goals. Each remote API is realized through [layered API realization](layered-api-realization.md)
(client SDK, provider SDK, transport stack).

Core participants:

- **API provider** and **API client** — a participant may be both (offering
  services while consuming others). The **API** is endpoints plus their contracts.
- **API endpoint** — provider-side channel terminus with a unique address (URL,
  queue name). In HTTP resource APIs, an endpoint maps to related resources; a
  **home resource** URI is an entry point to discover others.
- **Operation** — distinguished within an endpoint by identifier (SOAP body tag,
  HTTP method on a resource, OpenAPI `operationId`).

**Conversations** compose **messages** in sequences:

| Conversation | Shape |
| --- | --- |
| Request–reply | One request, one response |
| One-way | Request only |
| Event notification | Single event message |
| Request–multiple replies | Callback registration, then async replies |

Message kinds (command, document, event) align with those shapes. Wire formats
(JSON, XML, binary) are secondary to **representation element** structure.

A message's **data transfer representation (DTR)** is the wire-level analogue of
a DTO — paradigm-agnostic, no remote object stubs. **Serialization** maps program
data to DTR; **deserialization** reverses it. Elements may nest ([parameter tree](parameter-tree.md)),
link ([link element](link-element.md)), or carry ids and metadata ([id element](id-element.md),
[metadata element](metadata-element.md)).

The **API contract** specifies operations, messages, and addresses — minimum
shared knowledge for interoperable evolution. Public APIs are often offered as-is;
paying relationships may negotiate terms tied to [API description](api-description.md)
and [service level agreement as contract](service-level-agreement-as-contract.md).

**Coupling** grows with how much client and provider must know about each other
([architecturally significant API requirements](architecturally-significant-api-requirements.md)).
**Granularity** is how many endpoints/operations exist and how rich each request/
response contract is — a recurring dimension in [API design recurring trade-offs](api-design-recurring-trade-offs.md)
and [endpoint operation design challenges](endpoint-operation-design-challenges.md).

See also [local interface to remote API](local-interface-to-remote-api.md) and
[remoting technology landscape](remoting-technology-landscape.md).
