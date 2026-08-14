---
type: concept
title: "Never Mix Refactoring with Functional Changes in One Commit"
description: >
  Keep a commit either a pure refactoring or a pure functional change, never
  both — a mixed commit hides bugs from reviewers behind an otherwise
  behavior-preserving diff.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 12, Refactoring"
---

[Refactoring](refactoring-preserves-behavior.md) is defined by preserving
existing behavior exactly — which is precisely what makes it dangerous to
combine with a change that's *supposed* to alter behavior. A commit that
mixes the two forces a reviewer to hold both standards in mind at once:
"does this restructuring actually preserve behavior?" and "is this new
behavior correct?" Refactoring diffs are often large and mechanical, and
reviewers habituate to skimming them once the restructuring pattern is
recognized — exactly the frame of mind in which a smuggled-in functional
bug is easiest to miss.

The rule is a discipline for commit boundaries, not a claim that the two
activities can't happen close together in time: refactor in one commit,
verified purely by the fact that behavior hasn't changed; make the
functional change in a separate commit, on top of the now-restructured
code, where the diff a reviewer sees is exactly the intended behavioral
delta and nothing else. This also keeps each commit independently
revertible — if the functional change turns out to be wrong, it can be
reverted without also undoing the structural cleanup that unlocked it in
the first place.
