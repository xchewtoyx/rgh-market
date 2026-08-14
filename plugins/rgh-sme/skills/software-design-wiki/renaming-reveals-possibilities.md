---
type: concept
title: Renaming Reveals Possibilities
description: >
  Rename Class is claimed as the single most powerful refactoring, because a
  name that finally matches what a class actually does lets readers notice
  design possibilities the old name obscured.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 8"
---

"There are many powerful refactorings, but Rename Class is the most
powerful. It changes the way people see code and lets them notice
possibilities that they might not have considered before."

Worked illustration: a class starts as a passive `Properties`/flags bag
supporting [programming-by-difference](programming-by-difference.md)
configuration. As behavior migrates into it — first one computed method,
then another — it stops being passive data and becomes a genuine
collaborator with its own responsibilities. Once it's actively computing
results on request rather than just holding settings, renaming it from a
generic "configuration" name to a name matching its new role (e.g.
`MailingList`, for a class that mailing-list-forwarding code asks to compute
addresses and recipient lists) is what makes the mismatch between the old
name and current behavior visible — and once visible, further moves that
belong on the newly-named class become obvious in a way they weren't while
it was still labeled as passive configuration.

This is the same underlying claim as
[naming is a form of documentation](naming-as-documentation.md), applied
specifically to the moment a class's responsibility has shifted: the name is
not just a label but a working hypothesis about what the class is for, and
keeping it in sync with actual behavior is itself a design act, not
housekeeping.
