---
type: concept
title: Command/Query Separation
description: >
  A method should either change state and return nothing, or return a value
  and change nothing — never both — so a caller never needs to read a
  query's body just to know it's safe to call repeatedly.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 10"
---

Principle attributed to Bertrand Meyer: "A method should be a command or a
query, but not both." A **command** may change state but returns nothing; a
**query** returns a value but must not change state. The rationale is
readability and predictability at the call site: a caller shouldn't need to
read a query method's implementation just to know whether it's safe to call
repeatedly without side effects, or whether a command's return value (if any)
is meaningful to check.

See [Separate Query from Modifier](separate-query-from-modifier.md) for the
mechanical refactoring that splits an existing function violating this
principle into a pure query and a pure command.

This discipline is what makes extracting small, well-named methods out of a
tangled legacy method actually pay off: naming the extracted pieces for
*what they accomplish for the caller* (a command like `setDescription(...)`,
a query like `getAccountSymbol()`) rather than *how* they do it (skip naming
things after the underlying GUI widgets or database calls they touch)
deliberately hides implementation plumbing behind an honest command/query
shape — which then makes each piece a clean target for
[Subclass and Override Method](subclass-and-override-method.md) once the
side-effecting pieces are behind their own names.
