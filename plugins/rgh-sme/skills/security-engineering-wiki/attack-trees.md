---
type: concept
title: Attack Trees
description: >
  A structured, recursive decomposition of how an attacker could reach a
  goal — the root is a successful attack, each level breaks it into the
  ways to cause it, and the leaves become concrete scenarios to defend.
sources:
  - title: Software Architecture in Practice, 4th Edition
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 11"
---

# Attack Trees

An attack tree is fault-tree analysis turned toward an adversary instead
of an accident: the root node is a successful attack (an outcome you want
to prevent — data exfiltrated, service taken down, records altered), and
each level below decomposes it into the direct ways that outcome could be
caused. Decomposition continues recursively until the leaves are concrete
enough to reason about directly — a specific vulnerability class, a
specific missing control, a specific credential an attacker could obtain.

This gives threat modeling the same discipline fault trees give
reliability analysis: instead of trying to imagine "how could we get
attacked" as one unstructured brainstorm, you fix the goal first and work
backward systematically, which surfaces paths a free-form discussion would
miss and makes it visible when a whole branch has no mitigation at all.

**Feeding the tree into design.** Each leaf becomes the *stimulus* half of
a scenario: source (who or what triggers this path), artifact (what it
touches), environment (under what conditions), and the response you need
(detect, resist, react, or recover). A leaf with no credible response is
exactly the gap a [security design review](security-design-review.md)
should catch before launch, and the same leaves are what a
[Red Team](red-team-testing.md) engagement or [threat intelligence](threat-intelligence.md)
should be checked against — an attack tree built once and never revisited
only reflects the threats known at the time it was drawn.

Attack trees compose well with other adversary-modeling tools rather than
replacing them: [attacker profiles](attacker-profiles.md) and
[attacker TTPs](attacker-ttps.md) supply realistic branches and leaves
(a capable, resourced attacker reaches leaves a low-skill one can't), and
[insider risk](insider-risk.md)'s actor/motive/action/target frame is a
complementary way to generate scenarios when the "how" is less structured
than a technical attack path.
