---
type: concept
title: Dimensional Modeling Myths
description: Five recurring misconceptions about dimensional modeling's limits — on summarization, scope, scale, predictability, and integration.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 1"
---

Five recurring misconceptions about the limits of dimensional modeling, each false:

1. **"Dimensional models are only for summary data."** False — detailed, atomic data is needed to withstand unpredictable ad hoc queries and is "practically impervious to surprises or changes." Summary data should complement, not replace, granular detail; see [grain](grain.md). A corollary myth holds that only limited history should be stored — also false; history depth is a business requirement, not a technical constraint of the modeling style.
2. **"Dimensional models are departmental, not enterprise."** False — models should be organized around [business process](business-process.md)es (orders, invoices, service calls), not departments, to avoid multiple inconsistent extracts of the same source data. See [Kimball versus Inmon architecture](kimball-vs-inmon-architecture.md).
3. **"Dimensional models are not scalable."** False — fact tables frequently reach billions of rows, some reportedly into the trillions. Normalized and dimensional models contain identical logical content and relationships and can answer the same questions, "albeit with varying difficulty."
4. **"Dimensional models are only for predictable usage."** False — models should be designed around stable measurement processes, not a "top ten reports" list that will inevitably change. The corollary myth that dimensional models aren't responsive to change is also false; see [dimensional model extensibility](dimensional-model-extensibility.md). The key to flexibility is building fact tables at the most granular level — premature summarization creates "analytic brick walls" for both users, who can't drill down, and developers, who can't easily add dimensions, attributes, or facts.
5. **"Dimensional models can't be integrated."** False, if they conform to the [enterprise data warehouse bus architecture](enterprise-data-warehouse-bus-architecture.md). [Conformed dimensions](conformed-dimensions.md) are built and maintained as centralized, persistent master data in ETL and reused across models for integration and semantic consistency — but achieving this requires hard organizational consensus work regardless of whether the target is normalized or dimensional. It is the failure to adhere to the bus architecture, not dimensional modeling itself, that produces standalone, unintegrated solutions.

A related, more modern version of myth 3/5 holds that newer storage methodologies like Data Vault make dimensional modeling obsolete — see [Data Vault versus dimensional modeling](data-vault-versus-dimensional-modeling.md) for why the two operate at different layers and are typically combined rather than chosen between.
