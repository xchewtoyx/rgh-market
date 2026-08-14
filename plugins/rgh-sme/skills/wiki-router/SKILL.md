---
name: wiki-router
description: "Route SME wiki questions to the matching domain wiki skills. Use when you do not know which bundle applies or the question spans multiple bundles: dimensional-modelling, observability, reliability-engineering, incident-management, automation-engineering, change-engineering, capacity-performance, technical-communication, evidence-verification, requirements-architecture, decision-alignment, operational-handover, infrastructure-as-code, ci-cd, resilience-engineering, data-engineering, data-visualization, distributed-systems, software-design, security-engineering, agentic-engineering, api-design, judgment-calibration, organizational-learning. Compact charter extracts are routing hints only — hand off to `<slug>-wiki` skills. Do not answer from the summaries."
---

# Wiki router

Use this skill when you do not know which domain wiki applies, or when the
question spans multiple bundles. The compact extracts below are routing
hints only. **Do not answer the user's question from these summaries.**

## Route, then hand off

1. Compare the question to each bundle's In scope and Boundaries.
2. Select every matching bundle — not just one.
3. Hand off to each matching `<slug>-wiki` skill (folder
   `skills/<slug>-wiki/`). Follow that skill's retrieval steps
   (`concepts.json` scan, then Read, then hop-by-hop link follow).
4. If no bundle's In scope covers the topic, say it is uncovered. A named
   slug in Boundaries maps to that `<slug>-wiki` skill. A Boundary with no
   named slug is not a handoff. Never invent a bundle name, wiki note, or
   hub.

## Bundles

### `dimensional-modelling` — `dimensional-modelling-wiki`

