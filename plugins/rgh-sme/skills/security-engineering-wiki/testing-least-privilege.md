---
type: concept
title: Testing Least Privilege
description: >
  Test both that user profiles have exactly the access their role needs
  (testing of least privilege) and that test infrastructure itself runs
  with minimal access (testing with least privilege).
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 5"
---

# Testing Least Privilege

[Least privilege](least-privilege.md) has two testing dimensions.

**Testing *of* least privilege** verifies that access is granted correctly:
define what each user profile (data analyst, customer support, SRE) needs —
which APIs and data, read or write, permanent or temporary; define
scenarios where that profile attempts actions (read, bulk read, write,
delete, administer) with expected outcomes; run them and compare actual
against expected. Ideally these run *before* code or ACL changes land, so
an over-grant never reaches production; where coverage is incomplete,
compensate with access monitoring and alerting.

**Testing *with* least privilege** ensures the test infrastructure itself
holds only the access it needs. Without proper test infrastructure, tests
that read/write data or mutate service state force dangerous grants — e.g.
analysts given read/write on raw production user data because there is
nowhere else to work. Ask: do they need write? Can anonymized data sets,
test accounts, or a separate environment with its own credentials serve?
A separate keyed environment also means a botched test cannot overwrite
production data or take down a production service.

Tradeoff notes:

- Using special test accounts *in production* avoids building a mirror
  environment but muddies auditing and ACLs — a genuine
  security/reliability tradeoff, not a free shortcut.
- Start small rather than building the ideal stack: separate environments
  and credentials, limit access types, limit data exposure; short-lived
  cloud environments beat nothing.
- Weigh the cost of the infrastructure against the cost of *not* having
  it: can you live with every critical-operation test being able to take
  down production, and analysts holding avoidable access to sensitive
  data?
- Above all, build a framework people will actually use — if testing is
  too hard, people will test in production and circumvent every control
  you put in place.
