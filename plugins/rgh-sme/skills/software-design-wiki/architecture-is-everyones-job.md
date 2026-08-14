---
type: concept
title: Architecture Is Too Important to Leave to a Few People
description: >
  A single dedicated architect role works only if the architect stays
  embedded in day-to-day work; otherwise the code and the "official"
  architecture silently diverge, and the real safeguard is every
  contributor understanding and owning it.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 17"
---

Long-lived systems drift architecturally as teams lose track of the big
picture and default to editing near known "hack points" rather than
wherever the design actually intends. Three obstacles compound this: the
system is complex enough that grasping the big picture takes real time; it's
complex enough that there effectively *is* no single coherent big picture;
or the team is reactively firefighting enough that big-picture thinking
never happens at all.

A single dedicated architect role can work, but only if the architect stays
embedded in day-to-day work — otherwise the code and the "official"
architecture silently diverge, sometimes to the point that "the architect of
a group has a completely different view of the system than the
programmers." **"Architecture is too important to be left exclusively to a
few people"**: the real safeguard is every contributor understanding and
feeling ownership of the architecture. A team where only a small fraction of
people know the architecture well either burns those few out keeping
everyone aligned, or the rest make mistakes purely from unfamiliarity.

Techniques for building and maintaining that shared understanding across a
whole team include
[telling the story of the system](telling-the-story-of-the-system.md),
[Naked CRC](naked-crc.md), and
[conversation scrutiny](conversation-scrutiny.md). These work equally well
for evolving understanding of an *existing* system and for designing a new
one — "design is design, regardless of when it happens in the development
cycle," reinforcing that [design never actually finishes](continuous-design.md).
Treating design as done while changes keep landing is "no surer way to make
a legacy system worse," since new code then lands wherever's convenient
rather than where a live, shared design model would put it.
