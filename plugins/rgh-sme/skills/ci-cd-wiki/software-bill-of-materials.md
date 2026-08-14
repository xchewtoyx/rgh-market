---
type: concept
title: Software Bill of Materials
description: >
  A machine-readable inventory of every component and version that went into
  a build, generated automatically as a pipeline artifact so an org can query
  which deployed services are exposed when a new dependency vulnerability is
  disclosed.
sources:
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 22"
---

# Software Bill of Materials

A software bill of materials (SBOM) is a complete, machine-readable list of
every dependency — direct and transitive — that went into a given build,
generated automatically as part of the pipeline rather than assembled by
hand after the fact. It answers the question a security team otherwise can't
answer fast enough: "when a new CVE is published against library X, which of
our production services actually ship a vulnerable version of X, and where
did it come from?"

Producing an SBOM depends on the same [dependency pinning](dependency-pinning.md)
discipline that makes builds reproducible: an SBOM is only trustworthy if the
exact versions it lists are the exact versions that actually get deployed,
which is precisely what pinning guarantees. It's most useful when paired
with a centralized, deployed-artifact record — an org-wide index of which
SBOM belongs to which running service — so a newly disclosed vulnerability
can be matched against every affected deployment in one query instead of
asking every team individually.

This turns dependency risk from a per-team question ("did we remember we use
this library?") into an org-wide, queryable one, and is what makes
automated dependency-vulnerability response fast enough to matter: research
comparing high- and low-performing organizations found high performers were
dramatically more likely to maintain this kind of centralized deployed-
artifact record and to have automated the initial response (an auto-
generated pull request against the vulnerable dependency) rather than
routing the problem through a manual security review.
