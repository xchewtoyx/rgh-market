---
type: concept
title: Accuracy-First Review Ordering
description: Reviewing a document in a fixed pass order — technical accuracy, then completeness, then structure, then clarity — so effort on prose polish never gets wasted on content that turns out to be wrong.
sources:
  - title: "Docs for Developers: An Engineer's Field Guide to Technical Writing"
    resource: "Docs for Developers (Bhatti, Corleissen, Lambourne, Nunez, Waterhouse), ch. 4"
---

# Accuracy-First Review Ordering

A review that mixes truth-checking with prose polishing wastes effort: a reviewer who fixes a sentence's phrasing before confirming the claim inside it is true may spend real time improving something that gets deleted once the underlying fact turns out to be wrong. Doing every kind of review pass in a single read also raises the reviewer's cognitive load, since they're context-switching between "is this true?" and "does this read well?" on every sentence. The fix is a fixed pass order, each pass checking one thing and ignoring the rest:

1. **Technical accuracy** — is every claim, procedure, name, and number actually correct? For anything procedural, this means actually executing the steps as written (across every environment the document claims to support), not just reading them and judging plausibility — a procedure that looks correct on the page can still fail the moment someone follows it literally.
2. **Completeness** — is anything missing that a reader would need (a prerequisite, a version boundary, an unaddressed edge case)? Bringing in someone unfamiliar with the material at this stage is a deliberate way to expose assumptions the author can no longer see.
3. **Structure** — is the material organized so a reader can find and follow it?
4. **Clarity and brevity** — only once accuracy, completeness, and structure are settled does polishing the actual wording become worthwhile.

## Verification Action
- When asked to review a document, resist the pull to fix prose on first read — note accuracy problems first, and defer wording suggestions until a later pass (or a different reviewer) so accuracy issues don't get lost among style comments, and so no one spends effort polishing a claim that shouldn't survive review at all.
- When a procedure is the subject of a claim ("run X to get Y"), verification means actually running it, not just checking that it reads plausibly — see [claim-type-taxonomy](claim-type-taxonomy.md) for distinguishing claims that need this kind of direct reproduction from claims that can be checked against a source instead.
- Match reviewer expertise to review stage: a reviewer who already knows the subject is best used early for accuracy/completeness; a reviewer who resembles the eventual audience is best used later, since they'll catch gaps an expert reviewer no longer notices having internalized the missing context long ago.
