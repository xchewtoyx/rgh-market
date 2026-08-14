---
type: concept
title: Data Quality Dimensions (Accuracy, Completeness, Timeliness)
description: >
  The three characteristics used to judge whether data matches what the
  business expects of it, as a basis for building validation gates.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
---

Data quality is the optimization of data toward the state the business
expects it to be in — does it match business-metadata expectations? Three
characteristics define it:

- **Accuracy**: factually correct, free of duplicates, numerically right.
- **Completeness**: all required fields are populated.
- **Timeliness**: available when it's needed.

These three give a pipeline concrete, checkable targets to build
[validation gates](late-arriving-data.md) against, rather than a vague
"is the data good?" question. A dataset can fail on just one dimension — e.g.,
fully accurate and complete data that arrives too late to be useful is a
timeliness failure, not an accuracy one — so quarantine and error handling
should be able to distinguish which dimension failed, because the fix differs
(a completeness failure needs a missing-data policy; a timeliness failure
needs a [late-arriving data](late-arriving-data.md) policy; an accuracy
failure needs source-level investigation).
