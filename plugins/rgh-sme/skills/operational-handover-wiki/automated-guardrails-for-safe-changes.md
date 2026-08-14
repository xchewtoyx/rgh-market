---
type: concept
title: Automated Guardrails for Safe Changes
description: Encoding which changes are safe, discouraged, or prohibited as automated, conspicuous checks rather than relying on a maintainer having read and remembered a prose warning.
sources:
  - title: "Living Documentation"
    resource: "Living Documentation (Martraire), ch. 10"
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 6"
---

A prose warning about a brittle part of a system ("don't change this without checking X first") only protects a maintainer who happens to read it before making the change. An automated guardrail protects every maintainer, including one who never read the documentation at all, by turning the important constraint into a check that fires at the moment the risky change is attempted.

## Building the Guardrail

- **Turn the important decision into a check**: Where a "what's safe to touch" boundary can be expressed as a rule a machine can evaluate (a lint rule, a CI gate, a schema constraint, a required review path), encode it that way instead of, or in addition to, writing it down in prose. The check catches the violation regardless of whether the person making the change read the runbook first. Concrete example: gating a change on its own size (lines changed, or percentage of records affected by a data update) so an accidental oversized or runaway change requires explicit extra approval before it lands, rather than trusting every operator to notice for themselves that a change looks unusually large.
- **Distinguish enforcement from encouragement**: Not every guideline deserves a hard block. Reserve blocking enforcement for changes that are genuinely unsafe; use non-blocking signals (warnings, lint suggestions) for practices that are merely preferred. Treating every guideline as a hard block trains maintainers to route around the tooling; treating nothing as a hard block leaves the genuinely dangerous changes unprotected. A three-tier version of this same idea: hard-mandatory rules that always block, soft-mandatory rules that block by default but allow an explicit, reviewed override, and advisory rules that only warn — the middle tier matters because some constraints are usually but not always violations, and a reviewed override path keeps that judgment call from either becoming an unconditional block or losing enforcement entirely.
- **Make the safe path the easy path**: Where possible, use declarative tooling that makes the correct action the path of least resistance, rather than relying on a maintainer choosing correctly among equally-easy options.
- **Make violations conspicuous**: When a constraint can't be automatically blocked (e.g. a physical or organizational boundary rather than a code-level one), make crossing it visibly obvious after the fact — the equivalent of a "warranty void if tampered with" sticker — so anyone reviewing the system later can immediately see that a protected boundary was crossed, intentionally or not, instead of discovering it only when something breaks.
- **Evolve the rules**: Guardrails encode a point-in-time judgment about what's safe. Revisit and update them as the system changes, the same way playbooks need [ongoing revision](playbook-maintenance-tension.md) rather than being treated as permanent.

## Relationship to Change-Control Process

This is the tooling-level complement to a process-level rule like [Unauthorized Substitution Change Control](unauthorized-substitution-change-control.md): the process rule says a deviation must be routed back through the original design authority; an automated guardrail is what makes that rule actually get followed even by a maintainer who never read the process documentation.
