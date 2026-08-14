---
type: concept
title: Automation Bias in Verification
description: The dangerous assumption that automated system outputs and software logs are inherently correct without independent audit trails.
sources:
  - title: "Taking Testing Seriously"
    resource: "Taking Testing Seriously (James Bach, Michael Bolton), ch. 16"
---

# Automation Bias in Verification

**Automation bias in verification** (or the computer reliability presumption) is the systemic flaw of assuming that software outputs, automated reports, or database records are correct unless proven broken. Treating automated outputs as authoritative facts rather than checkable claims leads to catastrophic verification failures.

## Organizational and Legal Failure Modes
Relying uncritically on automated outputs introduces severe institutional risks:
- **Asymmetric Burden of Proof**: Shifting the burden of proving system failure onto reviewers or external parties who lack access to source code, error logs, or execution environments.
- **Defect Suppression**: Concealing known software bugs, chaotic patches, or intermittent data corruption to preserve legal liability postures or project prestige.
- **Superficial Compliance**: Substituting critical exploratory auditing with superficial green-check dashboards, creating false security around broken software.

## Verification Safeguards
To guard against automation bias and institutional gaslighting:
- **Treat Outputs as Assertions**: Evaluate automated system outputs as claims requiring [evidence triangulation](evidence-triangulation.md) against independent logs or physical records.
- **Demand Audit Trail Transparency**: Require full access to error logs, bug databases, and execution telemetry as part of [verification accounting](verification-accounting.md).
- **Maintain Critical Distance**: Reject legal or managerial presumptions of software infallibility by actively probing boundary conditions, intermittent anomalies, and system failure modes.
