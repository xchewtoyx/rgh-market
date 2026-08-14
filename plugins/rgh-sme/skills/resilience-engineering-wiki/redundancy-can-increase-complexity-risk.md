---
type: concept
title: Added Barriers Can Increase Complexity Risk
description: >
  Fixing a component-level vulnerability by adding a barrier, checker, or
  redundant layer creates new relationships between parts, and that
  relationship growth can make the system less safe even as each part
  individually becomes more reliable.
sources:
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Dekker), ch. 3"
---

The componential response to a failure is almost always to add something: a
barrier, a checklist step, a redundant sensor, an approval gate. Each
addition, considered on its own, looks like it can only help. But a system is
not just its parts — it is its parts *and* every relationship between them —
and each added part multiplies the number of relationships the system now
contains. The drive to make a system more reliable by adding parts therefore
also makes it more complex and more opaque, which can make it *less* safe
overall even though every individual part is now more reliable in isolation.

This is why a fix aimed at one [explanatory
factor](explanatory-vs-change-factors.md) can quietly introduce a new
vulnerability elsewhere: consolidating specialist staffing to fix a
scheduling problem can create shortages in the wards that staffing was drawn
from; standardising a container to fix a supply problem can introduce a new,
previously-impossible cross-connection hazard. The new hazard is often
invisible until it fires, because it lives in a relationship between two
parts that used to be unrelated, not in either part itself.

The practical implication is that "we added a check" or "we added a barrier"
is not by itself evidence of improved safety. Ask what new relationships the
addition created, and whether anyone is positioned to notice if one of those
relationships turns out to be hazardous.

A related cost applies even when the added layer works exactly as intended:
Rasmussen's observation from the nuclear industry is that layered defenses
reduce accident *frequency* but raise the *diagnostic* difficulty of the
accidents that do slip through, because operators must now untangle the
original malfunction plus the effects of every defensive system that reacted
to it, simultaneously. A system that silently auto-corrects small deviations
can mask a growing problem entirely until its correcting capacity is
exhausted and it fails all at once, with no warning the correction was ever
happening — turning a unit built to reduce small errors into the mechanism
that produces one large one. Rasmussen's suggested alternative to piling on
more defense-in-depth is to make malfunctions and corrections **visible** to
the people operating the system, trusting them to notice and diagnose,
rather than trusting an ever-more-elaborate stack of automation to absorb
the problem invisibly. This is the same paradox the
[Swiss cheese model](swiss-cheese-model.md) runs into when its "add another
layer" logic produces an unbounded number of latent pathogens to search for,
and the reason the [systems-theoretic accident
model](systems-theoretic-accident-model.md) treats safety as a property of
the whole system rather than something individual barriers can sum to.
