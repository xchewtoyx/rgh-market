---
type: concept
title: Token Boundary Inertness
description: >
  Tokenizing two concatenated strings together can yield a different token
  count than tokenizing them separately, so token budgets aren't additive.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

Pasting two prompt elements together doesn't just concatenate their token
arrays — tokenization of a composite string can differ from tokenizing each
piece separately, and the effect is tokenizer-dependent. Example (GPT-3.5+
and earlier GPT-family tokenizers): `"be" + "am"` becomes `"beam"`, which
tokenizes as a *single* token, while `"cat" + "tail"` becomes `"cattail"`,
which tokenizes as *three* tokens (`[c], [att], [ail]`) even though each half
alone was one token. Token count is not additive across a boundary.

This breaks the assumption behind [snippet formatting goals](snippet-formatting-goals.md)'s
inertness property: if you compute a snippet's token length once, in
isolation, and it later gets concatenated against different neighbors, the
actual prompt's token count can drift from your estimate. Practical
mitigations:

- Separate individual prompt elements with whitespace to prevent unwanted
  merging across the boundary.
- GPT tokenizers often have tokens that start with a blank space but not ones
  that end with one — so prefer elements that *start* with a space over ones
  that *end* with one, when you have the choice.
- GPT tokenizers combine multiple consecutive newline characters into fewer
  tokens, so snippets should consistently either never start or never end
  with a newline — never-start is usually easier for application code to
  enforce uniformly.

These rules matter most for
[prompt assembly](prompt-assembly-algorithms.md) logic that budgets context by
token count: get the boundary behavior wrong and the assembled prompt can
silently exceed its budget even though every element's length was checked.
