# Agent-context promotion

Criteria and process for adding a concept to the cross-repo
[`docs/agent-context/`](../docs/agent-context/) OKF bundle.

Governance lives here and in [`workflows/documentation.md`](../workflows/documentation.md);
the bundle itself does not link out — see
[`docs/agent-context/bundle-link-containment.md`](../docs/agent-context/bundle-link-containment.md).

## Living wiki

Treat `docs/agent-context/` as a **living wiki**, not a seeded snapshot that
only grows on milestone schedule. Agents **autonomously promote** concepts when
delivery surfaces a reusable pattern (documentation loop step 2a, or inline
during milestone delivery) — no separate milestone item is required when the
reuse test passes and the edit is docs-only. Milestones schedule load-bearing
harness work; concept promotion is continuous maintenance. Growth review (#189
policy) handles split/merge cadence on what is already there.

## When a concept belongs in the bundle

A concept earns a place in `docs/agent-context/` only when it passes the
**reuse test** from
[`docs/agent-context/atomic-concept.md`](../docs/agent-context/atomic-concept.md):
it must be useful in more than one repository. Anything true of exactly one
product belongs in that product's own docs.

**Promotion trigger.** Promote when the idea is reusable *in principle* — the
pattern is not tied to one checkout, product name, or deployment shape. When
reuse is borderline, prefer waiting until a second registered bundle actually
needs the concept; that keeps the bundle small without forbidding early capture
when the abstraction is already clear.

**Atomicity.** One concept per document. If the reuse test passes for only part
of a longer doc, promote that part and leave product-specific material behind.

## Who decides

1. **Implementor proposes** during a docs change (or milestone delivery) when
   they notice reusable material in harness policy, a product repo, or a
   workflow.
2. **Reviewer confirms** in the documentation loop that the reuse and atomicity
   tests pass before the PR merges. Review checks criteria; it does not invent
   new concepts.

## Product-side copy after promotion

Do not delete product-side prose silently and do not leave a full duplicate to
drift. **Replace** the promoted passage with a short defer pointer to the bundle
concept (link into `docs/agent-context/…` from harness docs; from a product
repo, link to the pinned harness path or registry doc that points at the
bundle). Keep any harness-specific enforcement checklist in the original policy
file — only the portable rationale moves into the bundle.

## Promotion steps

Named in [`workflows/documentation.md`](../workflows/documentation.md) Loop
step 2a. In short:

1. Add `docs/agent-context/<slug>.md` with OKF frontmatter (`type: concept`,
   `title`, `description`).
2. Link from at least one existing in-bundle concept when a reader there would
   plausibly want the new document next (see
   [`docs/agent-context/utility-led-linking.md`](../docs/agent-context/utility-led-linking.md)).
3. Regenerate `docs/agent-context/index.md` (`okf index --bundle agent-context
   --recurse` when `okf` is installed, or update the index list to match).
4. Replace the source passage with a defer pointer; run
   `scripts/validate-agent-context.py` and the repo `ci.local_command`.

Growth review (split/merge cadence, `okf unlinked-mentions`) is defined in
[`policy/agent-context-growth-review.md`](agent-context-growth-review.md); do not
fold it into promotion.

## Worked example

**Fresh-context dispatch** — portable rationale now lives at
[`docs/agent-context/fresh-context-dispatch.md`](../docs/agent-context/fresh-context-dispatch.md),
promoted from this repo's harness policy. Harness-specific reviewer inputs and
supervisor routing remain in
[`policy/review-policy.md`](review-policy.md#fresh-context-dispatch).

**Non-blocking reviewer note** — promoted during #189 delivery; see
[`docs/agent-context/non-blocking-reviewer-note.md`](../docs/agent-context/non-blocking-reviewer-note.md).

**CI tool determinism** — promoted during #190 after live review caught
non-deterministic `okf` resolution and index precedence; see
[`docs/agent-context/ci-tool-determinism.md`](../docs/agent-context/ci-tool-determinism.md).
Harness package/index choices remain in
[`policy/agent-context-okf-ci.md`](agent-context-okf-ci.md).
