---
type: concept
title: Data Retention and Lifecycle Management
description: >
  The engineering side of deciding when data gets archived or destroyed, and
  why regulation makes active destruction a pipeline requirement rather than
  an optional cleanup task.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 15"
---

Data lakes historically encouraged ignoring the end of a dataset's lifecycle —
"why discard when you can add more storage?" Two forces now push retention
and archival back into pipeline design:

- **Cost visibility**: cloud pay-as-you-go storage makes cost visible to
  finance every month, and cloud vendors offer cheap archival tiers (with
  policy controls against accidental or deliberate deletion) — though
  retrieval from those tiers isn't cheap, so tiering has to be paired with
  [data temperature tiering](data-temperature-tiering.md) decisions made
  deliberately, not by default.
- **Privacy and retention law**: regulation (GDPR, CCPA) requires *active*
  data destruction to honor rights like "right to be forgotten." This is easy
  in a SQL warehouse (`DELETE ... WHERE`) but was historically hard in
  write-once-read-many data lakes — a gap that transactional table formats
  (Hive ACID, Delta Lake) exist partly to close by making row-level delete
  and update tractable at lake scale.

Practically, this means a pipeline needs an explicit retention and deletion
path designed in from the start for any dataset that might contain regulated
personal data — bolting deletion on after the fact, once data has been copied
into a dozen downstream tables, is much harder than designing for it (and for
[data lineage](data-lineage.md) to know where all the copies are) up front.

**Per-customer, honor-anytime retention (delete-on-request, capped
lifespans) creates a reproducibility gap for any pipeline that spans longer
than the shortest retention window it draws on.** A multi-quarter pipeline
built from data with, say, a several-month retention cap will find that its
training or reference set is no longer reconstructible by the time someone
needs to reproduce or re-diagnose an old run — not a hypothetical risk: a
real incident traced a model regression to biased ground-truth labels, but
couldn't conclusively confirm it because the original dataset that would
have proven it had already expired under retention rules by the time anyone
went looking. Two concrete mitigations: exclude time-limited-retention data
from any set that specifically needs to stay stable for comparison over
time (an evaluation or reference set, not just the training data feeding a
single run), and monitor how that set's own composition and metrics drift
as retention deletes and any compensating backfill both alter it — treating
retention-driven composition change as a signal worth tracking, not an
invisible background process.

**Route all requests for retention-governed data through one team or
service that accounts for what's flagged for deletion**, rather than
letting every consumer issue its own ad hoc extraction against the raw
store. This mirrors [data access policy
enforcement](data-access-policy-enforcement.md)'s reasoning applied to
retention instead of authorization: a rule enforced only in documentation
depends on every consumer independently remembering it, while a single
structural choke point — here, a data-supply team or service that already
knows what's been deleted or is about to expire — makes "does this dataset
respect retention" true by construction instead of by convention.
