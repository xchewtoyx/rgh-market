---
type: concept
title: Action-Item Closure Tracking
description: >
  Give every follow-up action an owner and a tracked
  identifier, then audit whether it actually closes, so a
  decision's follow-through does not quietly stop at the
  meeting where it was named.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 15"
---

Naming an action item in a decision document is not the same
as it happening. Two separate mechanisms close that gap:

1. **Assign an owner and a tracking identifier at the moment
   the action is named** — not just a verbal commitment, but
   a linked ticket or bug ID that exists independently of the
   document and can be queried later. An action item without
   a tracking ID tends to be forgotten the moment the meeting
   ends, especially when it competes with the owner's other
   work.
2. **Audit closure on a cadence**, separate from whoever owns
   the individual item. Leadership periodically reviewing
   which action items actually closed — not just which were
   opened — is what catches items that silently stalled and
   confirms that the underlying fix was actually built, not
   only promised.

This is a stronger claim than
[small-observable-commitments](small-observable-commitments.md):
Block's discipline is about making each commitment specific
and owned at the point of decision;
closure tracking is about verifying, after the fact and at
scale, that owned commitments were actually kept. Both rest
on
[line-ownership-of-implementation](line-ownership-of-implementation.md) —
tracking makes that ownership auditable rather than assumed.

Practically, this means every action item carries an owner
and a target date at the moment it is proposed, and is linked
to a ticket that itself carries a due date — not left as a
line in the document with no independent existence. Making
the record easy to file this way, and easy to search later,
is what lets the resulting archive function as a
[searchable-decision-archive](searchable-decision-archive.md)
rather than a write-only report.

Not every open item surfaced during a decision is destined to
become a tracked action, though — some are accepted risks or
already resolved. [ROAM Risk Disposition](roam-risk-disposition.md)
is the upstream step that decides which category an item falls
into before this tracking discipline applies to the ones a
person actually owns.
