---
type: concept
title: Undocumented Automated Behavior Is a Safety Defect, Not Just a Gap
description: >
  When a system can act on its own initiative in ways an operator would
  need to recognize and respond to, leaving that behavior out of the
  operator-facing documentation isn't an incomplete manual — it is
  itself the defect that turns a survivable failure into a fatal one.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice (Bass, Clements, Kazman), ch. 10"
---

For most documentation, an omission is a usability cost: a reader has to guess, search elsewhere, or file a support request. For documentation covering a system that can act autonomously on something an operator is responsible for controlling, an omission is a different kind of failure entirely — the reader doesn't know there's anything to look up, because they don't know the behavior exists. The Boeing 737 MAX's MCAS system is the stark illustration: MCAS could push the aircraft's nose down automatically based on a single sensor reading, a disable procedure for it existed, but flight crews were never told MCAS existed at all — so when it activated and pushed against what pilots believed the aircraft was doing, they had no documented behavior to recognize, and no procedure they knew to reach for. The gap was not "the manual could have explained this better"; the gap was the direct mechanism by which a sensor fault became a fatal outcome.

The generalizable principle: for any system where the reader is an operator who needs to correctly interpret and respond to what they observe, an automated behavior capable of contradicting the operator's own model of what's happening is safety-relevant documentation by definition, not an optional deep-dive topic to include if space allows. This reframes a common [documentation-scoping instinct](selecting-content-by-stakeholder-concerns.md) — cut what a typical reader won't need day to day — because the relevant question for this category of content isn't "will most readers need this," it's "does leaving this out remove a reader's ability to correctly interpret a state they will eventually encounter." A rare-but-consequential automated behavior fails that second test even when it comfortably passes the first, and belongs in the documentation regardless of how rarely it fires.
