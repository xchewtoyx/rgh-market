---
type: concept
title: Organizing Documentation by User Goals
description: >
  Structure a documentation set around the tasks and mental models
  readers actually bring to it, not around the internal org chart or
  implementation structure, since most readers arrive by search rather
  than by following a planned path.
sources:
  - title: "Docs for Developers: An Engineer's Field Guide to Technical Writing"
    resource: "Docs for Developers (Bhatti, Corleissen, Lambourne, Nunez, Waterhouse), ch. 10"
---

A documentation set's information architecture has to work for a reader who arrives from search with no context, not only for one who starts at a landing page and follows a planned path — most readers do the former. That means organizing around user goals, tasks, and mental models rather than around the internal structure of the team or product that produced the content; research (search terms actually used, support-ticket themes, observed navigation behavior) is what reveals how readers actually name and group their own problems, which is often different from how the product team names and groups them internally.

Build a predictable hierarchy: a landing page gives orientation and surfaces the most important routes through the content; categories group genuinely related material; and every page title and heading should say exactly what a reader can do or learn there, not just what topic it touches on (see [choosing documentation types](choosing-documentation-types.md)). Consistency matters more than any individual naming choice — consistent naming conventions, page templates, URL structure, and navigation controls let a reader's experience of one page transfer to the next one, and every page arrived at from search should still include prerequisites and next steps so a visitor with no other context can orient themselves and keep going.

Keep each page focused on one purpose, but connect related concepts deliberately through navigation, breadcrumbs, contextual in-page links, and index or reference structures that support both guided, sequential learning and quick lookup by an already-oriented reader. Avoid duplicate, orphaned, and catch-all pages — when readers can't tell which of two similar pages is authoritative, consolidate them rather than leaving both. Because search functions as a primary navigation mechanism in practice, exact terminology, real error messages, and clear page metadata matter as much as the visible on-page structure.

Test the resulting organization with actual users rather than only reviewing it internally: card sorting reveals how readers naturally group content, and tree testing checks whether the chosen labels and hierarchy lead a reader to a specific target using only the navigation structure, with no page prose to lean on. Treat the architecture as living, not fixed — new features, new terminology, and shifts in how users actually talk about the product all require periodically re-testing structure that was correct when it was built.
