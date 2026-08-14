---
type: concept
title: Reviewing Documentation for Fitness of Purpose
description: >
  A structured documentation review checks correctness, completeness,
  consistency, understandability, and fitness for the reader's actual
  task, driven by concrete questions built from stakeholder needs rather
  than a passive read-through.
sources:
  - title: "Documenting Software Architectures: Views and Beyond"
    resource: "Documenting Software Architectures (Clements, Bachmann, Bass, Garlan), ch. 11"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 12"
---

A documentation review asks five separable questions of a draft: is it correct; is it complete enough (not exhaustively complete — enough for its stated purpose); is it internally consistent; is it understandable to its intended reader; and is it actually fit for the specific tasks that reader needs to do with it. Catching a gap or an ambiguity at review time is far cheaper than catching it once someone has already acted on the wrong assumption it created — the review's value is specifically in finding these problems before they become a downstream design, implementation, or integration failure that's much more expensive to trace back to a documentation gap.

A complementary way to assign reviewers is by **which dimension** each person is best positioned to test:

- **Technical review (accuracy)** — usually a subject-matter expert, often a teammate; often folded into code review when documentation lives in the same changelist as the code it describes.
- **Audience review (clarity)** — someone unfamiliar with the domain: a new team member, an API customer, or anyone who resembles the document's primary reader more than its author does.
- **Writing review (consistency)** — a technical writer or volunteer editor checking style, terminology, and structure against team conventions.

High-profile or externally published documents should get more of these review types; even one ad hoc reviewer beats none. When documentation is wired into normal engineering workflow, many pages get implicit audience review over time — the audience eventually uses them and files bugs when something does not work.

The procedure: establish the review's purpose, scope, and who's participating before it starts; distribute preparation material in advance rather than reviewing cold; build a concrete set of questions from the actual stakeholders' concerns and quality goals the document is supposed to satisfy, rather than reviewing against a generic checklist; have reviewers inspect individually first and then collectively, so individual findings aren't lost to groupthink in a live discussion; record every issue found along with an owner and a disposition; and follow up to confirm each issue actually reached closure rather than trusting that raising it was enough. This is sometimes called an Active Design Review: reviewers are given specific questions or tasks to work through against the documentation, not just asked for general impressions — a review built this way surfaces gaps a passive read-through reliably misses, because a reviewer without a concrete task tends to skim for obvious errors rather than actually trying to use the document the way its real audience would.

A good question set for a review typically covers: context and the document's boundary, whether its structural elements and their relationships are documented completely enough, its interfaces, whether the notation used is actually explained, consistency across any related pieces of the document set, traceability back to whatever requirement or need motivated the content, the reasoning behind any quality-relevant claims, the rationale behind decisions recorded in it, and the document's own long-term maintainability. The underlying discipline generalizes past architecture documents specifically: a review works best when reviewers have a concrete problem to solve using the documentation and can point to evidence in the text itself, not when review is a passive presentation the author walks reviewers through. See [layered editing passes for documentation](layered-editing-passes.md) for a complementary, more general editing-focused review sequence.
