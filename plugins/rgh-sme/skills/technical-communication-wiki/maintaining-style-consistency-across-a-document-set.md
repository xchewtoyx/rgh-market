---
type: concept
title: Maintaining Style Consistency Across a Document Set
description: >
  Consistency means similar things are presented the same way and
  different things are visibly different — a trust guarantee that lets
  a reader's pattern-matching from one document transfer safely to the
  next, and one that erodes on its own unless it's documented, enforced,
  and defended against well-meaning "improvements."
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 17"
---

Consistency across a set of documents — the same term always meaning the same thing, the same kind of section always structured the same way, the same formatting convention used everywhere it applies — pays off twice. It gives a reader **cognitive leverage**: once they've learned how one document in the set handles something, that knowledge transfers immediately to every other document following the same convention, instead of every document needing to be learned from scratch. It also prevents a specific class of mistake: a reader who recognizes a familiar pattern will import assumptions from where they last saw it, and if the pattern isn't actually consistent, those imported assumptions are wrong — inconsistency doesn't just cost extra learning, it actively produces incorrect inferences that feel confident.

Consistency erodes on its own, without anyone intending it to: different writers join a document set at different times, work from different prior habits, and often aren't aware of conventions another contributor already established elsewhere in the same set. Left alone, this drift only grows. Three practices counteract it:

- **Document the convention** somewhere genuinely visible — a style guide a new contributor will actually be pointed to, not a norm that only lives in the heads of whoever set it. Borrowing an existing, well-regarded style guide as a starting point is usually faster and more defensible than drafting one from scratch. For a narrower, local convention that doesn't warrant a whole guide entry, write it down right next to where it applies, since an unwritten convention is one nobody else can be expected to know about or follow.
- **Enforce it**, because documentation alone is routinely forgotten even by people who've read it — automated checks (a linter, a pre-commit hook, a build-time validation) catch mechanical violations far more reliably than anyone remembering to self-check, and review by another person catches the rest, including violations no automated check could reasonably express. The more consistently reviewers flag deviations, the faster a convention actually becomes second nature across the whole set rather than something only enforced after the fact.
- **Follow existing precedent before inventing a new pattern** — when starting a new document or section, look at how comparable ones nearby already handle the same kind of content and match that, even where nothing was ever formally written down. Before making a structural or stylistic choice, it's worth actively asking whether a similar choice was already made elsewhere in the set, and treating that precedent as the default rather than reasoning from scratch each time.

A settled convention should not be revisited casually just because someone has a marginally better idea for it later. The value of everything already conforming to the existing convention typically outweighs the value of any one alternative being somewhat cleaner, and a change that isn't retrofitted everywhere creates a worse problem than the one it was meant to fix — a mixed, partially-migrated document set where a reader can no longer trust that a familiar-looking pattern means what it used to. Changing a settled convention is only worth it when there's genuinely new information that wasn't available when the convention was set, and the improvement is large enough to justify updating every existing instance, not just the ones being touched anyway.

Consistency has a reciprocal failure worth guarding against too: forcing genuinely different kinds of content into the same template, heading pattern, or phrasing purely for uniformity's sake breaks the same trust guarantee from the other direction — a reader who's learned "this pattern means X" is misled when it's been imposed on content that isn't actually X. Consistency's whole value rests on "looks the same" reliably meaning "is the same"; applying it to things that aren't alike is not extra rigor, it's a different way of making the reader's pattern-matching wrong.
