---
type: concept
title: Stale Evidence Maintenance
description: A claim or document that was accurately verified when written can become false later through ordinary drift, so verification needs an ongoing maintenance owner, not just a one-time author.
sources:
  - title: "Docs for Developers: An Engineer's Field Guide to Technical Writing"
    resource: "Docs for Developers (Bhatti, Corleissen, Lambourne, Nunez, Waterhouse), ch. 11"
---

# Stale Evidence Maintenance

Verification is usually treated as something that happens once, at the moment a claim is written and checked. But a claim that was fully accurate at that moment can become false later without anyone editing it — the system it describes changed, the policy it cites was superseded, the dependency it names was deprecated, the price/number it states moved. The claim reads exactly as confidently as it did when it was true, which is precisely what makes stale evidence dangerous: nothing about the text itself signals that it needs to be re-checked.

## Why Staleness Is Different From an Error
An error is wrong from the moment it's written and can, in principle, be caught by verifying it once, carefully, before publication. Staleness is a property of *time*, not of the original verification effort — even a claim that was checked as rigorously as possible will eventually go stale if whatever it depends on changes and nobody re-checks it. This means no amount of up-front review diligence alone prevents staleness; it requires an ongoing process, not a one-time gate.

## Maintenance Practices That Catch Staleness
- **Assign an owner per claim-bearing section**, not just an author for the whole document — staleness is caught fastest by someone who is notified when the underlying thing changes, not by someone stumbling across the document later.
- **Tie re-verification to the events that cause staleness**: release notes, changelogs, support tickets, and deprecation announcements are natural trigger points for asking "does this affect anything we've already asserted was true?" rather than waiting for a scheduled audit to catch it much later.
- **Make version/time boundaries explicit** in the claim itself ("as of version X" / "as of [date]") rather than stating it as a timeless fact — this doesn't prevent staleness, but it tells a future reader exactly how much to trust the claim's current accuracy and gives a reviewer a concrete trigger for when it needs re-checking.
- **Run scheduled audits as a backstop**, not a primary defense — event-triggered re-verification catches staleness caused by known changes; a periodic audit is needed to catch the changes nobody thought to link back to the document at all.
- **Retire or flag content explicitly rather than leaving it to quietly go wrong** — a claim marked as deprecated or superseded is far less harmful than one that looks current but silently isn't; removing or clearly marking outdated material prevents it from being cited as if it were still verified.

## Verification Action
When reviewing an existing claim rather than a new one, do not assume prior verification still holds — check when it was last verified and whether anything it depends on has changed since, especially if no maintenance owner or re-verification trigger is evident. Treat "this was correct when checked" and "this is correct now" as two different questions requiring two different pieces of evidence.

## See Also
- [Continuous Integrity Auditing](continuous-integrity-auditing.md)
- [Ephemeral Source Preservation](ephemeral-source-preservation.md)
