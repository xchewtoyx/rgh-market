---
type: concept
title: "Parse, Don't Validate: Encoding Invariants as Types"
description: >
  Give a validated value its own type constructed only through a validating
  factory, so downstream code can treat the invariant as an assumption
  instead of every caller re-checking or re-trusting the raw value.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 6, Understanding Complex Data Flows"
---

A plain string carries no assertion about whether it's well-formed — "the
string type itself confers only that the value is a sequence of characters
... any other assumptions are implicit." Code downstream that assumes a
string is, say, a well-formed URL is only correct if *every* upstream path
that could produce that string actually validated it — and confirming that
requires reading and understanding all upstream code, not just the
downstream consumer. This is the general failure mode
[primitive obsession](primitive-obsession.md) names for design quality;
here the stakes are correctness and security, not just readability.

The fix is to represent the validated property as a dedicated type (e.g. a
`Url` class) whose *only* way to come into existence is through a
constructor or factory (`Url.parse(String)`) that performs the validation
and either returns a well-formed instance or signals failure — never a
half-validated one. Once that holds, understanding any code that consumes a
`Url` no longer requires re-tracing every caller: you inspect the type's
constructors once, in isolation, to confirm they enforce the
[invariant](invariants.md), and then treat "this is a `Url`" as a
established fact everywhere the type appears. This is the same underlying
mechanism as [information hiding](information-hiding.md) — the validation
decision is hidden inside the type's construction path — applied
specifically to shrink the amount of code a reader must inspect to trust a
property, rather than only to simplify an interface.

The same pattern generalizes past "is this well-formed" to "is this safe
for a specific sink": a `SafeSql` or `SafeHtml` type whose builders
guarantee every instance is safe to interpolate into a SQL query or HTML
document respectively lets a reviewer establish "this application is free
of SQL injection/XSS" by inspecting only the type's construction code and
the sink APIs that accept it — never the application code that merely
passes instances of the type around. Sink APIs that only accept the safe
type (not a raw string) make this enforceable rather than advisory: nothing
outside the type's own construction path can produce an instance that
skipped validation.

This differs from [defining errors out of existence](define-errors-out-of-existence.md),
which redesigns an operation's *semantics* so an error condition becomes a
well-defined normal outcome. Parsing into a validated type instead keeps a
real failure case at construction time, but confines the cost of checking
for it to one place — the factory — so every other piece of code that
handles the resulting value is freed from re-checking or re-trusting it.
