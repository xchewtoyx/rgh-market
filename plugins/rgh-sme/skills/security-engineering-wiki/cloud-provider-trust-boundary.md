---
type: concept
title: Cloud Provider as a Trust Boundary
description: >
  Renting infrastructure imports the provider's staff, hardware disposal
  practices, and legal exposure into your own threat model — a boundary
  with different failure and blast-radius properties than a private
  datacenter's.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 3"
---

# Cloud Provider as a Trust Boundary

Choosing a public cloud provider doesn't just outsource hardware — it
extends your [insider risk](insider-risk.md) surface to include the
provider's own staff, and extends your threat model to include failure
modes a private datacenter doesn't have:

- **Third-party-insider access.** Curious or malicious provider employees,
  and improperly wiped decommissioned hardware being resold or repurposed,
  are real leak vectors you cannot directly audit or control — you're
  trusting the provider's own screening, process, and disposal discipline
  rather than your own.
- **Legal access differs by structure, not just by data location.** A
  warrant served on a public cloud provider can compel data access without
  ever notifying you; in a private datacenter, the only normal access path
  runs through you directly. This is a distinct axis from data residency
  (which jurisdiction's law applies) — it's about who the compelling
  request is served on and who finds out.
- **Blast radius differs by tenancy.** A leak in a private cloud is
  contained to one company, however bad; a leak in a shared public cloud
  can expose data to anyone sharing that infrastructure, including
  competitors, and become public news — the same underlying failure has a
  categorically different worst case depending on tenancy model.

This trust boundary sits on the provider's side of the
[cloud shared responsibility model](cloud-shared-responsibility-model.md);
even a provider with impeccable staff-screening and legal practice doesn't
protect you from the misconfiguration risk that sits on your side of the
same line.

None of this makes public cloud unsafe by default — providers counter it
with contractual commitments, transparency reports, and third-party
audits, which is exactly the evidence to ask for before trusting a
provider with sensitive data. But it means the provider selection decision
is itself a security design decision, not purely a cost or operations
one: for regulated or highly sensitive data, weigh dedicated/private
infrastructure or contractual data-segregation guarantees against the
economics of shared multi-tenant infrastructure, the same way
[access classification by risk](access-classification-by-risk.md) weighs
control cost against what a given class of data is worth protecting.
