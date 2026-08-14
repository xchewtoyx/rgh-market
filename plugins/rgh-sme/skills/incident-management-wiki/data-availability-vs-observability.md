---
type: concept
title: Data Availability vs. Observability
description: The distinction between information physically present in a system (availability) and information perceivable by an operator under active cognitive workload (observability).
sources:
  - title: "The Field Guide to Understanding 'Human Error'"
    resource: "The Field Guide to Understanding 'Human Error' (Sidney Dekker), ch. 3"
---

Failure investigations often assume that because data was recorded in logs or displayed on a screen, the operator "had" the information and should have acted on it. This conflates two distinct states:
* **Data Availability**: The physical presence of data somewhere within the system (e.g., a byte in a database, a metric in a monitoring tool, or a minor status indicator).
* **Data Observability**: The ease with which data can be perceived, interpreted, and integrated by a human operator given the display design, active workload, lighting, and attentional focus.

Under high stress and cognitive load, human attention is highly selective. Cues that are technically "available" are frequently not "observable" because the interface fails to draw attention to them or they are drowned out by noise. Investigating with the [local rationality principle](local-rationality-principle.md) requires evaluating what was observable to the practitioner in their specific context, not merely what was available in the system logs.
