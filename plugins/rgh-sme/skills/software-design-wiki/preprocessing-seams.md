---
type: concept
title: Preprocessing Seams
description: >
  A preprocessing seam exploits the C/C++ macro preprocessor's raw text
  substitution to swap in test behavior via a conditional define, at the
  cost of maintaining what amounts to several different programs in the
  same source.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 4"
---

A [seam](seam.md) specific to C/C++, exploiting the macro preprocessor,
which runs before compilation and does raw text substitution — a build stage
most languages don't have. Worked example: a call to a real database update
function embedded directly in application code is moved into a separate
header, `#include`d, and inside that header conditionally (`#ifdef TESTING`)
`#define`d as a macro that records its arguments into test-visible globals
instead of calling the real function. The enabling point is the `TESTING`
preprocessor define set at build time.

The explicit caution: heavy production use of `#ifdef`/`#ifndef` conditional
compilation "pretty much force[s] you to maintain several different programs
in the same source code" and hurts clarity, and macros can hide terribly
obscure bugs. This is a double-edged tool worth having specifically in C/C++
because it compensates for those languages' other testing obstacles — not
something to want in a language with better seam options, like
[object seams](object-seams.md).

A second common shape: `#define`ing an entire troublesome call out of
existence under a `TESTING` build (`#ifdef TESTING #define ksr_notify(...)
#endif`), rather than substituting a fake body for it. Defining this inline
in the same file hurts readability and navigation; a cleaner organization
moves the test code (including a `main()` that runs it) into a separate
file `#include`d only under the `TESTING` define, keeping it out of the
normal build entirely otherwise. The scoping rule that makes heavy macro use
tolerable here: **"As long as we restrict rampant usage of macros to code
that runs under test, we don't have to be too concerned that we'll misuse
macros in ways that will affect the production code."** For non-C procedural
languages, which mostly lack a preprocessor at all, a [link seam](link-seams.md)
getting a larger chunk of code under test at once is usually the only lever
available for this kind of obstacle — see
[breaking dependencies in procedural code](breaking-dependencies-in-procedural-code.md).
