---
type: concept
title: Tool Definition Design
description: >
  Name, schema, and documentation choices that make tools easy for the model to
  select and call correctly without overlapping or over-complex surfaces.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 8"
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 16–30"
---

Tool definitions are prompt surface as much as API surface. Design them so a
human would find them clear — and so they resemble patterns the model already
saw in training.

- **Selection** — limit how many tools are available at once; partition the
  domain without near-duplicate overlaps; prefer simple tools over copying an
  entire web API into the [tool inventory](tool-inventory.md).
- **Naming** — self-documenting names; follow the provider's convention (for
  example TypeScript camelCase when tools render as TS signatures, since
  providers like OpenAI render tools as TypeScript — see
  [tool definition internal representation](tool-definition-internal-representation.md));
  avoid concatenated lowercase blobs that are hard to tokenize.
- **Definitions** — keep descriptions unambiguous but not legalese; if wrapping
  a public API the model already knows (verify by asking it to recite the docs
  back), mirror that API's names and argument shapes rather than inventing new
  ones.
- **Arguments** — few and simple (`string`, `number`, `integer`, `boolean`,
  enums/defaults). Do not assume every JSON Schema constraint is actually
  rendered into the prompt (nested-parameter descriptions and validators like
  `minItems`, `uniqueItems`, `minimum`, `maximum`, `pattern`, and `format` may
  be dropped depending on the provider). Be cautious with long-form text
  arguments in a JSON calling format — escaping newlines and quotes correctly
  gets riskier as text gets longer or more code-heavy; formats using
  XML-style tags for arguments avoid this escaping problem entirely. Prefer a
  dedicated structured parameter over free-form command syntax for any control
  the harness needs to reliably detect — for example a boolean `is_background`
  argument on a shell tool instead of relying on the model appending `&` to
  the command string, so the harness can parse the intent directly rather
  than pattern-matching arbitrary shell text.
- **Outputs** — define enough shape that the model can anticipate results; avoid
  stuffing "just in case" fields that distract.
- **Errors** — return meaningful, definition-relative errors so the model can
  retry; do not dump raw internal stack traces
  ([agent tool failure modes](agent-tool-failure-modes.md)) — this is what
  makes [reflection and error correction](reflection-and-error-correction.md)
  actually work at the tool-call level.

When the application already knows an argument value, omit it from the schema
(or use a detectable default) so the model cannot
[hallucinate placeholders](argument-hallucination.md). Dangerous tools still
need [human approval gates](human-approval-gates.md) at the application layer
regardless of how carefully the definition is worded.

For computer-use agents, definitions are incomplete without co-designed
observations: prefer an [agent-computer interface](agent-computer-interface.md)
with [stateful file viewers](stateful-file-viewer.md),
[guardrailed edits](guardrailed-edit-tool.md), and
[bounded search observations](bounded-search-observations.md) over exposing
raw shell utilities that flood context or fail silently.
