---
type: concept
title: Terraform State File
description: The JSON file Terraform uses to map resource declarations in code to the real-world identifiers of the infrastructure it created, and why it must never be treated as an ordinary version-controlled artifact.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 3"
---

Terraform records a state file (`terraform.tfstate`) mapping each resource declared in code to the actual identifier of the real-world object it created — for example, `aws_instance.example` to `i-0bc4bbe5b84387543` — along with cached resource attributes, the dependency graph, and output values. `terraform plan` reads this state to determine current known attributes without always hitting the cloud API directly, which is both a performance optimization and the mechanism that lets Terraform compute a diff between declared and actual [desired state](declarative-vs-imperative-infrastructure-code.md). If the state file is lost or corrupted, Terraform loses track of what it manages, and recovering usually means manually re-associating resources with `terraform import`.

Putting the state file into ordinary Git version control is a specific antipattern, for three compounding reasons: Git has no locking, so two people applying around the same time can race and corrupt the mapping; the state file stores every resource's attributes in plaintext, including secrets such as database passwords and TLS keys, so committing it leaks those secrets into Git history permanently, contradicting the rule that [secrets never belong in source control](handling-secrets-in-infrastructure-code.md); and Git provides no mechanism to stop two people running `terraform apply` at the same time, which corrupts state through concurrent writes even without a merge conflict in the traditional sense.

The standard fix is a [remote backend with distributed locking](terraform-remote-backend-and-locking.md). How much infrastructure a single state file should cover is a direct instance of the general [blast radius](blast-radius.md) problem — see [Terraform state isolation strategies](terraform-state-isolation-strategies.md) for the two main approaches to splitting it up.
