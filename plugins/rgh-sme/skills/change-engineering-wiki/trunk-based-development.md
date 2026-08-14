---
type: concept
title: Trunk-Based Development
description: >
  Integrating every change into the mainline at least daily, instead of on
  long-lived feature branches, keeps merge risk low and is a precondition
  for continuous delivery.
sources:
  - title: "Refactoring (2nd ed.)"
    resource: "Refactoring: Improving the Design of Existing Code (Fowler, Beck), ch. 2"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Trunk-Based Development

**Velocity is a team sport**: as teams grow, the antipattern is a subteam
branching off the shared codebase to avoid stepping on others — that
defers integration pain and makes culprit-finding harder later. The
preferred model is continued development at head in a shared codebase,
backed by CI testing, automatic rollbacks, and culprit finding.

Long-lived feature branches create a form of change risk that is easy to
underestimate: integration pain grows faster than linearly with branch age,
because version-control tooling only detects *textual* conflicts, not
*semantic* ones — for example, a rename or signature change on one branch
silently breaking a caller on another branch that never touches the same
lines. A branch that is four weeks old can be more than twice as hard to
integrate as one that is two weeks old, purely from this compounding
semantic drift between the branch and a moving trunk.

Trunk-based development avoids the problem at its source: every developer
integrates with the mainline at least once a day, so no branch lives long
enough to accumulate much semantic drift. Incomplete work that isn't ready
for users is hidden with a feature flag rather than isolated on a branch —
see [feature flag blast radius isolation](feature-flag-blast-radius-isolation.md).
Short-lived branches (hours, not weeks) are still compatible with this
practice; what matters is integration frequency, not the absence of
branches per se. A long-lived branch is only really justified for a
low-trust context (e.g., an open-source project integrating infrequent,
unfamiliar contributors) where the review overhead of frequent integration
isn't available.

Trunk-based development is what makes [working in small batches](working-in-small-batches.md)
possible at the code-integration level, not just the release level, and it
is a load-bearing precondition underneath [continuous deployment vs.
continuous delivery](continuous-deployment-vs-continuous-delivery.md): a
pipeline can't keep trunk always releasable if trunk itself only merges
large, infrequent, semantically-drifted branches. For a large change that
cannot land as one small commit without breaking trunk, [branch by
abstraction](branch-by-abstraction.md) decomposes it into a sequence of
small trunk commits instead of a long-lived branch.
