---
type: concept
title: Trimming Precision to What the Decision Needs
description: >
  Reporting more decimal places or finer units than a reader will ever
  act on costs reading time without adding information, so precision
  should be trimmed to whatever the reader's actual decision requires.
sources:
  - title: "Information Dashboard Design"
    resource: "Information Dashboard Design (Stephen Few), ch. 3"
---

$3,848,305.93, $3,848,305, and $3.8M can all be the same underlying fact, but they are not equally readable — every digit past what a reader would ever act on is pure processing cost with no informational return. A reader scanning a report of numbers has to consciously filter out the excess precision before getting to the figure that actually matters, and that filtering happens on every number, every time the report is read. The same failure shows up with units as much as digits: timestamps reported to the second, or measures carried to four decimal places, when the reader's decision only ever operates at the level of minutes or whole units.

The fix is to ask, for each number before it's published, what precision the reader's decision actually discriminates on — not what precision the underlying system happens to store or compute. A dashboard tracking whether a project is on budget doesn't need the underlying ledger's cent-level accuracy; a report meant to flag which regions are underperforming doesn't need a fourth decimal place on a percentage that will be read as "about 12%" regardless. This is the numeric-precision analog of [cutting clutter](cutting-clutter.md) from prose: excess precision, like excess words, doesn't make the result more correct, only slower to read, and the test is the same functional one — does this level of detail do work the reader needs, or can the number survive being rounded without losing anything the reader would have used?
