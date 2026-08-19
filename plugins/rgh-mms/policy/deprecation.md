# Deprecation

General policy for removing an observable harness behavior. Pinned products
depend on everything a harness generation exposes, not only the parts a
schema happens to cover — a script flag, a generated-adapter path, or a
workflow obligation is just as load-bearing to a product checkout as a
schema field, and a removal of any of them needs the same explicit
coexistence window and the same machine-readable marker a schema removal
gets.

This document does not re-derive the minor/major semantics or the
expand → dual-write → contract phase mechanics that
[`policy/schema-evolution.md`](schema-evolution.md) already covers for
schema fields and enum values — see that document for the "how" of those
two classes. This document is a strict superset in scope (it also covers
script flags, generated-adapter paths, and workflow obligations, which
`schema-evolution.md` is schema-file-scoped and cannot reach), and it owns
the taxonomy of what counts as a breaking removal across all five classes,
the minimum coexistence window, and where the machine-readable marker
lives.

## Breaking-removal classes

A change in any of these five classes that an existing, unmodified consumer
cannot safely ignore is a **breaking removal**. "Cannot safely ignore" means
the consumer would error, silently misbehave, or lose functionality it
previously had — the same test `schema-evolution.md` uses to distinguish
minor from major.

| Class | What counts as breaking | Example |
|-------|--------------------------|---------|
| Schema field | Removing a field, renaming it, changing its type, or making an optional field required | Removing `telemetry.grafana_cloud.loki.endpoint` from `schemas/repo-registry.schema.json` |
| Enum value | Removing an enum member, or changing what an existing member means | Removing `deprecated` from `status`'s enum, or repurposing it to mean something else |
| Script CLI flag | Removing a flag, changing its default in a way that changes behavior, or repurposing its meaning | Removing `scripts/verify.py --bundle`, or `--stale-report` starting to gate CI instead of staying advisory |
| Generated-adapter path | Removing or relocating a managed output path a product checkout may reference | `scripts/generate-adapters.py` no longer writing `.claude/skills/` |
| Workflow obligation | Removing a step a role or workflow currently requires (a checklist item, a required output field, a gate) | Dropping the Author integration checklist's prompt-engineer gate from `roles/implementor.md` step 6 |

An **additive** change in any of these five classes — a new optional field,
a new enum value that doesn't change existing members' meaning, a new flag,
a new adapter path, a new *optional* workflow step — is not a breaking
removal and does not require this document's coexistence window. This
mirrors `schema-evolution.md`'s minor/major split, generalized past
schemas.

## Coexistence window

**Minimum: at least one released harness `VERSION`** (see `VERSION` at
repo root and `AGENTS.md` "Update `VERSION` on release; products pin
tags") between the commit that starts coexistence (the deprecation is
announced and the old and new shapes/behaviors both work) and the commit
that performs the actual removal.

This document reads the issue's "one released version minimum, stated per
class" as a request for a single uniform floor, explicitly restated under
each class below — not five independently-numbered windows. The
justification: every one of the five classes is consumed the same way, by
a product checkout pinned to a harness `VERSION` tag
(`policy/mission-boundaries.md`, `AGENTS.md` "Products depend on harness
versions; harness does not contain products") — there is no class-specific
reason a script flag needs a shorter or longer grace period than a schema
field, since both are only ever observed by a checkout that has or hasn't
yet bumped its pin. A future contract may split this per class if evidence
shows one class's consumers upgrade meaningfully faster or slower than
another's; nothing here forecloses that.

Restated per class:

- **Schema field** — at least one released `VERSION` of dual-write
  (old and new field both present/read) before the old field is removed
  from the schema. Mechanics: `schema-evolution.md` expand → dual-write →
  contract.
- **Enum value** — at least one released `VERSION` where both the old and
  new enum values are accepted before the old value is rejected. Mechanics:
  `schema-evolution.md`, same lifecycle.
- **Script CLI flag** — at least one released `VERSION` where a removed or
  renamed flag still works (accepted, with a deprecation notice printed)
  before it is rejected outright.
- **Generated-adapter path** — at least one released `VERSION` where both
  the old and new managed path are written (or the old path is written
  with a pointer to the new one) before the old path stops being
  generated. A product checkout that has not re-run
  `scripts/bootstrap.py`/`scripts/generate-adapters.py` against the newer
  `VERSION` yet must not find a referenced path silently gone.
- **Workflow obligation** — at least one released `VERSION` where the
  obligation is downgraded to optional/advisory (documented as such,
  still checkable) before it is dropped from the role/workflow text
  entirely.

## Machine-readable marker

A deprecation must be discoverable by a script or a careful reader without
relying on a changelog line alone.

### Schema field / enum value

Convention: a documented free-text marker inside the property's or enum
member's JSON Schema `description`, of the form:

```
DEPRECATED (since vX.Y.Z, removal no earlier than vX+1.0.0): <reason>. Use <replacement> instead.
```

This repo deliberately does **not** introduce a sibling `x-deprecated`
key. JSON Schema 2020-12 has no standard `deprecated` validation keyword
(OpenAPI's `deprecated: true` is not part of core JSON Schema), so any
marker here is a local convention either way — a `description`-embedded
convention needs no schema-shape change, no validator change, and no new
`additionalProperties: false` allowance to introduce, while a custom
sibling key would require all three. The description convention is the
smaller-footprint option; a future contract may promote it to a real
sibling key (and wire a validator check for it) if the free-text
convention proves insufficient in practice — see this document's own
Settle Criteria via
`.agent-metrics/contracts/0041_deprecation_policy.md`.

See `policy/schema-evolution.md`'s expand phase for the mechanics of
introducing the replacement shape alongside the deprecated one.

### Script CLI flag / generated-adapter path / workflow obligation

Convention: a `DEPRECATED (since vX.Y.Z, removal no earlier than
vX+1.0.0): <reason>` note in the flag's `--help` text (`argparse` `help=`
string), the adapter path's entry in `harnesses/README.md` **Layout**, or
the workflow-obligation's own row/step text, respectively.

**No enforcement surface exists for these three today.** Nothing lints an
`argparse` help string, a `harnesses/README.md` row, or a workflow step
for the presence or removal timing of this marker — this is stated
explicitly rather than implied, per this repo's convention of not
asserting coverage that hasn't been built (see
`roles/implementor.md#self-referential-claims`). A future contract may add
such a check; until then, the Author integration checklist
(`policy/change-safety.md`) item 1 ("Single source of truth") is the
closest process gate, since it requires an author to route a new
deprecation topic here rather than letting it sit undocumented.

