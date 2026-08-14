---
type: concept
title: Pull Up Feature
description: >
  Pull a dependency-clean cluster of methods up into a new abstract
  superclass, leaving the dependency-laden methods behind — a test-only
  subclass of the superclass can then be instantiated freely, even though
  the split reflects no strong conceptual boundary.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

Compare [Pull Up Method](pull-up-method.md) and
[Pull Up Field](pull-up-field.md), the similarly-named design refactorings
aimed at removing duplication across siblings rather than at test
isolation.

Use when you need to work with a specific cluster of methods on a class, and
the dependencies blocking instantiation are **unrelated** to that
cluster — the wanted methods don't directly or indirectly touch the
problematic dependencies. This is judged more direct, for this shape of
problem, than [Expose Static Method](static-as-a-staging-area.md) or
repeated [Break Out Method Object](expose-static-method-and-break-out-method-object.md).

Mechanism: pull the wanted method — and everything it depends on — up into a
new abstract superclass, leaving the untouched, dependency-laden methods
behind in the original concrete class. A test-only concrete subclass of the
new abstract class can then be instantiated freely, since the bad
dependencies never made it into the class hierarchy above the split point.

Honest design assessment: explicitly judged "less than ideal" — the
resulting split doesn't reflect a strong natural conceptual boundary, and
the spread "can be confusing if the relationship among the features in each
of the classes isn't very strong." The theoretically better fix (having the
original class delegate to a dedicated collaborator that owns the
problematic dependency) is named directly, with Pull Up Feature offered as
an acceptable, lower-risk **first step** when that fuller redesign feels too
risky to attempt immediately, or other bad dependencies are still in the
way — [Preserve Signatures](preserve-signatures.md) and
[leaning on the compiler](lean-on-the-compiler.md) keep the mechanical move
itself low-risk, with full delegation achievable later once more tests
exist.

The intermediate class is made *abstract* rather than concrete-but-unused
specifically to keep the codebase easy to reason about: "it is great to be
able to look at the code in an application and know that every concrete
class is being used. If you search the code and find concrete classes that
are not being instantiated anyplace, they could appear to be 'dead code.'"

Steps: identify the methods to pull up; create an abstract superclass; copy
the methods there and compile; copy each further compiler-flagged missing
reference up too, using Preserve Signatures throughout; once both classes
compile, create a concrete testing subclass with whatever setup methods the
tests need.
