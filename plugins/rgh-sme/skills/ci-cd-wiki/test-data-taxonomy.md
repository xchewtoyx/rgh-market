---
type: concept
title: Test Data Taxonomy
description: >
  Reference, master, and transactional test data need different sourcing
  strategies — version-controlled scripts, programmatic builders, and dynamic
  generation, respectively — rather than one approach applied uniformly.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 12"
---

# Test Data Taxonomy

Not all test data should be created the same way:

- **Reference data**: static lookup tables (country codes, currency symbols,
  status codes). Managed via
  [version-controlled migration scripts](database-migration-scripts.md) —
  it's effectively part of the schema, not test-specific data.
- **Master data**: core business entities (users, products, accounts).
  Created programmatically in test setup via builder patterns — see
  [acceptance test data management](acceptance-test-data-management.md)'s
  data builder pattern.
- **Transactional data**: operational event records (orders, audit logs).
  Generated dynamically during test execution, since it's meant to represent
  the specific scenario each test is exercising rather than fixed state.

Treating all three the same — e.g. trying to seed transactional data via
static migration scripts, or reference data via ad hoc builders in every test
— produces either brittle tests or an unmaintainable pile of duplicated setup
code. Matching the sourcing strategy to the data's actual nature keeps test
setup both fast and realistic.
