---
type: concept
title: Remoting Technology Landscape
description: >
  Major integration styles — sockets, RPC, messaging, HTTP, and streaming — and
  how their persistence or decline shapes API contract choices today.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 1"
---

Remote APIs always sit on lower-layer connectivity. Historical and current options
share the goal of triggering remote processing or manipulating remote data:

| Style | Examples | Current role |
| --- | --- | --- |
| Sockets / TCP/IP | Berkeley sockets, FTP | Universal transport backbone |
| RPC | DCE, CORBA, Java RMI, gRPC | Distributed objects faded; gRPC remains popular |
| Message queues | IBM MQ, ActiveMQ, RabbitMQ, cloud queues | Time-decoupled integration |
| HTTP / hypermedia | RESTful and non-RESTful HTTP APIs | Dominant Web integration |
| Streaming pipelines | Kafka, UNIX pipes-and-filters | Analytics and event fan-out |

Not every HTTP API is RESTful — REST requires all architectural constraints, not
HTTP alone. TCP/IP, HTTP, and async messaging remain central; distributed object
middleware survives mainly in legacy systems; file transfer stays common for bulk
data.

Contract design is largely **technology-agnostic** at the message and resource
layer ([remote API domain model](remote-api-domain-model.md)); the transport choice
affects reliability expectations, [context representation](context-representation.md),
and which [operation responsibility patterns](operation-responsibility-patterns.md)
fit naturally (sync request–reply vs one-way events).
