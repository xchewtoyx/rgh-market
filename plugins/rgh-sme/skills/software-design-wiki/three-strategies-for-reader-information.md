---
type: concept
title: Three Strategies for Supplying Reader Information
description: >
  Nonobvious code is really just code where the reader is missing a specific
  piece of information; the three strategies for fixing that, in order of
  preference, are eliminating the need for it, letting convention supply it,
  or explicitly documenting it.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 18"
---

Reframed through an information lens, every instance of
[nonobvious code](nonobvious-code-patterns.md) reduces to the same shape: the
reader is missing one specific piece of information they need (that a
constructor spawns background threads; what `result.getKey()` actually
represents). Three complementary strategies address this, in order of
preference:

1. **Reduce how much information is needed in the first place** — via
   [abstraction](abstraction.md) and
   [eliminating special cases](design-special-cases-out-of-existence.md).
   This is the best option because it removes the burden entirely rather
   than relocating it.
2. **Piggyback on information readers already have** — following
   [established conventions](consistency-as-a-design-tool.md) and conforming
   to reasonable expectations means readers don't have to learn anything new
   specifically for your code.
3. **Explicitly supply the needed information in the code** — via
   [good names](precise-names.md) and well-placed, well-targeted
   [comments](comments-describe-non-obvious-things.md), for whatever
   information can't be eliminated or inherited from convention.
