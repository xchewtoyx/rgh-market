---
type: concept
title: Drawing Boundaries Between Infrastructure Components
description: Five lenses — change patterns, component life cycle, organizational structure, resilience, and security/governance — for deciding where to split infrastructure into separate, independently deployable components.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 15"
---

Dividing infrastructure, like dividing any system, means looking for *seams* — natural places where you can change behavior in one part without editing another. Several complementary strategies help find them, all ultimately optimizing for the ability to make changes easily, safely, and quickly:

- **Natural change patterns** — examine what tends to change together (ideally at the fine grain of individual commits, not high-level tickets) to find things that are already effectively coupled, and things that already change independently.
- **Component life cycle** — group resources that are rebuilt or replaced at similar rates and for similar reasons. Fast-changing compute and slow-changing, stateful storage are the classic split (see the [micro stack pattern](micro-stack-pattern.md)), and this alignment pays off in faster [pipeline](infrastructure-delivery-pipeline.md) feedback, since a stage doesn't need to rebuild something that rarely changes just to test something that does, and in cost management, since slow-changing pieces can be left running while fast-changing ones are torn down.
- **Organizational structure** — Conway's Law predicts that a system's structure will mirror the structure of the organization that builds it; components that multiple teams must jointly change tend to create friction, so aligning infrastructure boundaries to team boundaries (or restructuring teams to match the desired architecture, the "Inverse Conway Maneuver") reduces that friction directly.
- **Resilience** — components that can be automatically or routinely rebuilt via well-defined tooling need less risky manual "infrastructure surgery" when something fails; organizing by life cycle also supports this, since it clarifies what a rebuild process needs to preserve.
- **Security and governance** — aligning boundaries to differing regulatory or compliance requirements (PCI-scoped services, personal-data-handling services) lets each component's delivery process be tailored to what it actually needs, rather than applying the strictest requirement everywhere.

A common trap is organizing infrastructure by *technical* function — all networking together, all database infrastructure together — rather than by the service each piece supports. This "horizontal" grouping means a single user-facing service's infrastructure is spread across multiple stacks owned by different specialist teams (adding coordination overhead for every change), and it means one team's shared stack change can carry the [blast radius](blast-radius.md) of every unrelated service it happens to host. Prefer grouping vertically, around the service or domain concept, over grouping horizontally, around the technology. A related trap: network security zones (frontend/app/database) are a real and useful boundary for defending against network attacks, but they are not automatically a good boundary for infrastructure *code* — the threat model for a malicious infrastructure code change is different from the threat model for network intrusion, so code boundaries should be chosen using the criteria above, not copied from the network diagram.
