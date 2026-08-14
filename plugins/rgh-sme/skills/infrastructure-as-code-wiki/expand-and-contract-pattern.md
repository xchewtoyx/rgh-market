---
type: concept
title: "Pattern: Expand and Contract"
description: Changing a live provider's interface in three safe steps — add the new resource alongside the old one, migrate consumers over, then remove the old resource — rather than replacing it in a single risky operation.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 21"
---

Expand and contract (also called *Parallel Change*) changes a live [provider stack's](test-fixtures-for-infrastructure-stacks.md) interface in three separately-delivered, separately-tested steps rather than one: first *expand* by adding the new resource while leaving the old one in place and unaffected; then migrate each consumer over to the new resource one at a time (which may mean creating a new consumer-side resource attached to the new provider resource, cutting traffic over to it, and only then removing the old consumer-side resource); finally *contract* by removing the now-unused old provider resource once every consumer has migrated. Each step goes through the ordinary [delivery pipeline](infrastructure-delivery-pipeline.md), so each one is independently tested and independently reversible.

The pattern exists specifically for the case where a [backward compatible transformation](backward-compatible-infrastructure-transformation.md) isn't enough — where applying new code to a *live* instance would need to destroy or detach resources still actively serving traffic, which most platforms will refuse to do, or will do disruptively. By keeping the old resource alive and functioning throughout the expand step, and only migrating consumers when they're individually ready, no single step ever needs to destroy something still in use.

Expand and contract is the safer, fully pipeline-delivered alternative to [infrastructure surgery](infrastructure-surgery-technique.md), which achieves a similar-looking end state by directly and manually editing a stack tool's own state/data structures — a much higher-risk, non-idempotent operation that should be reserved for situations expand and contract genuinely can't reach, followed by a blameless postmortem whenever it's used.
