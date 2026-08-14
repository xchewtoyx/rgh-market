---
type: concept
title: Support Logging Versus Diagnostic Logging
description: >
  Log output meant for customers or support staff is observable behavior and
  must be tested; developer-only diagnostic logging is an implementation detail
  and should not drive test design.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 8"
---

Apply the same [observable behavior versus implementation
details](observable-behavior-vs-implementation-details.md) lens to logging as to
any out-of-process side effect:

- **Support logging** — messages for support staff, system administrators, or
  customers tracking workflows. Part of observable behavior; must be tested when
  business requirements mandate it.
- **Diagnostic logging** — helps developers understand internal state. An
  implementation detail; should not be tested.

A logging library's own logs are its entire observable behavior and must be
tested. Business-mandated workflow logging is a business requirement.

## Testing support logging

Because logging touches an out-of-process dependency, use mocks to verify
interactions — but **do not mock raw `ILogger` directly** for support logging.
Introduce a dedicated **`DomainLogger`** (or equivalent) that explicitly lists
all business-required support log entries; verify interactions with that wrapper.
Diagnostic start/end logs can remain raw `_logger.Info(...)` calls.

`DomainLogger` wraps the infrastructure logger in domain language — close in
spirit to **structured logging**, which decouples capturing log data from
rendering it (message template + parameters, rendered later as flat text, JSON,
CSV, etc.).

## Keeping domain logic clean

Injecting `DomainLogger` directly into domain classes reintroduces out-of-process
coupling in the domain model. Prefer [domain events for deferred side
effects](domain-events-for-deferred-side-effects.md): raise `UserTypeChangedEvent`
in the domain; let the controller's dispatcher convert it to
`_domainLogger.UserTypeHasChanged()`. Unit tests assert event creation; the
integration test mocks `DomainLogger` to confirm the interaction.

If support logging is needed in a **controller** (not a domain class), call
`DomainLogger` directly — controllers already orchestrate out-of-process
communication.

## How much logging

Support logging amount is dictated by business requirements. Diagnostic logging
is discretionary — excessive logging clutters code (especially the domain model)
and lowers signal-to-noise ratio. **Guideline**: avoid diagnostic logging in the
domain model; move it to controllers temporarily while debugging, then remove.
Ideally reserve diagnostic logging for unhandled exceptions only.

## Passing loggers

Anti-pattern: resolving `ILogger` via static ambient context — hides the
dependency and masks underlying problems. If injecting a logger into a domain
class feels inconvenient, that signals too much logging or too many indirection
layers; fix the root cause. Always inject dependencies, including loggers,
explicitly via constructor or method argument.

See [mock at system edges](mock-at-system-edges.md) and [defer side effects for
testability](defer-side-effects-for-testability.md).
