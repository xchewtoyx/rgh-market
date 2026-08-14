---
type: concept
title: Thinness After Deduplication Is Fine
description: >
  Once duplication is fully removed and subclasses shrink to almost
  nothing, resist collapsing them further into a single generic method or
  factory — thinness by itself isn't a problem, and the alternatives push
  bookkeeping onto every call site or force every caller to change.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 21"
---

After [systematic duplication removal](duplication-removal-as-emergent-design.md)
leaves a set of subclasses reduced to a constructor and a one-line override
each, it's tempting to collapse the hierarchy further. Two further
collapsing options are worth explicitly considering and usually rejecting:
replacing the whole hierarchy with a single method taking a raw discriminant
parameter (a command-type byte, say) pushes bookkeeping — remembering the
right raw value for each case — onto every call site instead of hiding it
behind a named subclass; one static factory method per original type would
achieve the same shrinkage but force every existing call site across the
codebase to change to adopt it.

The conclusion: **keeping the now-tiny subclasses is fine — thinness by
itself isn't a problem** once the duplication driving the original
complexity is actually gone. A class shrinking down to almost nothing is
evidence the refactoring worked, not a sign it went too far or needs
further collapsing for its own sake.
