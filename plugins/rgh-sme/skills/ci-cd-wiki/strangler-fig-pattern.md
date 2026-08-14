---
type: concept
title: Strangler Fig Pattern
description: >
  A migration technique for replacing a legacy system incrementally by
  putting it behind a frozen API and building new functionality alongside it
  until the legacy system can be retired, rather than attempting a big-bang
  rewrite.
sources:
  - title: The DevOps Handbook
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 13, Architect for Low-Risk Releases"
---

# Strangler Fig Pattern

Named by Martin Fowler after strangler vines that grow around a host tree and
gradually replace it. Rather than rewriting a legacy application or service
wholesale ("rip out and replace" — a high-risk, high-lead-time undertaking
where the big cut-over date looms and every old bug has to be reproduced in
the new system), the strangler fig pattern freezes the legacy system behind a
stable, versioned API and builds all new functionality in the new
architecture, calling into the legacy system only when necessary. Over many
iterations, functionality migrates out of the legacy system until it shrinks
and can eventually be retired.

This is the system-level counterpart to [branch by abstraction](branch-by-abstraction.md):
both replace a big, risky, all-at-once change with an incremental one that
keeps the system releasable throughout. Branch by abstraction changes an
implementation detail inside one codebase while staying on trunk; the
strangler fig pattern replaces an entire application or service, external
callers routed through the frozen API rather than through an in-process
abstraction layer.

For the pattern to actually reduce coupling rather than relocate it, the new
"strangler" application must itself stay loosely coupled to the legacy
system — in particular it must go through the legacy system's API rather than
reaching directly into its database. If the legacy system doesn't expose a
clean API, either build one or wrap the messy interaction behind a client
library that exposes a clean one to the rest of the new system.

The pattern also guards against copying the legacy system's incidental
complexity into the replacement: because old business processes often carry
years of accumulated workarounds unrelated to real user need, the safest
increment is the smallest piece of new-architecture work that delivers a real
business outcome, not a literal port of old behavior — deliver that, learn,
and iterate. Each iteration also depends on [independent deployability](independent-deployability.md):
the new services built behind the frozen API need their own release schedule,
decoupled from the legacy system's, or the migration reintroduces the same
coordinated-release bottleneck it was meant to remove.
