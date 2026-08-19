# Schema evolution

General versioning doctrine for this repo's own schemas
(`schemas/loop-telemetry-v1.schema.json`,
`schemas/harness-contract.schema.json`,
`schemas/repo-registry.schema.json`). Schema-agnostic on purpose — one
doctrine, several schemas, each with its own consumers and enforcement
points. See [Consumers](#consumers) below for what is actually
implemented today vs. documented-but-not-yet-built.

## Minor vs. major

- **Minor** — an additive, optional change that every existing consumer
  can safely ignore: a new optional field, a new enum value that doesn't
  change the meaning of existing ones, a new optional top-level key.
  Nothing that already validated against the old shape stops validating
  against the new one.
- **Major** — anything a consumer written against the old shape cannot
  safely ignore: removing a field or enum value, renaming a field,
  changing a field's type or semantic meaning, tightening a constraint
  (e.g. making an optional field required). If an old, unmodified
  consumer would misbehave (reject a previously-valid record, or worse,
  silently misinterpret one) on the new shape, it's major.

### Worked example (a): add an optional field — minor

Adding `metrics.retry_count` (a new optional numeric metric) to
loop-telemetry: existing consumers that don't know about
`retry_count` keep working unchanged — they don't read it. This is
purely additive. No `schema_version` major bump is required; see
[loop-telemetry's own convention](../instrumentation/loop-telemetry.md#schema-versioning-and-persist-boundary-tolerance-issue-212)
for how the minor number communicates this.

### Worked example (b): rename a field — major, via expand/dual-write/contract

Renaming `escalation_reason` to `escalation_cause` is **not** a single-step
change, even though "rename" sounds atomic. Treat it as deprecate-old-
add-new-then-remove-old — itself an expand → dual-write → contract cycle
spanning at least two releases:

1. **Expand.** Add `escalation_cause` as a new optional field alongside
   the existing `escalation_reason` (this half is itself minor — see (a)
   above). Producers keep writing `escalation_reason` only; nothing reads
   `escalation_cause` yet.
2. **Dual-write.** Producers write **both** `escalation_reason` and
   `escalation_cause` with the same value, for a window long enough that
   every consumer has had a chance to move to the new field name (see
   [Dual-send window rule](#dual-send-window-rule) below). Consumers
   migrate to reading `escalation_cause`, tolerating its absence
   (falling back to `escalation_reason`) until the window closes.
3. **Contract.** Once every consumer reads `escalation_cause` and no
   producer depends on `escalation_reason` being read, stop writing
   `escalation_reason` and remove it from the schema. *This* step is the
   actual breaking, major-version change — not the rename itself, which
   was smeared across steps 1–2 as two overlapping minor changes.

A rename is never one commit. If it looks like one commit, one of the two
migration windows (dual-write, or consumer migration) has been skipped.

## Expand → dual-write → contract lifecycle

Every major change to a schema this doctrine governs follows the same
three phases, regardless of which specific field/value/constraint is
changing:

1. **Expand.** Add the new shape alongside the old one. Old consumers
   are unaffected; nothing depends on the new shape yet. Revertible with
   no data loss (stop writing the new shape).
2. **Dual-write.** Producers emit both shapes for a defined window;
   consumers migrate to the new shape at their own pace within that
   window, tolerating either. Revertible mid-window (roll consumers back
   to reading only the old shape; producers keep writing it).
3. **Contract.** Once every consumer has migrated, stop writing the old
   shape and remove it. This is the only phase that is not trivially
   revertible (the old shape's data is gone going forward) — it should
   only happen after the dual-write window has actually closed, not on a
   calendar deadline alone.

Each phase should ship as its own change (its own contract, if
`contracts.enabled`), not bundled with the others — a phase that is
revertible on its own stays revertible; bundling the contract phase into
the same change as the expand phase collapses the whole migration into
one irrevertible step.

## Dual-send window rule

"Dual-send" applies specifically to **pipeline and mapping** changes —
where a value doesn't just live in a schema, it also gets pushed to an
external sink with its own separately-versioned mapping (Loki stream
labels/structured metadata, OTLP export). Renaming or restructuring a
field used by such a mapping requires the pipeline to send **both** the
old and new shapes to the sink for the whole dual-write window described
above — not just the source-of-truth JSONL. A consumer of the *sink*
(a Grafana dashboard query, an alert rule) has no visibility into the
JSONL schema version at all; it only sees what actually arrived at the
sink. If the pipeline stops sending the old shape before every downstream
dashboard/query/alert has migrated, those break with no warning at the
schema level — the schema-level dual-write window closing is not the
same event as the pipeline-level dual-send window closing, and the
second must be at least as long as the first.

For loop-telemetry concretely, this means: a field-rename affecting
`telemetry_loki.PROPERTY_DESTINATIONS` must keep pushing the old field to
its Loki destination for the same window that consumers are expected to
migrate their Loki queries, in addition to whatever dual-write the JSONL
schema itself is doing — see
[grafana-cloud.md](../instrumentation/grafana-cloud.md) for the transport
this applies to.

## Who updates stale checkouts

An operator running a pinned harness version below a schema's current
major version is responsible for upgrading their pin before any *new
major* version is emitted by any producer they consume from. This mirrors
the general pin/upgrade responsibility already documented for the harness
contract itself (`AGENTS.md` "Products depend on harness versions;
harness does not contain products") — nothing in this doctrine changes
who owns that pin.

Minor versions are the opposite: a producer is free to emit a new minor
version at any time without coordinating with consumers first, and a
consumer is not required to upgrade merely because a minor version moved
— that is the entire point of minor being additive-and-safe-to-ignore.
Only a major bump requires a coordinated consumer upgrade before it ships
from any producer.

## Consumers

| Schema | Minor/major doctrine applies | Runtime tolerance implemented |
|--------|-------------------------------|-------------------------------|
| [`schemas/loop-telemetry-v1.schema.json`](../schemas/loop-telemetry-v1.schema.json) | Yes | Yes — persist-boundary minor-version tolerance (issue #212 / contract 0040); see [instrumentation/loop-telemetry.md](../instrumentation/loop-telemetry.md#schema-versioning-and-persist-boundary-tolerance-issue-212) |
| [`schemas/harness-contract.schema.json`](../schemas/harness-contract.schema.json) | Yes | **No** — `scripts/schema_validate.py::validate_contract` enforces the current shape only; no minor-version parsing or tolerance exists. Explicitly out of scope for issue #212/contract 0040; a future contract may add it (see contract 0040's IMPROVE criterion) |
| [`schemas/repo-registry.schema.json`](../schemas/repo-registry.schema.json) | Yes | **No** — same gap, same explicit non-scope, via `scripts/validate-manifests.py` |

Do not read the "Yes" in the first column as "already tolerant" — the
doctrine (what counts as breaking, how to phase a breaking change) is
schema-agnostic and applies to all three today; the *mechanical*
tolerance (a validator that actually accepts a newer minor version
without erroring) is implemented only where the second column says Yes.
