# Mission Boundaries

Canonical statement of what rgh-mms is and is not. Every other policy,
workflow, and template defers here on scope questions rather than restating
these boundaries.

## Personal overlay, not mandatory standard

rgh-mms is a personal overlay of Russell's own development preferences — an
optional convenience layer a product repo may adopt. It is never a mandatory
standard a product repo must conform to. A maintainer who does not want the
overlay is not wrong to skip it, and nothing in this repo may treat
non-adoption as a defect to fix.

## No automatic onboarding-time rewrites of hand-authored instructions

Onboarding or bundle creation must never wholesale-overwrite or refactor a
product repo's own hand-authored `AGENTS.md`, `CLAUDE.md`, or equivalent
adapter file (e.g. `.cursor/rules/`, `.github/copilot-instructions.md`) as an
*automatic onboarding-time* side effect. These files are not permanently
frozen: explicitly-tracked later work — an issue or plan the maintainer
requested — may still deliberately edit them. The boundary is against
unrequested rewrites at onboarding time, not against all future change.
`scripts/generate-adapters.py` `plan_files()` no longer reads or replans a
product target's existing `CLAUDE.md`; issue #87 removed the code path that
proposed that rewrite.

## Product convention over harness contract

On any conflict between a product repo's own documented convention and the
harness contract (`.agentic/harness.yaml` or profile defaults), the product
repo's convention wins. Nothing beyond the harness version pin is ever
schema-required of a product repo.

## Fully removable

Every file rgh-mms adds or generates must be fully removable. Deleting
`.agentic/`, generated `.claude/agents/`, `.claude/skills/`, and equivalent
adapter output must leave the product repo coherent and fully functional for
a maintainer who has never heard of rgh-mms — no broken references, no
orphaned conventions in the product's own docs.

## Enforcement-point audit (issue #88)

Per the "Product convention over harness contract" boundary above, no
validation/review/workflow step may compare a *product* repo's own
`.agentic/harness.yaml` fields (`capabilities`, `ci.local_command`,
`delivery.*`, `reviewer.*`) against a harness-side expectation and fail or
block on mismatch. Issue #88 enumerated every candidate on `main` at the
time of audit:

- `scripts/validate-manifests.py::_check_self_host_ci_local_command` —
  compares `.agentic/harness.yaml` `ci.local_command` against
  `repos/rgh-mms.yaml` `ci.local_command` and errors on drift. This looks
  like a harness-vs-product comparison but is not one: `SELF_HOST_MANIFEST`
  is hardcoded to `"rgh-mms.yaml"`, so the check only ever loads and
  compares rgh-mms's own two self-referential files. It has no code path
  that reads any other `repos/<bundle>.yaml`, so it structurally cannot
  fire against a third-party product repo. **Verdict: legitimately
  self-host-only** — rgh-mms keeping its own dogfooded checkout internally
  consistent, not the harness overruling a product's stated convention.
  Exempt from the overlay rule for that reason; see
  `scripts/validate-manifests.py` docstring and AGENTS.md "Self-host
  `ci.local_command` equality" for the mechanics.
- `scripts/validate-policy-pack.py::check_profile_capabilities` — compares
  capabilities declared in rgh-mms's own `profiles/*.yaml` templates
  against rgh-mms's own `workflows/*.md` / `skills/*/` / `policy/INDEX.md`
  allowlist. Never reads any product's `.agentic/harness.yaml`. **Verdict:
  not a candidate** — internal consistency of harness-shipped templates,
  not a product-vs-harness comparison at all.
- `scripts/generate-adapters.py` (`plan_files()` / `apply_plan()`) — copies
  files and gates unmarked overwrites; does not read or compare against a
  product's declared `capabilities`, `ci.local_command`, `delivery.*`, or
  `reviewer.*` values. **Verdict: not a candidate.**
- `scripts/verify.py` — reads a product's `.agentic/harness.yaml` `harness.
  version` pin and compares it against the local checkout's `VERSION`,
  printing `WARN` on mismatch; that specific pin-version comparison remains
  WARN-only/non-blocking. It is also outside this audit's scoped field set
  (`capabilities`, `ci.local_command`, `delivery.*`, `reviewer.*`) —
  `harness.version` is the one field product convention cannot override
  (see "Nothing beyond the harness version pin is ever schema-required"
  above). **Verdict: not a candidate** (the pin comparison is advisory-only,
  and the compared field is explicitly out of scope). Note: `main()` as a
  whole is no longer unconditionally exit-0 as of issue #89's removability
  check — a genuine dangling reference to a managed path in a product's own
  hand-authored files now makes `verify.py` return 1; see contract
  `.agent-metrics/contracts/0016_removability_check.md`. That is a scan of
  the product's own files for stale references, not a harness-vs-product
  field comparison, so it does not change this bullet's verdict.
- `scripts/bootstrap.py` — reads a product target's `.agentic/harness.yaml`
  and `return`s 1 (blocking) if the file does not exist and no `--bundle`
  resolves a detached registry entry in its place (issue #174: `--bundle`
  lets a detached target — no product-side contract by design — bootstrap
  without that file). **Verdict: not a candidate: existence/registry-
  membership check only, no field-value comparison** — it never reads or
  compares `capabilities`, `ci.local_command`, `delivery.*`, or
  `reviewer.*`, so it cannot fire on a harness-vs-product mismatch, only on
  the contract or registry entry's absence.
- `.github/workflows/ci.yml` — runs rgh-mms's own gate (black, ruff,
  pytest, `validate-manifests.py`, `validate-policy-pack.py`,
  `generate-adapters.py --check .`) against this repo only; never executes
  against a product repo's checkout. **Verdict: not a candidate.**
- Prose in `policy/review-policy.md` ("Concurrency"), `policy/
  engineering-principles.md` ("Delivery"), and `policy/change-safety.md`
  ("Contract-first") reference `.agentic/harness.yaml` but describe
  guidance agents follow, not code that compares harness-side and
  product-side field values and blocks on mismatch. **Verdict: not
  candidates.**

Net result: zero enforcement points found that block a real product repo
on a harness-vs-product mismatch. No remediation fix was needed as of this
audit — this section exists so a future enforcement point added to any of
the files above is checked against this precedent before it ships, and so
`_check_self_host_ci_local_command` in particular is never read as
establishing "harness wins" as a general pattern.

**Source:** GitHub issue #86 (boundaries above) and issue #88 (enforcement-point
audit above), both milestone #11 ("Scope Lock — Personal Overlay
Boundaries").
