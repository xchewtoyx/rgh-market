---
type: concept
title: Defensive Prompt Engineering
description: >
  Prompt injection is the LLM-specific instance of the injection pattern,
  made structurally harder to fully close than SQL injection because
  natural language has no clean syntactic boundary between instruction
  and data — so the defense is necessarily layered, not a single fix.
sources:
  - title: AI Engineering
    resource: "AI Engineering: Building Applications With Foundation Models (Huyen), ch. 5"
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering (Yang, Jimenez, Wettig, Lieret, Yao, Narasimhan, Press), Appendix E.1"
---

# Defensive Prompt Engineering

Prompt injection — malicious instructions smuggled into a model's input,
either directly by the user or indirectly via content the model later
ingests through tools, retrieval, or a monitored inbox — is
[injection](sql-injection.md)'s root cause applied to a natural-language
interface: untrusted content gets interpreted as instruction rather than
as data. Indirect prompt injection additionally makes the model a
[confused deputy](confused-deputy.md): the model retains whatever tool
authority it was legitimately granted, and the attack's real goal is
getting that authority exercised on the attacker's instruction rather than
the user's.

**Why this can't be closed the way SQL injection can.** Parameterized
queries work because SQL has a rigid, machine-checkable structural
boundary between the query and its bound values — an interpreter can
enforce the separation absolutely. Natural language has no equivalent
boundary: an LLM decides what counts as an instruction by inference over
meaning, not by parsing a fixed grammar, and instructions can be encoded
implicitly (a roleplay framing, a hidden directive inside retrieved text)
in ways no structural parser can reject outright. This is why defense here
is necessarily [defense in depth](defense-in-depth.md) — layered,
each catching what the previous layer misses — rather than one structural
fix that closes the class the way prepared statements close SQL
injection:

- **Model-level**: training the model to weight instruction sources by
  trust level (system prompt over user prompt over retrieved tool output)
  narrows, but does not eliminate, the model's susceptibility to content
  it processes as data actually redirecting its behavior.
- **Prompt-level**: stating constraints explicitly and reinforcing them
  (restating the task instruction around untrusted content the model must
  process) raises the cost of a successful injection without making it
  impossible — treat this as a mitigation, not a boundary, since there is
  no guarantee a model actually follows any given instruction.
- **System-level, the layer that matters most because it doesn't depend
  on the model behaving:** apply the same authority-scoping defenses that
  answer [confused deputy](confused-deputy.md) generally — least-privilege
  scoping of what tools and actions the model can invoke, explicit human
  approval gating before any high-impact action executes (irreversible
  writes, sending communications, running generated code), and running any
  model-generated code or command in an isolated environment rather than
  on infrastructure the rest of the system depends on. These layers hold
  even when a novel injection technique defeats every layer above them,
  because they don't assume the model correctly resisted the attempt —
  they bound what a successful one can accomplish.

**"Run it in a sandbox" is not one control — isolation strength must match
the adversary the boundary is meant to resist.** Namespace-based isolation
(containers) and full hardware virtualization (VMs) are different-strength
boundaries, and the choice should follow
[trusted computing base](trusted-computing-base.md) reasoning: draw the
boundary against the threat model, not around a box. SWE-agent's own
analysis of running LM-generated code against arbitrary, untrusted issue
descriptions is a worked instance of this: the team judged Docker's
namespace isolation adequate for code that is merely diverse and
untrusted — containing accidental damage like a wayward `rm -rf` — while
explicitly noting it is *not* equivalent to full virtualized hardware
isolation, and therefore insufficient against input deliberately
engineered to exploit a container-escape vulnerability. A sandbox sized
for accidental harm is not automatically a sandbox that resists a
targeted escape attempt; the required isolation strength should be chosen
against the adversary capability actually in scope, not assumed from
"it's isolated."

**Treat any content the system did not itself author as untrusted input**,
regardless of how it entered the context window — a retrieved document, a
tool's return value, and a field a user typed all deserve the same
suspicion an application would apply to unsanitized input in any other
system, because from the model's perspective they're indistinguishable
sources of "things that appear in my context."
