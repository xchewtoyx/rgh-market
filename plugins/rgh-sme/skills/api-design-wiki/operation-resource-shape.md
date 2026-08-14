---
type: concept
title: Operation Resource Shape
description: >
  The generic Operation interface with done flag, parameterized result and
  metadata, and distinct error envelope for tracked work failures.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 10"
---

```text
interface Operation<ResultT, MetadataT> {
  id: string;
  done: boolean;
  result?: ResultT | OperationError;
  metadata?: MetadataT;
  expireTime?: Date;
}

interface OperationError {
  code: string;
  message: string;
  details?: any;
}
```

- `id` — required; the operation is a resource.
- `done` — explicit boolean rather than inferring completion from `result`,
  because success may legitimately return an empty result. Named `done`, not
  `complete`, so it does not imply success — important for
  [cancel semantics](operation-cancel-pause-resume.md).
- `result` — success payload (`ResultT`) or `OperationError`. `ResultT` need
  not be a resource; it can be empty or an ephemeral value such as a translation
  result.
- `metadata` — progress type (`MetadataT`); null when there is nothing to
  report. Pause state lives here — see
  [operation cancel, pause, and resume](operation-cancel-pause-resume.md).

`GetOperation` / `WaitOperation` return HTTP errors only when **fetching the
Operation resource** fails. Failure of the underlying work appears as
`OperationError` in `result`, separating "could not read status" from "work
failed." Use a type guard (for example `isOperationError`) on the client.

`OperationError.code` must be unique, specific, and **machine-readable**.
`message` is for humans — client logic must not depend on its exact text.
Structured extras belong in `details`, not folded into `message`.