### CHANGELOG entry point

Every deprecation, once marked, gets its own fragment under
`changelog.d/` (issue #251; see
[`workflows/documentation.md`](../workflows/documentation.md#changelog-fragments)
for the fragment format generally), whose content leads with a line
starting `Deprecated:`. That prefix line is the fragment-directory
equivalent of the pre-#251 convention below: `grep -l '^Deprecated:'
changelog.d/*.md` finds every deprecation entry the same way `grep
'### Deprecated' CHANGELOG.md` found them in the monolithic file, scoped
to one file per entry instead of one section shared by all of them.
This document does not force a first use of the marker — it is a
convention for the next deprecation, not a retroactive requirement on
prior removals; no deprecation has used it yet (confirmed against
`CHANGELOG.md`, which carries only its original `[Unreleased]` section and
no `### Deprecated` subsection ever added under it).

**Pre-#251 history.** Before fragments, the convention was a per-
deprecation entry under a new `### Deprecated` section in `CHANGELOG.md`'s
`[Unreleased]` block, per [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
which this repo otherwise still follows for the file's preserved history.
That convention is superseded by the fragment marker above for every
deprecation going forward; `CHANGELOG.md` itself is not edited to add it
retroactively, per its own "preserved as-is" disposition
(issue #251 AC4).

## `status: deprecated` in `repos/*.yaml`

`schemas/repo-registry.schema.json` `status` enum's `deprecated` value
means: this bundle's registry entry is retained for historical/audit
reference, but the bundle should not receive new delivery work. Two
concrete operational effects today:

1. **Already true, now documented.** `scripts/validate-manifests.py`'s
   registered-manifest AC-requirement block (`ci.local_command`,
   `github.owner`/`ado.organization`/`bitbucket.server` presence) is gated
   on `status == "registered"`, so a `deprecated` manifest is exempt from
   those requirements — it was never mechanically enforced for anything
   but `registered` bundles, and this was true before this change; it is
   undocumented until now.
2. **New in this change.** `scripts/validate-manifests.py` prints a
   non-blocking `WARN: <bundle>.yaml: status is deprecated ...` line for every
   manifest carrying `status: deprecated`, naming it in CI output so a
   deprecated bundle does not go silently unnoticed in the registry
   listing. This is a warning only — it does not exclude the bundle from
   any fleet report or dispatch path that does not itself already branch
   on `status`, and no such branch exists elsewhere in this repo today.
   A future contract may extend this into an actual dispatch-time
   exclusion (e.g. a milestone-delivery precondition check) — out of
   scope here.

## See also

- [`policy/schema-evolution.md`](schema-evolution.md) — minor/major
  doctrine and expand → dual-write → contract mechanics for schema field
  and enum-value deprecation specifically.
- [`policy/change-safety.md`](change-safety.md) — Author integration
  checklist, including where a new deprecation topic must be registered.
- [`policy/INDEX.md`](INDEX.md) — canonical defer map; this document's
  topic-map row.
