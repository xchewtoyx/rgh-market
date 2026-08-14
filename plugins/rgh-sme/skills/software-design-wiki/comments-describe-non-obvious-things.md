---
type: concept
title: Comments Should Describe Things That Aren't Obvious From the Code
description: >
  The core rule for what to write: a comment should describe things that
  cannot be seen from reading the code next to it, not restate what's
  already visible there.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 13"
---

Comments exist because code alone can't capture everything that was in the
developer's mind. Non-obvious things worth capturing: whether a range's
bounding indices are inclusive or exclusive; why some code is needed, or why
it's implemented a particular way; implicit rules a developer must follow
("always invoke a before b") that could in principle be inferred by reading
everything, but shouldn't have to be.

This is why [comments complete the abstraction](comments-complete-the-abstraction.md):
an abstraction is meant to be a simple way to think about something, but code
itself is too detailed to reveal the abstraction directly. Comments can state
the abstraction plainly — "after this method is invoked, network traffic
will be limited to `maxBandwidth` bytes per second." Even when the
abstraction is technically derivable from reading the implementation,
requiring users to do that defeats the purpose of having an abstraction at
all: users should be able to understand a module from its declarations plus
comments, without reading unrelated code.

Obviousness itself is judged from the standpoint of a first-time reader of
the code — never the author, who already knows what it does. The practical
corollary for code review: if a reviewer says something isn't obvious, don't
argue that it actually is — if a real reader found it unclear, it *is*
unclear by definition. The productive response is to find the specific
source of confusion and address it, via a better comment or, sometimes, a
redesign of the code itself if a concept keeps needing lengthy comments to
explain.

See [commenting conventions](commenting-conventions.md) for what to comment
and where, [comment repeats code](comment-repeats-code-red-flag.md) for the
most common failure to avoid, and
[precision-adding](precision-adding-comments.md) and
[abstraction-raising](higher-level-comments.md) comments for the two
directions a good comment can move away from restating the code.
