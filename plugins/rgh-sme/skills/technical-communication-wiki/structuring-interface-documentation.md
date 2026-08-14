---
type: concept
title: Structuring Interface Documentation
description: >
  Documentation for a callable unit reads best in a fixed order —
  behavior, then parameters, then side effects, exceptions, and
  preconditions — and must stay confined to what a caller needs,
  never leaking how the thing works internally.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 13"
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice (Bass, Clements, Kazman), ch. 15"
---

Documentation for something callable — a function, an endpoint, a command — has two audiences that must never be mixed into the same passage: someone who needs to *use* it, and someone who needs to *maintain* it. Interface documentation is for the first reader only, and everything in it should be something a caller genuinely needs to know before or while calling the thing; documentation of how it works internally belongs in a separate place entirely, next to the implementation, not folded into the same paragraph. A reliable check for the boundary being violated: if explaining what a function does to callers keeps forcing you to explain internal mechanics to make the explanation make sense, that's a sign the interface itself isn't hiding enough — not a sign the documentation needs more detail.

A consistent order for interface documentation lets a reader learn to skip to the part they need rather than reading the whole thing every time:

1. **A behavioral summary from the caller's perspective** — what happens when this is called, stated as the abstraction a caller should think in terms of, not as a restatement of the implementation.
2. **Each parameter and the return value**, including constraints and any dependency between them (an argument that's only valid in combination with another, a return value whose shape depends on an input).
3. **Side effects** — any consequence that outlives the call and isn't part of what's returned: state that persists and can be observed later, a write to storage, anything else the caller needs to know happened even though it isn't in the return value.
4. **Failure modes** — what can go wrong and how the caller finds out (an error return, a raised exception), covered as part of the interface precisely because a caller has to plan for it, not as an implementation detail.
5. **Preconditions** — anything the caller must ensure is true before calling, stated explicitly rather than left to be discovered by a failure at runtime. The best number of these is as few as possible; a design that constantly demands preconditions is pushing work onto every caller that the callee could have absorbed instead, but whatever preconditions remain still need documenting.

The same discipline applies to describing what any single piece of documented behavior actually represents, not only whether it belongs in this document at all — see [labeling systems for clarity](labeling-systems-for-clarity.md) for building the names underneath this structure, and [comments complete the interface](comments-complete-the-interface.md) for why this kind of documentation has to exist as prose at all rather than being left implicit in a signature.

Documenting an interface also means deliberately choosing what *not* to promise, and that choice is worth defending even against a real, well-known pressure against it: Hyrum's Law observes that with enough callers, every actually-observable behavior of a system — documented or not — eventually gets depended on by somebody, whether or not it was ever part of the stated contract. This is true, but it doesn't change where the documented boundary should sit: the fact that some caller will inevitably notice and rely on an implementation detail is not a reason to document that detail as part of the contract, since doing so would convert something the maintainer should be free to change into something they're no longer free to change. The discipline is to keep documenting only what's genuinely promised, and treat any later breakage from undocumented reliance as the cost of that caller depending on something never promised to them.

A single interface also has more distinct documentation audiences than "caller" and "maintainer" alone once a project has any scale: a developer consuming the interface needs the contract to use it correctly; a systems integrator or tester needs the full provided-and-required picture to assemble and validate the whole system; an analyst (e.g., someone reasoning about performance) needs whatever quality-attribute commitments the interface makes, such as a stated latency SLA; and someone scouting the interface for reuse in a different context needs to know its capabilities and its available variability. These aren't just the same document read by different people — each role is actually looking for different content, which is itself a reason a single flat reference page sometimes needs distinct sections, or distinct documents, addressed to each of these readers rather than one generic description of "what this interface does."
