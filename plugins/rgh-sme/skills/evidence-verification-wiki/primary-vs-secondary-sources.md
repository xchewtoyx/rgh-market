---
type: concept
title: Primary vs. Secondary Sources
description: The distinction between raw original evidence and interpretative summaries, and how to evaluate their credibility in verification.
sources:
  - title: "The Chicago Guide to Fact-Checking, Second Edition"
    resource: "The Chicago Guide to Fact-Checking, Second Edition (Brooke Borel), ch. 5"
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 10"
  - title: "The Craft of Research, Fifth Edition"
    resource: "The Craft of Research, Fifth Edition (Booth, Colomb, Williams, Bizup, FitzGerald), ch. 3"
---
# Primary vs. Secondary Sources

A core discipline of claim verification is distinguishing between **primary sources** (raw, original evidence) and **secondary sources** (interpretations or summaries of primary evidence) and evaluating each appropriately.

## Definitions
- **Primary Sources**: Original, firsthand materials created at the time of an event or by the creator of a system. Examples include:
  - Raw system metrics, test logs, and database records.
  - Eyewitness reports, interview recordings, and emails.
  - Original scientific research papers reporting new experimental data.
  - Source code, architectural blueprints, and formal specifications.
- **Secondary Sources**: Documents that synthesize, analyze, interpret, or summarize primary sources. Examples include:
  - Technical reviews, summaries, and meta-analyses.
  - Trade magazines, news articles, and blogs.
- **Tertiary Sources**: Orientation tools that compile and distill secondary work for a reader who is new to a topic — encyclopedias, textbooks, and reference summaries. Useful for getting oriented and for finding leads into the secondary and primary literature, but too many steps removed from original evidence to cite as the basis for a specific factual claim; use a tertiary source to find the primary or secondary source, then verify against that.

## Evaluation Principles
1. **Source Status is Context-Dependent**: A source can be primary in one context and secondary in another. For example, a newspaper article is a primary source if cited as evidence of "how the public reacted to a release," but a secondary source if cited for a statistic reported inside it. Creation date relative to the event matters here too: a map drawn in 1725 is a primary source for what Lower Manhattan looked like in 1725, while a map drawn in 2019 that reconstructs 1725-era Manhattan is a secondary source for the same subject, however accurate its reconstruction. See [source authority scope](source-authority-scope.md) for the related case where the *same* source is primary for one claim and secondary (or unreliable) for another, based on their expertise rather than the source type.
2. **Quality Does Not Map to Category**: Being a primary source does not guarantee accuracy (e.g., a buggy system log or a biased eyewitness). Conversely, a rigorous secondary source (e.g., a peer-reviewed scientific review) can be highly reliable.
3. **Trace Back to the Primary Source**: When a draft relies on a secondary source (e.g., a blog post citing a whitepaper), the reviewer's standard practice must be to locate and check the underlying primary document directly. This prevents errors introduced by secondary summary or mischaracterization.
4. **Cite the Source Actually Consulted**: Never cite a primary source you only encountered secondhand, through another document's description of it, as if you had verified it directly — either trace it back and confirm it yourself, or cite the secondary source you actually read. Capture the full bibliographic locator (author, title, edition, page/section) at the moment a source is first consulted, not after — a fact recalled later without its locator can become effectively unusable even if it was accurately transcribed.
4. **Attribute Transparently**: If a primary source is completely inaccessible, the document must explicitly attribute the claim to the secondary source (e.g., "According to the analysis by Company X...") rather than presenting it as absolute fact.

## Distortion Chains
Each hop away from the primary source is a place where an accurate claim can be quietly reshaped, even without anyone acting in bad faith. A real case: a survey found applications "down at 39% of surveyed schools, up at 35%" — essentially noise. A news article accurately mentioned the decline stat while downplaying the comparably sized increase. A social-media summary of that article then misread "down *at* 40% of schools" as "down *by* 40%," turning statistical noise into a viral claim of a large, systemic decline. Each individual hop was a small, plausible-looking distortion; the cumulative effect was a claim unrecognizable from the original data. A reviewer who only checks the immediately-cited secondary source, rather than tracing all the way back to the primary data, will not catch this — extreme or shocking claims are also disproportionately likely both to be distorted this way *and* to spread fastest, which is exactly why they most need tracing to origin before being repeated.

## See Also
- [Evidence Triangulation](evidence-triangulation.md)
- [Evidence Weighting vs. False Balance](evidence-weighting-vs-false-balance.md)
- [Evaluating Scientific Literature](evaluating-scientific-literature.md)
- [Source Authority Scope](source-authority-scope.md)
