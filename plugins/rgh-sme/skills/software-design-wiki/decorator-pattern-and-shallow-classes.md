---
type: concept
title: Decorators Tend to Be Shallow
description: >
  The decorator (wrapper) pattern is a legitimate way to layer functionality
  onto an object, but it tends to produce shallow classes full of pass-through
  boilerplate, and there's usually a better alternative worth checking first.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 7"
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 6"
---

A decorator wraps an object, exposing a similar or identical API while adding
some functionality, with most of its methods delegating straight to the
wrapped object — `BufferedInputStream` decorating `InputStream` (its `read()`
pulls a larger block from the underlying stream and buffers the remainder),
or a `ScrollableWindow` decorating a plain `Window` with scrollbars. The
purpose is legitimate — separating a special-purpose extension from a generic
core — but decorators tend to be [shallow](shallow-modules.md) in practice:
lots of [pass-through](pass-through-methods.md) boilerplate for a small
increment of new functionality. Overuse produces an explosion of shallow
classes — the mechanism behind the Java I/O [classitis](classitis.md) example.

Before reaching for a decorator, consider four alternatives:

1. **Add the functionality directly to the underlying class**, if it's fairly
   general-purpose, logically related, or used by nearly everyone. (Buffering
   is universal enough that it arguably should have been merged into the base
   I/O class rather than split into `BufferedInputStream`.)
2. **Merge specialized functionality into its one use case** instead of
   creating a generic decorator for it.
3. **Merge new functionality into an existing decorator** rather than
   stacking another shallow one on top — fewer, deeper decorators beat many
   shallow ones.
4. **Ask whether it needs to wrap the base object at all** — could it be a
   fully independent, stand-alone class instead? (Scrollbars probably don't
   need to wrap the whole window's functionality.)

Decorators are sometimes the right call, but check these first.

The pattern's real motivation is combinatorial: a class with several optional
cross-cutting behaviors (alarms, logging, notification) would need a
subclass per combination if handled through inheritance alone. An abstract
decorator base holds a wrapped instance and delegates every method by
default; concrete decorator subclasses override just the methods they need
to augment, and decorators can be **nested** at construction time to compose
behaviors (at least one non-decorator "basic" concrete class terminates the
chain). This is also a legitimate way to add a behavior to
[legacy code](legacy-code-definition.md) that can't easily be modified in
place — see [wrap class](wrap-class.md). The caution: layered decorators can
become hard to read, "a lot like peeling away the layers of an onion... 
necessary work, but it does make your eyes water."
