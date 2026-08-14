---
type: concept
title: Sketching and Markup as Reading Aids for Unfamiliar Code
description: >
  Draw informal, disposable diagrams and mark up printed code by hand while
  reading — the artifact's job is to support the current reading session and
  hold your mental state, not to become lasting documentation.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 16"
---

Understanding-gathering *feels* like not working, which tempts people to
rush past it into premature "real" work — "if we can get through the
understanding bit very fast, we can really start to earn our pay." These are
deliberately low-tech antidotes to that impulse: cheap enough to use
constantly, disposable enough that no one mistakes them for a spec.

**Notes/sketching**: when reading gets confusing, draw informal pictures —
name the last thing you saw, name the next thing, draw a line if related.
Explicitly *not* meant to be formal UML — "blobs and lines and shapes that
would be indecipherable to anyone who wasn't there when we drew them" are
fine, because the sketch's job is to support a live conversation and
preserve your mental state while untangling something complex, not to be a
lasting artifact. It tends to spread informally on a team just by one person
starting to sketch out loud with a colleague, without needing to be
mandated.

**Listing markup**: print the code and mark it up by hand, with the style
depending on the goal — different symbols or colors to group related pieces
when separating responsibilities; manually matching brace pairs inside-out
to untangle deeply indented block structure; circling candidate
[Extract Method](splitting-and-joining-methods.md) targets and annotating
each with a coupling count; or, as a manual paper-based alternative to
[effect sketches](effect-sketches.md), marking the lines you're changing,
then everything they affect, then everything *that* affects, recursively, to
build intuition for what needs test coverage.
