---
type: concept
title: WHO WHAT WHEN WHERE WHY for Documents
description: >
  Beyond explaining how something works, a technical document should
  answer who it is for, what job it does, when it was last reviewed,
  where it canonically lives, and why a reader should care — usually in
  the opening paragraphs.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 12"
---

Most technical writing concentrates on **HOW**, but the opening of a document should also settle four framing questions that HOW alone leaves implicit:

- **WHO** — the audience. Sometimes this needs an explicit callout ("For new engineers on the Secret Wizard project") rather than leaving readers to infer it.
- **WHAT** — the document's purpose. Stating it explicitly helps keep the page focused; material that does not serve the stated WHAT probably belongs in a separate document with its own purpose.
- **WHEN** — when the document was created or last reviewed. Note the date if the publishing system does not track it automatically — stale-looking undated docs erode trust even when the content is still correct.
- **WHERE** — where the canonical copy lives. Prefer version control alongside the code or system the document describes; collaborative drafts may live in a wiki or doc editor, but durable records should move to an owned, reviewable home (see [documentation as code](documentation-as-code.md)).
- **WHY** — what the reader should take away. State it in the introduction and use it when writing a summary to check whether the document met its original expectations.

Nearly every document longer than a trivial note should have at least **beginning, middle, and end** sections — a one-section document rarely has only one thing to say. Sections give readers a roadmap. **Useful redundancy** is allowed: state and summarize the key point up front, then make the detailed case in the body, so an important conclusion buried mid-page is not lost to skimmers — the same discipline as [point-first paragraphs](point-first-and-point-last-paragraphs.md) and [pyramid structure](pyramid-structure.md), applied at section scale.
