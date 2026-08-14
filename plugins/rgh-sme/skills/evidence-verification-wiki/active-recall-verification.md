---
type: concept
title: Active Recall Verification
description: A verification methodology that avoids leading or yes/no questions, forcing sources or test systems to independently produce data to prevent passive confirmation bias.
sources:
  - title: "The Chicago Guide to Fact-Checking, Second Edition"
    resource: "The Chicago Guide to Fact-Checking, Second Edition (Brooke Borel), ch. 3"
  - title: "Documenting Software Architectures: Views and Beyond"
    resource: "Documenting Software Architectures (Clements, Bachmann, Bass, Garlan), ch. 11"
---
# Active Recall Verification

**Active recall verification** is the practice of structuring verification queries to force a source or a system to independently produce evidence rather than passively confirming a pre-existing statement. This methodology is designed to prevent "rubber-stamping," where a tired or biased source agrees to a statement without carefully checking it.

## The Problem with Passive Confirmation
When asked a leading or yes/no question (e.g., "Is your name spelled John Smith?" or "Is the system latency 12 milliseconds?"), a human source or a system interface is highly likely to respond with a simple "yes." This happens because:
- **Cognitive Laziness**: It is easier to agree than to recall and verify.
- **Acquiescence Bias**: A tendency to agree with the researcher or the draft document.
- **Superficial Review**: The source reads the draft quickly and assumes minor details are correct.

If the draft contains a subtle error (e.g., "Jon Smith" or "21 milliseconds"), passive confirmation will fail to catch it.

## Verification Techniques
To implement active recall verification, the reviewer must rephrase questions to require active retrieval:
- **Avoid Leading Questions**: Instead of asking, "Is the release date October 15th?", ask, "What was the exact release date?"
- **Avoid Yes/No Spelling Queries**: Instead of asking, "Is your title Principal Architect?", ask, "Can you spell your exact title for our records?"
- **Force Independent Calculation/Measurement**: In technical settings, instead of showing a system metric and asking if it is correct, ask the engineer to retrieve the log or run a fresh query to provide the raw value.
- **Require Documented Proof**: Ask the source to provide the underlying document or link rather than verbally confirming.

## Also Applies to Whole-Document Review Sessions
The same passive-confirmation failure occurs at the level of an entire review meeting, not just a single fact query: a reviewer handed a document and asked "does this look right?" tends to skim and confirm, the same way a source asked a yes/no question tends to agree. A review session designed instead to hand each reviewer a concrete question or task to actively work through against the document — grounded in a specific anticipated stakeholder use, not a generic "any comments?" — forces the same kind of active retrieval that makes single-fact verification queries effective, and surfaces gaps a passive read-through would miss.

## See Also
- [Defining Checkable Claims](defining-checkable-claims.md)
- [Verification Models](verification-models.md)
