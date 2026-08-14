---
type: concept
title: Monster Methods
description: >
  A monster method is so long and complex that touching it feels
  dangerous — bulleted (flat, low-indentation) and snarled (deeply nested)
  are the two recurring shapes, and which shapes are available changes
  entirely based on whether a safe automated Extract Method tool exists.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 22"
---

Ordinary long methods are a recurring, often-avoidable pain (see
[sprout method](sprout-method.md)); a **monster method** is qualitatively
different — "so long and so complex that you really don't feel comfortable
touching it," potentially hundreds or thousands of lines, with indentation
scattered enough that navigation itself becomes hard.

Two recurring shapes, blending in real code rather than being sharp
categories: **bulleted methods** have minimal overall indentation — a flat
sequence of chunks, like a bulleted list. This deceptively invites naive
"extract each chunk as a method" treatment, but chunks are often coupled by
shared temporary variables declared in one chunk and used in the next, so
naive copy-paste extraction frequently isn't safe. **Snarled methods** are
dominated by one large indented section, from a single big conditional up to
several nested layers of conditionals and loops. Diagnostic test: try to
line up the method's blocks by hand; if you feel vertigo, it's a real
snarl. Nesting itself blocks writing tests that pin down behavior at that
depth, and many snarls have long bulleted stretches buried deep inside them.

**Tooling changes the whole approach**: a safe automated Extract Method
tool's own analysis can guarantee an extraction is behavior-preserving,
meaning you don't need tests in place first to validate it — see
[using an automated refactoring tool exclusively without tests](automated-refactoring-tool-exclusive-use.md).
Without such a tool, correctness has to come from tests, which is exactly
what's hardest to get for a monster method in the first place — see
[introduce sensing variable](introduce-sensing-variable.md),
[extract what you know](extract-what-you-know-and-coupling-count.md), and
[gleaning dependencies](gleaning-dependencies.md) for the manual techniques
that substitute for tool-verified safety.
