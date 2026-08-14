---
type: concept
title: Data Transfer Resource
description: >
  A shared storage endpoint with creation and retrieval operations that lets
  parties exchange data without simultaneous availability or prior mutual
  knowledge.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 3"
---

A **data transfer resource** is a specialized [information holder resource](information-holder-resource.md)
— shared storage at a globally unique address writable and readable by multiple
clients. Requires at least one [state creation operation](state-creation-operation.md)
and one [retrieval operation](retrieval-operation.md).

Decouples participants in **time and location** when direct connection is
impossible or undesirable. Asynchronous persistence is more reliable than
synchronous client/server for some handoffs but adds latency; unknown recipient
count affects scalability; storage ownership and retention must be explicit.

Use when two or more parties exchange payloads without knowing each other in
advance or being online together.
