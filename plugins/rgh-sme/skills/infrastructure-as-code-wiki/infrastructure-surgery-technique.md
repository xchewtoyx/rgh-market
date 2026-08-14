---
type: concept
title: Infrastructure Surgery
description: Directly editing a stack management tool's own data structures to move, rename, or reassign resources between stack instances without touching the real infrastructure — a powerful but high-risk, non-idempotent technique.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 21"
---

Some [stack](infrastructure-stack.md) management tools (Terraform, for example, via `terraform mv`) expose the data structures that map real infrastructure resources to the code that manages them — the same structures used by the [stack data lookup pattern](stack-data-lookup-pattern.md). Infrastructure surgery uses this access to move a resource from one stack instance's bookkeeping into another's, rename it, or detach it, purely as an edit to that bookkeeping — the underlying resource in the infrastructure platform is never touched.

This can achieve a result that looks like [expand and contract](expand-and-contract-pattern.md) without actually rebuilding anything, but the risk profile is very different: the edits are typically not idempotent (they assume a specific starting state, and behave unpredictably if that assumption doesn't hold), it's easy to make a mistake by hand while doing it, and after the surgery the source code and the tool's bookkeeping must agree, or the next ordinary apply will try to "fix" what you just did — silently recreating or destroying something you meant to keep.

Infrastructure surgery should be viewed as a last resort — it's sometimes genuinely necessary to resolve a live outage — never as a routine technique. Any time it's used, the team should follow up with a blameless postmortem to understand what made it necessary and, ideally, close that gap so [expand and contract](expand-and-contract-pattern.md) or another ordinary, pipeline-delivered approach would have sufficed next time. Even when not editing it, viewing a stack tool's data structures can be a useful debugging aid on its own.
