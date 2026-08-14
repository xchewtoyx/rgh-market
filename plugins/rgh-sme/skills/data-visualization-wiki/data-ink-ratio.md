---
type: concept
title: Data-Ink Ratio (Reduce Non-Data Pixels, Enhance Data Pixels)
description: >
  Maximize the proportion of a display's visual weight that actually
  represents data, by removing decoration and non-essential elements first
  and only then enhancing what's left for clarity.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.11, ch. 5 §5.2, ch. 8 §8.1"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 3 (citing Tufte; Duarte, Resonate)"
---

Adapted from Edward Tufte's data-ink ratio (*The Visual Display of
Quantitative Information*, 1983): "A large share of ink on a graphic should
present data-information, the ink changing as the data change... Maximize the
data-ink ratio, within reason. Every bit of ink on a graphic requires a
reason." Nancy Duarte (*Resonate*) frames the same idea as maximizing
**signal-to-noise ratio** — signal is the information to communicate; noise
is everything that does not add to (or actively detracts from) the message.
Both framings serve
[minimizing extraneous cognitive load](minimize-extraneous-cognitive-load.md).
Few translates "ink" to **pixels** for screen displays: any pixel that isn't
displaying data (excluding plain background) should be reduced to a
reasonable minimum.

Two fundamental, sequential goals of visual dashboard design:

1. **Reduce the non-data pixels.**
   - First, *eliminate* unnecessary non-data pixels entirely: purely
     decorative graphics; color variation on bars/objects that encodes no
     meaning; borders or fill colors delineating sections where white space
     would work; color gradients where a solid color would do (gradients on
     bars also actively *distort* the bar's perceived value depending on
     where its edge falls within the gradient — a real perceptual cost, not
     just visual noise); grid lines in graphs (one of the most prevalent
     forms of distracting non-data pixels); grid lines or alternating-row
     fills in tables where white space would suffice; a complete border
     around a graph's plot area where two axis lines define it just as well
     (see [Gestalt closure](gestalt-closure.md)); 3-D effects that encode no
     data (see [avoid 3-D effects and occlusion](avoid-3d-effects-and-occlusion.md));
     ornamentation that simulates a physical object.
   - Then, for non-data pixels that remain genuinely necessary (e.g.,
     delineating lines when data is packed too tightly for white space
     alone), **mute them** — light, low-saturation colors, thin strokes — so
     they don't compete with the data, and **regularize** them so the same
     kind of non-data pixel looks identical everywhere on the dashboard (an
     application of the [visual consistency principle](visual-consistency-principle.md)).
     This also applies to navigation/selection controls and instructional
     text: functionally necessary but visually recessive, placed out of the
     way (e.g., bottom-right) rather than competing with data for the
     highest-emphasis screen positions.
2. **Enhance the data pixels that remain.**
   - First *eliminate unnecessary data pixels*: resist including everything
     anyone might ever want. Condense via
     [summarization and exceptions](summarization-and-exception-reporting.md)
     so displayed detail doesn't exceed what the task actually needs (raw
     transaction-level data has no place on a dashboard; some summarization
     level is always required, and choosing it is the designer's job).
   - Then *highlight what remains important* — see
     [screen position as a static highlighting tool](screen-position-emphasis.md)
     and [static vs. dynamic highlighting](static-vs-dynamic-highlighting.md).

Edward Tufte's related term for the worst offenders: a "duck" (borrowed from
a duck-shaped roadside building) is a visualization where decorative form
overwhelms the data itself — bar-chart bars redrawn as lipstick tubes, a pie
chart redrawn as an ice-cream cone. A duck isn't necessarily deceptive, but
it still impairs the reader's ability to extract the actual data, exactly
like any other non-data pixel. See also [proportional
ink](proportional-ink-principle.md) for the related, stricter requirement
that whatever ink *does* represent data must be sized proportionally to the
value it represents.

The underlying test for any pixel on a dashboard: could it be removed without
losing information? If yes, remove it — Tufte's own line, quoted by Few:
"Blank space is better than meaningless decoration." Decorative elements that
seem entertaining on first use reliably become "just plain annoying" within
days; this is the same failure mode as [chartjunk](avoid-3d-effects-and-occlusion.md)
and the reason [aesthetics should serve communication](aesthetics-serve-communication.md)
rather than decorate it.
