---
type: concept
title: Serverless Handler Isolation
description: >
  Separating cloud-provider entry-point code from application logic so tests
  run against plain functions and provider swaps require changing only the
  handler layer.
sources:
  - title: Serverless Design Patterns and Best Practices
    resource: "Serverless Design Patterns and Best Practices (Brian Zambrano), ch. 9"
---

# Serverless Handler Isolation

Serverless functions tempt teams to mix provider APIs, routing, and business
logic in one file. The durable layout isolates them:

- **Handler / entry point** — the file the cloud provider invokes directly;
  contains all provider-specific bootstrapping (path setup, runtime wiring).
- **Application logic** — namespaced in its own directory, with no imports of
  provider SDKs or deployment metadata.
- **`tests/`** — wholly separate; mocks and factories live here and are never
  deployed with the function.

Benefits: changing cloud providers or frameworks touches only the handler;
tests target application code without emulating the full serverless runtime;
the repo stays easy to navigate. In Python, path manipulation for imports
belongs in one place (handler at runtime, `conftest.py` under test); Node.js
resolves libraries by convention via `node_modules` and typically needs less
explicit path setup.

Test bootstrapping must replicate handler-side setup the framework normally
supplies at deploy time — environment variables, library paths — inside test
configuration, with CI-specific overrides (e.g. database host `localhost` when
Postgres runs as a linked container in the pipeline instead of a named local
Docker link).

This is the serverless application of [independent testability](independent-testability.md)
at the function boundary: verify business logic in isolation before the
[commit stage](commit-stage.md) runs integration against real managed services.
