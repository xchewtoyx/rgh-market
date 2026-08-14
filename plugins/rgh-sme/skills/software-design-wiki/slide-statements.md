---
type: concept
title: "Refactoring: Slide Statements"
description: >
  Move a statement to sit next to related code it belongs with, subject to
  four interference conditions that determine whether the slide preserves
  behavior — most often done as groundwork that makes a later Extract
  Function possible.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 8 (formerly Consolidate Duplicate Conditional Fragments)"
---

Code is easier to follow when related things sit physically near each
other — statements touching the same data structure should cluster rather
than being interleaved with unrelated code. At its simplest this is a
readability move (declaring a variable right before its first use, rather
than declaring everything up front), but its more common use is as
**preparatory groundwork for another refactoring**, especially
[Extract Function](extract-function.md): a clump of logic often can't be
extracted into its own function until its pieces are actually adjacent in
the source.

**Mechanics**: identify the destination position, then scan every statement
between the source and target positions for interference. Four concrete
no-go conditions — abandon the slide if any hold: a fragment can't slide
*backward* past the declaration of anything it references; it can't slide
*forward* past anything that references it; it can't slide over any
statement that *modifies* something it references; and a fragment that
itself modifies something can't slide over any other statement that
references that modified thing. Otherwise, cut and paste the fragment into
position; test. If the test fails, don't push through — break the slide
into smaller steps, either sliding over less code at once or shrinking the
fragment being moved.

**Reasoning about interference**: a bare declaration with no side effects
and no outgoing references can be freely slid forward as far as its first
real use — a very common prerequisite before extracting the surrounding
logic. A side-effect-free assignment can likewise slide down over other
side-effect-free code without issue; reasoning confidently about "side-
effect-free" in practice depends on the code actually following
[Command/Query Separation](command-query-separation.md) — otherwise
verifying it means checking inside the called function, and everything it
calls, transitively.

The naive rule "can't slide fragment A over fragment B if they share any
data either one modifies" is **not fully general** — `a = a + 10;` and
`a = a + 5;` can be freely swapped with each other even though both modify
`a`, because their combined effect is commutative. The real requirement is
understanding what the operations actually do and how they compose, not
applying a rule mechanically. Because reasoning about mutable-state
interference is genuinely hard, reducing how much shared mutable state
exists in the first place — for example applying
[Split Variable](split-variable.md) to a reused variable before sliding
code around it — often makes the later slide easier to reason about and
safer to attempt. With more complex data structures, interference is much
harder to prove by inspection, so tests become the real safety net: slide,
run the tests, see what breaks; unreliable tests mean either extra caution
or investing first in improving the tests for that code, following the same
"take smaller steps" discipline as any other refactoring that starts
failing tests partway through.

Sliding statements *out* of both branches of an if/else, when both branches
end with the same statement, collapses that duplicate line into a single
statement placed after the whole conditional — removing duplication as a
side effect of the slide. The reverse also holds: sliding a statement
*into* a conditional necessarily means duplicating it into every branch.
