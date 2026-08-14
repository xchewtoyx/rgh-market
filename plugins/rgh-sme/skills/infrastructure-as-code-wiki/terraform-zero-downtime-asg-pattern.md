---
type: concept
title: Zero-Downtime Autoscaling Group Deployment Pattern
description: The specific Terraform resource lifecycle configuration (name_prefix, create_before_destroy, ELB-aware capacity) needed to replace a launch configuration without an availability gap.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 5"
---

By default, changing an autoscaling group's launch configuration in Terraform destroys the old launch configuration and autoscaling group before creating their replacements, which drops capacity to zero for a window — a concrete instance of the general problem [changing live infrastructure](testing-infrastructure-in-production.md) safely creates. Terraform's `create_before_destroy` lifecycle setting reverses the order — the new resource is created and confirmed healthy before the old one is torn down — but on its own this still collides with naming: the old and new launch configuration can't coexist if they share a fixed name.

The concrete recipe: give the launch configuration and autoscaling group a `name_prefix` rather than a fixed `name`, so Terraform generates a unique suffix per revision and the old and new resources can genuinely exist side by side; set `lifecycle { create_before_destroy = true }` on both; and make the autoscaling group's health checking ELB-aware (`health_check_type = "ELB"`, `min_elb_capacity` set to the desired minimum), so new instances only count as ready once they've actually passed the load balancer's health check, not merely once the compute layer reports them as running.

This is the Terraform-specific mechanics behind the general [blue-green infrastructure change](blue-green-infrastructure-change.md) pattern applied to a single autoscaling group replacement, rather than a full separate environment swap.
