---
type: concept
title: Boolean Field Conventions
description: >
  Naming and default-value rules for yes-no wire fields so clients parse intent
  without double negatives or ambiguous zero-value defaults.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 5"
---

Use Booleans for simple flags, but watch for sprawl into many related toggles
(`allowChatbots`, `allowModerators`, `allowChildren`, …) — a structured field
or enumeration usually scales better.

**Positive naming:** prefer `allowChatbots` over `disallowChatbots`. Double
negatives (`if (room.disallowChatbots === false)`) add cognitive load versus
`if (room.allowChatbots)`.

**Zero-value default trap:** in formats without true null for primitives (for
example Protocol Buffers before optional fields), unset Booleans default to
`false`, so you cannot distinguish "user omitted the field" from "user
explicitly set false." One pragmatic fix: choose polarity so the zero value
*is* the desired default (name `disallowAnonymousUsers` when anonymous access
should default to allowed). That locks the default into field semantics
permanently — trading future default changes for wire clarity.

See [missing versus null policy](missing-versus-null-policy.md) for the
broader absent/null/default model across primitive types.
