---
type: concept
title: API Comments Versus Implementation Comments
description: >
  Reference documentation in code splits into comments on the public
  surface, written for callers who may know nothing about the
  implementation, and comments on the implementation itself, written for
  maintainers who need the reasoning behind non-obvious choices.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 12"
---

Most day-to-day reference documentation lives in code comments, but not every comment serves the same reader. **API comments** document the public surface — what a caller needs to invoke something correctly without reading its body. They must not assume the reader knows the API as well as the author does, and they should not discuss internal design decisions that belong in a design document or implementation comment instead. **Implementation comments** document the code behind the surface. They can assume more domain knowledge because their audience is whoever will maintain that implementation, but people leave projects — so even here, spell out *why* non-obvious code was written the way it was, not just what it does.

The split mirrors interface-versus-implementation separation in code design: a reader using an API should not have to reconstruct internal trade-offs from reference material, and a maintainer should not have to infer rationale that was never written down because "everyone on the team knew." When reference material drifts across that boundary — design rationale in an API comment, or caller-facing preconditions buried only in a `.cc` file — both audiences lose. See [structuring interface documentation](structuring-interface-documentation.md) for keeping customer-facing reference free of provider-only reasoning, and [comments complete the interface](comments-complete-the-interface.md) for why signatures alone are not enough documentation for either audience.
