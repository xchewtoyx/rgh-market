---
type: concept
title: Change Description as Verification Record
description: >
  The summary and body of a proposed change should document what changed and why,
  because they become the searchable audit trail future reviewers rely on.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 9"
---
# Change Description as Verification Record

The first line of a change description often becomes the permanent summary in search history, email subjects, and archaeology tools — it should state the change type and essence, not a vague label like "bug fix" with no context.

The full description explains **what** changed and **why**, enumerating related edits within the same atomic change. It is a record for future readers debugging or auditing, not merely a note to the current reviewer. If understanding requires detail that should not appear in a public API, that detail belongs in implementation comments — but if a competent reviewer still cannot follow the change, the code likely needs clearer structure.

## Verification Action

When verifying that a change was appropriately reviewed, read the description as a standalone document: could someone who never saw the review thread understand the intent months later? Vague descriptions make [review as historical record](review-as-historical-record.md) useless for later independent verification.
