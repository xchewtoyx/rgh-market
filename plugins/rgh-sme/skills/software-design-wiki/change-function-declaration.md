---
type: concept
title: Change Function Declaration
description: >
  A function's name and parameters are "the joints in our software systems"
  — how well they're shaped determines how easily new parts can be added
  later, and there is no universally right parameter shape as understanding
  evolves.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 6 (aka Rename Function, Change Signature)"
---

Function declarations are **"the joints in our software systems"** — how
well they're shaped determines how easily new parts can be added later. A
good function name lets you understand what it does from the call site
alone, without reading the implementation, but good names are rarely found
on the first try; fix a name as soon as you know a better one, so future-you
doesn't have to re-derive the understanding a bad name is hiding. Practical
tactic: write a comment describing the function's purpose, then turn that
comment into the name — see [comments as a design
diagnostic](comments-as-a-design-diagnostic.md).

**Parameters get the same "joint" treatment.** They define the context a
function can be reused in, and over-specific parameters constrain reuse and
add coupling — a phone-formatting function that takes a whole `Person`
can't format a company's number, while one that takes the phone number
directly is more broadly usable and decouples the formatting logic from
needing to know about people at all. But the tradeoff isn't one-directional:
passing a whole object instead of one specific field of it *increases*
encapsulation, since future logic needing other properties of that object
won't require changing every call site. **There is no universally right
answer for parameter shape, especially as understanding evolves over
time** — which is exactly why fluency with this refactoring matters: the
joints need to be reshaped as understanding changes, not gotten right once
and left alone.

**Two mechanics variants.** Use **Simple Mechanics** — change the
declaration, then find and update every caller, testing — when you can
update all callers in one pass without trouble. Prefer **Migration
Mechanics** when there are many or hard-to-reach callers, the function is
polymorphic, or the change is more involved: apply [Extract
Function](extract-function.md) to the whole body under the new declaration
(using a deliberately ugly, greppable placeholder name if it needs to match
the old name); test; then apply [Inline Function](inline-function.md) to the
*old* function one caller at a time, testing after each — this is what lets
migration happen gradually instead of atomically. For a **published
API** — callers you don't control — the refactoring can legitimately pause
right after creating the new function: mark the old one deprecated, let
external clients migrate on their own schedule, and only delete the old
declaration once (and if) you're confident every client has moved. "Even if
I'm never able to reach the happy point of deleting [the old function], at
least I have a better name for new code." This deprecate-alongside-the-new
pattern is one instance of the general [interface evolution
techniques](interface-evolution-deprecation-versioning-extension.md) —
here, versioning at the level of a single function signature.

Static typing plus a good IDE makes simple renames close to risk-free
automatic operations; without static types, even good search tooling yields
false positives on ambiguous or overloaded names, which pushes toward
migration mechanics even for what looks like a trivial rename.
