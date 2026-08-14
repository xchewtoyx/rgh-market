---
type: concept
title: Sharp End vs. Blunt End
description: The distinction between practitioners who directly interact with a safety-critical process (sharp end) and the organizational layers that shape their constraints (blunt end).
sources:
  - title: "The Field Guide to Understanding 'Human Error'"
    resource: "The Field Guide to Understanding 'Human Error' (Sidney Dekker), ch. 2"
---

In complex socio-technical systems, work is distributed across two structural layers:
* **The Sharp End**: Practitioners who are in direct physical or operational contact with the hazardous process (e.g., control room operators, on-call SREs, pilots). They inherit the defects of design, policy, and management.
* **The Blunt End**: The organizational hierarchy (executives, regulators, policy makers, tool vendors) that controls resources, designs procedures, and determines operational priorities.

```
       +--------------------------------------------------+
       |                    BLUNT END                     |
       |  (Executive Priorities, Budget Constraints,     |
       |   Equipment Vendors, Regulatory Frameworks)      |
       +------------------------+-------------------------+
                                |
                   Shapes, Resource-Constrains,
                     and Pushes Trade-offs
                                |
                                v
       +--------------------------------------------------+
       |                    SHARP END                     |
       |  (Pilots, Nurses, Control Room Operators, Techs) |
       +--------------------------------------------------+
```

The blunt end shapes the environment of the sharp end by supplying resources, technology, and goal constraints. When a failure occurs, the proximal bias causes observers to focus on the sharp-end operators who were closest to the event. However, to find systemic vulnerabilities, investigations must look at how blunt-end decisions pushed trade-offs down to the sharp end, causing [practical drift](practical-drift.md) and creating [safety bureaucracy](safety-bureaucracy.md).
