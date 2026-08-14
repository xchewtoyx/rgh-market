---
type: concept
title: Bullet-Point Compression Hides Technical Nuance
description: >
  A condensed slide-bullet format can quietly discard the magnitude
  comparisons, caveats, and reasoning chain a complex or high-stakes
  technical finding depends on, so the format itself becomes a source
  of miscommunication independent of the underlying analysis.
sources:
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Sidney Dekker), ch. 5"
---

Compressing a complex technical finding into a slide bullet does more than shorten it — it forces a choice about which parts of the reasoning survive, and a writer under time pressure tends to keep the headline and drop exactly the qualifications that would let a reader judge whether the headline is warranted. The Columbia Space Shuttle disaster investigation found this failure in a real engineering slide: a debris-strike risk assessment titled "Review of Test Data Indicates Conservatism for Tile Penetration" was actually reporting that the calibration data used to model the strike covered impacts hundreds of times smaller than the one that had actually occurred — the opposite of reassuring — but the slide's title stated the reassuring reading and the compressed bullets underneath never surfaced the magnitude gap. See [numbers need comparative context](numbers-need-comparative-context.md): the missing comparison here (how much bigger the real impact was than anything the model had been tested against) was exactly the number the decision depended on, and compression is what let it disappear.

Two mechanisms make bulleted compression specifically dangerous for complex or high-stakes material, beyond ordinary information loss:

- **A conclusory title can assert more than the compressed bullets underneath actually support**, and a reader who scans the title first (see [formatting for scanning](formatting-for-scanning.md)) forms a judgment before ever reaching the qualifying detail — if that detail didn't survive compression at all, the title's claim goes unchecked.
- **A word repeated across several compressed bullets can silently carry different meanings each time**, because the format has no room for the qualifying context that would normally disambiguate it — the same investigation found one slide using "significant" five times with meanings ranging from a barely detectable effect in irrelevant test data to a magnitude gap large enough to be fatal, with nothing on the slide marking the shifts. This is the same failure as [precise and consistent naming](precise-and-consistent-naming.md) describes for identifiers, playing out in prose: a reader who has anchored on one meaning of a recurring word carries that meaning into its next occurrence rather than re-deriving it each time, and compression removes the surrounding context that would otherwise have caught the drift.

The practical implication is not that bulleted, scannable formats are wrong in general — [formatting for scanning](formatting-for-scanning.md) and [adapting pyramid structure for presentations](adapting-pyramid-structure-for-presentations.md) both depend on them for material that genuinely compresses cleanly. It's that the decision to compress should be made deliberately against how much the finding's credibility rests on caveats, magnitudes, and reasoning steps that a bullet format has no room to carry: where a decision is high-stakes and the underlying analysis is genuinely complex, a full technical document that can carry that reasoning is the correct medium, not a slide summarizing it. The investigation into this incident put the point directly: presenting safety-critical technical analysis as slide bullets instead of technical papers was itself named as a contributing failure of technical communication, independent of whatever the underlying engineering analysis got right or wrong.
