---
type: concept
title: Business Process
description: A low-level operational activity, expressed as an action verb, that generates measurement events and forms the unit of dimensional design and bus matrix rows.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
---

A business process is an operational activity performed by the organization — taking an order, processing a claim, registering students, a monthly account snapshot. Business processes generate the performance metrics that become [fact-table](fact-table.md) rows. Characteristics: they are expressed as action verbs, supported by an operational source system, and generate key performance metrics (direct or derived) — one process's outputs often feed the next process's inputs, forming a [value chain](value-chain.md) that becomes a chain of related fact tables.

Business processes are **not** the same as organizational departments or functions. Modeling around departments causes the same underlying data to be duplicated and inconsistently labeled across teams; publishing data once, organized by process, is what keeps the model consistent. Business users often talk in terms of strategic initiatives rather than processes — these must be decomposed into underlying business processes to become project-sized dimensional modeling work.

Selecting the business process is the first step of the [four-step dimensional design process](four-step-dimensional-design-process.md). Most fact tables focus on a single business process, and each business process typically corresponds to one row in the [enterprise data warehouse bus matrix](enterprise-data-warehouse-bus-matrix.md). The first DW/BI project should target the business process that is both most critical to users and most feasible given data availability, quality, and organizational readiness.
