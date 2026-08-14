---
type: concept
title: Principle of the Moving Part
description: >
  A fixed scale with a moving pointer preserves the whole range and the
  viewer's position within it; a moving scale behind a fixed window hides
  everything outside that window and destroys spatial/trend context.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Sidney Dekker), ch. 4"
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Gary Klein), ch. 6"
---

A classic instrument-design finding, illustrated by comparing two airspeed
displays: a classic round-dial gauge (fixed circular scale, a pointer that
moves around it) versus a modern "speed tape" (a linear scale that scrolls
behind a fixed pointer/window). The round dial keeps the entire scale and
both endpoints visible simultaneously, so the viewer always has spatial
context for where the current value sits within the full range — and the
pointer's angular speed around the dial gives a natural, directly-perceived
sense of rate of change. The speed tape shows only a narrow window of the
scale at any moment, with the endpoints hidden; because rate of change is no
longer visible as a natural property of the display, showing it at all
requires adding an engineered trend-vector arrow as a substitute.

The general principle: prefer a fixed scale with a moving indicator over a
moving scale behind a fixed indicator, because the fixed-scale form preserves
[2-D position](preattentive-attributes-for-dashboards.md) as a natural,
preattentive cue for both current value and rate of change, while the
moving-scale form trades that context away for a narrower field of view. This
is one of the reasons Few's [bullet graph](bullet-graph.md) uses a fixed
scale with a bar and tick marks rather than a scrolling or windowed display —
a viewer can see the whole range, the target, and the current value at once,
with no hidden context.

A more severe version of the same failure is a display with no rate-of-change
cue at all, not even a windowed one. In the USS Vincennes shootdown (July 3,
1988), the ship's combat display showed a tracked aircraft's altitude only as
a raw 4-digit number on a small alphanumeric side display, embedded among
other numeric readouts and with no trend indicator whatsoever. To tell
whether the aircraft was climbing or descending, crew had to mentally compare
successive raw readings themselves — a task the ship's commander later
estimated took 5-10 seconds, done while switching attention between that
small display and the main screen, inside a noisy Combat Information Center
with sailors juggling several simultaneous audio channels. Against a total
engagement window of roughly three minutes, a 5-10 second lag to extract a
single derived fact (is this number going up or down?) was proportionally
severe, and the official investigation (the Fogarty report) recommended
adding an altitude trend indicator to the main display — the same fix in
kind as the engineered trend-vector arrow a speed tape needs once its moving
scale hides the natural cue. Where the bullet-graph and speed-tape cases are
about *preserving* an existing rate-of-change cue against a design choice
that would hide it, this case shows what happens when rate of change was
never encoded visually at all: the viewer is forced to compute a trend from
raw numbers in working memory, under time pressure and noise, which is
exactly the condition under which that kind of mental arithmetic is least
reliable (Klein, *Sources of Power*, ch. 6).
