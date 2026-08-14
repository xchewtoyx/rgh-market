---
type: concept
title: "Refactoring: Inline Class"
description: >
  Fold a class that no longer earns its keep into another class that uses
  it, either because it has been whittled down to a near-empty residue or
  as a stepping stone toward re-splitting two classes along better lines.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 7"
---

Inline Class is the inverse of [Extract Class](extract-class.md). It applies
in two situations. The common case: a class has stopped earning its keep —
most often the residue of earlier refactoring that moved most of its
original responsibilities elsewhere, leaving a near-empty "runt" class not
worth maintaining separately, so what's left is folded into whichever other
class makes most use of it. The second, less obvious use: when two existing
classes have the wrong feature split between them and need reorganizing, it
can be *easier* to first Inline Class them together into one class, then
re-split with Extract Class along better lines, rather than trying to move
features directly between the two originals piecemeal. This generalizes into
a broader reorganizing tactic — sometimes moving elements one at a time
between existing contexts is right, but sometimes it's easier to collapse
contexts together first and then split them apart again along new lines.

**Mechanics**: in the target class, add delegating functions matching every
public function of the source class (pure pass-throughs, for now). Redirect
every external reference from the source class's methods to the target's new
delegators, testing after each change. Move all functions and data from
source into target one at a time — via
[Move Function](move-function.md) and [Move Field](move-field.md) — testing
after each, until the source class is empty. Delete the now-empty source
class.

In practice the migration order can differ from a standard Move Function:
rather than moving the source's methods first, it can be easier to start by
adding a delegating method directly on the target (redirecting callers to go
through the target first) and only afterward move the actual field or logic
across. Once the target is the only remaining referencer of a field, the
usual "keep a working reference from source back to target during the
transition" scaffolding in Move Field becomes unnecessary and can be
skipped.
