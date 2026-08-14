---
type: concept
title: "Refactoring: Pull Up Constructor Body"
description: >
  Relocate constructor logic shared across subclasses up into the
  superclass's own constructor, working around a constructor's stricter
  ordering rules that make the ordinary Extract-then-Pull-Up sequence
  unsafe to apply directly.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 12"
---

Constructors are trickier than ordinary methods because of language-imposed
rules on what can happen when — a superclass constructor must typically run
before subclass-specific initialization. For an ordinary method, the
standard move for shared subclass logic would just be
[Extract Function](extract-function.md) followed by
[Pull Up Method](pull-up-method.md), but constructors' special ordering
constraints mean this needs more careful handling. If the shared logic and
constructor sequencing get too tangled to cleanly separate, fall back to
[Replace Constructor with Factory Function](replace-constructor-with-factory-function.md)
instead, sidestepping the constructor-specific constraints entirely.

**Mechanics**: ensure a superclass constructor exists (creating one if
needed) and that every subclass constructor calls it. Use
[Slide Statements](slide-statements.md) to move any code common across
subclass constructors to sit immediately after the superclass constructor
call. Cut that common code out of each subclass and place it in the
superclass constructor instead, threading through any constructor
parameters the moved code references via the superclass call's arguments.
Test.

**When common logic can't run first** — it depends on subclass-specific
state that isn't assigned until later in the subclass constructor — don't
fight the ordering rules. Apply [Extract Function](extract-function.md) to
pull that trailing shared logic into its own ordinary method, called
explicitly at the end of each subclass constructor, then apply
[Pull Up Method](pull-up-method.md) to relocate that method onto the
superclass, where it's available to every subclass without being
constrained by constructor call-ordering rules at all.
