---
type: concept
title: Opportunity Solution Tree
description: >
  An opportunity solution tree structures discovery as a visual hierarchy
  from a desired outcome down through the needs that could drive it, the
  solutions considered for each need, and the tests run to evaluate them.
sources:
  - title: Continuous Discovery Habits
    resource: "Continuous Discovery Habits (Teresa Torres), ch. 2"
---

An opportunity solution tree (OST) is a four-level structure for
organizing discovery work so that a desired outcome, the needs that could
drive it, the solutions being explored, and the evidence for each solution
are all visible in one place, with the tree's shape itself indicating what
work is needed next:

1. **Root — the desired outcome**: the business or customer impact the
   team is trying to create, not a feature to ship. Fixing this first,
   before opportunities are explored, is what keeps a customer-centric
   discovery process from drifting away from business need — every branch
   below has to trace back to it.
2. **Opportunities** — customer needs, pain points, and desires that, if
   addressed, would plausibly drive the outcome. Deliberately not called
   "problems": many opportunities are desires rather than fixable
   problems, and framing them as problems narrows what a team will
   consider addressing them.
3. **Solutions** — the candidate ways of addressing a specific
   opportunity, explored side by side rather than committed to
   individually and in sequence.
4. **Assumption tests** — how the team evaluates whether a given solution
   would actually create the customer value it's meant to, before
   committing to build it.

The tree's diagnostic value comes from its shape: a shallow opportunity
space signals more discovery is needed; a sprawling one signals the need
to narrow scope; an opportunity with too few candidate solutions signals a
need for more idea generation; too few assumption tests in flight signals
the team is moving to build before evaluating what it has. Reading the
tree top-down (outcome → opportunities → solutions → tests) and revising
it bottom-up (a failed assumption test should update the team's
understanding of the opportunity, not just eliminate one solution and move
to the next) is the same iterative discovery discipline described in
[requirements are discovered, not gathered](requirements-discovery-vs-gathering.md),
expressed as a maintained artifact rather than a one-off interview
process.

Explicitly separating the opportunity level from the solution level gives
the same protection against solutioning prematurely that the [requirement
vs. design decision](requirement-vs-design-decision.md) boundary gives on
the specification side: an opportunity is what the customer needs, stated
independently of any particular way of meeting it, so several competing
solutions can be evaluated against the same opportunity instead of the
team anchoring on the first idea that came up. A tree with only one
solution per opportunity has usually skipped this comparison rather than
concluded it wasn't needed.

A candidate belongs in the opportunity layer, not the solution layer,
only if it passes a simple test: **is there more than one plausible way to
address it?** "I wish I could fast-forward through the boring parts"
has exactly one solution (fast-forwarding) and so is a solution wearing
an opportunity's clothing; digging one level further ("what's actually
bothering you about the boring parts?") usually surfaces the real
opportunity underneath, which does admit multiple solutions. Two other
markers of a malformed opportunity node: it's phrased as company
perspective rather than something a real customer would plausibly say
("we should have more subscriptions" is not a customer need), and it's an
expressed feeling rather than its cause ("I'm frustrated" is a signpost
toward a nearby opportunity, not one itself — dig for what's actually
causing the frustration).

Because the tree already records the chain from outcome through
opportunity, solution, and evidence, it doubles as a [rationale
capture](requirement-rationale.md) artifact for presenting that reasoning
to stakeholders: walking someone through it top to bottom — restate the
outcome, then the opportunities considered, then why a particular one was
chosen, then the solutions and evidence for the one selected — lets them
follow and challenge the actual reasoning, rather than being handed only
the resulting conclusion and left to either accept it or fight it on
authority alone.

Opportunities also nest: a **parent** opportunity is addressed only
partially by each of several **child** opportunities underneath it (a
subset of the reasons the parent occurs), and **sibling** opportunities
sit under the same parent, each independently addressable. Decomposing a
large, intractable-feeling opportunity into its children is what makes an
otherwise unsolvable problem tractable one piece at a time — and, per
[requirements prioritization](requirements-prioritization.md), lets a team
compare a handful of siblings against each other rather than trying to
rank the entire opportunity space at once.
