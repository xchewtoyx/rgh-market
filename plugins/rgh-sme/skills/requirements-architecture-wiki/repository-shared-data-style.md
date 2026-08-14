---
type: concept
title: Repository/Shared-Data Style
description: >
  Repository and shared-data styles center interaction on persistent
  shared state, and documentation must cover ownership, schema,
  access/transaction/concurrency rules, replication, and consistency.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

Repository and shared-data is a [component-and-connector
style](component-and-connector-view.md) in which components interact
indirectly through persistent shared state rather than through direct
calls or events — a database, file store, or blackboard that multiple
components read from and write to. The interaction is defined by the
shape and rules of the shared state itself, not by a message passed
between two named endpoints.

Because the connector here is data rather than a channel, documentation
needs a different set of properties than a call or event connector would:
who owns each part of the schema and is allowed to change it, what access
rules apply (who can read, who can write, and to what), how transactions
and concurrent access are handled, whether and how the data is replicated,
and what consistency guarantees hold when it is. See also [data model
view](data-model-view.md) for the structure of the shared entities
themselves. Crosscutting choices that apply across any C&C style —
granularity of interaction, distribution, synchrony, failure semantics,
security, and whether connectors are treated as first-class architectural
elements at all — matter especially here, since a repository connector
often silently carries several of these decisions at once.
