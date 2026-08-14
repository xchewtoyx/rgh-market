---
type: concept
title: Integration Versus End-to-End Tests
description: >
  End-to-end tests are a subset of integration tests distinguished by how many
  out-of-process dependencies they touch — run them late and sparingly because
  they are the most expensive to maintain.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 2"
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 8"
---

The [London school](classical-vs-london-unit-testing-schools.md) labels any test
using a real collaborator an integration test; this book uses the **classical
definition**: a unit test verifies a single unit of behavior quickly, in
isolation from other tests; an integration test fails at least one criterion.

Concrete triggers:

- Touching a **shared dependency** (e.g. database) — tests cannot run in
  parallel without interference.
- Touching an **out-of-process dependency** — cross-process calls add hundreds
  of milliseconds per test.
- Verifying **two or more units of behavior** at once (sometimes deliberate
  optimization merging slow tests).
- Verifying modules from **separate teams** together — usually also slow.

**End-to-end tests are a subset of integration tests.** The distinguishing
factor is scope of out-of-process dependencies:

- Typical **integration test** — one or two out-of-process dependencies (database,
  filesystem) — those easiest to automate.
- **End-to-end test** — all or almost all out-of-process dependencies, verifying
  from the end user's viewpoint including external integrations.

The line is blurred; UI/GUI/functional tests are often synonymous terms.

Example (database + filesystem + payment gateway): integration test uses real DB
and filesystem but substitutes a test double for the payment gateway (hard to
automate test accounts); end-to-end test covers everything but runs late in the
build (after unit and integration pass), possibly only on the build server. Even
end-to-end tests may need doubles when no test version of a dependency exists.

**End-to-end versus integration in practice** (Khorikov ch. 8): an end-to-end
test runs against a deployed application with no mocks for out-of-process
dependencies — emulating the external client. Integration tests host the
application in-process, use real managed dependencies, and mock unmanaged ones.
End-to-end tests should not check managed dependencies directly — only
indirectly through the application. Integration tests that mock only unmanaged
dependencies often provide protection close to end-to-end tests, so end-to-end
testing can often be skipped except for one or two post-deployment sanity checks
through the longest happy path.

See [test pyramid](test-pyramid.md) and [integration testing
fundamentals](integration-testing-fundamentals.md).
