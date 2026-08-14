---
type: concept
title: Adversarial Evidence Elicitation
description: Having independent parties each search for and present the strongest evidence for opposing conclusions, rather than one party assembling a case for a single predetermined answer, so a judge sees the strongest evidence on both sides instead of only the side someone chose to look for.
sources:
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    resource: "WebGPT: Browser-assisted question-answering with human feedback (Nakano, Hilton, Balaji, Wu, Ouyang, Kim, et al.), ch. 6"
---
# Adversarial Evidence Elicitation

A single searcher assembling evidence for one conclusion is structurally prone to [cherry-picking](cherry-picking.md): the searcher's task, as usually framed, is to find support for the claim in front of them, not to give a fair accounting of the total evidence — and that framing holds even when the searcher has no intent to deceive, because "find evidence" quietly becomes "find *convincing* evidence" under any process that rewards persuading a judge. **Adversarial evidence elicitation** (the mechanism behind AI-safety "debate" proposals) turns the same search capability into a check on itself: instead of one party searching for evidence toward a single answer, two or more independent parties each search for and present the strongest evidence for *different* candidate conclusions, and a judge weighs the competing cases rather than reviewing one party's unopposed search.

## Why Opposition Improves the Search, Not Just the Judgment
The benefit isn't only that a judge gets to hear both sides — it's that each side's search is disciplined by the existence of an opponent who will surface exactly what that side left out. A single-direction search has no built-in pressure to look for the evidence that undermines its own conclusion; an adversarial structure supplies that pressure externally, from an opponent whose incentive is precisely to find whatever the first search omitted. This is a *process-level* countermeasure to cherry-picking: rather than asking the original searcher to be more scrupulous (a request that competes directly with whatever else they're optimized for), the structure adds a second search that is optimized to find the opposite.

## Distinct From Self-Testing an Argument
This is a different mechanism from [objection anticipation in argument construction](objection-anticipation-in-argument-construction.md), where a single author tests their own claim against likely objections before a document goes to review. Objection anticipation still relies on one party's willingness and ability to generate a strong case against their own conclusion — a capability-and-incentive combination that degrades exactly when the stakes for reaching a particular conclusion are highest. Adversarial elicitation instead assigns the search for opposing evidence to a separate party whose actual task is to win by finding it, removing the dependence on the first party's self-critical effort.

## Judging the Result
The technique only pays off if the judge (human or automated) actually weighs the two searches rather than defaulting to whichever presentation is more persuasive in style — the same [evidence weighting vs. false balance](evidence-weighting-vs-false-balance.md) discipline applies here: strength of *evidence*, not confidence of *delivery*, should decide the outcome. A judge who cannot tell a well-supported case from a merely well-argued one gets no benefit from having two cases instead of one.

## Verification Action
- When a claim is contested or consequential enough to warrant it, structure the review as two independent searches for opposing conclusions rather than one search plus a single reviewer's skepticism — especially where the searcher (a person, team, or system) has any incentive to reach a particular answer.
- Check that the two searches were genuinely independent (not one party lightly editing the other's output) — a searcher who can see and defer to the opposing case loses the disciplining effect of not knowing what the opponent will find.
- When acting as judge over an adversarial presentation, evaluate the evidence each side actually produced, not which side argued more persuasively — see [evidence weighting vs. false balance](evidence-weighting-vs-false-balance.md).

## See Also
- [Cherry-Picking](cherry-picking.md)
- [Objection Anticipation in Argument Construction](objection-anticipation-in-argument-construction.md)
- [Evidence Weighting vs. False Balance](evidence-weighting-vs-false-balance.md)
- [Source-Grounded Evaluation Simplifies Verification](source-grounded-claims-simplify-verification.md)
