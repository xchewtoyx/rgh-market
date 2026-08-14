---
type: concept
title: Customer Versus Provider Documentation
description: >
  End users and maintainers need different material — keep customer-facing
  reference free of implementation and design reasoning that only
  providers should see.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 12"
---

Not every reader of a codebase or API is on the team that built it. **Customer documentation** (API users, integrators, downstream teams) needs task-oriented, complete reference and conceptual material at the right altitude for using the surface — not maintaining it. **Provider documentation** (team members, owners, future maintainers) needs implementation detail, design rationale, operational process, and internal context.

Keep the two apart as much as possible. Implementation details matter to maintainers, not to end users; design-decision reasoning belongs in design documents and implementation comments, not in API reference — the same boundary as [API comments versus implementation comments](api-comments-versus-implementation-comments.md) and [structuring interface documentation](structuring-interface-documentation.md). **Landing pages** should not try to serve both audiences from one URL; give customers and the owning team separate entry points (see [landing pages as traffic cops](landing-pages-as-traffic-cops.md)).

This split is where [when to involve technical writers](when-to-involve-technical-writers.md) matters most: providers often write provider docs well but under-estimate what customers cannot infer.
