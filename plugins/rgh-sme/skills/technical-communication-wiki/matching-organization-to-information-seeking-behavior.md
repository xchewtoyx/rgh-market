---
type: concept
title: Matching Organization to Information-Seeking Behavior
description: >
  Readers look for information in different modes — a known item, an
  exploratory trawl, exhaustive research, or refinding something seen
  before — and a document set's organization should support movement
  between these modes rather than assume every reader follows the same
  path.
sources:
  - title: "Information Architecture: For the Web and Beyond, Fourth Edition"
    resource: "Information Architecture (Rosenfeld, Morville, Arango), ch. 3"
---

A simple model of how readers find information — a fixed need, a query, one right answer — fails to describe most real searches: many needs are ambiguous even to the reader who has them, evolve as the reader learns more during the search, don't have a single correct answer, and are shaped heavily by the reader's context and existing knowledge going in. A more useful model distinguishes several distinct modes of seeking, which the same reader may move between within a single session: **known-item seeking** (looking for one specific thing already identified), **exploratory seeking** (gathering a few useful leads and learning as you go, without a precise target yet), **exhaustive research** (trying to find everything relevant to a question), and **refinding** (recovering something the reader has already seen once and wants again). A structure optimized only for known-item seeking — a precise index, a fast search box — actively works against a reader in exploratory mode, who needs to browse and follow associative links instead.

Real seeking behavior also isn't a straight line even within one mode: a reader's request evolves as they collect useful fragments along the way, revising what they're actually looking for based on what they've found so far, rather than executing one fixed query and stopping. Two useful specific patterns: starting from one good item and looking for similar ones (as opposed to starting from a query), and a two-step pattern of first finding the right general area and then searching or browsing within it rather than searching the whole content set at once. An information structure should support this kind of movement between searching, browsing, and directly asking someone — not force a reader down a single prescribed path just because it's the path the writer imagined.

Understanding which modes actually matter for a given audience takes direct evidence, not assumption: search analytics reveal the language readers actually use, which searches succeed and fail, and where the underlying content or structure has gaps; direct observation of a reader in their actual working context (rather than in an artificial interview) reveals behavior and motivation a log file can't. The goal of this research isn't completeness for its own sake — it's a defensible-enough understanding of the major needs and likely behaviors to prioritize which of several possible structural investments (better indexing, more browsing paths, better search) actually matters most, given real constraints of budget and effort. See [the curse of knowledge and audience research](curse-of-knowledge-and-audience-research.md) for the equivalent research discipline applied to what a reader needs to accomplish, as distinct from how they go about looking for it.
