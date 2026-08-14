---
type: concept
title: Data Governance for Conformed Dimensions
description: The business-led process of reaching enterprise consensus on dimension attribute names, definitions, and domain values.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 4-5"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 4"
---

Reaching enterprise consensus on a [conformed dimensions](conformed-dimensions.md)'s attribute names and contents is the key challenge behind conformance — departmental data-governance history tends to produce silos with "similar but slightly different versions of the truth." IT can facilitate this process but is rarely successful as its sole driver, since it typically lacks the organizational authority to force cross-departmental agreement.

Governance should instead be business-driven: subject matter experts from the business should lead, ideally people with organizational respect, broad operational knowledge, the ability to balance enterprise-wide against departmental needs, enough gravitas and authority to challenge the status quo and enforce policy, strong communication skills, and politically savvy negotiation and consensus-building ability. The [enterprise data warehouse bus matrix](enterprise-data-warehouse-bus-matrix.md) identifies which business experts should serve as governance leads for each conformed dimension.

Governance objectives are to agree on data definitions, labels, and domain values, and to establish policies for data quality, accuracy, security, and access control. Two naming problems recur constantly during this work and are worth spotting by name:

- **Homonyms** — the same term used with genuinely different meanings across departments (Sales and Finance both use "Customer Type," but Sales' version has five values and Finance's has three). If stakeholders can't be brought to agree on one shared meaning, the fix is to give each meaning its own uniquely named attribute (`sales_customer_type`, `finance_customer_type`) rather than force a false conformance — though doing this reflexively for every homonym just perpetuates incompatible reporting, so it should be a fallback after a genuine attempt at compromise, not a first move.
- **Synonyms** — different terms across departments or processes that turn out to mean the same thing (an insurance company's Customer, Enrollee, Subscriber, Policy Holder, and Claimant; a pharma company's Physician, Doctor, Healthcare Provider, and Practitioner). These are often the easiest conformance wins available, once recognized as referring to the same underlying entity.

Working through concrete example values with stakeholders — not abstract attribute names — is what actually surfaces homonyms and synonyms: people who believe they understand a shared term until asked for real examples routinely discover they meant different things by it, or that two differently named things were the same thing all along.

Technology alone doesn't solve any of this: strong governance is a necessary prerequisite regardless of the technical approach chosen, whether an ERP system, a master data management (MDM) platform, or ETL-side cleansing and mapping is used to actually implement the agreed-upon conformed dimension. Identifying which operational system is the actual [system of record](agile-data-profiling.md) for a conformed dimension is itself part of this groundwork, since a conformed dimension is often independently maintained across several systems with no single obvious best source.

Attribute-level agreement doesn't need to be complete before work starts: identifying a minimal subset of enterprise-significant attributes — even a single one, such as an enterprise product category — is an acceptable starting point that can expand iteratively across delivery cycles. Also see [slowly changing dimension](slowly-changing-dimension.md) for the related governance decision of how each dimension attribute should respond when its value changes.
