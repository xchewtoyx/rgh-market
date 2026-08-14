---
type: concept
title: Introduce Instance Delegator
description: >
  Static methods suffer "static cling" — no object seam exists to
  substitute behavior at the call site — so add a delegating instance
  method purely to create one, even when the result looks structurally odd
  on a utility class.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

Static methods are common for two legitimate reasons: implementing the
Singleton pattern, and building utility classes (bundles of stateless
static helpers, like a math library) that exist because no natural object
abstraction was found for a set of related operations. The testing problem
this creates: static methods that are hard to depend on under test suffer
from **"static cling"** — you can't use an [object seam](object-seams.md) to
substitute alternate behavior at a static call site the way you could with
an instance method.

**Mechanism**: add a plain instance method to the static-method-holding
class that simply delegates to the existing static method
([Preserve Signatures](preserve-signatures.md) for the new instance method);
update call sites to obtain an instance of the class and call the new
instance method instead of referencing the static method directly. This
creates a genuine object seam where none existed, since instance method
calls — unlike static calls — can be intercepted via
[subclassing and overriding](subclass-and-override-method.md) or fake
substitution.

Honest aesthetic acknowledgment: applying this to a genuine utility class
with many static methods and few or no instance methods looks distinctly
odd at first — "a class with 5 or 10 static methods and only one or two
instance methods does look weird... even weirder when they are just simple
methods delegating to static methods." The justification is that it's a
cheap, mechanical way to get a real object seam in place and substitute
behavior under test. The long-term cleanup path: once *every* call site has
migrated to go through the delegating instance methods, the static methods'
bodies can simply move into the instance methods and the statics deleted
outright — the delegation layer was only ever transitional scaffolding.

Steps: identify the static method causing test trouble; add a same-signature
instance method that delegates to it; find every call site using the static
method within the area under test, and use
[Parameterize Method](parameterize-method.md) (or another
dependency-breaking technique) to get an appropriate instance supplied to
each call site so it can go through the new instance method instead.
