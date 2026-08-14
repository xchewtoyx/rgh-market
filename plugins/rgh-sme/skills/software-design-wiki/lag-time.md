---
type: concept
title: Lag Time
description: >
  Lag time is the delay between making a change and getting real feedback
  about it, and unlike the time needed to understand code, it is usually
  self-imposed by unnecessary build dependency rather than an inherent cost.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 7"
---

A change taking a long time to make has two independent causes, easy to
conflate: **understanding** — how long it takes to figure out what to
change — and **lag time** — how long it takes to get real feedback once the
change is made (the build/link/test cycle). A team can navigate its code in
minutes and still be unable to ship a change for hours, purely from (2). Long
understanding time is a symptom of code that's hard to read or badly
structured; long lag time is a symptom of unnecessary
[dependency](dependencies-as-a-cause-of-complexity.md) between the part of
the system you're changing and the parts you have to rebuild or re-run to
find out if it worked.

The analogy: driving the Mars rover Spirit from Earth involves a several-
minute one-way signal delay — issue a command, wait, observe the result,
decide the next move. Most developers work exactly this way with slow
builds: batching several changes together to avoid paying the lag cost too
often, and going *even slower* through debugging when something's wrong,
because each diagnostic step pays the same lag. Unlike the rover's
physics-bound delay, build lag is "completely unnecessary" in most
languages — in principle, dependencies can be broken so any class or module
compiles and tests separately from the rest of the system in seconds, not
minutes.

The cognitive cost compounds beyond wasted wall-clock time: if a short task
can only be attempted once a minute, the mind executes the step and then
idles or wanders while waiting. Compress the interval to a few seconds and
"the quality of the mental work becomes different" — work feels continuous
and engaged rather than like waiting at a bus stop, and mistakes get caught
and corrected far faster. This is the same underlying payoff as
[regression testing as a software vise](regression-testing-as-a-software-vise.md)
and [fast unit tests](unit-testing-fundamentals.md): feedback speed changes
not just how long you wait but how well you think while waiting. The main
obstacle to short lag time in compiled languages is usually unnecessary
compilation of code you don't actually need to rebuild — see
[the dependency inversion principle](dependency-inversion-principle.md) and
[compilation firewalls](compilation-firewall.md) for how that dependency is
broken deliberately, and
[dependency-breaking for testability](dependency-breaking-for-testability.md)
for the underlying family of techniques used to get a single class isolated
enough to compile and test on its own in the first place. When a single
class is too large or too dependency-laden to reasonably isolate on its own,
look for a larger cutset instead — a [pinch point](pinch-point.md), a place
where writing tests is comparatively easy for a whole cluster of related
classes at once.
