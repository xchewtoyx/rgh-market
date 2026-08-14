---
type: concept
title: Eliciting a Hidden Threshold by Offering Absurd Bounds First
description: >
  When a source insists they have no opinion on a number, ask about a
  deliberately extreme value first and progressively tighten it — the
  reflexive "no, that's too much" reaction usually reveals a real,
  usable threshold that a direct open-ended question never would have.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice (Bass, Clements, Kazman), ch. 19"
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything (Douglas W. Hubbard), ch. 5"
---

A source asked directly "what response time do you need" or "how fast does this have to be" will often, honestly, say they don't know — not because no threshold exists in their head, but because it's never been made explicit enough to state on demand. Asking the same question a second way surfaces it: propose a deliberately absurd value first ("would 24 hours be acceptable?"), let the source react — usually with an immediate, confident "no, absolutely not" — and then narrow the range with each subsequent guess (an hour? five minutes? ten seconds?) until the source lands somewhere they can actually defend ("I suppose I could live with something like that"). The reaction to an obviously-wrong anchor is much easier for someone to produce than an answer to an open-ended question, because rejecting a bad number requires no real commitment, while stating a number from nothing feels like inventing a requirement out of thin air.

This works because it converts an act of recall (find the number in your head) into an act of recognition (tell me if this number is wrong), and recognition is a far easier cognitive task — the source doesn't need to already have a crisp figure in mind, only a working sense of what would clearly be too slow, too costly, too long, or too loose, which almost everyone has even about things they've never had to quantify. A workable range extracted this way is often precise enough to matter a great deal downstream — the difference between "an hour is fine" and "it has to be under ten seconds" can imply completely different designs, even though neither number was ever stated as a firm figure before the conversation started.

The technique degrades if the interviewer's own bias leaks into the choice of starting anchor or the direction of narrowing — deliberately start from an anchor far outside any value you expect to land on, in both directions if time allows, so the source's own reaction does the narrowing rather than the interviewer's expectations. See [subject-matter-expert interview technique](subject-matter-expert-interview-technique.md) for the broader interview discipline this technique slots into, and [calibrated estimates](stating-forecasts-as-calibrated-probabilities.md) for the related family of techniques that convert a source's vague felt sense into a stated, checkable range.

The same reflex works self-applied, when you are the one trying to state your own range rather than draw one out of someone else: building a range by starting from a single point estimate and padding it with a margin tends to anchor too narrowly around that first number, because the point estimate itself already carries whatever bias produced it. Starting instead from a deliberately absurd range — for a project budget, "somewhere between $1,000 and $10 billion" — and narrowing only by rejecting bounds you actually know to be implausible reframes the task from "what do I think this is" to "what do I know is ridiculous," which is a much easier and more honest judgment to make, and tends to produce a wider, better-calibrated range than starting from the middle and working outward ever does.
