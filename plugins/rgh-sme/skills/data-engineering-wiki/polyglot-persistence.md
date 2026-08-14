---
type: concept
title: Polyglot Persistence
description: >
  Storing different data types in whichever storage technology best fits
  their access pattern, instead of forcing everything into one database.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 7"
---

Polyglot persistence means picking a different storage technology for each
kind of data based on how it will actually be used, rather than forcing every
data type in a system into one database because that's the database already
in use. The analogy is polyglot programming: writing different parts of an
application in whichever language suits that part best, rather than one
language for everything.

A typical e-commerce example: shopping-cart and session data goes in a
key-value store (needs very fast single-key retrieval); completed orders go
in a document store (fast, flexible storage of a naturally nested record);
inventory and pricing go in an RDBMS (structured, relational data with
integrity constraints); a customer social/referral graph goes in a graph
store (traversal queries that a relational join chain handles poorly at
scale). Each choice follows from the query pattern that data type actually
needs, not from a preference for standardizing on one engine.

The distinct but related term **polyglot data store** describes the same
idea applied at the organization level rather than within a single
application: different teams or business units each using the storage
technology best suited to their own workload, rather than one shared
database serving every team's needs equally poorly.

The trade-off is operational, not architectural: every additional storage
technology is a new system to learn, operate, monitor, and secure. The
payoff — avoiding the performance and development-velocity cost of jamming
naturally non-relational data (a graph, a deeply nested document) into a
relational schema it doesn't fit — is usually worth that added surface, but
it's a real cost a pipeline team has to plan staffing and operational
capacity for, not a free win. This is the same trade-off
[choosing a source or target technology](source-system-evaluation.md) always
involves, just multiplied across every storage type a system's data actually
needs rather than settled once for the whole system.
