---
type: concept
title: Feature Sketches
description: >
  Draw a bubble per instance variable and method, with a line from each
  method to what it uses — the same diagram technique as effect sketches
  with the arrows reversed, used to find natural class boundaries by
  tracing which methods cluster around which state.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 20"
---

Classes are rarely uniform: most have "lumps" where only a subset of methods
touches a given subset of instance variables. A **feature sketch** makes
this visible: draw a bubble per instance variable and per method, drawing a
line from each method to every variable or method it uses or calls
(constructors are typically skipped, since they usually touch everything).

This is nearly the same diagram technique as
[effect sketches](effect-sketches.md), but with the **arrows reversed** —
a feature sketch points from a method toward what it *uses*; an effect
sketch points from a change toward what it *affects*. Like effect sketches,
feature sketches are disposable, roughly-ten-minute throwaway artifacts
drawn with a partner just before making changes, not persistent
documentation — which is also why the visual similarity between the two
doesn't cause real confusion in practice.

Worked example: a reservation class's sketch reveals a tight cluster of
fields and methods connected to the rest of the class through exactly one
link — one method calling another. That single thin connection between two
large clusters is a [pinch point](pinch-point.md) in the feature sketch:
when found, it marks a natural class boundary. Not every sketch has one, but
even without a clean pinch point, seeing the dependency layout is useful on
its own. A feature sketch usually admits more than one reasonable split —
worked alternatives here are extracting the tight cluster itself, versus
extracting everything *else* into its own collaborator — and the choice
between them is partly guided by which grouping yields a good class name.

Practical exercise: literally circle candidate groupings on the sketch —
"the lines that you cross can define the interface of a new class" — and
try naming each circled group. This is valuable naming and design practice
independent of whether the extraction is actually carried out.
