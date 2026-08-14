---
type: concept
title: Pre-Commit Peer Review
description: >
  Requiring independent review and explicit consent before a change enters shared
  state, so verification happens while rollback is still cheap.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 9"
---
# Pre-Commit Peer Review

**Pre-commit review** means another engineer examines a proposed change — typically as a diff with description — and grants explicit consent before it lands in the shared codebase. The consent marker ("looks good to me," LGTM) is a permission bit combined with other approval bits before commit is allowed.

## Typical Review Loop
The author uploads a change snapshot; reviewers comment on the diff; the author revises and re-uploads until reviewers are satisfied; reviewers then mark LGTM; the author commits once required comments are resolved and all approval bits are present. Iteration is expected — review is a conversation on the artifact, not a one-shot gate.

## Why Pre-Commit Matters for Verification
Review before merge keeps the shared artifact's audit trail clean: every accepted change has a named reviewer who attested they understood what the change does. Errors caught here are cheaper to fix than defects discovered after deployment. This is a technical instance of [verification checkpoint proximity](verification-checkpoint-proximity.md) — checking close to the point of change.

## Verification Action

When a document claims a change was "reviewed," check whether review happened **before** the change entered shared/production state, who granted consent, and whether unresolved review comments remained open at commit time. A post-hoc sign-off after merge is weaker evidence than pre-commit LGTM with a traceable diff history — see [verification accounting](verification-accounting.md).
