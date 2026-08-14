---
type: concept
title: "Antipattern: Manual Stack Parameters"
description: Typing stack instance parameter values on the command line by hand each time the stack tool runs — simple for experimentation, unsafe for anything that matters.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 7"
---

The most direct way to configure a [reusable stack](reusable-stack-pattern.md) instance is to type parameter values on the command line each time you run the stack tool. It's the simplest option for learning a tool or experimenting, but it doesn't scale to anything a team relies on: it's easy to mistype a value, hard to remember which values belong to which instance, and impossible for everyone on a team to reliably remember the same values — and it can't be automated for CI or CD, since there's no unattended way to "type" the values.

Every other pattern for [configuring stack instances](stack-parameter-design-principles.md) — [stack environment variables](stack-environment-variables-pattern.md), [scripted parameters](scripted-parameters-pattern.md), [stack configuration files](stack-configuration-files-pattern.md), and beyond — exists to move parameter values out of a human's memory and into something repeatable, reviewable, and automatable.
