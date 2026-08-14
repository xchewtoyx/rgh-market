---
type: concept
title: Hyrum's Law
description: With enough users of an interface, every observable behavior becomes something somebody depends on, whether or not it was ever documented or promised.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 15"
---

Quoted in full because the precision matters: "With a sufficient number of users of an interface, it does not matter what you promise in the contract: All observable behaviors of your system will be depended on by somebody" (hyrumslaw.com). A documented interface contract only describes what a maintainer is *entitled* to assume will keep working — it does not describe what will actually break if changed. Every side effect, timing quirk, error-message wording, or field-ordering accident that a caller can observe is a candidate for someone, somewhere, to have quietly built on top of.

## Why This Matters for Handover

This is the reason a new maintainer cannot treat "the documented interface didn't change" as proof that a change is safe. It's the underlying mechanism behind why [characterization tests for undocumented behavior](characterization-tests-for-undocumented-behavior.md) are worth writing before touching legacy code with no test coverage: the tests exist precisely because undocumented behavior is still real behavior that something out there may depend on, law or no law about what was "supposed" to be depended on. It's also why silently drifting an [external annotation](external-annotations-for-fragile-legacy-systems.md) or a runbook's stated contract out of sync with the actual implementation is more dangerous than it looks — the documented contract was never the full list of things that could break.

The practical implication for anyone writing a handover document: don't stop at describing the documented interface. Where you know of an observable-but-unpromised behavior that has become load-bearing in practice (a specific response ordering, a timing characteristic, an error format some downstream system parses), call it out explicitly as a known dependency — otherwise the next maintainer has no way to distinguish it from genuine implementation freedom.
