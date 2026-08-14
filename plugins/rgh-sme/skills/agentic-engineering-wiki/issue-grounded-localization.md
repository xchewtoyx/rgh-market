---
type: concept
title: Issue-Grounded Localization
description: >
  Prefer searches that quote symbols and patterns from the issue text early —
  speculative filenames burn budget before the agent ever reaches the fix site.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 61–75"
  - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
    resource: "SWE-bench (Jimenez et al.), pp. 46–52"
---

In software-engineering agents, early
[trajectory phases](agent-trajectory-phases.md) succeed or fail on
**localization quality**. After reproducing the bug, prefer queries grounded in
the issue statement — class names, stack symbols, exact error strings — over
guessing filenames (`derivative.py`) or opening lookalike modules that only
*mention* the symbol.

Failure pattern (SymPy `Derivative.kind` case): reproduce succeeds, then
`find_file` / speculative `core.py` opens and an unbounded
`search_dir "Derivative"` (>182 hits, system asks to narrow) burn turns before
a commonsensical `class Derivative` search. Even after landing on the long
class body, a [blind scroll loop](blind-scroll-loop.md) can exhaust the episode
**without submit**. The gold fix may require understanding **inheritance**
(override an inherited `kind` from a base module) — local scrolling alone never
surfaces that hop.

Harness implications under [ACI design principles](aci-design-principles.md):

- [Failure-derived prompt tips](failure-derived-prompt-tips.md): search issue
  identifiers first; refine when
  [bounded search observations](bounded-search-observations.md) say “narrow”.
- Demos that show `search_dir`/`search_file` with `class …` / symbol literals
  before `find_file` filename guesses.
- After finding a large definition, require `search_file` / `goto` (and
  parent-class lookup) rather than scroll-only exploration.
- Do not treat the **first hit file** as the fix site — comments or
  special-cases that *mention* a widget (admin `helpers.py`) and templates that
  omit `<label>` can be dead ends while the real hook lives on a related
  Widget/Field API elsewhere. Prefer source-tree paths over `build/lib`
  duplicates when `find_file` returns both.
- **Under-generation from missed third-party/cross-module symbols.** Some
  fixes require reaching for a symbol in a dependency the issue text never
  names — a jargon-heavy sphinx `rst_prolog` bug is correctly diagnosed as
  "the regex is involved," but the gold fix replaces a homemade regex with
  `docutils.parsers.rst.states.Body.patterns['field_marker']`, a third-party
  library pattern the agent has no textual hook toward. When a narrow local
  edit (tweaking one regex/constant in place) passes some but not all
  fail-to-pass tests, treat that as a signal to search **imports and
  dependency modules** the current file already pulls in, not only sibling
  files in the same package — under-generation (a plausible-looking but
  too-narrow fix) is a distinct failure from wrong-file localization and
  needs a different next action (broaden the search surface, not re-search
  the same tree).

Treat inefficient search as a first-class
[agent planning failure mode](agent-planning-failure-modes.md): the plan never
reaches the edit–evaluate phase, so raising max turns without better
localization policy rarely helps.
