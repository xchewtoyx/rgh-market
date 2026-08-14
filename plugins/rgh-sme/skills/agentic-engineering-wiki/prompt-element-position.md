---
type: concept
title: Prompt Element Position
description: >
  Where a prompt element appears matters — most elements need a specific
  order, even though skipping an element outright is usually harmless.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

Position is one of three relational dimensions any
[prompt assembly](prompt-assembly-algorithms.md) method must account for
between elements (alongside
[importance](prompt-element-importance.md) and
[dependency](prompt-element-dependency.md)). Elements usually need to appear
in a specific order — omitting an element from the assembled prompt is
usually fine, but rearranging the elements that remain can confuse the
resulting document. Quoted reference snippets should keep their original
order; chat and narrative content should stay chronological; a description of
a book the user liked shouldn't land inside a "Books I really hate" section.

Position is typically managed via an array or linked list of elements, an
explicit index, or a unique position value per element. In practice, order
often just mirrors how information was gathered — for example scanning a
source document section by section — so the common case is simply appending
each new element to the end as it's produced, rather than computing position
explicitly.
