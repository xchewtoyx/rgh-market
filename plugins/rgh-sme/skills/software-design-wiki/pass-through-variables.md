---
type: concept
title: Pass-Through Variables
description: >
  A pass-through variable is threaded as a parameter through a long chain of
  method calls purely so a low-level method can eventually use it, forcing
  every unrelated method in between to carry it too.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 7"
---

Example: a `cert` command-line argument needed only by a low-level
socket-opening method, threaded as an explicit parameter through every
function on the call path from `main` down to where it's actually used, even
though every intermediate function just forwards it without touching it.

The cost compounds over time: every intermediate method's signature has to
carry a variable it never uses, and adding a *new* such variable later (say,
retrofitting certificate support after the fact) can require touching many
unrelated signatures along every affected call path.

Three ways to eliminate a pass-through variable, in roughly ascending order of
how often they apply:

- **Route it through a shared object already available to both ends** — if
  the top and bottom of the call chain already share access to some other
  object, stash the variable there instead of threading it explicitly.
  Caveat: that shared object might itself have reached the bottom via
  pass-through, just moving the problem rather than solving it.
- **Make it a global variable** — avoids threading entirely, but reintroduces
  classic global-state problems, notably making it impossible to run two
  independent instances of the system in one process, a capability that's
  often useful in testing even when it looks unnecessary in production.
- **Route it through a [context object](context-object-pattern.md)** — the
  usual preferred solution: one object per system instance holding all the
  state that would otherwise be pass-through or global.
