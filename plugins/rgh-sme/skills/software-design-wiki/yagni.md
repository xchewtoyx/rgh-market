---
type: concept
title: "YAGNI: Build for Understood Needs, Refactor as Understanding Grows"
description: >
  Build only for currently-understood needs, done well for those needs, and
  add complexity-increasing flexibility only once it's proven necessary —
  credible as a strategy only because refactoring exists as its foundation.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 2"
---

**YAGNI** ("you aren't going to need it") argues requirements usually can't
be fully understood up front — people typically only learn what they
actually need once they've used the software. Speculative flexibility
mechanisms, like adding many parameters "just in case," are expensive and
often wrong: guessed-at flexibility frequently doesn't match how needs
actually evolve, and unused parameterization impedes future changes rather
than easing them — see [configuration parameters as incomplete
solutions](configuration-parameters-as-incomplete-solutions.md) for the same
failure mode in a narrower context, and [self-check questions for
calibrating generality](generality-questions-checklist.md) for how to judge
whether a given generalization is earning its keep versus being speculative.

YAGNI's alternative: build only for currently-understood needs, done
excellently for those needs, and [refactor the design as understanding
grows](continuous-design.md); only add complexity-increasing flexibility
once it's proven necessary. A useful calibrating heuristic: estimate how
hard it would be to refactor the capability in later — only add it now if
that would be substantially harder than adding it when actually needed.

This is explicitly not synonymous with "no architectural thinking" — it's
only a credible strategy because [refactoring](refactoring-preserves-behavior.md)
exists as its foundation. Refactoring and YAGNI reinforce each other
bidirectionally: refactoring is what makes it safe to defer a decision, and
a simpler, YAGNI'd system is easier to refactor further when the need
eventually does arrive. This underlying design style is also called simple
design or incremental design, and connects to the broader discipline of
evolutionary architecture.
