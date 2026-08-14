---
type: concept
title: Aesthetics Serve Communication, Not Decoration
description: >
  An unattractive dashboard puts viewers in a mindset that isn't conducive to
  use, but the fix is displaying the data itself attractively — not adding
  ornamentation, which is a distinct failure mode from ugliness.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.13, ch. 7 §7.3"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 4–6, ch. 9"
---

Ugliness is its own design failure, separate from clutter or decoration: a
dashboard that looks unattractive (dreary backgrounds, stretched sections,
mismatched proportions) puts viewers in a mindset not conducive to using it
well, even before you consider whether it's cluttered. People also perceive
more aesthetic designs as *easier to use* — and more aesthetic designs are
more readily accepted over time, promote better problem solving, and make
people more tolerant of remaining flaws. Investing in polish therefore buys
patience for the message. But the response is not to add prettifying touches
— it's to display the data itself attractively without additions that
distract from or obscure it: smart
[color](vivid-color-restraint.md), clean
[alignment and white space](alignment-and-white-space.md), and restrained
chrome. Build instinct by collecting appealing examples and mimicking what
works. When stakeholders resist an unfamiliar but better form, see
[gaining acceptance for new visual designs](gaining-acceptance-for-new-visual-designs.md).

Citing Donald Norman: aesthetically pleasing design has genuine psychological
benefit — pleasant design relaxes viewers, which primes better insight and
response — so this isn't "usability vs. aesthetics," it's "usability vs.
anything that flagrantly undermines usability." In dashboard design
specifically, aesthetic effort should go entirely into the data display
itself, never into ornamentation:

- Keep bright, fully saturated colors to a minimum, reserved for data that
  needs attention (see [vivid color restraint](vivid-color-restraint.md)).
- Match color *tone* to the communication: grey+blue can read as "too nice"
  for a clinical statistical report that wants bold black and restrained
  typography, while hot pink and teal can fit a lively magazine piece and
  still be wrong for a quarterly business report. Color evokes emotion;
  choose it deliberately, and when audiences are international, treat color
  meanings as culturally contingent (see
  [colorblind-safe encoding](colorblind-safe-color-encoding.md)).
- Prefer **dark grey** over pure black for default titles and axis chrome —
  enough contrast to read without the harshness of black-on-white, reserving
  black as a standout when no other accent is used.
- Use a barely-off-white background rather than pure white, to soften
  contrast. Prefer light grounds over dark ones for dense data; when a dark
  template is mandatory, see
  [color logic on dark backgrounds](color-logic-on-dark-backgrounds.md).
- Use high-resolution, crisp rendering — dense information demands legibility,
  not photorealism or fancy shading.
- Use one legible body font consistently; a distinct heading font is the
  practical limit of font variety. Don't choose fonts for "mood" — ornate
  text suits a circus poster, not a dashboard.

The guiding principle throughout is the same one that drives
[data-ink ratio](data-ink-ratio.md) reduction: simplicity, applied to the
data display itself, is what produces an aesthetically pleasing result —
not decoration layered on top of it.
