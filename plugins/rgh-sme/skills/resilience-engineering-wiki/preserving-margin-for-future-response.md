---
type: concept
title: Preserving Margin for Future Response
description: >
  Resilient decision-making under escalating uncertainty optimises not for
  the current moment alone but for keeping enough adaptive capacity in
  reserve to handle whatever comes next — avoiding irreversible commitments
  while the situation is still unfolding.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 1"
---

Resilience under an unfolding, worsening situation is not just monitoring
the current gap to a boundary — it is a recursive act: continuously
estimating whether the adaptive capacity available *right now* will still be
sufficient for whatever the situation demands *next*. French practice calls
the resource being protected here the *marge de manoeuvre* — room to
manoeuvre — and the discipline is choosing actions that preserve it over
actions that would be locally optimal but consume it.

**US Airways Flight 1549 (2009)** is the exemplar. After a bird strike
disabled both engines shortly after takeoff, the captain chose to ditch in
the Hudson River rather than attempt to stretch a glide back to an airport.
Returning to the airport was the higher-reward option if it worked, but it
required committing to a flight path with no fallback: once irreversibly
committed to that approach, a misjudged glide would have left no remaining
option at all. Ditching kept the margin for manoeuvre intact for longer,
trading away the higher-reward outcome for one that stayed recoverable at
every point along the way. This is the same logic in reverse from [plan
continuation bias](plan-continuation-bias.md): where plan continuation is an
unrecognised, default erosion of margin, this is a recognised, deliberate
choice to protect it.

**Tactical reserves** are the concrete organisational mechanism for
protecting margin for manoeuvre in real time. An incident commander running
an urban fire holds a portion of available units uncommitted rather than
deploying everything the current picture seems to justify, precisely so
there is capacity left to absorb a demand shift nobody predicted — a
back-draft explosion trapping a unit with no planned egress, for instance.
Declaring "all hands" (every available unit committed) is itself a signal
worth treating as a warning independent of the fire's current state: it
means the system is at its adaptive ceiling and any further surge has
nothing left to draw on, the operational trigger for
[decompensation](decompensation.md).

Margins of manoeuvre are also **shared and interdependent, not private to
one unit** — a workaround that helps the unit that invents it can shrink
another unit's margin without anyone deciding that trade-off, the same
mechanism as [working at cross-purposes](working-at-cross-purposes.md): a
crew venting a window to clear smoke can simultaneously cut off a peer
crew's planned escape route through that same window.

The generic competency this implies is not a fixed skill but continuous
self-monitoring: is the system's current adaptive capacity — its distance
from having no options left — still adequate for the demands the situation
is likely to make next, and is the action under consideration now spending
that capacity or protecting it. Bergström et al.'s formal treatment of team
competencies for managing escalating situations builds directly on this:
teams need to monitor not only the current state of the disruption but their
own organisational suitability to keep handling it, updating that assessment
as the situation develops rather than fixing a strategy at the outset. This
is the decision-time complement to the structural properties in [buffering
capacity, margin, and tolerance](buffering-margin-and-tolerance.md): those
describe what margin a system has; this describes the discipline of not
spending it prematurely.
