---
type: concept
title: Prompt Element Dependency
description: >
  Some prompt elements require another element already be present, and some
  exclude each other, both of which prompt assembly must be able to express.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

Dependency is one of three relational dimensions any
[prompt assembly](prompt-assembly-algorithms.md) method must account for
between elements (alongside [position](prompt-element-position.md) and
[importance](prompt-element-importance.md)). It governs how including one
element affects whether another can or should be included, in two categories:

- **Requirements** — one element depends on another being present first, for
  example needing to establish "Richard is the protagonist of *The Beach*"
  before a later element can state "He grew up in England" and still make
  sense.
- **Incompatibilities** — one element excludes another, often when the same
  information has multiple presentations (a summary versus a detailed
  explanation of the same fact). If the assembly engine supports
  incompatibilities as a first-class relation, you can register both versions
  with an exclusion note between them — using the longer version when space
  allows, and falling back to the shorter one otherwise. This is exactly the
  mechanism [elastic snippets](elastic-snippets.md)'s "multiple overlapping
  prompt elements" approach relies on.

Once content — static and dynamic alike — has been transformed into prompt
elements carrying position, importance, and dependency properties, the prompt
is ready to be assembled.
