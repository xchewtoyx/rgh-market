---
type: concept
title: Behavior Documentation
description: >
  Structural views describe what a system is made of, not how it acts
  over time; behavior documentation records interactions, state changes,
  and exceptional paths at the level of detail a given stakeholder task
  actually needs.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan), ch. 8"
---

Structural views — [module](module-view.md),
[component-and-connector](component-and-connector-view.md), or
[allocation](allocation-view.md) — describe what a system is made of and
how the pieces relate. None of them fully specify how the system behaves
over time: the interactions between elements, state changes, workflows,
and what happens on exceptional paths need their own documentation.

Choose notation by the question being answered, not by habit: use cases
or scenarios for externally meaningful interactions, sequence or
communication diagrams for message ordering, activity diagrams for flows
and concurrency, state machines for lifecycle or state-dependent behavior,
and tables or plain prose when they're simply clearer than a diagram would
be. Sequence-style diagrams in particular only fully specify behavior when
the set of communicating elements is small and fixed — once branching,
exceptions, or resource contention enter the picture, they're still useful
for illustrating a typical case, just not as a complete specification on
their own. Document behavior at the level a given stakeholder actually
needs it at — a whole-system scenario, a view-specific interaction, a
single interface's protocol, or one element's internal behavior — rather
than defaulting to maximum detail everywhere. When state-dependent
behavior is complex and high-stakes enough that a diagram's completeness
can't be taken on faith, a [state transition
matrix](state-transition-matrix.md) forces every state-event combination
to be accounted for; the same forced-enumeration idea applied to branching
input conditions instead of states is a [decision table](decision-table.md).

Behavior documentation is what supports requirements traceability
(showing that a documented interaction actually satisfies a stated
[requirement](functional-requirement.md)), validation with stakeholders,
testing, integration, and reasoning about performance and concurrency. For
it to do that job, it has to stay aligned with the structural elements and
interfaces it describes — a scenario that references a component or
interface the structural views don't have is a sign the two have drifted
apart. See [requirements traceability](requirements-traceability.md).
