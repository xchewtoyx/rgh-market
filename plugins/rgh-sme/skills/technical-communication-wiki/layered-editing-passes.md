---
type: concept
title: Layered Editing Passes for Documentation
description: >
  Edit a draft in a fixed order — accuracy, then completeness, then
  structure, then clarity and brevity — so each pass has a narrow enough
  focus to actually catch its category of problem.
sources:
  - title: "Docs for Developers: An Engineer's Field Guide to Technical Writing"
    resource: "Docs for Developers (Bhatti, Corleissen, Lambourne, Nunez, Waterhouse), ch. 4"
---

Editing documentation is the documentation equivalent of testing and refactoring code, and it works better as several narrow, ordered passes than as one attempt to fix everything at once, because each pass has a different question in mind and mixing them overloads what a single read-through can catch.

1. **Accuracy** — actually execute the documented procedure, across every environment it claims to support, checking names and terminology against the real product; explicitly call out any foreseeable critical failure, data loss, or injury the procedure could cause if followed carelessly.
2. **Completeness** — remove leftover TODOs, state any version or expiration boundaries the content depends on, and bring in a genuinely new reader to expose assumptions the writer can no longer see. This pass has a built-in tension worth naming explicitly: completeness means "enough for the reader to succeed," not "tell the reader everything the writer knows" — the second failure mode buries the useful content as badly as omission does.
3. **Structure** — check that title, headings, prerequisites, templates, and next steps are predictable and match whatever pattern the rest of the documentation set uses, so a reader's expectations from other pages transfer to this one.
4. **Clarity and brevity** — only now, remove duplication and needless words, normalize terminology, avoid idioms, slang, or biased language that don't travel to every reader, and check remaining stylistic questions against a public style guide rather than individual preference. See [cutting clutter](cutting-clutter.md) and [correctness versus clarity](correctness-versus-clarity.md).

A repeatable process pairs this pass order with review from other people: self-review against a fixed checklist (purpose stated early, working title and headers, procedures actually tested, concepts and links checked, prerequisites and next steps present) before handing a draft to peer and technical reviewers. State explicitly what kind of review is being asked for and where feedback should go. Early reviewers should already know the product, since they can catch accuracy problems fastest; later reviewers should resemble the actual intended audience, since they're the ones who can tell whether the document works for someone who doesn't already know the answer. Targeted expert review of one unfamiliar area is faster and more reliable than a single writer trying to independently learn every integration domain a document touches.

When integrating feedback, go through it one reviewer at a time and weigh every comment rather than accepting all of them automatically; resolve disagreement between reviewers by asking what best serves the reader, not by seniority. The most useful review pattern is Pixar's "plussing": criticize an idea only alongside a constructive proposed improvement, focus comments on the work rather than the person who wrote it, and give the writer time to actually respond rather than treating review as a final verdict. Treat review feedback as being about making knowledge communicable, not about judging the author — and explicitly acknowledge useful help and strong writing worth other people emulating, not only what needs to change.
