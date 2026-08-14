---
type: concept
title: Unfair Comparison Detection
description: Checking whether entities in a ranked list or comparison are actually measured on comparable terms before accepting the ranking as meaningful.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 7, 8, 10"
---
# Unfair Comparison Detection

A comparison or ranked list can be built from accurate, correctly-computed data and still be misleading, if the entities being compared are not actually measured on comparable terms. **Ranked lists are meaningful only when the compared entities are genuinely comparable.**

## Worked Example: City Crime Rankings
"Most dangerous cities" rankings based on violent-crime-per-capita consistently favor certain cities — but a large driver turned out to be how each city's administrative boundary is drawn. Cities whose limits hug only the historic urban core (excluding suburbs) show inflated crime-per-capita relative to cities whose limits sprawl to include most of the metro area, independent of actual danger. A scatter-plot test (violent crime rate vs. fraction of metro population living within city limits) confirmed a real, statistically significant relationship — meaning the ranking was measuring boundary-drawing as much as it was measuring danger. Notably, the very agency that published the underlying crime data warned against this exact kind of city-ranking misuse of it.

## Worked Example: Germ-Count Headlines
A headline claiming a surface "carries more germs than a toilet" can be a technically true statement about one narrow germ category (e.g., respiratory viruses, which the compared surface naturally accumulates more of due to how people interact with it) engineered to produce maximum unfair shock value, while omitting that the two surfaces carry very different overall germ profiles.

## Worked Example: Machine-vs-Human "Contest" Claims
A paper claiming a machine-learning model could infer a trait from photos "better than human judges" pitted a model trained on thousands of labeled images against untrained crowdsourced human raters given no practice at the task. A win in that contest doesn't establish that the model perceives something humans can't: humans can be good at *perceiving* individually relevant cues while being poor at *aggregating* many weak, probabilistic cues into a single decision — exactly the aggregation task ML systems are built for. This is the same failure mode as an ML system beating an untrained human at blackjack: a win doesn't imply the system saw marked cards, only that it aggregated legitimately available weak signals better than an untrained opponent did. A fair comparison needs a human baseline given comparable training, practice, or information to the system it's being compared against.

## Worked Example: Unnormalized Group Comparisons
A chart of total car-accident-fatality counts by driver age group made it look like the youngest licensed drivers were safer than drivers a few years older, and that elderly drivers showed no decline in driving ability — because it compared raw counts without accounting for how many total miles each age group actually drives. Replotted as fatalities *per mile driven*, the expected pattern (both the youngest and oldest drivers being disproportionately dangerous per mile) reappeared. A raw-count comparison across groups with very different exposure, opportunity, or population size is not yet a fair comparison until normalized by that exposure.

## Verification Action
When a draft cites a ranking, league table, or head-to-head comparison, check what measurement or definitional choices underlie each entity's value — geographic boundaries, category scope, time window, denominator choice, or unequal exposure/opportunity between compared groups — and whether those choices themselves, rather than the underlying phenomenon, are driving the apparent difference.

## See Also
- [Numeric Sanity Checking](numeric-sanity-checking.md)
- [Cherry-Picking](cherry-picking.md)
- [Proportional Ink Principle](proportional-ink-principle.md)
