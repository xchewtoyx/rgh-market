---
type: concept
title: Organizing Infrastructure Code Across Repositories
description: The trade-offs between a single repository for everything, one repository per project, and the more common middle ground, and how that choice interacts with project integration timing.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 18"
---

Given multiple infrastructure code projects, spreading them across repositories is a genuine design decision with real trade-offs: separate repositories make it easier to maintain clean boundaries at the code level and to restrict team access per-repository, but they complicate any change that needs to span multiple projects at once and can't be branched or versioned together; a single shared repository makes cross-project consistency easy but adds friction (churned changelogs, potential conflicts) when unrelated teams work in it simultaneously, and different version control systems handle very large repositories with very different degrees of grace.

**One repository for everything** (sometimes called a monorepo) makes checking out a fully consistent set of projects trivial, and pairs naturally with [build-time project integration](build-time-project-integration-pattern.md), since everything needed for a combined build is already checked out together. Even within a single repository, most organizations run several different builds over different project subsets rather than one build over everything.

**A separate repository per project** (microrepo) enforces the cleanest boundaries — a change that spans two projects' files fails obviously, since the pipeline can only see one repository at a time — and pairs naturally with [delivery-time or apply-time project integration](delivery-time-project-integration-pattern.md), where the pipeline is what stitches independently-versioned projects together rather than the repository.

**Multiple repositories, each holding multiple projects** is the most common real-world arrangement, usually emerging organically rather than from an explicit strategy. It works best when the grouping tracks two things: whether the grouped projects are actually build-time integrated (integrated projects belong together; loosely-coupled ones don't need to), and team ownership, since access control is typically managed per-repository and unrelated teams working in the same repository create both process friction and (within a repository) the temptation to reach across project boundaries via file paths rather than a defined interface, quietly tightening coupling.
