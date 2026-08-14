---
type: concept
title: Local Interface to Remote API
description: >
  How program-internal interfaces differ from network-exposed contracts in shared
  knowledge, failure modes, and strategic exposure when opening a system to clients.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 1"
---

Every component exposes an **interface** — operations, properties, and events —
without revealing internal structure (information hiding). **Local interfaces**
support in-process or same-machine decomposition; **remote APIs** cross process
and network boundaries so independently deployed parts communicate.

Remote APIs commonly sit between mobile or Web frontends and cloud backends,
often serving many concurrent client kinds. Opening a system to external clients
raises **security** questions (who may access which operations and data) and
**strategic** ones (data ownership, service levels, ecosystem control). APIs are
not permanent — providers may expand access to grow an ecosystem and later restrict
or retire surfaces when business models shift.

## Shared knowledge

Both local and remote parties assume **shared knowledge**, like matching electrical
sockets:

- Exposed operations and the services they provide
- Representation and meaning of exchanged data
- Observable properties — state and valid transitions
- Event notifications and error handling

Remote APIs must additionally specify **communication protocols**, **network
endpoints** (addresses, credentials), and **distribution failure policies**
(timeouts, transport errors, outages). The [API contract](remote-api-domain-model.md)
expresses these expectations while hiding implementation — e.g. a GitHub issues
API reveals create/retrieve semantics and field shapes, not the provider's language,
database, or schema.

Defining a contract requires agreeing on protocols/endpoints **and** deliberate
[message structure](parameter-tree.md) — even for file import/export or clipboard
integration.

## Relation to web APIs

[Web API characteristics](web-api-characteristics.md) emphasize immediate provider
control over all remote clients; this note frames the broader local-to-remote
shift and the extra contract surface distribution introduces.
