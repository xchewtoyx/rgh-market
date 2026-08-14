---
type: concept
title: Wrap Class
description: >
  The class-level analogue of wrap method — add a class that wraps the
  target and layers new behavior around a call to it, either transparently
  everywhere (the decorator pattern) or at just the one call site that needs
  it.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 6"
---

Instead of adding to an existing method like [wrap method](wrap-method.md),
add a *class* that uses that method. If the wrapped class can't be
instantiated for testing directly, extract an interface from it first, then
have the wrapper implement that interface too — this is literally the
[decorator pattern](decorator-pattern-and-shallow-classes.md): a logging
wrapper around an `Employee` interface logs, then delegates `pay()` to the
real implementation.

A non-decorator variant applies when the new behavior is needed at only one
call site rather than transparently everywhere: a plain wrapper class that
takes the target object, calls its method, then adds the new behavior —
instantiated only where it's actually needed, rather than substituted
system-wide.

Steps: identify the change point; if expressible as a single sequence of
statements, create a wrapper class taking the wrapped class as a constructor
argument (extracting an interface first if needed to instantiate it in a
harness); TDD the new method plus a combining method that calls both new and
old behavior; instantiate the wrapper at the point where the new behavior
needs to be enabled.

Reach for wrap class over wrap method — a higher threshold — when either the
new behavior is genuinely independent and shouldn't pollute an
already-focused class with an unrelated low-level concern, or the target
class has grown so large and unwieldy that you refuse to make it worse:
wrapping instead puts a marker in the ground for later cleanup. On that
second case specifically: the real obstacle to improving a bad codebase is
often not the difficulty of the code but the belief it induces — that
nothing small is worth doing when most of the surrounding code is still
murky. Consistent small improvements compound over a couple of months into a
visibly different system, often reaching a psychological tipping point after
which people want to refactor more than strictly necessary, purely because it
now feels good and pays off.
