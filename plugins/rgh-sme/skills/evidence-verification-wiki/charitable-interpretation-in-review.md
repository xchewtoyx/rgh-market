---
type: concept
title: Charitable Interpretation in Review
description: Before attributing an error to bad faith, checking whether the reviewer is mistaken or whether an honest mistake fully explains it.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 7, 11"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 9"
---
# Charitable Interpretation in Review

When a reviewer finds an error in someone else's claim, a specific order of consideration keeps the resulting critique honest and credible:
1. **You might be the one who's wrong.** Check your own reasoning and sourcing before assuming the author's claim is the mistake.
2. **Incompetence or an honest mistake is usually a sufficient explanation** without invoking deliberate deception — most errors, even serious ones, don't require assuming bad faith to explain.
3. **An honest mistake doesn't imply general incompetence** — a single error doesn't license discounting an author's other work or credibility wholesale.

## Understand Before You Disagree
Before critiquing a source's argument, a reviewer should be able to summarize it fairly, to their own satisfaction, without straw-manning it — disagreeing with a version of the argument the source didn't actually make wastes the critique's force and undermines the reviewer's credibility once the mismatch is noticed. See [source critique strategies](source-critique-strategies.md) for angles to apply once that understanding is confirmed.

## Worked Example
A widely-criticized graphic plotted an axis with zero at the top instead of the bottom, making a genuine post-policy increase in an outcome visually read as a decrease. The designer's own explanation was a deliberate stylistic choice (representing a negative outcome in "negative," downward terms), not an attempt to mislead. The chapter's general formulation applies directly: "never assume malice or mendacity when incompetence is a sufficient explanation, and never assume incompetence when a reasonable mistake can explain things" — a reviewer should still flag the misreading risk the choice creates, but the write-up and tone should reflect a plausible non-deceptive explanation rather than assuming the designer meant to distort the result.

## Why It Matters
Attacking the argument rather than the person preserves the working relationship, keeps the critique focused on what's actually checkable, and protects the reviewer's own credibility if the finding turns out to be wrong. Someone repeating a debunked claim has frequently never seen the retraction or correction themselves — assuming they knowingly spread misinformation is usually both incorrect and counterproductive to actually fixing the error.

## Professional Norms in Technical Review
Code review adds stress even for capable engineers — feedback must stay professional. Authors should remember they are not their code; reviewers should avoid piecemeal feedback cycles (surfacing new unrelated issues after each fix pass). Treat every reviewer comment as something to address: accept, explain disagreement, or propose an alternative and ask for another look — don't mark threads resolved until both sides have had a chance to respond. Prompt acknowledgment (e.g., within one working day) when a full review cannot finish immediately prevents authors from blocking on silence.

## Verification Action
Before writing up a finding as a correction, draft it assuming an honest mistake first, and only escalate the framing if there is specific, independent evidence of deliberate misrepresentation (e.g., a documented pattern of the same unsupported claim being made after being corrected before).

## See Also
- [Pertinence Test for Objections](pertinence-test-for-objections.md)
