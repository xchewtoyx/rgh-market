---
type: concept
title: "Terraform Provisioners vs Boot-Time User Data"
description: Why cloud-init-style boot scripts are usually preferable to Terraform's local-exec/remote-exec provisioners for configuring a new server instance.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 8"
---

Terraform provisioners (`local-exec`, run on the machine executing `terraform apply`; `remote-exec`, run over SSH/WinRM on the newly created resource) let you run arbitrary commands as part of provisioning a resource. They're a genuine escape hatch, but a fragile one for configuring servers specifically: `remote-exec` only fires the one time Terraform happens to apply, so it does nothing for instances an autoscaling group creates later on its own; it requires opening inbound SSH or WinRM access purely to run the provisioner, widening the attack surface for no ongoing benefit; and its output is only visible in the `apply` console, with no persistent log to check after the fact.

Boot-time configuration mechanisms — user data plus cloud-init being the standard AWS/cloud pattern — avoid all three problems: they run automatically on every instance boot, including ones created outside a direct `terraform apply` (autoscaling, auto-recovery); they need nothing more than the platform API and no inbound network access to the instance itself; and they log persistently (to `/var/log/cloud-init.log` and typically the platform console) for later debugging. This is the concrete Terraform-level version of the general [push vs pull server configuration](push-vs-pull-server-configuration.md) trade-off — `remote-exec` is a push mechanism with push's downsides, while user data/cloud-init is a pull mechanism triggered at boot.

`null_resource`, combined with a `triggers` map (commonly a fresh `uuid()` on every apply), is a workaround for running a provisioner independent of any specific resource's lifecycle — useful when a script genuinely needs to run on every apply regardless of what changed. An `external` data source (running a script that exchanges JSON over stdin/stdout) is another escape hatch worth using sparingly, since it ties a module to whatever language runtime the script needs, undermining the portability a module otherwise offers its callers.
