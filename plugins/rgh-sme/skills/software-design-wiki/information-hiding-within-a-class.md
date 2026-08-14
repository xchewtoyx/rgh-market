---
type: concept
title: Information Hiding Within a Class
description: >
  Information hiding applies below the module-interface level too — private
  methods and instance variables benefit from the same discipline of
  minimizing how many places touch a given piece of internal knowledge.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 5"
---

The same technique that applies at a module's public boundary — see
[information hiding](information-hiding.md) — applies inside a class as well.
Design private methods so each one hides some sub-capability from the rest of
the class, and minimize how many places within the class touch each instance
variable. Reducing a variable's usage footprint eliminates internal
dependencies and lowers the class's internal complexity, even though none of
this is visible to anything outside the class. It's the same underlying goal
— fewer places that have to change together — applied one level down.
