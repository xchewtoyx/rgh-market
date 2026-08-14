---
type: concept
title: Document Observed Behavior, Not Intended Behavior
description: >
  When documenting a system that has evolved past its original design or
  specification, ground the documentation in what the system actually
  does, verified directly, rather than what it was supposed to do —
  the two quietly diverge, and only one of them is what a reader can rely on.
sources:
  - title: "Working Effectively with Legacy Code"
    resource: "Working Effectively with Legacy Code (Michael C. Feathers), ch. 13"
---

Any system old or organically-grown enough to have outlived its original design documents has two competing versions of "how it works": what the specification, ticket, or original design intended, and what the running system actually does after years of patches, edge-case fixes, and forgotten workarounds. These diverge more than writers expect, and a reader who acts on documentation describing the intended version — because it was easier to write from an old spec than to go verify current behavior — will be caught by the very real gap between the two.

The reliable fix is to treat direct observation as the source of truth and the older intended description as, at best, a hint about where to look. Concretely: exercise the actual behavior (run it, call it, trigger it) rather than describing it from memory of how it was designed, and let what actually happens dictate what gets written down — the goal is a description a reader can act on today, not a historically accurate record of what someone once meant to build. This is uncomfortable when the observed behavior looks like it might be a bug: the right response is not to silently document the bug as if it were correct, nor to silently "fix" the documentation to match the old intent, but to write down what was actually observed and flag it explicitly as suspicious, leaving the question of whether it's a bug worth fixing to a separate decision — conflating "what does this do" with "what should this do" is exactly the failure mode this discipline exists to avoid.

This matters most for reference material — API behavior, configuration effects, error conditions — precisely because a reader consulting reference material is about to rely on it directly, with no separate context to catch a stale claim before it causes a mistake. See [reviewing documentation for fitness of purpose](reviewing-documentation-for-fitness-of-purpose.md) for the complementary discipline of periodically re-checking documentation against the system it describes, since the gap this note is about doesn't just appear once — it reopens continuously as the system keeps changing after the documentation is written.
