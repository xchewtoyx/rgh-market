---
type: concept
title: Pull Complexity Downwards
description: >
  When a module has unavoidable complexity related to its own functionality,
  the module should absorb it internally rather than pushing it onto its
  callers — it's more important for a module to have a simple interface than
  a simple implementation.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 8"
---

Most modules have more users than developers, so it's a better trade for the
(few) developers to absorb extra suffering than for the (many) users to each
absorb a share of it. The one-line design ethic: when developing a module,
actively look for opportunities to take on a bit of extra difficulty yourself
in order to reduce the difficulty imposed on the module's users.

The tempting opposite behavior is to solve the easy problems yourself and
punt the hard ones to callers: throwing an exception when unsure how to
handle a condition, or exporting a
[configuration parameter](configuration-parameters-as-incomplete-solutions.md)
when unsure of the right policy. Both feel easier in the moment, but they
amplify complexity by forcing *every* caller or administrator to deal with a
problem that one developer could have solved once.

Worked example: a line-oriented text-class interface is simple to implement,
but pushes line-splitting and line-joining work onto every piece of
higher-level UI code, since UI operations routinely cross or land mid-line.
A [character-oriented interface](interface-vs-implementation-abstraction-gap.md)
pulls that complexity down into the text class instead — the class's own
implementation gets more complex, but it's a net win because the complexity
is now encapsulated in one place rather than duplicated across every caller.

This isn't unconditionally good; see
[limits of pulling complexity down](limits-of-pulling-complexity-down.md) for
when absorbing complexity backfires.
