---
type: concept
title: Explanatory Text Should Sit at a Different Altitude Than What It Explains
description: >
  A caption or comment pitched at the same level of detail as the thing
  beside it just repeats it — real value comes from either dropping
  down to add precision the original leaves out, or rising above it to
  state the point the detail exists to serve.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 13"
---

Explanatory text placed right next to what it explains — a code comment, a figure caption, a footnote — only earns its place when it operates at a different level of detail than its subject. Pitched at the same level, it can only restate what's already there; pitched differently, in either direction, it adds something the original genuinely lacks.

**Dropping to a more precise level** fills in exactly what a name or a summary can't carry on its own: units, whether a boundary is inclusive or exclusive, what a permitted edge case actually means, an invariant that always holds. A generically-named quantity ("current offset") becomes useful once its explanation states precisely what "current" means in this specific context — the position of the first item not yet returned to the caller, say, rather than some other plausible reading. One useful discipline for this direction: describe what something *represents*, not the sequence of ways surrounding logic manipulates it over time — a flag's meaning when true is more durably useful to state than a chronological account of which parts of the code set and clear it.

**Rising to a more abstract level** does the opposite: it deliberately omits low-level detail to state the overall intent or purpose that the detail exists to serve. A paragraph that mechanically re-describes a conditional's branches in prose ("if X and not Y, then Z") has added a translation, not an explanation — restating logic in sentence form is still restating it. A genuinely higher-level explanation instead answers a different question: what is this trying to accomplish, and why does it matter in the context it sits in? A single well-pitched sentence at this altitude can let a reader reconstruct most of the surrounding structure themselves, and — just as importantly — gives them a basis for judging whether the detail actually accomplishes what it claims to, which a blow-by-blow restatement never can.

Three questions reliably locate the right altitude for a rising explanation: **what is this trying to do; what is the simplest way to say what explains all of it; and what is the single most important thing about it?** Answering these requires a genuine shift in thinking — noticing and cataloging detail is a different skill from stepping back and deciding which few things about that detail actually matter, and the second skill is the harder, rarer one. See [summarizing grouped ideas](summarizing-grouped-ideas.md) for the prose-document version of the same "state the point, not the category" discipline, and [annotations must add information, not repeat the name](annotations-must-add-information-not-repeat-the-name.md) for the companion failure of an annotation that matches its subject's altitude exactly and so adds nothing at all.
