---
type: concept
title: ReAct Loop
description: >
  Interleave reasoning traces that update context without side effects and
  environment actions so plans stay grounded and exceptions stay recoverable.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 8"
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 31–45"
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    resource: "ReAct (Yao et al.), pp. 1–15"
---

ReAct (Yao et al., 2022) interleaves **reasoning traces** with
**task-specific actions** so each reinforces the other: reasoning induces,
tracks, and updates plans and handles exceptions (**reason to act**); actions
query external sources and fold observations back into reasoning (**act to
reason**). Formally, augment the action space with language thoughts
\(\hat{a}_t \in L\) that do **not** affect the environment — they only update
context \(c_{t+1} = (c_t, \hat{a}_t)\) — while true actions \(a_t \in A\)
produce observations. This is now a default pattern for
[LLM agents](llm-agent.md) on multi-hop and tool-using tasks — the agentic
counterpart to a fixed-depth [iterative multi-hop retrieval](iterative-multi-hop-retrieval.md)
pipeline, deciding hop count at runtime instead of design time.

A common prompted format is `Thought` / `Act` / `Observation`, ending with a
finish act. Thought types include goal decomposition, commonsense injection,
extracting signal from observations, progress tracking, and exception
handling. Density varies: reasoning-primary tasks often alternate densely;
long interactive episodes may emit thoughts **sparsely** only at high-leverage
steps. Few-shot human trajectories of thought+action+observation are the usual
scaffold on a frozen LM.

Evidence for the Thought step's contribution is not only architectural: on
HotpotQA multi-hop QA, few-shot-only ReAct initially underperformed both
standard and chain-of-thought prompting — in-prompt examples alone didn't
sufficiently teach the reasoning-plus-tool-use pattern — but after fine-tuning
on just 3,000 examples, a fine-tuned 8B ReAct model beat standard prompting on
a much larger 62B model, and fine-tuned 62B ReAct beat standard prompting on a
540B model, i.e. reasoning plus fine-tuning beat raw scale.

For knowledge-intensive few-shots, keep four styles on the **same** questions
so ablations stay fair: Original (answer only), Act (tools, no thoughts),
CoT (thoughts, no tools), ReAct (interleaved). Exemplar Thoughts should
plan multi-hop retrieval, notice missing fields → `Lookup`, disambiguate
entities, and Finish with uncertainty-aware labels (SUPPORTS / REFUTES /
NOT ENOUGH INFO) when evidence is incomplete — not only when the gold answer
is known.

**Thinking vs acting-only:** Act without Thought can still help via search on
some QA tasks; on environment-heavy agents, Thought is critical against
hallucinated object state and plan drift. Reasoning-only
[chain of thought](chain-of-thought-prompting.md) stays a static black box
grounded only in internal weights — prone to hallucination and error
propagation without tool observations. Humans can inspect which facts came
from the environment versus the model and, when needed, steer via thought
editing.

Cost: every thought and observation consumes context and raises latency.
Enforcing the format usually needs few-shot examples, which further shrink the
budget left for tool docs under [context engineering](context-engineering.md).
For long interactive episodes, structure prompts as an
[agent episode prompt stack](agent-episode-prompt-stack.md), enforce
[action format](action-format-enforcement.md) in the harness, and
[collapse old observations](collapsed-observations.md). Combine with
[plan-and-solve prompting](plan-and-solve-prompting.md) when an overarching plan
should precede the loop, and with [Reflexion](reflexion.md) when lessons must
persist across whole trials.

**Interactive decision-making (sparse thoughts):** On long-horizon,
sparse-reward environments (ALFWorld household tasks, WebShop shopping),
few-shot **Act** trajectories alone lose subgoal structure and environment
state; the same trajectories with **sparse** thoughts — decompose the goal,
mark subgoal completion, choose the next subgoal, inject pretrained
commonsense about where objects live — raise success sharply (ReAct best
~71% vs Act ~45% on ALFWorld; ~10 absolute points success-rate on WebShop
over strong IL/IL+RL). Thoughts need not be dense every turn: emit them at
high-leverage control points. Prompt templates often encode thoughts as
environment-noop acts (`think[...]` → Observation `OK.`) so the same
action parser handles reasoning and side-effecting commands — keep Act and
ReAct exemplars on the **same** action vocabulary for clean ablations. Weak
thought scaffolds that **repeat** an unfinished subgoal each turn (ReAct-IM)
underperform concrete advancing subgoals even when physical actions match.
WebShop traces show the shopping form: Act may Buy Now on the first mismatched
over-budget hit; ReAct's think steps reject candidates attribute-by-attribute
before selecting options — put that filter pattern in few-shots.

**Flexible thoughts vs feedback-only monologue:** Ablating to dense
Inner-Monologue-style thoughts that only restate environment progress and
remaining goal (ReAct-IM) underperforms flexible sparse ReAct thoughts that
also decide *when* a subgoal finishes, *what* comes next, and *where* to
look using internal knowledge. For harness design, prefer thought scaffolds
that invite planning and retrieval from weights — not only narrating
observations — and keep an Act-only ablation in
[offline prompt evaluation](offline-prompt-evaluation.md) so you know whether
reasoning tokens are earning their keep.

**Knowledge-intensive QA:** With a weak Wikipedia search/lookup/finish API
(few-shot dense thought–action–observation), ReAct cuts hallucination versus
CoT but raises reasoning-error and non-informative-search failures; Act
without thoughts is weaker still on answer synthesis. Prefer
[internal–external knowledge routing](internal-external-knowledge-routing.md)
(ReAct ↔ CoT-SC fallbacks) over a single mode when step budget and vote
confidence are available as harness signals. Audit episodes with the
[ReAct success and failure taxonomy](react-success-and-failure-taxonomy.md)
so false positives and label ambiguity do not inflate "wins." Qualitative
FEVER/ALFWorld traces: ReAct uses contradicting observation details Act/CoT
miss; Act and ReAct-IM loop after illegal cleans or skipped subgoals — keep
those failure stories in
[failure-derived prompt tips](failure-derived-prompt-tips.md).

**HITL and grounding:** Prefer
[ReAct thought editing](react-thought-editing.md) over action-only correction
when diagnosing drift. On knowledge tasks, interleaved search can surface
**up-to-date** observations that outdated dataset labels miss — Act without
reasoning may retrieve poorly; CoT without tools may hallucinate. Limits:
large action spaces need many demonstrations that can blow the in-context
budget; finetuning on ReAct trajectories helps but high-quality human
annotations remain desirable. Always bound external act permissions —
interpretable traces aid diagnosis but do not by themselves prevent harmful
tool use.
