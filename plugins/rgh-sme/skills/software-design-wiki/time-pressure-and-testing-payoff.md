---
type: concept
title: Testing Under Time Pressure Pays Off on the Next Nearby Change
description: >
  You usually can't know in advance whether writing tests before a change
  "paid off," because the counterfactual is invisible — but changes cluster
  in systems, so the investment tends to pay back on the very next change to
  the same area.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 6"
---

Writing tests and [breaking dependencies](dependency-breaking-for-testability.md)
takes real time up front, and you often can't know whether it was worth it —
there's no way to see how long the change or its debugging would have taken
without tests. The real payoff tends to show up on the *next* change nearby,
because changes cluster in systems: if you're touching an area today, you'll
likely be back soon.

A useful team experiment: for one iteration, ban any change without a
covering test (if someone believes a test is impossible, call a quick group
meeting to check). Early iterations feel slow and uncomfortable; teams
gradually notice they're revisiting better code and changes get easier — a
hump every team needs to personally feel to internalize the value.

Under genuine time pressure with no reliable estimate, the pragmatic
sequence: first just try instantiating the class you need to change in a
test harness — it may be easier than feared. If that's genuinely not
affordable right now, ask whether the needed change can be written as fresh,
separately-tested code instead — see
[sprout method](sprout-method.md), [sprout class](sprout-class.md),
[wrap method](wrap-method.md), and [wrap class](wrap-class.md). These
techniques test the *new* code, not its integration with the untested code
that calls it, so use them with caution. As a closing maxim: "Remember, code
is your house, and you have to live in it."
