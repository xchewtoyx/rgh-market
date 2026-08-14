---
type: concept
title: "Define Everything as Code (Core Practice)"
description: The IaC core practice of specifying infrastructure elements in externalized, version-controlled text files rather than through closed-box tools, so the specification can be reviewed, tested, and delivered like software.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 4"
---

Defining everything as code means specifying infrastructure elements — [stacks](infrastructure-stack.md), server configuration, [server images](server-image-as-code.md), application packages, delivery pipeline configuration, and validation rules — in text files managed separately from the tool that applies them, rather than through a GUI, ad hoc CLI commands, or a tool with its own opaque internal state.

This "externalized configuration" property is what unlocks the rest of software engineering practice for infrastructure: you can only version code, run CI against it, and build delivery pipelines for it if the specification lives in files you control, rather than being trapped inside a closed-box tool's own storage. A tool that stores its configuration as inaccessible internal data limits you to whatever workflow the tool's own UI or API happens to support.

Defining things as code delivers three benefits directly:

- **Reusability** — a defined thing can be instantiated repeatedly, by anyone, identically.
- **Consistency** — things built from the same code are built the same way every time, which makes behavior predictable and testing reliable.
- **Transparency** — anyone can read the code to see how something is built, review it, and learn from it.

Putting that code into [version control](version-control-for-infrastructure-code.md) is what turns "defined as code" into a full engineering practice — with traceability, rollback, and triggerable automation. The choice of what kind of language to write that code in — [declarative or imperative](declarative-vs-imperative-infrastructure-code.md), and general-purpose or a [domain-specific language](infrastructure-domain-specific-languages.md) — shapes what kinds of infrastructure concerns the code can cleanly express.
