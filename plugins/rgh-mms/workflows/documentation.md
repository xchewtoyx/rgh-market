# Documentation Loop

Workflow for docs-only changes: README, AGENTS.md, orientation guides, API
docs, changelog prose.

## When to use

- No runtime behavior change (or behavior already shipped; docs catching up).
- Typos, clarifications, examples, architecture docs.
- Harness/meta repo documentation (like `rgh-mms` itself).

## When not to use

- Behavior changes → use [contract-first-change](contract-first-change.md) or
  full [milestone-delivery](milestone-delivery.md).
- Research spikes → use [research](research.md).

## Roles

Typically **implementor → reviewer** only. Skip `approver` unless the work item
has explicit acceptance criteria beyond "docs are accurate."

Skip contract scaffold unless target repo requires it for all merged changes.

## Changelog fragments

Canonical definition of the per-change changelog format (issue #251) —
`changelog.d/README.md` and every consumer below defer here rather than
restating it.

**Why fragments.** A monolithic `CHANGELOG.md` `[Unreleased]` section means
every PR that adds a changelog entry edits the same lines, so two concurrent
PRs each adding an entry conflict on merge even when their actual code
changes don't overlap (see this section's own contract,
`.agent-metrics/contracts/i251_changelog_fragments.md`, for the concurrent-
merge evidence). A fragment directory removes the shared edit point: each
change adds its own new file, and two new files never conflict.

**Filename format.** `changelog.d/<ulid>-<slug>.md` — a
[ULID](https://github.com/ulid/spec) (26-character Crockford-base32 string,
lexicographically time-ordered) followed by a short hyphenated slug.
Generate the ULID with `scripts/ulid.py` (`generate_ulid()`, or run the
script directly — it prints one to stdout). The ULID makes the id
collision-free by construction across concurrent branches (no shared
counter or registry to race, unlike the legacy sequential contract-id
scheme fixed by issue #250) and keeps `ls changelog.d/` in chronological
order for free.

**Entry length.** 2-3 lines. Point at the change contract
(`.agent-metrics/contracts/<id>.md`) when one exists and the PR/issue
number either way — do not restate the contract's Proposed Change or
Verification Plan here. When contracts are enabled for the target repo
(`policy/change-safety.md` "Contract-first"), the contract is the
long-form record and the fragment is a pointer to it, not a summary; when
they are not, the fragment points at the PR/issue directly.

**Deprecation marker.** A fragment documenting a deprecation leads its
content with a line starting `Deprecated:` — the fragment equivalent of
the old monolithic file's `### Deprecated` `[Unreleased]`-section
convention (still `grep`-discoverable, now across `changelog.d/*.md`
instead of within one file's section). See
[`policy/deprecation.md`](../policy/deprecation.md#changelog-entry-point)
for the full deprecation-entry-point rule.

**`CHANGELOG.md` itself.** Preserved as the historical record up to the
commit that introduced fragments; it carries a pointer to this directory
and gets no new entries after that point.

## Loop

1. **Plan (optional).** Short planner dispatch if scope is large or touches
   many files; otherwise skip for single-file edits.
2. **Implement.** Dispatch `implementor` with docs-only subtasks:
   - Update affected docs in one commit.
   - Add a `changelog.d/` fragment (see
     [Changelog fragments](#changelog-fragments)) when user/contributor-facing.
   - Run link checks or `ci.local_command` if the repo's CI covers docs.
2a. **Agent-context promotion (when applicable).** When the change surfaces
    material that passes the reuse test in
    [`policy/agent-context-promotion.md`](../policy/agent-context-promotion.md),
    the implementor adds a concept under `docs/agent-context/`, regenerates
    `index.md`, and replaces the source passage with a defer pointer. The
    reviewer in step 3 confirms promotion criteria and runs
    `scripts/validate-agent-context.py` when the bundle changed. Skip when no
    concept is promoted.
2b. **Agent-context growth review (when triggered).** When
    [`policy/agent-context-growth-review.md`](../policy/agent-context-growth-review.md)
    says a review is due (concept-count multiple of six, 90-day cadence, or
    baseline adoption), dispatch a fresh `reviewer` to run the reading pass:
    capture `okf unlinked-mentions --bundle agent-context`, answer the four
    review questions, and write a dated record under
    `docs/agent-context-reviews/`. Structural edits may follow in the same PR or
    a follow-up; recording is mandatory. Skip when no trigger fired.
3. **Review.** Dispatch `reviewer` with focus on:
   - Accuracy vs current code behavior (no aspirational claims).
   - Internal consistency across linked docs.
   - Progressive disclosure (essentials first, pointers for depth).
   - Documentation lenses per `policy/review-policy.md` and
     `policy/documentation-lenses.md` when prose or instruction files change.
4. **PR.** Open PR; land per manifest `delivery.integration_mode` (human merge
   to default in `per-issue`; or into a milestone tracking branch when that
   docs change is part of an aggregate milestone run).

## Review emphasis

Documentation review is correctness review. Flag any statement that contradicts
the codebase, CLI `--help`, or tests.

## Supervisor thinness

Same as other workflows — summaries only.
