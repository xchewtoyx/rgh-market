---
type: concept
title: Snippet Formatting Goals
description: >
  A well-formatted prompt snippet is modular, natural in its document, brief,
  and inert — its token count doesn't shift when neighboring text changes.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

Four properties to aim for when formatting a snippet for
[insertion into a prompt](snippet-formatting-by-document-type.md):

- **Modularity** — the snippet should be a string insertable or removable
  with relative ease. Ideally the surrounding document is list-like
  (conversation turns) or tree-like (report sections, structured document
  fields), so a snippet is naturally a list item or tree leaf rather than
  something woven irremovably into surrounding prose.
- **Naturalness** — the snippet should feel organic to the document it's
  embedded in. For code completion, natural-language info belongs in a
  comment, not dumped as plain text between code lines; for conversation or
  report documents, data should be interpolated into appropriately-toned
  prose rather than pasted in raw.
- **Brevity** — fewer tokens for the same content is better, the same budget
  discipline [context engineering](context-engineering.md) applies generally.
- **Inertness** — a snippet's token length should be computable once and stay
  correct regardless of what ends up next to it. See
  [token boundary inertness](token-boundary-inertness.md) for why this isn't
  automatic and what breaks it.
