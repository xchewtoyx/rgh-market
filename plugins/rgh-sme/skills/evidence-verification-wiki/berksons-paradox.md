---
type: concept
title: Berkson's Paradox
description: Selecting a subgroup on a combination of two otherwise-unrelated traits can create an artificial negative correlation between those traits within the selected subgroup alone.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 6"
---
# Berkson's Paradox

**Berkson's paradox**: selecting on a combination of two variables that are genuinely uncorrelated in the general population can induce an artificial *negative* correlation between them within the selected subgroup — with no real underlying trade-off between the two traits at all.

## Worked Examples
- Two otherwise-uncorrelated traits (e.g., two independent desirable qualities) show no relationship in the general population, but restricting attention only to cases that clear a combined threshold on both traits (a "would select" region) creates an apparent negative relationship within that narrowed group — because cases high on one trait need less of the other to clear the same combined bar, and cases low on one trait need more of the other, mechanically producing the negative slope.
- A hiring process that already heavily selects candidates for one trait (e.g., a technical assessment score) can show a negative correlation between that trait and on-the-job performance *within the hired population*, without that correlation existing in the general applicant population — the hiring filter itself is what manufactures the negative relationship among those who passed it.
- The same mechanism explains why a nomination process using a shared cutoff across subgroups with differently shaped underlying distributions can produce an apparent gap between subgroups within the nominated pool, without the cutoff process itself favoring either subgroup.

## Verification Action
When a draft reports a correlation (often surprising or counterintuitive) observed within an already-filtered or already-selected population (hired employees, admitted applicants, published papers, cases that passed some earlier gate), check whether the selection process itself could mechanically produce that relationship, independent of any real relationship between the traits in the broader unfiltered population. A correlation found only within a selected subgroup should not be generalized to the population that subgroup was selected from.

## See Also
- [Selection Bias](selection-bias.md)
- [Confounding Variables](confounding-variables.md)
