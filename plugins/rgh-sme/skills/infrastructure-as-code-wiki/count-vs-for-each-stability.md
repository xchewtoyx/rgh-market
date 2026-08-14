---
type: concept
title: "Count vs For-Each: Stable Identity for Looped Resources"
description: Why using an integer position to identify a looped resource makes every later resource shift and get destroyed/recreated when an early item is removed, and why keying by a stable name avoids it.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 5"
---

When a stack tool's language lets you generate multiple resource instances from one declaration, *how* each generated instance is identified matters as much as the loop syntax itself. Identifying instances by integer position (Terraform's `count`, indexed as `aws_iam_user.example[0]`, `[1]`, ...) ties each resource's identity to its position in a list. Removing or reordering an item partway through the list shifts every subsequent index down by one — and because the stack tool sees a changed identity at every shifted index, it destroys and recreates every one of those resources, even though conceptually nothing about them changed.

Identifying instances by a stable key drawn from the data itself (Terraform's `for_each`, over a map or set, indexed as `aws_iam_user.example["neo"]`) avoids this entirely: adding, removing, or reordering elements only affects the specific key that actually changed, leaving every other resource's identity — and the real infrastructure behind it — untouched.

This is a specific, easy-to-miss case of the more general [idempotency](idempotent-infrastructure-code.md) and [blast radius](blast-radius.md) concerns that apply to any declarative infrastructure code: a construct that looks purely cosmetic (how you loop over a list) can have real destructive consequences depending on how the tool computes identity, so preferring stable, meaningful keys over positional indices is a good default whenever a stack language offers the choice.
