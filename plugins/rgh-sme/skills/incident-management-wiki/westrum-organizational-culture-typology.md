---
type: concept
title: Westrum Organizational Culture Typology
description: Ron Westrum's three-way classification of organizations by how they handle information flow and failure, used to explain why some cultures sustain blameless learning and others don't.
sources:
  - title: "Accelerate"
    resource: "Accelerate: The Science of Lean Software and DevOps (Nicole Forsgren, Jez Humble, Gene Kim), ch. 3"
---

Ron Westrum, studying high-risk socio-technical environments (aviation, healthcare, nuclear power), classified organizations into three cultures based on how information — especially bad news — flows through them:

- **Pathological (power-oriented)**: information is withheld, hoarded, or distorted; messengers of bad news are **shot**; failure is handled by scapegoating; responsibility is shirked.
- **Bureaucratic (rule-oriented)**: information moves through strict formal channels; messengers are **neglected**; failure is handled through procedural justice; responsibilities are narrowly defined within silos.
- **Generative (performance-oriented)**: information is shared transparently across boundaries; messengers are **trained** and welcomed; failure is handled through **inquiry** rather than blame; responsibilities are shared collectively; novel signals are implemented and evaluated rather than crushed or merely tolerated.

The typology matters for incident work because it predicts whether a [blameless postmortem](blameless-postmortems.md) process can actually function as designed. A blameless template imposed on a pathological or bureaucratic culture doesn't produce blameless outcomes — the underlying information-flow incentives still punish or ignore people who surface uncomfortable signals, so honest reporting during and after incidents quietly dries up regardless of what the postmortem document says. Generative-culture traits (messengers trained, failure handled by inquiry) are the organizational precondition for the honesty that a [restorative just culture](restorative-just-culture.md) and [chronic unease](chronic-unease.md) both depend on.
