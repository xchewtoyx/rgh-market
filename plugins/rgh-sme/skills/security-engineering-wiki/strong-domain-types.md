---
type: concept
title: Strong Domain Types
description: >
  Wrapping primitives in purpose-specific types — User, Width, Radius,
  Duration — catches invalid parameters, implicit conversions, and unit
  confusion at compile time instead of in production.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 12"
---

# Strong Domain Types

Prefer strongly typed languages with static checking: invariants enforced
at compile time surface errors during development, whereas dynamic or
weak typing defers them to testing — or production, on rarely exercised
paths (`[9, 8, 10].sort()` → `[10, 8, 9]` in JavaScript). For
dynamic-by-default languages, add incremental checkers (Pytype for
Python, TypeScript for JavaScript).

Beyond language choice, avoid untyped primitives for domain concepts.
Failure modes of raw strings/numbers:

- **Conceptually invalid parameters**: `AddUserToGroup(string, string)` —
  which is the group? `Rectangle(3.14, 5.67)` — width or height first?
  `Circle(double)` — radius or diameter? Documentation and tests catch
  some of this; `Add(User("alice"), Group("root-users"))`,
  `Rectangle(Width(3.14), Height(5.67))`, `Circle(Radius(1.23))` catch it
  at compile time and self-document.
- **Implicit conversions**: truncation, precision loss, and surprise
  object creation — in C++, `Foo(5)` and `Foo(NULL)` silently construct
  `Bar(is_safe=...)` via coercion; make single-value constructors
  `explicit`, prefer `nullptr`.
- **Unit confusion**: `Timer(30)` — seconds or minutes? The Gimli Glider
  (fuel in pounds vs. kilograms) and the $125M Mars Climate Orbiter
  (imperial vs. metric) are the canonical costs. Types encapsulating
  units (timestamp, duration, weight) expose only sensible operations
  (timestamp−timestamp=duration; timestamp+timestamp is meaningless) and
  explicit conversions (`Duration::ToHours`); Go's `time` and C++
  `chrono` provide these natively.

Strong domain types are the general-correctness sibling of
[safe types for security properties](safe-types.md) — the same mechanism,
aimed at bugs rather than attackers, with the same payoff of shrinking
what a reviewer must read (and distinct types for sensitive data — credit
card numbers, not strings — also restrict serialization and enforce
encryption, preventing accidental exposure).
