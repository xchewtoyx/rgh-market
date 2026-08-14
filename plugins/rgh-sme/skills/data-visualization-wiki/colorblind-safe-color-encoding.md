---
type: concept
title: Colorblind-Safe Color Encoding
description: >
  Roughly 10% of men and 1% of women cannot reliably distinguish red from
  green, so meaning encoded purely via hue (especially a red/yellow/green
  traffic-light scheme) is invisible to a meaningful share of viewers.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.12, ch. 5 §5.2.2.2, ch. 6 §6.2.2"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 4"
---

Casual reliance on red/yellow/green to encode status excludes colorblind
viewers outright — about 10% of men and 1% of women in Few's figures
(Knaflic cites roughly **8% of men and 0.5% of women**), most commonly
difficulty distinguishing red from green. The fix is not to avoid color, but
to change *what varies*: encode the meaningful distinction as the
**intensity of a single hue** (e.g., pale red vs. deep saturated red) rather
than switching between different hues. Intensity variation remains legible to
colorblind viewers, whereas hue-only encodings (red vs. green with similar
lightness) do not.

When red/green connotations are still useful (loss vs. growth), keep them
only if a second cue travels with the color — bold weight, saturation/
brightness difference, or explicit +/− signs — so hue is never the sole
channel. A common substitute pair is blue for positive and orange for
negative: recognizable polarity without the red/green conflict. Also ask
whether both ends of the scale need color at all, versus highlighting one
end (or each end in sequence). Simulator tools (e.g., Color Oracle, Vischeck,
CheckMyColours) help verify encodings before shipping.

This shows up concretely in the book's recommended components:

- The [bullet graph](bullet-graph.md)'s background qualitative bands
  (bad/satisfactory/good) vary in intensity of one hue, not hue itself.
- [Status icon design](status-icon-design.md) recommends one consistent
  simple shape whose severity is shown by intensity, and — for up/down
  icons specifically — varying hue *and* intensity together (e.g., fully
  saturated red for "wrong direction" vs. pale green for the other) rather
  than hue alone.
- [Evaluative state banding](evaluative-state-banding.md)'s good/bad states
  should follow the same rule when color is the encoding channel.

A further caveat: color meanings are culturally contingent, not universal —
red does not mean "urgent/bad" in every culture (in China it connotes
happiness) — another reason to design the encoding deliberately rather than
assume a color's meaning is self-evident. See also
[color perception context dependence](color-perception-context-dependence.md)
for why the same color can read differently depending on what surrounds it,
and [vivid color restraint](vivid-color-restraint.md) for when to use fully
saturated color at all.
