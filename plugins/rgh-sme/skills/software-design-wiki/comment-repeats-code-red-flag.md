---
type: concept
title: Comment Repeats Code
description: >
  The most common comment-writing failure is restating what's already
  obvious from the adjacent code, often using the same words already present
  in the name of the thing being described.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 13"
---

**Red flag: comment repeats code** — "If the information in a comment is
already obvious from the code next to the comment, then the comment isn't
helpful. One example of this is when the comment uses the same words that
make up the name of the thing it is describing."

Typical instances: `// Add a horizontal scroll bar` immediately above
`hScrollBar = new JScrollBar(...)`, or a comment built purely from the words
already in a method's name plus a stray "the" or "to" —
`/* Downcast PARAMETER to TYPE. */` above `downCastParameter(String
parameter, String type)`, where the only word not already in the signature is
"to." Meanwhile the genuinely useful information — what "normalized" means
for a resource name, what "downcast" actually does, what units a padding
constant uses, whether padding is one- or two-sided — goes unstated.

**Diagnostic test**: after writing a comment, ask "could someone who has
never seen the code write this comment just by looking at the code next to
it?" If yes, delete or improve it.

**Fix pattern**: use different words in the comment than in the name, chosen
to add genuine meaning rather than restate it. Replacing a bare `// padding`
comment on `textHorizontalPadding` with `/* The amount of blank space to
leave on the left and right sides of each line of text, in pixels. */`
supplies units, clarifies "both sides," and spells out what "padding" means
for readers unfamiliar with the term — see
[precision-adding comments](precision-adding-comments.md) for more of this
pattern.
