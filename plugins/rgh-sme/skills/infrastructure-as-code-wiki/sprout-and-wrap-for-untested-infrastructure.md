---
type: concept
title: Sprout and Wrap for Untested Infrastructure
description: Adding new, separately-tested infrastructure code alongside an untested legacy stack rather than inlining the change into code that can't be safely verified.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Michael Feathers), ch. 6"
---

When a required change to an untested legacy stack can't be made safely — see the [legacy infrastructure code dilemma](legacy-infrastructure-code-dilemma.md) — one practical fallback is to write the change as new code that itself gets full test coverage, and connect it to the untested stack at as few points as possible, rather than inlining it into code nothing verifies. Two shapes this takes:

**Sprout a new module.** Write the new piece of infrastructure (a resource, a small module, a new role) as its own separately-tested unit, then reference it from the existing stack with a single new resource block or module call — one narrow, easy-to-review addition to the untested code, instead of new logic woven into it. The new module can be tested in isolation before the untested stack ever applies it for real.

**Wrap the existing stack.** When the new requirement needs to run alongside something the stack already does — tagging every resource with a cost-center label, say — rather than editing the untested resource definitions directly, wrap them: a thin outer module that calls the existing (untested) module and then layers the new, tested behavior around it. This works cleanly when the new behavior only needs to happen strictly before or after the existing behavior, not interleaved with it.

Both are a deliberate, honest trade-off, not a design improvement: the untested legacy code stays exactly as untested and risky as it was, and the codebase now has a visible seam between tested and untested territory. That's the point — it makes forward progress possible without pretending the underlying risk has been addressed, and it leaves an obvious, low-cost starting point (the sprout or wrapper's own call site) for whoever eventually brings the wrapped legacy code itself under test.
