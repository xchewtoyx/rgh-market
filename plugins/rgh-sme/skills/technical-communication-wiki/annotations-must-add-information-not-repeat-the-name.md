---
type: concept
title: Annotations Must Add Information, Not Repeat the Name
description: >
  A caption, comment, or label that only rearranges words already
  present in the thing it labels has added an extra thing to read
  without adding any actual information — a reliable test catches this
  before it ships.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 13"
---

The most common failure in a short piece of explanatory text — a code comment, a figure caption, a table footnote — is that it restates what's already obvious from what it's attached to, at the same level of detail, adding nothing a reader didn't already have. A sharper version of the same failure is an annotation built entirely from the words already in the name of the thing it's describing, plus a stray connective ("to," "the"): a comment reading "Downcast parameter to type" above a method literally called `downCastParameter(parameter, type)` supplies exactly one word — "to" — that wasn't already in the signature. The annotation exists, costs the reader a moment to read, and delivers nothing.

A reliable diagnostic catches this before publishing: **could someone who has never seen the surrounding content produce this same annotation just by looking at what it's attached to?** If yes, the annotation is worthless as written — delete it, or replace it with something that couldn't be derived that way. What such a replacement needs is usually specific: units, a boundary condition (inclusive or exclusive, one-sided or symmetric), what a term actually means for readers who don't already know it, or a piece of context that isn't visible from the label alone. Fixing this kind of comment is a matter of using *different* words than the name already supplies, chosen because they carry meaning the name couldn't — not just words with the same meaning restated more formally.

This is a stricter, more mechanical version of [cutting clutter](cutting-clutter.md): ordinary clutter is a word that isn't earning its place in a sentence, while a name-repeating annotation is an entire piece of supporting text that isn't earning its place at all, and the fix isn't trimming it but replacing it with something that actually says what the name couldn't.
