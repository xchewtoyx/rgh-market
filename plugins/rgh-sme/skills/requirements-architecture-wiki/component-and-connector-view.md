---
type: concept
title: Component-and-Connector View
description: >
  A component-and-connector (C&C) view documents a system's runtime
  structure — units of computation or storage, and the interaction
  mechanisms between them — answering how the system actually runs.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

A component-and-connector (C&C) view describes runtime structure:
**components** are units of computation or data storage, **connectors**
are the interaction mechanisms between them, and **ports**/**roles**
specify how a component or connector attaches to others. This is a
different structure from a [module view](module-view.md) — components
should be named by their runtime responsibilities, not conflated with the
source modules that happen to implement them; one module can show up in
several running components, and one component can be built from several
modules.

Document component and connector *types* as well as *instances*, the
topology connecting them, their interfaces, their behavior/protocols, and
relevant properties such as timing, reliability, and security. The
connector is not incidental: its abstraction has to make the interaction's
semantics visible — see [connector semantics](connector-semantics.md) for
the vocabulary (call/return, message queue, shared data, event, stream).

C&C views are what let you reason about performance, availability,
concurrency, communication, fault handling, and security, because those
properties are consequences of how things actually run, not of how the
source is organized. They also clarify process and thread boundaries and
distribution — questions a module view cannot answer on its own. See
[concurrency structure](concurrency-structure.md) for the C&C style
purpose-built for reasoning about parallelism and resource contention.

UML component diagrams can communicate C&C structure, but only with an
explicit profile or legend attached; plain boxes and arrows conceal the
connector and port semantics that make the diagram useful. Data-flow and
control-flow models are often useful complements to a C&C view, not
substitutes for it. See the specific styles: [data-flow](data-flow-style.md),
[call-return](call-return-style.md), [event-based](event-based-style.md),
[repository/shared-data](repository-shared-data-style.md), and
[ports-and-adapters](ports-and-adapters-style.md).
