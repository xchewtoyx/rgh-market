---
type: concept
title: Catalog Entry Structure for Reusable Techniques
description: >
  A catalog of named, reusable techniques (patterns, refactorings,
  runbook moves) reads fastest when every entry follows the same fixed
  shape — name, a before/after sketch, motivation, and mechanics — so
  a reader can jump straight to whichever part they currently need.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Martin Fowler, with Kent Beck), ch. 1, 5–12"
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Martin Fowler), ch. 5, Introducing the Catalog"
---

A document that catalogs many named, reusable techniques — refactorings, design patterns, runbook procedures — is a different genre from a narrative explanation, and it needs a different structure: not a single continuous argument, but many short, self-contained entries that all share one fixed shape. Once a reader has internalized that shape from the first few entries, every later entry becomes skimmable — they can jump straight to the part they currently need (just the name, just the trade-off, just the steps) without re-reading the parts they already know from having used the catalog before.

A workable fixed shape has five parts, each answering a distinct question:

1. **Name** (plus known aliases) — the vocabulary term itself, chosen so that once a team shares it, referring to the technique in conversation or in a code review no longer requires re-explaining what it means each time. Listing aliases matters because the same technique often already circulates under a different name in some readers' background — omitting them makes the entry harder to find, not more authoritative. A catalog's real payoff is often this shared vocabulary as much as the mechanics behind it.
2. **A sketch** — the shortest possible cue (a one-liner, a small before/after illustration) whose only job is helping a reader who half-remembers the technique locate the right entry fast, not to teach it.
3. **Motivation** — when to reach for this technique, and explicitly also when *not* to; this is the part a reader consults when deciding *whether* to use it, and it's the part most often skipped by writers who assume the mechanics speak for themselves.
4. **Mechanics** — the actual ordered steps, written as a deliberately terse, small-as-possible checklist rather than descriptive prose. Mechanics should describe the safest possible path — the smallest steps, verified at every step — even though a practiced reader will usually take bigger strides in practice; the terse safe version is what a reader falls back to when a bigger stride breaks. Mechanics exist to be followed once the technique is already understood, not to explain why it works — that's the motivation and example's job.
5. **Example** — a deliberately small, simplified illustration built to show one technique in isolation with minimal distraction, not to model realistic production code. It's normal and expected for an isolated example to leave the surrounding code imperfect afterward, since fixing the rest would invoke a *different* catalog entry — a catalog's examples are not required to chain into a continuous, cleaned-up narrative the way a worked-example chapter's would.

Keeping every entry to this same shape, in the same order, is what makes a catalog different from a chapter: a chapter earns a reader's attention once, in sequence; a catalog is designed to be dropped into and out of repeatedly, at unpredictable entry points, over the life of a project — a consistent shape is what makes that possible. See [worked example before principles](worked-example-before-principles.md) for the complementary move of using one extended worked example to build intuition before a reader ever needs to consult individual catalog entries on their own.

A catalog also needs an explicit, non-obvious scope decision: it should hold what's "most useful to have written down," not everything that's technically valid. A technique too small or obvious to be worth a formal entry, or one that's just the rarely-needed logical inverse of an entry that already exists, is better left out — padding a catalog with low-value entries makes the genuinely useful ones slower to find. This is a judgment call revisited over time, not a one-time decision: a technique used constantly but originally judged "too obvious to write up" can turn out, in practice, to be worth adding once its absence keeps being felt.
