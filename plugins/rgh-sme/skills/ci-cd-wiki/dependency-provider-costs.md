---
type: concept
title: Dependency Provider Costs
description: >
  Publishing or exporting a library creates ongoing reputation, fork-sync, and
  support obligations — not a one-time release — and neglected exports can break
  unrelated builds years later.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 23"
---

# Dependency Provider Costs

Adding a dependency is a consumer-side cost; **being a provider** carries its
own. Exporting a library — open source or internal shared dependency — is not
pure upside. Two recurring failure modes:

1. **Reputation drag** when the release is poorly maintained — good code with
   bad community stewardship still harms the organization (community over
   code).
2. **Efficiency tax from fork divergence** — given time, internal and external
   (or otherwise forked) copies drift apart and keeping them aligned consumes
   ongoing engineering effort.

**Do not release without a plan and mandate for long-term support.** Google's
gflags open-source release (~2006) illustrates structural traps: legal/repo
segregation prevented unifying internal and OSS copies; outside contributions
could not flow back; product priorities shifted away from the portability the
library served; original authors left; the OSS release rotted until external
developers forked again.

Technical fallout followed reputational damage: other Google-backed OSS
projects converged on an undocumented stable subset between internal and
external forks (~2008–2017). When C++ library teams later changed observable
implementation details, builds broke across projects relying on **unpromised
stability** — delaying a large optimization because a handful of dependents
depended on behavior nobody had committed to support. Hyrum's Law applies
across forked APIs maintained by separate organizations.

Provider-side costs pair with consumer-side discipline in
[semantic versioning](semantic-versioning.md),
[minimum version selection](minimum-version-selection.md), and preferring
[source-level integration](source-vs-binary-component-integration.md) where
organization boundaries allow — more code under one coordinator's transparency
simplifies dependency management.

See [external consumer upgrade blocking](external-consumer-upgrade-blocking.md)
when paying customers or invisible external usage constrains provider evolution.
