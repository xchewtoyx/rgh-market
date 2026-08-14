---
type: concept
title: OLTP vs. OLAP
description: The core distinction between transactional and analytical database systems.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 3"
---

Analytical database environments are designed around the core operational differences between transactional processing and analytical processing workloads:

*   **OLTP (Online Transaction Processing):** User-facing systems that handle high volumes of low-latency reads and writes, typically targeting individual records by their primary key. They represent the current, highly dynamic point-in-time state of the business.
*   **OLAP (Online Analytical Processing):** Decision support systems designed for internal analysts. They handle low query volumes but scan millions or billions of historical event records to execute aggregate functions (such as `COUNT`, `SUM`, `AVG`).

To protect production OLTP databases from performance degradation caused by expensive analytical queries, analytical data is typically extracted, transformed, and loaded (ETL) into a separate read-only data warehouse. In this analytical environment, data is modeled using specialized schemas such as the [star-schema](star-schema.md) or [snowflake-schema](snowflake-schema.md), or pre-aggregated into an [olap-cube](olap-cube.md).
