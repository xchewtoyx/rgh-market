---
type: concept
title: Error-Reporting Mechanism Is Part of an Interface's Contract
description: >
  How an interface reports failure — exception, status code, queryable
  property, error event, or log stream — must be specified and consistent
  as part of the interface itself, and the right remediation depends on
  identifying the error's actual source.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman, with Cesare Pautasso), ch. 15, Error Handling"
---

Beyond deciding *how many* [exceptions](exception-handling-complexity.md)
an interface should have and where to [define errors out of
existence](define-errors-out-of-existence.md), an interface designer has
to pick and document a **mechanism** for reporting whatever failures remain
— this choice is as much a part of the contract as the operation's normal
return type, and callers need to know it up front, not discover it by
reading the implementation. Common mechanisms: throwing an exception;
returning a status code the caller must check; storing success/failure
state in a queryable property, read separately from the result; triggering
an error event for a failed asynchronous interaction (a timeout); exposing
a dedicated error log stream a caller can inspect after the fact.
Consistency in *which* mechanism an interface uses matters as much as the
mechanism itself — mixing status-code and exception-based reporting across
sibling operations on the same interface is exactly the kind of
inconsistency that raises [cognitive load](cognitive-load.md) for no
benefit.

**Remediation depends on the error's actual source**, not just its
symptom, and a well-designed interface exposes enough for the caller to
tell the two apart:

- A transient failure on an idempotent operation → wait and retry.
- An invalid-input error → fix the input and resend; this is the caller's
  bug, not the callee's.
- A missing or unavailable dependency → the dependency needs attention
  (reinstall, reconnect) before retrying the original operation makes
  sense.
- An implementation bug surfacing as an error → add the failure scenario
  as a regression test case once diagnosed, rather than treating it as a
  one-off.

Common error sources worth planning for explicitly, since an interface's
error-handling strategy should cover all of them up front rather than
being patched in reactively: invalid or illegal input (an unexpected
`null`); the element being in the wrong state for the request (called
before initialization completes, or a write attempted against a resource
that's offline); genuine hardware or software failure (unresponsive
network, exhausted memory); and misconfiguration (a malformed connection
string). Planning for the non-nominal case is as much a part of interface
design as planning for the nominal one — retrofitting it after the
interface is already published is far more disruptive than deciding on it
up front.
