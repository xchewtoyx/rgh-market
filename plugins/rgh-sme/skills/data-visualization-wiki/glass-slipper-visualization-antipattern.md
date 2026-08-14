---
type: concept
title: Glass-Slipper Visualization Antipattern
description: >
  Borrowing a visualization form's implied structure or rigor for data that
  doesn't actually have that structure — like forcing a foot into a shoe it
  doesn't fit.
sources:
  - title: Calling Bullshit
    resource: "Calling Bullshit: The Art of Skepticism in a Data-Driven World (Carl T. Bergstrom, Jevin D. West), ch. 7"
---

Named by Bergstrom and West after the Grimm version of Cinderella, where the
stepsisters mutilate their feet to fit a shoe that was never made for them. A
"glass slipper" visualization takes a form whose visual grammar carries real
theoretical meaning and applies it to data with no such structure, borrowing
the form's implied rigor without earning it.

Examples: the periodic table's grid position encodes real atomic/electron-
shell structure and its gaps once predicted undiscovered elements — a "periodic
table of cloud computing vendors" borrows the grid-and-numbering aesthetic
with no underlying logic and no real gaps to predict anything. A subway map's
lines and stops are legitimate when they represent genuinely topological or
sequential relationships (stops in a real order along a real line), but
become an empty gimmick when the "stops" are just an arbitrary list. A Venn
diagram's overlapping regions have precise set-membership meaning; using
Venn-shaped ovals merely as decorative containers for three unrelated numbers
or phrases — or drawing circles whose overlap doesn't match the true
subset/intersection relationship of the data — discards that meaning while
keeping the visual claim to rigor.

The test: does the chosen form's visual grammar (position, overlap,
adjacency, grid structure) correspond to a real structural property of the
data, or is the form just being worn for its borrowed credibility? This is
the same failure mode as [when geography belongs on a
dashboard](when-geography-belongs-on-a-dashboard.md) applied more broadly:
plotting non-geographic categories on a map is one specific instance of
putting data in a form whose implied structure it doesn't possess.
