---
type: concept
title: Extract Implementer
description: >
  When the interface name you want is already taken by the class you're
  extracting from, invert the usual direction — copy the class under a new
  name, then strip the original down to a pure interface — rather than
  settling for an awkward interface name.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

[Extract Interface](extract-interface.md) requires naming the new interface,
and often the ideal name is already taken — by the class you're extracting
from. Without a rename-capable IDE, the usual fallback options (an awkward
alternative name, a subset-of-methods name, or an `I`-prefix) are all worth
resisting: an `I`-prefix convention applied inconsistently across a
codebase means "half of the time that you type the name of a type, you'll
be wrong." "Naming is a key part of design. If you choose good names, you
reinforce understanding in a system... if you choose poor names, you
undermine understanding and make life hellish for the programmers who
follow you."

**Extract Implementer inverts the usual direction**: copy the class's full
declaration into a new, differently-named class (convention: a
`Production`-prefix), then strip the *original* class down to nothing but
its public method signatures made abstract, turning the original name into
a genuine interface that the new concrete class implements. Every
construction site across the system is then updated, via compiler errors,
to construct the new concrete class instead. Honest caveat: this move
**doesn't reduce overall dependency** by itself — you've substituted one
concrete class's construction for another's; its value is purely enabling
the interface separation, and it's worth revisiting those construction sites
afterward to see whether a factory could reduce dependency further.

Steps: copy the source class's declaration under a new name; strip the
*original* class to only its public methods with no data, turning it into
an interface; make all remaining methods abstract (watch for accidental
non-virtual overrides in C++); prune now-unnecessary imports from the
interface file, using the compiler to detect which are actually still
needed; make the production class implement the new interface; compile the
production class to confirm full interface coverage; compile the whole
system to find and update every construction site; recompile and test.

**Complication inside an inheritance hierarchy**: if the class being
extracted from is itself both a subclass and a superclass of other classes,
the technique has to be layered — applied once per level of the hierarchy,
inserting a "Production" class at each level and re-pointing subclasses
above it. Once a hierarchy is involved this way, seriously reconsider using
plain [Extract Interface](extract-interface.md) with distinct interface
names instead — "a far more direct refactoring." Extract Implementer's
naming-preservation benefit stops paying for its added structural
complexity once more than one level of hierarchy is in play.
