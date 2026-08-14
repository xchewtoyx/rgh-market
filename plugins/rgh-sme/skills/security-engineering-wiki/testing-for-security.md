---
type: concept
title: Testing for Security
description: >
  Unit and integration tests earn their security value by exercising
  hostile and edge-case inputs, encoding access-control requirements as
  tests, and never using sensitive production data in test environments.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 13"
---

# Testing for Security

Standard unit/integration testing practice (fast, hermetic, reliable
tests; fakes for external dependencies; fixing flakes before developers
learn to ignore results) is assumed here; the security-specific angles:

- **Write hostile-input test cases.** Beyond the happy path: negative
  byte counts, capacity overflows near variable-type limits, malformed
  and malicious input expecting a clean error. Unexpected input
  combinations cause both data corruption and query-of-death
  availability bugs.
- **Turn security requirements into tests.** "Only billing admins of the
  owning group can request quota" translates directly into unit tests —
  especially valuable for access-control checks in complicated
  permission models, where code is hard to reason about and bugs are
  security bugs. Tests written at security-review time pin a bug fix
  against reintroduction by later refactoring.
- **Check that tests can fail.** If replacing new code's condition with
  `if (true)`/`if (false)` fails no tests, the tests are decorative —
  mutation testing automates this check.
- **Never mirror production databases into test environments.** Real
  data is rich but exposes sensitive records to anyone running tests —
  an anti-pattern against [least privilege](least-privilege.md) (see
  [testing with least privilege](testing-least-privilege.md)). Seed with
  nonsensitive data; wiping to a known clean state also reduces flake.
- **Validate correctness against known attacks.** Curated suites like
  Wycheproof test cryptographic implementations against specific known
  attack vectors through standard interfaces; RFC-exhaustive suites
  verify a replacement parser matches the old one's observable behavior.
- **Full coverage isn't absence of bugs** — unknown edge cases and thin
  error handling survive 100% coverage; complement with
  [fuzzing](fuzz-testing.md) and
  [static analysis](static-analysis-for-security.md), and design for
  testability from the start.

Each testing form answers questions the others can't; none substitutes
for another. Integrate all of them into CI/CD so they run consistently —
that integration is what turns techniques into posture
([secure-by-construction frameworks](secure-by-construction-frameworks.md),
[initial vs. sustained velocity](initial-vs-sustained-velocity.md)).
