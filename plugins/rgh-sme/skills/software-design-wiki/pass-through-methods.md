---
type: concept
title: Pass-Through Methods
description: >
  A pass-through method does little beyond invoking another method with a
  similar or identical signature, adding interface complexity without
  contributing distinct functionality — usually a sign that two classes
  don't have a clean division of responsibility.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 7"
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3, Middle Man"
---

**Red flag: pass-through method** — "does nothing except pass its arguments
to another method, usually with the same API as the pass-through method. This
typically indicates that there is not a clean division of responsibility
between the classes." A real example: a student `TextDocument` class where 13
of its 15 public methods were pure pass-throughs to an internal `TextArea`
(`getLastTypedCharacter()`, `getCursorOffset()`, `insertString(...)`, each
just forwarding to `textArea`'s method of the same name).

The costs are concrete: interface complexity goes up (callers have one more
thing to learn) for zero net functionality gain, and it creates a
signature-change [dependency](dependencies-as-a-cause-of-complexity.md)
between the two classes — change `TextArea.insertString`'s signature and
`TextDocument.insertString` must follow.

Diagnosis: when you see pass-through methods, ask "exactly which features and
abstractions is each of these classes responsible for?" You'll typically find
the responsibilities overlap. Four refactoring options follow from that
diagnosis:

1. Expose the lower-level class directly to callers, removing the higher
   class's responsibility entirely.
2. Redistribute functionality between the two classes so the calls between
   them aren't needed at all.
3. Merge the classes if the responsibilities can't be cleanly disentangled.
4. (Sometimes overlooked) accept that same-signature methods aren't
   automatically a problem — see
   [when interface duplication is OK](interface-duplication-when-ok.md) for
   the cases where a shared signature is legitimate.

In the worked example, the fix collapsed three tangled classes into two with
clearer boundaries.

Fowler and Beck name the class-level version of this pattern **Middle Man**:
healthy encapsulation delegates (asking a director's diary about
availability without needing to know it's a diary) taken too far, until a
class is mostly forwarding calls to another class. Their cure vocabulary
overlaps with the four options above:
**[Remove Middle Man](remove-middle-man.md)** once too much of the interface
is pure delegation (option 1), **[Inline
Function](inline-function.md)** for a few
thin pass-throughs, and — when the middle man does have some real extra
behavior worth keeping rather than collapsing away entirely — folding it in
via [Replace Superclass with Delegate](replace-superclass-with-delegate.md)
or [Replace Subclass with Delegate](replace-subclass-with-delegate.md).
[Message Chains](message-chains.md) are the usual origin of an accidental
Middle Man: hiding every link of a navigation chain with
[Hide Delegate](hide-delegate.md) can turn each intermediate object into
exactly this smell, which is why Message Chains' preferred cure is often
pushing the final usage down the chain instead of hiding every step.
