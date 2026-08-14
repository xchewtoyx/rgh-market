---
type: concept
title: Data Governance Program
description: >
  Establishing an organization-wide framework and center of excellence for
  data policy before building pipelines, rather than bolting governance on
  after the fact.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 9"
---

Data governance is the organization-wide management of data: policies and
procedures for how data is collected, stored, secured, transformed, and
reported, aimed in large part at legal and regulatory compliance, plus
ongoing monitoring of data quality and accuracy. It needs an explicit
framework naming which people and roles are responsible for managing,
maintaining, and using an organization's data — governance without named
ownership tends to stay aspirational.

A common organizational mechanism is a **governance center of excellence
(CoE)**: a hub that develops governance policies, procedures, and standards,
and defines the roles, responsibilities, and decision processes for
data-related work across the organization. The practical recommendation is
to invest in defining this framework and standing up the CoE *before*
building a data warehouse or lake, not after — projects that treat
governance as something to retrofit once quality or compliance problems
surface tend to fail more often than ones that establish ownership and
standards up front.

This is the organizational counterpart to the technical mechanisms a pipeline
team builds regardless: a [data catalog](data-catalog.md) and
[data lineage](data-lineage.md) tracking are what a governance program's
policies actually get enforced *through*, and
[master data management](master-data-management.md) is typically one of the
concrete programs a governance CoE sponsors. A governance framework without
those technical mechanisms has no way to observe whether its own policies are
being followed; the technical mechanisms without a governance framework have
no organizational mandate deciding what they should be checking for.
