---
type: concept
title: Effect Propagation Mechanisms
description: >
  A method's change can only reach the outside world through three
  channels — its return value, mutation of an object it was passed, or
  mutation of global/static data — and the last is the sneakiest because
  it's invisible from the method's own signature.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 11"
---

Three mechanisms by which a method's effect can reach code outside itself,
used as a checklist while building an [effect sketch](effect-sketches.md):

1. **Return values used by a caller** — the most easily noticed; scan for
   these first out of habit.
2. **Modification of objects passed as parameters**, when those objects are
   used later by other code. Subtle because most mainstream OO languages
   pass object references "by value" (the handle is copied, not the
   object), so a callee can silently mutate shared state through a
   parameter with no trace in its own return type. C++'s `const` parameter
   qualifier is the named mechanism for blocking this class of effect at the
   type level — though see
   [know your language for effect analysis](know-your-language-for-effect-analysis.md)
   for how that guarantee can itself be locally circumvented.
3. **Modification of global/static data used elsewhere** — "the sneakiest
   way." Worked example: a method that, in addition to updating its own
   object's field, also pushes the same value into some globally-reachable
   display or registry — a side channel completely invisible from the
   method's own signature. Blunt aside on the
   [limits of information hiding](limits-of-information-hiding.md)
   here: **"Information hiding is great, unless it is information that we
   need to know."**

Compressed as a checklist for tracing a specific change: identify the
changing method; if it returns a value, check its callers; if it modifies
any values, check what uses those values, and what uses *those* things,
recursively; check superclasses and subclasses that might touch the same
instance variables or methods; check whether parameters (or objects returned
from calls on them) are used elsewhere by the code being changed; check for
global or static data mutated anywhere in the methods identified so far.

(Aspect-oriented languages introduce an additional propagation mechanism
beyond these three, not covered in depth here.)
