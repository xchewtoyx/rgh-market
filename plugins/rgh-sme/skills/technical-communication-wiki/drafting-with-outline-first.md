---
type: concept
title: Drafting from an Outline
description: >
  Draft a document by first fixing its audience, purpose, and type, then
  building an outline as documentation pseudocode — cheap to restructure
  before any prose commits effort to a particular order.
sources:
  - title: "Docs for Developers: An Engineer's Field Guide to Technical Writing"
    resource: "Docs for Developers (Bhatti, Corleissen, Lambourne, Nunez, Waterhouse), ch. 3"
---

Before drafting a specific page, state its audience, purpose, and [documentation type](choosing-documentation-types.md) explicitly — not as a mental note, but written down, since it's cheap to check a draft against those three things and expensive to discover mid-draft that they were never actually settled. The tool used to write doesn't matter much; using a familiar editor and an existing code-review workflow reduces friction more than switching to a purpose-built documentation tool does.

A page's **title** should be the shortest, clearest, user-oriented restatement of its purpose — it has to tell someone scanning a list of links what goal the page will help them reach, not just what topic it covers. A page should have one goal; if a draft is accumulating several, that's usually a sign it should split into several documents rather than one page trying to serve all of them.

Build the outline in two passes: first list the concepts or subtasks the page needs to cover without worrying about their order, then arrange that list into the sequence the reader will actually need, filling in prerequisites, setup, verification steps, and any known friction points from research. Treat the outline as documentation pseudocode — a structure cheap to review and rearrange before prose has been written around it, the same way a code outline is cheap to change before it's implemented. When the right structure genuinely isn't obvious, this is also the cheapest point to [sketch a second, radically different outline](sketching-competing-outlines-before-committing.md) for comparison, rather than committing prose to the first shape that seemed workable. Once a draft stalls, the fix is usually not more thinking but less: write a deliberately imperfect first pass leaning on the outline and the [research artifacts](documentation-research-artifacts.md) already gathered, set a small time box, and defer polishing entirely to a later editing pass — see [layered editing passes](layered-editing-passes.md) and [separating drafting from revision](separating-drafting-from-revision.md).
