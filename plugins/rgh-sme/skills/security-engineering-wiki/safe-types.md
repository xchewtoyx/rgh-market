---
type: concept
title: Safe Types for Security Properties
description: >
  Encode security-relevant properties (well-formed URL, safe SQL, safe
  HTML) in dedicated types whose constructors enforce the contract, so
  whole-application injection safety reduces to understanding the types.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), chs. 6, 12"
---

# Safe Types for Security Properties

Many security properties are assertions about *values* flowing through a
system. A plain string carries no assertion — code assuming "this string
is a well-formed https URL" is implicitly trusting every upstream caller
to have validated it, so verifying correctness means reading all callers,
transitively. Instead, represent the value as a type whose contract *is*
the property: `Url.parse(String)` validates at construction and returns a
`Url` or throws. Now understanding splits into two small parts — inspect
the type's constructors in isolation (they guarantee the contract), then
reason about consumers using the contract as an assumption. The code that
merely passes instances around no longer needs reading.

**Injection prevention is the killer application.** Data flows from
frontend through backends into storage and back out to an HTML template
(stored XSS) are far too complex for humans to review exhaustively. With
safe types:

- Constructors/builders for `SafeSql`, `SafeHtml`, etc. ensure every
  instance is safe for its sink context, via runtime validation,
  correct-by-construction builder APIs, or context-sensitive autoescaping
  template systems.
- Sinks accept only the safe type — a SQL API taking `SafeSql` is safe
  by construction — or, if they accept raw strings, take responsibility
  for validating/encoding at runtime themselves.

The result: an assertion that the *entire application* is free of SQL
injection or XSS, based solely on understanding the type implementations
and typed sink APIs — a tractable
[TCB-like](trusted-computing-base.md) core for the
[invariant](security-invariants.md). Caveat: language encapsulation is
not a security boundary — reflection and casts can pierce it — so the
argument holds against *nonmalicious mistakes* in the codebase, with
repository access controls, code review, and audit trails covering the
actively-malicious-code case.

**Enforcement mechanics.** Prepared statements/bound parameters prevent
SQL injection, but a *guideline* to use them doesn't scale — every
developer must remember, every reviewer must check (and reviewers can't
hold global context about which arguments carry user input across all
transitive callers). Instead make mixing user input into SQL impossible:
`TrustedSqlString` accepts only compile-time constants, enforced per
language (Go package-private type alias that only literals convert to;
Java Error Prone `@CompileTimeConstant`; C++ template constructors). For
HTML, per-context types (`SafeHtml`, `SafeUrl`, `TrustedResourceUrl`)
with builders and strict contextually autoescaping templates; untrusted
HTML goes through a sanitizer. Google code-generates builders in each
language from one declarative config of element/attribute contracts.

**Escape hatches, reviewed.** Some features legitimately need arbitrary
strings (user-supplied analytics SQL). Provide an explicitly unsafe
package (`unsafequery.String`) gated on security-engineer approval. The
review load is small (one part-time rotating engineer per hundreds of
developers), reviews stay interesting and thorough, and repeated
exemption requests for the same use case are the signal to build a safe
library for it. Start libraries small and simple for common cases rather
than handling every corner (triple-nested escaping contexts, authz DSLs
as expressive as a programming language) — simple libraries get adopted.

**Rollout into legacy code.** New code on safe-typed frameworks showed
*two orders of magnitude* fewer XSS reports than carefully reviewed code
without them — with the residue in components not using safe types. For
existing code: exempt legacy callers (e.g. `@RestrictedApi` with a
legacy-allowlist annotation, or build-visibility allowlists), block new
uses via commit hooks, let active development drift to the safe overload,
then clean up the tail manually. Consolidate exemptions into a single
obvious legacy-conversion function per type, so you monitor one function
instead of many APIs.

**Prefer compile-time feedback.** Compiler errors (and IDE underlines)
arrive while the developer has full context, and fixing a type error is
trivial; opt-in linters and review-time findings arrive after the code
"works," when rearchitecting frustrates. Experience favors fast, simple,
explainable syntactic checks over sophisticated whole-program analyses
tuned for false-positive/negative rates — findings from complex checkers
take debugger-grade effort to understand. With quick feedback and easy
fixes, developers embrace inherently safe APIs even where their unsafe
code was actually fine.

Usability makes or breaks adoption: a contextually autoescaping template
feels identical to a normal template minus the escaping chores, so
developers gain productivity while shedding responsibility for the
invariant (see
[secure-by-construction frameworks](secure-by-construction-frameworks.md);
for the same philosophy applied to crypto, see
[secure cryptographic APIs](secure-cryptographic-apis.md)).