- In scope: Dimensional modelling technique; Fact table types (transaction, periodic snapshot, accumulating snapshot, factless), additivity, degenerate dimensions.; Dimension design; The bus architecture, bus matrix, and enterprise conformance, including the business-led governance process that…; The dimensional design process; Physical implementation of a dimensional model; Schema patterns that absorb operational/timing realities; Trade-offs versus other modelling styles (Inmon's Corporate Information Factory, stand-alone data marts, Data Vault…
- Boundaries: `observability-wiki`; `capacity-performance-wiki`; `automation-engineering-wiki`; `change-engineering-wiki`; `decision-alignment-wiki`

### `observability` — `observability-wiki`

- In scope: Telemetry types and their trade-offs; Instrumentation practice; Debugging methodology; AI agent & LLM observability; Observability data systems; Sociotechnical & developer feedback loops
- Boundaries: `reliability-engineering-wiki`; `incident-management-wiki`; `capacity-performance-wiki`; `dimensional-modelling-wiki`

### `reliability-engineering` — `reliability-engineering-wiki`

- In scope: SLI identification; SLO development; Error budgets; Alerting on SLOs; Service-level management practice; Reliability principles; Service-level management for nondeterministic, model-backed services
- Boundaries: `observability-wiki`; `incident-management-wiki`; `change-engineering-wiki`; `capacity-performance-wiki`; `automation-engineering-wiki`; `agentic-engineering-wiki`

### `incident-management` — `incident-management-wiki`

- In scope: Incident response structure; On-call design; Postmortems and learning from incidents; Preparedness
- Boundaries: `resilience-engineering-wiki`; `observability-wiki`; `reliability-engineering-wiki`; `change-engineering-wiki`; `automation-engineering-wiki`

### `automation-engineering` — `automation-engineering-wiki`

- In scope: Toil; The automation maturity path; Designing safe automation; Operational software engineering; Ironies of automation; Self-healing and auto-remediation patterns and their risks.
- Boundaries: `ci-cd-wiki`; `incident-management-wiki`; `capacity-performance-wiki`

### `change-engineering` — `change-engineering-wiki`

- In scope: Progressive delivery; Rollback engineering; Release verification; CI/CD as a safety system; Change risk management; Delivery metrics (DORA-style) as they inform delivery safety.
- Boundaries: `reliability-engineering-wiki`; `incident-management-wiki`; `automation-engineering-wiki`; `observability-wiki`; `api-design-wiki`

### `capacity-performance` — `capacity-performance-wiki`

- In scope: Capacity planning; Performance analysis methodology; Load characterisation and testing; Latency engineering; Efficiency and cost; Scalability patterns as they affect capacity
- Boundaries: `observability-wiki`; `reliability-engineering-wiki`; `automation-engineering-wiki`; `incident-management-wiki`

### `technical-communication` — `technical-communication-wiki`

- In scope: Audience analysis; Clarity technique; Document structure; Adapting the same material for different formats and reader types (executive summary vs deep reference vs quickstart)…; Editing practice
- Boundaries: `evidence-verification-wiki`; `requirements-architecture-wiki`; `decision-alignment-wiki`; `operational-handover-wiki`

### `evidence-verification` — `evidence-verification-wiki`

- In scope: Substantiating claims; Verification method; Review process; Review workflows; Common failure modes
- Boundaries: `technical-communication-wiki`; `requirements-architecture-wiki`; `decision-alignment-wiki`; `operational-handover-wiki`; `judgment-calibration-wiki`

### `requirements-architecture` — `requirements-architecture-wiki`

- In scope: Requirements practice; Architecture documentation; Constraints and trade-offs; Rationale capture; Traceability; Requirements for machine consumers
- Boundaries: `evidence-verification-wiki`; `technical-communication-wiki`; `decision-alignment-wiki`; `operational-handover-wiki`; `agentic-engineering-wiki`

### `decision-alignment` — `decision-alignment-wiki`

- In scope: Decision-document genres; Options analysis; Stakeholder alignment; Making decisions defensible; Turning a decision into coordinated action
- Boundaries: `evidence-verification-wiki`; `technical-communication-wiki`; `requirements-architecture-wiki`; `operational-handover-wiki`; `judgment-calibration-wiki`

### `operational-handover` — `operational-handover-wiki`

- In scope: Runbook and playbook writing; Handover documents; Capturing tacit/tribal knowledge; Maintenance documentation; Troubleshooting guides and onboarding documentation aimed at building independent operating competence, not just…
- Boundaries: `incident-management-wiki`; `technical-communication-wiki`; `evidence-verification-wiki`; `requirements-architecture-wiki`; `decision-alignment-wiki`; `organizational-learning-wiki`

### `infrastructure-as-code` — `infrastructure-as-code-wiki`

- In scope: Infrastructure expressed as version-controlled, reviewable declarations.; Resource, module, component, and stack design; State management, drift detection, import, migration, and reconciliation.; Safe live-infrastructure change; Infrastructure testing, validation, policy-as-code, and compliance controls.; Cost governance embedded in infrastructure code and its pipeline; Reusable infrastructure interfaces, environment promotion, and team workflows.; Tooling choices and trade-offs for provisioning and configuration systems.
- Boundaries: `ci-cd-wiki`; `automation-engineering-wiki`; `capacity-performance-wiki`

### `ci-cd` — `ci-cd-wiki`

- In scope: Continuous integration, build automation, artifact management, and commit-stage feedback.; Deployment pipelines, release orchestration, environment promotion, and automated rollback execution.; Automated acceptance, integration, and non-functional testing as delivery gates.; Software supply chain security; Evolutionary database schema migrations, database sandboxing, and zero-downtime schema deployment patterns.; Pipeline design for repeatability, fast feedback, traceability, and safe change flow.; Versioning, branching, dependency management, and release coordination.; On-demand, self-service provisioning of ephemeral test environments within delivery pipelines.; Delivery metrics and pipeline bottleneck diagnosis when they guide pipeline improvement.; Delivery of LLM/agent artifacts
- Boundaries: `change-engineering-wiki`; `infrastructure-as-code-wiki`; `automation-engineering-wiki`; `incident-management-wiki`; `agentic-engineering-wiki`; `observability-wiki`

### `resilience-engineering` — `resilience-engineering-wiki`

- In scope: Accident causation models; Safety-I versus Safety-II; Human factors of failure; Safety culture and organisation; The human-factors critique of procedures
- Boundaries: `incident-management-wiki`; `reliability-engineering-wiki`; `automation-engineering-wiki`; `operational-handover-wiki`

### `data-engineering` — `data-engineering-wiki`

- In scope: Pipeline design; Loading dimensional and analytical structures; Data quality engineering; Orchestration; Analytical platform architecture; Data lifecycle engineering
- Boundaries: `dimensional-modelling-wiki`; `ci-cd-wiki`; `reliability-engineering-wiki`; `capacity-performance-wiki`; `observability-wiki`

### `data-visualization` — `data-visualization-wiki`

- In scope: Matching visual form to analytical question; Perceptual foundations; Dashboard design; Graphical integrity; Analytical interaction
- Boundaries: `evidence-verification-wiki`; `technical-communication-wiki`; `dimensional-modelling-wiki`; `observability-wiki`

### `distributed-systems` — `distributed-systems-wiki`

- In scope: Replication; Partitioning; Transactions and consistency; Coordination and consensus; The failure semantics of distribution; Distribution architecture
- Boundaries: `capacity-performance-wiki`; `reliability-engineering-wiki`; `data-engineering-wiki`; `infrastructure-as-code-wiki`

### `software-design` — `software-design-wiki`

- In scope: Module design; Complexity management; Interface and API design; Public API surface as a product; Refactoring; Test design at the code level; Code-level readability
- Boundaries: `ci-cd-wiki`; `requirements-architecture-wiki`; `automation-engineering-wiki`; `change-engineering-wiki`; `api-design-wiki`

### `security-engineering` — `security-engineering-wiki`

- In scope: Threat modelling; Secure-design principles; Identity, authentication and authorisation as design concepts; Vulnerability classes as concepts; Security and reliability as related system properties; Security assurance practice; Machine-agent identity and delegated authority; The LLM/agent threat surface as a vulnerability-class family
- Boundaries: `ci-cd-wiki`; `infrastructure-as-code-wiki`; `incident-management-wiki`; `reliability-engineering-wiki`; `agentic-engineering-wiki`

### `agentic-engineering` — `agentic-engineering-wiki`

- In scope: Prompt and context engineering; Harness and agent-computer interface (ACI) design; Agent loop and orchestration design; External memory and knowledge architecture for agents; Agent failure modes and design-time evaluation; Maintenance and evolution
- Boundaries: `observability-wiki`; `automation-engineering-wiki`; `ci-cd-wiki`; `requirements-architecture-wiki`; `security-engineering-wiki`; this skill does not cover model alignment manufacturing (RLHF / preference training pipelines) and chip-level or generic inference-service optimization

### `api-design` — `api-design-wiki`

- In scope: Resource and endpoint modelling; Wire-contract naming, typing, and identification; Message and parameter structure; Operation semantics for async and bulk work; Reliability-facing contract mechanics; Response shaping and transfer efficiency; API evolution and lifecycle governance; API-as-product decisions
- Boundaries: `software-design-wiki`; `change-engineering-wiki`; `distributed-systems-wiki`; `security-engineering-wiki`; `requirements-architecture-wiki`; `technical-communication-wiki`; `agentic-engineering-wiki`

### `judgment-calibration` — `judgment-calibration-wiki`

- In scope: The dual-process frame and bias mechanism; Statistical-reasoning failure modes; The overconfidence family; Calibration and scoring; Structured estimation method; Belief updating as its own skill; Debiasing technique and deliberate practice; Team and aggregation epistemics for judgment; Choice under uncertainty and its distortion
- Boundaries: `decision-alignment-wiki`; `evidence-verification-wiki`; `resilience-engineering-wiki`; `incident-management-wiki`; `capacity-performance-wiki`

### `organizational-learning` — `organizational-learning-wiki`

- In scope: Psychological safety as a group-level construct; Silence and voice dynamics; Leadership practice for learning cultures; Team learning as a discipline distinct from individual learning; Mental models and shared vision as organisational routines; Failure taxonomy and blameless learning at organisational scale; Systems thinking as a shared diagnostic language for learning failures; Knowledge flow as a social phenomenon
- Boundaries: `resilience-engineering-wiki`; `incident-management-wiki`; `operational-handover-wiki`; `technical-communication-wiki`; `decision-alignment-wiki`
