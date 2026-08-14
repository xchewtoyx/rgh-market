---
type: concept
title: One Version Rule
description: >
  At most one version of any given dependency may exist in a codebase at a
  time, eliminating diamond-dependency choice and making upgrades org-wide
  events rather than per-team decisions.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 20, 23"
---

# One Version Rule

For every dependency — internal or third-party — developers must never choose
"which version should I depend on?" **One version** at steady state prevents
the **diamond dependency problem**: if `libuser` depends on `liba` (using
`libbase` v1) and `libb` (using `libbase` v2), no reconcilable build exists
without shading or forks that partition the codebase.

Enforcement patterns:

- **Monorepo** — internal deps built from source at one commit; no per-target
  version. See [source-level vs. binary-level component integration](source-vs-binary-component-integration.md).
- **Global external manifest** — Bazel-style workspace file listing every
  third-party artifact with a single version; no auto-resolving transitive
  closures that silently introduce second versions.
- **No in-place forks** without rename/repackage — forked libraries with the
  same symbols partition consumers.

Brief coexistence during migrations is allowed (old and new while incrementally
migrating), with new deps on the old version blocked. Technical workarounds
(shading, hiding symbols) patch around debt rather than solve it — types
passed across package boundaries still break.

Pairs with [live at head dependency model](live-at-head-dependency-model.md)
and [trunk-based development](trunk-based-development.md) — dev branches reintroduce
version choice. [Virtual monorepo](virtual-monorepo.md) approaches aim for
one-version discipline across physical repos.
