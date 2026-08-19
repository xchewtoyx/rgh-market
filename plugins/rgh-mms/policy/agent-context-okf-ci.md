# Agent-context OKF tooling in CI

Decision for issue #190: whether `okf-core` belongs in `requirements-dev.txt`
and whether `okf index --recurse` drift is gated in CI.

## Decision

**Adopt option 2** — add `okf-core` to `requirements-dev.txt` (with the
self-hosted index URL) and run `scripts/validate-agent-context.py --with-okf`
in the registry CI gate.

Options 1 and 3 are rejected for this bundle.

## Failure-mode reasoning

| Option | Failure mode | Why not (for rgh-mms) |
|--------|--------------|------------------------|
| **1. Leave as-is** | Format conformance and `okf index` output are checked only when a human remembers `--with-okf` or regenerates the index. CI passes while OKF profile/taxonomy drift and index formatting diverge. | Conflicts with the living-wiki model (#188/#189): agents promote concepts and regenerate `index.md` in delivery loops — the gate should match what maintainers run. |
| **2. `requirements-dev.txt`** | CI depends on the self-hosted PEP 503 index (`xchewtoyx.github.io/okf-core`). If that host is down, CI fails loudly. If index precedence is wrong, pip may resolve `okf-core` from PyPI instead of the intended index (dependency confusion). | Acceptable for this meta repo: same org owns the index and the bundle. Fail-closed beats silent drift. Self-hosted index is **primary** (`--index-url`); PyPI is `--extra-index-url`. `okf-core==0.4.2` is pinned. See [`docs/agent-context/ci-tool-determinism.md`](../docs/agent-context/ci-tool-determinism.md). |
| **3. Separate optional job** | Split dependency hides failures in a non-blocking job; operators must watch two gates. | Adds workflow surface without removing the Pages dependency — option 2 already fails loud when the index is unreachable. |

## What CI runs

`ci.local_command` (and `.github/workflows/ci.yml`) invoke:

```bash
.venv/bin/python3 scripts/validate-agent-context.py --with-okf
```

`--with-okf` delegates to the `okf` CLI when installed:

- `okf validate --bundle agent-context`
- `okf graph --broken --bundle agent-context`
- **Index drift** — regenerate `index.md` via `okf index --bundle agent-context
  --recurse` in a temp tree and compare to the committed file (same
  fail-closed shape as `generate-adapters.py --check`).

Native stdlib+PyYAML checks in the same script still run first and do not
require `okf-core`; they remain the fallback if a checkout installs only
`requirements-dev.txt` without the index URL resolving (bootstrap should not
hit that path for this repo).

## Install

`requirements-dev.txt` carries the index URL precedence and `okf-core==0.4.2`.
`session.bootstrap_command` (`pip install -r requirements-dev.txt`) is
sufficient — no separate manual install step for routine development.

Manual reference (also in `okf-core.toml`):

```bash
.venv/bin/pip install okf-core \
  --index-url https://xchewtoyx.github.io/okf-core/simple/ \
  --extra-index-url https://pypi.org/simple/
```

Growth-review `okf unlinked-mentions` and promotion `okf index` remain
operator commands documented in
[`policy/agent-context-growth-review.md`](agent-context-growth-review.md) and
[`policy/agent-context-promotion.md`](agent-context-promotion.md).
