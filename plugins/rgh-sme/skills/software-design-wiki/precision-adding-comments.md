---
type: concept
title: Precision-Adding Comments
description: >
  One way to sit at a different level of detail than the code is to be more
  precise than it — supplying units, boundary semantics, and invariants that
  a name and type alone can't carry, described in terms of what a variable
  represents rather than how it's manipulated.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 13"
---

Comments pitched at the *same* level as the code tend to just
[repeat it](comment-repeats-code-red-flag.md); one way to avoid that is to go
more precise. This is most valuable on variable declarations — instance
variables, parameters, return values — since names and types alone are
typically imprecise. Worth spelling out explicitly: units; whether boundary
conditions are inclusive or exclusive; the meaning of a permitted null value;
who owns responsibility for freeing or closing a resource-holding variable;
invariants that always hold (e.g. "this list always contains at least one
entry").

The scoping rule for "obvious from the code": obvious from the code *right
next to the declaration*, not from scanning every use site across the whole
application. A good declaration comment should make that broader search
unnecessary.

Worked example: `// Current offset in resp Buffer` clarifies nothing about
what "current" means; `// Position in this buffer of the first object that
hasn't been returned to the client.` does. A field named `lineWidths` with a
comment reading "Contains all line-widths inside the document and number of
appearances" was improved by renaming it to `numLinesWithLength` and writing
a comment that spells out that keys are character-counts-per-line
(deliberately changing "width" to "length" to disambiguate from pixels) and
that values are counts of lines with that length — and stating explicitly
what an absent key means (no lines of that length).

**"Think nouns, not verbs"**: describe what a variable *represents*, not how
the surrounding code manipulates it over time. A verbose comment describing
when `receivedValidHeartbeat` gets toggled true and false, and by which
threads, was replaced by a comment simply stating what `true` currently means
("a heartbeat has been received since the last time the election timer was
reset") plus its cross-thread role — the toggle behavior is easy to infer
from that, and the comment itself became both shorter and more useful.
