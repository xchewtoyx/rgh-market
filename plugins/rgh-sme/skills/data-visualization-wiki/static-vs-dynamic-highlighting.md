---
type: concept
title: Static vs. Dynamic Highlighting
description: >
  Highlight always-important data through fixed screen position; highlight
  data that's only important right now through a preattentive attribute that
  changes with the data, and never over-highlight either way.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 5 §5.2.2.2"
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Gary Klein), ch. 7"
---

Once [unnecessary data pixels are eliminated](data-ink-ratio.md), what
remains still isn't all equally important, and the two kinds of importance
call for different highlighting mechanisms:

- **Always-important data** — highlight it via **static** means, chiefly
  fixed [screen position](screen-position-emphasis.md), since this kind of
  importance doesn't change moment to moment.
- **Data that's important only at the moment** (a measure that's fallen
  behind target, a fleeting opportunity, an operational condition needing
  immediate attention) — highlight it **dynamically**, using a
  [preattentive attribute](preattentive-attributes-for-dashboards.md) that
  changes in response to the data condition, since a fixed position can't
  react to something that's only sometimes true.

Dynamic highlighting comes in two flavors:

- Attribute expressions **greater than the norm** — darker or more saturated
  color intensity, bigger size, thicker line width — all read as "more
  important."
- Attribute expressions that merely **contrast with the norm** — a distinct
  hue, a different orientation, an enclosure or added mark where none is
  typical — stand out purely by being different, regardless of greater or
  lesser.

Color is especially useful for dynamic highlighting because it's easy to
change programmatically in response to a data condition. A favored technique:
pair a simple added mark (circle, checkmark, asterisk) with a distinct color
intensity next to whatever needs attention — see
[colorblind-safe color encoding](colorblind-safe-color-encoding.md) for why
intensity, not hue, should carry the meaning.

The final caution applies to both static and dynamic highlighting equally:
over-highlighting defeats the purpose. "If you highlight too much
information, nothing will stand out and your effort to communicate will
fail." Used with restraint, highlighting achieves immediate recognition and
quick response; used everywhere, it achieves nothing.

**Worked example with measured impact**: a 1991-92 redesign of the US Air
Force's AWACS (Airborne Warning and Control System) weapons-director display
identified, via task analysis, that operators needed to stay especially
vigilant for "high, fast flyers" — the highest-threat category of enemy
aircraft — among many simultaneous radar tracks. The fix was exactly this
kind of dynamic highlighting: a simple algorithm auto-highlighted any track
meeting the high-threat condition with a red circle, so the display itself
flagged the condition rather than requiring the operator to keep scanning
every track for it. Tested against the old interface with experienced
weapons directors (~1,500 hours on the old display) given only 4.5 hours to
learn the new one, the highlighting change (plus related fixes — color to
distinguish land from water, and relocating a control panel onto the main
screen) produced a measured 15-20% overall performance improvement,
including 20% fewer hostile strikes completed against the defended force and
15% fewer friendly aircraft shot down. The result illustrates both the power
of a well-targeted dynamic highlight and how little extra could be squeezed
from the old interface no matter how much operators studied it — the display
itself, not operator effort, was the bottleneck (Klein, *Sources of Power*,
ch. 7).
