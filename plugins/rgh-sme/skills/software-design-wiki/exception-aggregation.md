---
type: concept
title: Exception Aggregation
description: >
  Exception aggregation lets an exception propagate up several stack levels
  to one shared handler, rather than handling many distinct occurrences with
  many distinct, duplicated handlers.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 10"
---

Worked web-server example: naive code wraps every individual `getParameter`
call in its own `catch (NoSuchParameter)` handler inside each URL-specific
service method — duplicated boilerplate, since every handler does
essentially the same thing (produce an error response). The better design
lets the exception propagate uncaught out of the service methods, up to the
top-level request dispatcher, where one handler catches every
`NoSuchParameter` exception from every service method.

This extends further: many distinct error types (missing parameter, wrong
parameter syntax, insufficient permission) can all funnel into the same
single top-level "produce an error response" handler, as long as each
specific error condition carries its own human-readable message generated at
the throw site (`getParameter` produces "parameter 'quantity' not present in
URL"). The top-level handler just extracts and reports whatever message it
receives, without needing to know what actually went wrong. This has good
[information-hiding](information-hiding.md) properties: the top handler knows
how to *format* an error response but nothing about specific causes; each
throwing method knows its own domain-specific failure but nothing about
response syntax. New failure-prone methods added later automatically plug
into the existing error-reporting machinery as long as they follow the same
convention (exceptions inheriting from a shared superclass, carrying a
message). The generalized pattern: for any system processing a stream of
discrete requests, define an exception type that aborts just the current
request and cleans up, caught once near the top of the main request loop —
kept clearly distinct from exceptions meant to be fatal to the whole system.

Aggregation works best when an exception can propagate *far* up the stack
before being handled — the more methods it flows through, the more distinct
call sites one handler covers — which is the mirror image of
[masking's](exception-masking.md) sweet spot (a low-level, widely-shared
method, where letting the exception propagate would only multiply handling
sites instead of consolidating them).

**RAMCloud's crash-recovery example** shows aggregation at a larger scale:
rather than building a bespoke recovery mechanism for every distinct failure
mode, this distributed storage system "promotes" a smaller failure into a
larger one it already has to handle — on discovering a single corrupted
object, it simply crashes the entire server holding it and lets the existing
whole-server crash-recovery machinery reconstruct from other replicas,
instead of writing a separate single-object-repair path. This avoids writing
and maintaining a second recovery mechanism, and it exercises the
crash-recovery path more often, increasing the odds that recovery bugs get
found and fixed. The explicit caveat: this trades higher per-incident
recovery cost for lower mechanism complexity, which only makes sense because
object corruption is rare — promoting a *frequent* error (every lost network
packet) into a full server crash would be impractical. This is a special case
of [general-purpose modules being deeper](general-purpose-modules-are-deeper.md):
aggregation replaces several special-purpose recovery mechanisms with one
general-purpose mechanism covering multiple situations.
