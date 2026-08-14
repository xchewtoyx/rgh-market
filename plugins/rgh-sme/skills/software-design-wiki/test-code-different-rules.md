---
type: concept
title: Test Code Follows Different Rules Than Production Code
description: >
  Hygiene that would be a red flag in production code — empty method
  bodies, public mutable fields, throwaway inline subclasses — is
  acceptable in code that exists only to make testing possible.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 9"
---

"The rules are different for classes we use to make testing possible."
A `FakeConnection` with empty, no-op method bodies and a public field the
test sets directly would be a design smell in production code, but is simply
what a [fake object](fake-objects.md) is for. Likewise, an inline anonymous
or local subclass defined inside a single test method purely to override one
troublesome method is explicitly endorsed for tests even by an author who
avoids the same move in production code: "it is very convenient when we are
testing."

This license is not unlimited — test code is still held to a duplication and
clarity standard of its own (shared setup extracted into a `setUp()` method,
for instance). The relaxation is specifically about exposing internals and
skipping behavior that production code would need, not about tolerating
unclear or duplicated test logic.
