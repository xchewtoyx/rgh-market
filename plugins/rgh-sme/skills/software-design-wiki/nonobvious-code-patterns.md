---
type: concept
title: Nonobvious Code Patterns
description: >
  Event-driven indirection, mismatched declared and allocated types, and
  code that violates a strong reader convention are recurring patterns that
  reduce obviousness and need deliberate compensating documentation.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 18"
---

**Red flag: nonobvious code** — "If the meaning and behavior of code cannot
be understood with a quick reading, it is a red flag. Often this means that
there is important information that is not immediately clear to someone
reading the code."

**Event-driven programming** is a structural source of nonobviousness:
handler functions are invoked indirectly through registration with a
dispatch module, so a reader following control flow can't identify *which*
function will run at a given event without knowing what was registered at
runtime. This undermines the ability to reason about or verify the code by
reading it alone. The mitigation is for every handler's own
[interface comment](interface-documentation.md) to state explicitly when and
why it gets invoked — e.g. documenting that a `failed()` method "is invoked
in the dispatch thread by a transport if a transport-level error prevents an
RPC from completing."

**Generic containers in place of purpose-specific types** are a related
failure; see
[design for ease of reading, not writing](design-for-reading-not-writing.md).

**Mismatched declared vs. allocated type** — declaring a field as an
interface type (`private List<Message> incomingMessageList;`) but assigning a
specific implementation (`new ArrayList<Message>()`) is legal but misleading:
a reader who only sees the declaration doesn't know the concrete runtime
type, and the concrete type can matter — different implementations of the
same interface carry different performance and thread-safety
characteristics. Keep declared and allocated types matched wherever the
concrete type's specific properties are relevant.

**Code that violates reader expectations**: a Java `main` method that ends
by constructing an object and returning, with no further code, leads readers
to reasonably expect the application exits once `main` returns — a
near-universal convention. If that constructor actually spawns background
threads that keep the process alive, the code has silently broken a strong
convention. That behavior belongs in the constructor's own interface comment
as a matter of course, but because it so sharply contradicts a near-universal
expectation, it's also worth a short explicit comment right at the point of
surprise (the end of `main`) noting that execution continues elsewhere.
Obviousness partly comes from conforming to conventions readers already
carry with them; deviating from a strong one specifically requires extra,
deliberate documentation to prevent the resulting confusion.
