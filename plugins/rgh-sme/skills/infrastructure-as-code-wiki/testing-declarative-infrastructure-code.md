---
type: concept
title: Testing Declarative Infrastructure Code
description: Why low-level assertions against declarative infrastructure code tend to have little value, and where testing such code actually pays off.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 8, ch. 9"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 5, ch. 11"
---

A test that simply restates a piece of [declarative infrastructure code](declarative-vs-imperative-infrastructure-code.md) — asserting a subnet exists with the exact address range the code declares — has low value. It can only catch three things: the code was never applied; the tool applied it incorrectly without erroring (a bug in the tool, better fixed there or by switching tools); or someone changed the code but forgot to update the test (a risk the test itself creates by existing). None of these justify blanketing a declarative codebase in one-to-one assertions.

Testing declarative code becomes worthwhile in two situations: when the code's output can genuinely vary — because it uses variables, conditionals, or calls out to functions whose result depends on runtime state — and when multiple simple declarations combine into something whose *emergent* behavior is worth proving, such as whether a full network path is actually reachable rather than whether each individual routing rule was created. In general, testing that a tool created what you declared is less valuable than testing that the result lets you do what you actually need — see [progressive testing for infrastructure](progressive-testing-for-infrastructure.md) for how "outcome" tests fit alongside cheaper existence checks.

If declarative code needs complex conditional logic to be worth testing thoroughly, that's usually a sign the logic belongs in an imperative library instead — see the [infrastructure domain entity pattern](infrastructure-domain-entity-pattern.md) — where it can get proper unit test coverage rather than living inside YAML or HCL conditionals.

Retrofitting tests onto infrastructure code that predates any test coverage runs into a circularity of its own — see the [legacy infrastructure code dilemma](legacy-infrastructure-code-dilemma.md) for why the fix usually has to come before the tests, not after.

A tool's dry-run mode gives a second, distinct thing worth testing that a plain "does it exist" assertion can't: whether refactoring [idempotent](idempotent-infrastructure-code.md) code accidentally changed its effective output. Running dry-run mode against an already-converged instance after a refactor (restructuring a template, reorganizing tasks) should report no differences if the refactor was truly behavior-preserving; any reported change flags either an intentional-but-undocumented behavior change or an accidental regression, before either one is actually applied. The same dry-run mechanism doubles as a lightweight, no-side-effects way to detect [configuration drift](configuration-drift.md) on live infrastructure.

A narrower, code-level idempotence check is a useful minimum test even where broader assertions aren't worth writing: apply the code twice in a row against the same instance and assert that the second run reports zero changes and zero failures. This directly operationalizes [idempotency](idempotent-infrastructure-code.md) as a pass/fail test rather than trusting it by inspection, and catches the common regression where a task that should be a no-op on rerun (a `command`/`shell`-style escape hatch missing an explicit change condition) keeps reporting itself as changed forever.
