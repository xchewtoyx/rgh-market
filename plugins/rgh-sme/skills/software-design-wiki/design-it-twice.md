---
type: concept
title: Design It Twice
description: >
  For each major design decision, deliberately generate and compare multiple
  radically different candidate designs rather than committing to the first
  idea, because first-draft designs are rarely the best ones.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 11"
---

Software design is genuinely hard, so first-draft designs are rarely the
best available ones. The practice: for each major decision, sketch multiple
candidates at a rough level — not fully fleshed out, just the key structure —
before committing. Pick alternatives that are **radically different** from
each other, since that's where the real learning happens. Even when you're
confident there's only one sane approach, sketch a second, deliberately weak
one anyway: articulating *why* it's worse sharpens your understanding of what
makes the first one good.

**Evaluation criteria differ by what's being designed.** For an interface,
the primary criterion is ease of use for the higher-level code that will call
it; secondary questions include whether one candidate is simpler, more
[general-purpose](general-purpose-modules-are-deeper.md), or enables a more
efficient implementation than the others. For an implementation, simplicity
and performance take priority instead. [Design it twice](design-it-twice.md)
generalizes across levels: apply it once to choose a module's interface, then
separately again to choose its implementation, and it's equally applicable
well above the module level — choosing UI features, or decomposing a whole
system into its major modules.

After comparing candidates, the best outcome is sometimes picking one
outright, but often it's synthesizing features from several into a new design
that beats all the originals. If a shared weakness shows up across every
candidate — e.g. two different interface shapes both forcing "extra text
manipulation" onto every caller — that shared weakness is itself a
[red flag](red-flags-as-design-smells.md) pointing at what the next candidate
needs to fix, and following it can lead directly to a design that eliminates
the flaw entirely.

**Cost/benefit**: this is cheap insurance. A small module might need only an
hour or two of comparative design work against days or weeks of
implementation, and the resulting design improvement more than repays that
time — see [how much to invest in design](design-investment-level.md). Larger
modules warrant proportionally more exploration time, but also yield
proportionally bigger payoffs from getting the design right.

**The psychological obstacle** is specifically acute for people used to
succeeding on their first idea — a habit formed by getting good grades early
with minimal iteration. As problems scale up over a career, everyone
eventually reaches ones where the first idea isn't good enough; large
software system design is squarely in that category, and nobody is skilled
enough to nail it on the first attempt. The mistaken underlying belief is that
"smart people get it right the first time," so needing multiple attempts
would supposedly disprove one's own competence — needing more than one
attempt is just a function of how hard the problem is, not a verdict on
skill. There's a secondary benefit beyond the immediate artifact, too: the
comparative process itself trains better intuition over time for what
separates good designs from bad ones, making it progressively easier to rule
out weak options and converge on strong ones.
