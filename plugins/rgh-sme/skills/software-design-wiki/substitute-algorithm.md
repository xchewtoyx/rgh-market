---
type: concept
title: "Refactoring: Substitute Algorithm"
description: >
  Rip out a working but unwieldy algorithm and swap in a clearer one
  wholesale, after first decomposing it down to a single isolated function
  so the substitution has a testable seam to compare old against new.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 7"
---

Sometimes you don't want to incrementally decompose an algorithm — you want
to rip the whole thing out and replace it with something clearer. Common
triggers: learning more about the problem reveals an easier way to do it, a
library becomes available that already does what the hand-rolled code does,
or swapping in a different algorithm first turns out to make an *upcoming*
behavior change easier to express than evolving the existing one in place
would.

**Precondition**: the method must already be decomposed as much as
possible before attempting a wholesale swap — replacing a large, tangled
algorithm outright is very difficult; reducing it to something simple first
is what makes the substitution tractable at all. This is why
[Extract Function](extract-function.md) so often pairs with this
refactoring: it isolates the algorithm into its own function specifically to
make it substitutable.

**Mechanics**: arrange the code to be replaced so it occupies one complete,
isolated function. Write tests against that function alone, capturing its
current behavior as a specification —
[characterization tests](characterization-tests.md) if you don't already
understand the existing behavior precisely. Prepare the alternative
algorithm. Run static checks. Run the tests comparing old and new algorithm
output; if they match, you're done — otherwise, keep the old algorithm
around as a reference implementation to compare against while debugging the
new one.
