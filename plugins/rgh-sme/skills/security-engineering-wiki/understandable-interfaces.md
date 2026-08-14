---
type: concept
title: Understandable Interfaces
description: >
  Narrow typed interfaces, a common object model, and idempotent
  operations make a system's behavior predictable and its security
  posture auditable.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 6"
---

# Understandable Interfaces

Interface design choices determine how much of a system a reader must
load into their head — and whether tooling can reason about it at all.

**Prefer narrow interfaces with less room for interpretation.** Typed
frameworks (gRPC, Thrift, OpenAPI) declare each method and its
input/output types, enabling cross-referencing, conformance tooling, and
safe evolution (versioning, backward-compatibility guidelines). A
free-form RESTful endpoint validating JSON in application code hides its
real surface: independently updated clients and servers can interpret
payloads differently (crashes), and without an explicit API definition
you can't build automatic audits correlating authorization policies with
the actually-exposed surface. This is the interface-level face of
[small functional APIs](small-functional-apis.md).

**Prefer a common object model** for systems managing many resource
types (Kubernetes-style): every object satisfies base invariants,
standard scoping/annotation/grouping applies across types, operations
behave consistently, and custom types inherit the same mental model.

**Pay attention to idempotency.** In distributed systems operations
arrive out of order and responses get lost; an idempotent method lets
clients simply retry until success. Mismatched expectations are the
danger: a client author who *believes* an operation is idempotent will
retry and create duplicate records. Operations can often be restructured
to be idempotent (e.g. client-supplied UUID per mutation; server treats
repeats as duplicates). Idempotency also simplifies the responder's
mental model during incidents: keep trying until it works, no need to
track partial completion.
