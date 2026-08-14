---
type: concept
title: The Modal Risk-Trading Paradox
description: >
  A safety intervention that protects one population can increase net harm
  if it pushes activity onto a substitute that carries a higher baseline
  risk — protecting the visible group can cost the displaced group more
  than it saves.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 9"
---

Dutch railway regulators demanded full track closures during maintenance
work to protect track workers, who were otherwise exposed to a much higher
mortality rate than the industry norm from working alongside live traffic.
The demand was locally correct — closures do protect workers — and still
produced a worse aggregate outcome once its full effect was quantified.
Closing rail lines pushes the passengers who would have travelled by train
onto substitute transport, overwhelmingly road (car and bus), and road
travel carries a substantially higher baseline fatality rate per
person-kilometre than rail. The net increase in passenger road deaths from
the mode shift significantly outweighed the worker lives the closures would
have saved.

**The paradox is structural, not a miscalculation.** A safety intervention
scoped to protect one identifiable population (workers on the track) is
evaluated as if that population's risk were the whole picture, when the
intervention actually operates on a shared system with a substitute channel
(the road network) already carrying its own baseline risk. Protecting the
visible, directly-affected group by removing an option pushes exposure onto
an already-riskier alternative that absorbs the displaced activity — the
people bearing the new cost are invisible to an analysis scoped only to the
original intervention's direct population.

This generalises past transport modes to any safety measure that removes or
restricts an option rather than making the option itself safer: banning a
service, adding friction to a workflow, or removing a shortcut all displace
the activity somewhere, and that somewhere has its own risk profile which
the intervention's designers may never have measured. The corrective is
scoping risk analysis to the whole system the intervention touches,
including where displaced activity actually goes, rather than only to the
population the intervention was designed to protect — the same widened
frame [systems-theoretic accident models](systems-theoretic-accident-model.md)
apply to causation, applied here to the evaluation of a fix rather than the
diagnosis of a failure.
