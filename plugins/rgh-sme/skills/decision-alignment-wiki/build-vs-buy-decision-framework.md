---
type: concept
title: Build-vs-Buy Decision Framework
description: >
  Sort a build-or-buy choice on business value and ubiquity
  before debating it, since most of the argument only exists
  in the one quadrant where both are high.
sources:
  - title: "Observability Engineering (2nd Edition)"
    resource: "Observability Engineering (2nd Edition) (Charity Majors, Liz Fong-Jones, George Miranda), ch. 29"
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 12"
---

Plot a component on two axes — **business value** (none to
differentiator) and **ubiquity** (commodity to bespoke) —
before arguing about whether to build or buy it. Three of the
four resulting quadrants resolve themselves:

- **Build** (bespoke + high value): the thing that actually
  differentiates the organization. Build it.
- **Buy** (commodity + low value): most infrastructure. Buy
  it and move on.
- **Should not exist** (bespoke + low value): custom
  engineering effort spent on something with no differentiating
  value is the worst kind of technical debt — expensive to
  build, expensive to keep alive once the original engineers
  leave, and delivering nothing unique in return.

The fourth quadrant — **commodity + high value** — is where
the hard conversation actually happens, because the component
is important enough to matter but common enough that a
credible off-the-shelf option probably exists. Work through it
with explicit questions rather than gut feel: What is the job
to be done? How unique are the organization's requirements
really (usually less unique than the team assumes)? What is
the smallest version of the problem worth solving? Does the
team have real product-management capacity to own a build,
not just engineering capacity? What is the timeline? Who
supports the result after the original builder moves on or
leaves?

**Named biases that distort this call**, worth checking for
explicitly before trusting a recommendation either way:

- **Vendor bias** — vendors systematically underrate the true
  cost of buying (integration, migration, lock-in) because
  they are selling it.
- **Engineer bias** — engineers are inclined to want to build
  regardless of the economics, the same way surgeons are
  inclined to want to operate.
- **Sunk cost fallacy** — defending a past build decision to
  avoid admitting it was wrong, rather than evaluating the
  choice fresh.
- **Not-invented-here** — assuming the organization's needs
  are too special for any existing tool, without testing that
  assumption.
- **Vendor-lock-in fear** and **migration-fatigue fear** —
  real risks, but ones that can tip a decision toward building
  even when the actual switching cost would be lower than the
  cost of maintaining a bespoke system indefinitely.
- **Promotion incentives** — career systems that reward
  visible engineering output over good judgment quietly push
  individual engineers toward recommending a build even when
  buying is the better call for the organization; reward
  the decision, not the lines of code it produced.

A concrete illustration of vendor bias and hidden build costs
compounding: a manager rejected an ~$80K/month commercial
offer to keep a "free" self-hosted stack, without counting the
hardware, the three extra engineers required to run it, their
recruiting cost, and ramp time — the true cost of the "free"
option exceeded the commercial quote by more than double.

This framework is a lens for *framing* the choice, not a
substitute for making it — pair it with
[compare-and-contrast-framing](compare-and-contrast-framing.md)
to make sure build, buy, and any hybrid path are all named
options on the table, and with
[multi-lens-comparison-without-false-precision](multi-lens-comparison-without-false-precision.md)
to compare them without manufacturing false certainty. Because
committing to a build is usually far more costly to reverse
than committing to a vendor contract, weigh that asymmetry
explicitly using
[reversibility-as-decision-criterion](reversibility-as-decision-criterion.md).

**A minimum factor set for scoring the choice once it reaches
this quadrant**, drawn from a platform build-vs-buy call in an
ML context but applicable to any component-level version of the
question:

- **Alignment** — does the option actually meet the need? Are
  required customizations available, and are data-privacy and
  security requirements satisfied?
- **Investment** — what is the total cost of ownership (human
  capital, software, hardware), and is there a stated ROI or NPV
  target to weigh it against?
- **Time** — how fast can the option actually reach production?
- **Competitive advantage** — does building it produce a
  proprietary asset that adds real value for customers,
  employees, or investors — or would the same engineering effort
  buy nothing distinctive?
- **Maintenance and support** — what does it cost, on an ongoing
  basis, to keep the people, hardware, and software behind this
  option running?

Weight these factors for the specific decision rather than
treating them as a fixed formula, and expect the weighting to
select different parts of a system to build versus buy rather
than one binary answer for an entire platform — a long-term,
large-scale initiative more often justifies a fuller buy (or
build) than a short-lived, small-scale one, since fast-moving
tooling can become obsolete before a large build's implementation
cost is recouped.

Treat the final call as strategic enough not to rush: convene the
actual stakeholders — not just the engineers who will do the
work, but leadership, product, and sales — to review the scoring
criteria together and build real consensus, and talk to vendors
directly rather than only through their sales materials, since a
frank conversation surfaces information a pitch deck omits. See
[stakeholder-buy-in-sequencing](stakeholder-buy-in-sequencing.md)
for the order that consensus-building should happen in. The right
answer here draws on earlier discovery-phase work rather than
being decided in isolation — see
[discovery-before-solutioning](discovery-before-solutioning.md).
