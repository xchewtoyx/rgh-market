---
type: concept
title: "Refactoring: Change Value to Reference"
description: >
  Replace independent copies of what's conceptually one shared entity with
  a single referenced instance looked up from a repository, once the
  entity needs updating and keeping every copy in lockstep has become the
  real risk.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 9"
---

The complementary problem to [Change Reference to Value](change-reference-value.md):
several logical records point at what is conceptually "the same" underlying
entity — several orders all belonging to the same customer, say. Modeled as
a **value**, each order gets its own independent copy of the customer data;
modeled as a **reference**, every order links to one shared object. If the
shared entity never needs updating, either representation is fine — some
duplication is mildly confusing but rarely a real problem. **The real
trouble appears once the shared data needs updating**: with independent
value-copies, every copy must be found and updated in lockstep, and missing
even one produces silent, hard-to-spot data inconsistency — a specific case
of the general [mutable data](mutable-data-smell.md) risk, made worse
because the duplication itself is often invisible until an update reveals
it. In that situation, converting to a single shared reference is
worthwhile — a single update then becomes visible to every referencer
automatically.

The practical consequence of adopting a single-instance-per-entity model is
usually needing some kind of **repository** to look entities up by
identity, so the object is constructed exactly once and every other
reference retrieves the same instance from the repository rather than
constructing its own copy.

**Mechanics**: create a repository for instances of the shared entity type
if one doesn't already exist. Ensure the constructor of the object that
will hold the reference has a way to look up the correct shared instance
(an ID it can query the repository with). Update that constructor to fetch
from the repository instead of constructing its own copy; test after each
change.

**Two repository population strategies**: "create on first reference" —
the repository creates and caches an instance the first time an ID is seen,
otherwise returns the cached one — is simple but means a typo'd or unknown
ID silently mints a new, spurious entity rather than surfacing an error.
Pre-populating the repository from a known, complete list before processing
any referencing records is the alternative: a reference to an unknown ID
then correctly signals a real data error instead of masking it.

Routing a constructor through a module-level or global repository couples
that code directly to a [global](global-state-opacity.md) — small amounts
of global data are tolerable as long as they stay encapsulated behind a
narrow point of access, but if that coupling becomes a real concern, the
mitigation is to pass the repository in as an explicit constructor
parameter instead.
