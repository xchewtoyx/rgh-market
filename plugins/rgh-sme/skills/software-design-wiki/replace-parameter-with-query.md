---
type: concept
title: "Refactoring: Replace Parameter with Query"
description: >
  Drop a parameter the function could compute itself, shifting the work of
  producing that value from every caller into the function body — safest
  when the value is derivable from another parameter already present, and
  guarded by referential transparency when it isn't.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 11 (formerly Replace Parameter with Method)"
---

A function's parameter list should summarize its real points of
variability; anything a parameter list makes callers compute that the
function could just as easily compute itself is a form of duplication that
needlessly burdens the caller. This is a responsibility-shifting decision:
with the parameter present, computing its value is the *caller's* job;
removing it moves that job into the function body. The general bias is
toward simplifying the caller's life — shifting responsibility inward — but
only if that responsibility is genuinely appropriate there. This is one of
the targeted cures for the
[Long Parameter List](long-parameter-list-smell.md) smell.

**The main reason to hold back**: removing the parameter might force the
function body to take on a new, unwanted dependency — an awkward function
call, or reaching into a receiver object you'd rather decouple later. The
safest, least controversial case is when the parameter's value can be
derived purely from *another parameter already in the same list* — there's
rarely a good reason to pass two parameters when one determines the other.

**Guard rail**: watch for **referential transparency** — a function
reliably giving the same output for the same inputs. Don't apply this
refactoring if it would mean deriving the removed parameter from a mutable
global, since that would strip the function of a property worth
protecting. See
[Replace Query with Parameter](replace-query-with-parameter.md) for the
inverse move, which exists specifically to *restore* referential
transparency by pushing an internal, non-transparent reference back out to
the caller.

**Mechanics**: if needed, apply
[Extract Function](extract-function.md) on the calculation that currently
produces the parameter's value at the call site. Replace references to the
parameter *inside* the function body with direct calls to that extracted
calculation instead, testing after each change. Use
[Change Function Declaration](change-function-declaration.md) to drop the
now-unused parameter. Turning a local temp value into an accessor first
([Replace Temp with Query](replace-temp-with-query.md)) is a very common precursor to this refactoring,
since it's what makes the parameter's value reachable from inside the
callee in the first place.
