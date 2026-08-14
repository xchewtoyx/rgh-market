---
type: concept
title: Single-Site Edit Blind Spot
description: >
  A fix that only patches the first matching occurrence of a duplicated
  pattern can pass the target test yet regress the sibling occurrences it
  never touched.
sources:
  - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
    resource: "SWE-bench (Jimenez et al.), pp. 31–45 (Appendix F)"
---

Some bugs are not localized to one symbol — the buggy behavior is produced by
a pattern that recurs across several related sites (multiple regexes derived
from or feeding into one another, several call sites sharing duplicated
validation logic). An agent that searches for and edits the first site that
reproduces the symptom can miss that the pattern has siblings, submitting a
patch that fixes the immediate reproduction case while leaving the same bug —
or a new inconsistency — at the untouched sites.

Example (`astropy` QDP command-case handling): the issue is that QDP command
parsing assumes uppercase (`READ SERR`) though QDP is case-insensitive. The
agent hard-edits the single regex it finds (`_command_re`) to lowercase
literals. The gold patch instead compiles the shared `_line_type_re` with
`re.IGNORECASE` and normalizes comparisons (`v.upper() == "NO"`) — because
that one regex feeds `_type_re` and other call sites, not just the one the
agent found. Result: the agent's patch fails the target unit test **and**
regresses existing pass-to-pass tests that depended on the untouched sibling
behavior, because it changed one instance of a shared pattern instead of the
shared source.

This is distinct from [idiomatic minimal patch preference](idiomatic-minimal-patch-preference.md)
(over-building relative to the smallest hook) — here the patch is
*under-scoped* relative to how many places the same pattern actually lives.
Distinguishing "is this bug produced by one site or by a pattern shared
across several" may need execution feedback the agent doesn't have from
[issue-grounded localization](issue-grounded-localization.md) alone: after a
plausible fix passes the reproduction script, prompt the agent to search for
other occurrences of the same regex/logic fragment (grep the literal pattern,
not just the symbol name) before `submit`, and require the fix touch the
shared definition when one exists rather than the first call site found.
Score against **pass-to-pass** regression, not only fail-to-pass success, in
[per-task offline harness tests](per-task-offline-harness-tests.md) — a patch
that only fixes the reproduction case while breaking previously-passing
behavior is a distinct and worse failure than an incomplete fix that changes
nothing else.
