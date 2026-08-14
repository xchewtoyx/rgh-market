---
type: concept
title: Supply-Chain Compromise
description: >
  Attacking a trusted upstream input — a dependency, a build tool, a CI
  job — instead of the target directly, so the blast radius spans every
  downstream consumer of that input rather than one system.
sources:
  - title: The DevOps Handbook
    resource:
      "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 22"
  - title: Infrastructure as Code
    resource: "Infrastructure as Code, 3rd Edition (Morris), ch. 7"
---

# Supply-Chain Compromise

The general pattern behind this vulnerability class: instead of attacking
a target directly, an adversary compromises something the target *trusts
by default* — an open-source dependency, a build tool, a CI/CD job, a
signing key — and lets the target's own trust do the work of delivering
the payload. What makes this class distinct from a direct exploit is
blast radius: one poisoned upstream input compromises every downstream
consumer simultaneously, not just the one system an attacker directly
reached. SolarWinds (a malicious payload inserted into a legitimate
software update, reaching 18,000+ customers) and Codecov (a CI-poisoning
attack that stole CI-environment credentials from its uploader tool,
reaching a large share of its customer base) are the same pattern at
different points in the chain: the update mechanism and the CI tooling,
respectively, were the trusted inputs that got poisoned.

**The CI/CD pipeline itself is part of the supply chain, not just a
delivery mechanism for it.** A build/test server holding
version-control credentials is a target in its own right — compromising
it can enable source theft or, with write access, injection of malicious
changes into the repository. One documented technique: hiding malicious
code inside unit tests, on the reasoning that "no one actually looks at
the unit tests, and they're run every time someone commits code." This is
the concrete argument for treating CI/build infrastructure as
production-tier attack surface — code review, hardening, and
least-privilege scoping apply to the pipeline that produces an artifact,
not only to the artifact's own logic. A specific reason CI/CD secret
storage deserves that scrutiny: most pipeline tools that "encrypt" stored
secrets can also decrypt them on demand to run a job, so anyone who can
get the tool to execute a command — in practice, often anyone who can
merge code the pipeline will run — can typically extract any secret it
holds, encrypted at rest or not. [Secretless authorization](secretless-authorization.md),
where available, removes this exposure entirely by never giving the
pipeline a static secret to hold.

**Old, unpatched vulnerabilities dominate real exploitation, not novel
ones.** Multiple independent breach studies converge on the same finding:
a handful of known CVEs, most of them years old, account for the large
majority of exploited supply-chain vulnerabilities in practice, and
median time to remediate a known vulnerable dependency has been measured
in the hundreds of days. The practical implication is that supply-chain
risk is overwhelmingly a *currency* problem — staying reasonably close to
upstream — rather than a novel-attack problem. A further caution: a
dependency's popularity (stars, forks, download counts) does not predict
faster remediation or better security practice, so popularity is not a
substitute for actually checking a dependency's patch cadence.

**Structural defense follows the same shape as any trust-boundary
problem**: don't trust an input because of where it claims to come from —
verify properties of the input itself. This is
[verify artifacts, not just people](verify-artifacts-not-people.md)
applied to the supply chain specifically: a build artifact should carry
checkable provenance (what produced it, from what source, having passed
what checks) rather than being trusted because it arrived through the
expected pipeline. The mechanics of building that verification — signed
build provenance, SBOM generation, dependency-vulnerability scanning,
admission policy gating deployment on passed checks — are a delivery-
pipeline concern with its full treatment elsewhere; what belongs here is
the threat model those mechanisms exist to answer, and the general
principle of never letting "it came from the usual place" substitute for
an actual integrity check.
