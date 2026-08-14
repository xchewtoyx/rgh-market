---
type: concept
title: Name Length Should Scale With Distance From Use
description: >
  The greater the distance between a name's declaration and its uses, the
  longer and more descriptive the name should be — short names only work
  when a reader can see the whole usage span at once.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 14"
---

A genuine counter-view holds that long names obscure what code does, and
favors very short — sometimes single-letter — names throughout (`i`, `n`, `b`
instead of `index`, `count`, `buffer`). Weighed against that: a reader
usually doesn't find the longer names harder to read — if anything, a name
like `count` communicates immediately, whereas a name like `n` requires
actively hunting for its meaning. A short name used *consistently*
system-wide for one narrow meaning (always `n` for counts, nothing else) can
work fine for readers steeped in that convention — but reusing the same short
name for different things depending on context (`ch` for character or
channel; `d` for data, difference, or distance) is exactly the ambiguity
pattern that causes bugs like the [`block` naming bug](naming-as-documentation.md):
a violation of [name consistency](consistent-names.md).

Readability should ultimately be judged by the *readers* of a codebase, not
its author — an empirical, audience-driven question rather than a matter of
taste to assert unilaterally. One rule of thumb both sides of that debate
agree on: **the greater the distance between a name's declaration and its
uses, the longer the name should be.** This is why short loop variables
(`i`, `j`) are fine only when the whole usage span is visible at a glance —
see [precise names](precise-names.md) — and why a name used far from its
declaration, or across a wide span of code, needs to carry more information
on its own.
