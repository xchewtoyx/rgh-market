---
type: concept
title: When to Involve Technical Writers
description: >
  Engineers can document for their own team; technical writers earn
  their place on documentation that must work for readers outside the
  authoring team's assumptions — especially cross-team or external API
  audiences.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 12"
---

Assigning a technical writer to every "important" project does not automatically improve velocity. Most engineering teams can document for themselves well: the feedback loop is immediate, domain assumptions are shared, and needs are obvious. **Engineers most need writing help when the audience is not themselves** — when documentation must work for another team, an external API consumer, or any reader who does not share the author's mental model.

Technical writers are a limited, specialized resource, so they should concentrate where teams have the least visibility into reader needs: **cross-boundary documentation** that spans APIs or organizations. A team knows its own gaps; it often cannot see what another team needs to know. A technical writer is well positioned to stand in for that unfamiliar reader and challenge assumptions about what is obvious, useful, or missing — the same function as an [audience review](reviewing-documentation-for-fitness-of-purpose.md), but sustained across a documentation set rather than one changelist. See [customer versus provider documentation](customer-versus-provider-documentation.md) for why boundary-crossing material is where provider assumptions fail most often.
