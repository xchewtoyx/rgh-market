---
type: concept
title: Wrap Method
description: >
  To add behavior that must run strictly before or after an existing
  method's call sites, without interleaving with it, rename the old method
  and reintroduce its old name as a thin wrapper that calls the new behavior
  plus the renamed original — avoiding temporal coupling.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 6"
---

For adding behavior that must run alongside an existing method's call sites
without inlining new logic into it, which risks
[temporal coupling](temporal-coupling.md). Two variants, illustrated on a
`pay()` method needing a new logging step:

1. **Rename-and-delegate**: rename the old method's body to a new private
   name (`dispatchPayment()`), then create a new `pay()` that calls
   `logPayment()` then `dispatchPayment()`. Existing callers of `pay()` are
   unaffected and automatically get the new behavior.
2. **Additive**: leave `pay()` untouched; add a new method
   (`makeLoggedPayment()`) that calls `logPayment()` then `pay()`, giving
   callers an explicit opt-in path rather than changing behavior under them.

The constraint that makes this work at all: the new behavior must run
strictly before or after the old behavior, not interleaved with it — a
feature, not a limitation, when it applies. The real downside is being
forced to invent an artificial new name for the old code (`dispatchPayment`,
which now does more than "dispatch") — something to resolve later, once
tests exist, via further extraction.

Rule of thumb for choosing between [sprout method](sprout-method.md) and
wrap method: reach for sprout method when the existing method still clearly
communicates one coherent algorithm; reach for wrap method when the new
feature is roughly as important as what was already there, which often
yields a cleaner higher-level method afterward once the pieces are
eventually split further (`pay() { logPayment(); amount = calculatePay();
dispatchPayment(amount); }`).
