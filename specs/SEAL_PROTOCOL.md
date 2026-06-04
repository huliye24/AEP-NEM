# AEP Seal Protocol v0.1

## 1. Purpose

The AEP Seal Protocol defines the closure layer of an Atomic Engineering Package.

It answers one question:

> When can an AEP move from **Function Complete** to **Industrial Done**?

The purpose of the Seal Protocol is to prevent false completion, weak closure, missing evidence, and unverifiable engineering claims.

## 2. Core principle

```text
Function Complete ≠ Seal Complete ≠ Industrial Done
```

- **Function Complete** means the requested function or task exists.
- **Seal Complete** means the closure evidence is complete.
- **Industrial Done** means the AEP can be safely used as a dependency by future AEPs, NEMs, E-Chains, or E-Organisms.

## 3. Relationship with PoEW and Gate

The Seal Protocol does not replace PoEW or Gate. It sits above them.

```text
AEP execution
→ PoEW evidence
→ Gate evaluation
→ Seal review
→ Industrial Done
```

### PoEW

PoEW proves that engineering work happened.

### Gate

Gate decides whether quality conditions are met.

### Seal

Seal decides whether the AEP is formally closed and dependency-safe.

## 4. Status machine

### 4.1 Standard path

```text
DRAFT
→ IN_PROGRESS
→ FUNCTION_COMPLETE
→ EVIDENCE_PENDING
→ SEAL_REVIEW
→ SEAL_COMPLETE
→ INDUSTRIAL_DONE
```

### 4.2 Rework path

```text
SEAL_REVIEW
→ REOPEN_REQUIRED
→ REWORK_IN_PROGRESS
→ FUNCTION_COMPLETE
```

### 4.3 Deprecated path

```text
FUNCTION_COMPLETE
→ ABANDONED
```

Used when a function exists but is no longer aligned with the engineering direction.

## 5. Status definitions

### DRAFT

The AEP is defined but not started.

### IN_PROGRESS

The AEP is being executed.

### FUNCTION_COMPLETE

The primary function or deliverable exists and can be demonstrated.

Requirements:

- Main task output exists.
- Basic command or usage path is known.
- No obvious blocking runtime error remains.

This status does **not** mean industrial completion.

### EVIDENCE_PENDING

The function exists, but required closure evidence is incomplete.

Typical missing evidence:

- No final summary.
- No reproducible log.
- No hash or output reference.
- No regression check.
- No risk statement.
- No downstream dependency note.
- No reviewer signature.

### SEAL_REVIEW

The AEP enters formal closure evaluation.

Requirements:

- PoEW record available.
- Gate result available.
- Output artifacts listed.
- Evidence bundle assembled.
- Seal report drafted.

### SEAL_COMPLETE

The AEP has complete closure evidence.

Requirements:

- All must-pass items passed.
- No must-stop condition active.
- PoEW is complete.
- Gate result is accepted.
- Evidence bundle is complete.
- Known risks are documented.
- Downstream dependency impact is documented.

### INDUSTRIAL_DONE

The AEP is officially closed as an industrial-grade engineering unit.

Requirements:

- Seal Complete.
- Reviewer or automated verifier approval.
- Version or commit reference.
- Integration note.
- Archive or artifact location.
- Reopen criteria defined.

## 6. Seal evidence layers

An AEP Seal contains six evidence layers.

### 6.1 Functional evidence

Proves that the requested function exists.

Examples:

- CLI command output.
- Generated file.
- API response.
- UI screenshot.
- Test audio output.
- Runtime summary.

### 6.2 Execution evidence

Proves that the engineering work ran.

Examples:

- PoEW log.
- Run timestamp.
- Environment information.
- Executor identity.
- Runtime duration.
- Input/output paths.

### 6.3 Quality evidence

Proves that the output passed validation.

Examples:

- Gate result.
- Unit tests.
- Smoke tests.
- Integration tests.
- Performance benchmark.
- MRS score report.
- Regression report.

### 6.4 Integrity evidence

Proves that the output can be referenced safely.

Examples:

- File hash.
- Git commit.
- Artifact checksum.
- Version tag.
- Immutable output directory.
- Dependency manifest.

### 6.5 Risk evidence

Proves that remaining risks are known.

Examples:

- Known limitation.
- Failed non-blocking tests.
- Manual review warning.
- Edge case not covered.
- Performance concern.
- Security note.

### 6.6 Downstream evidence

Proves that future AEP/NEM work can rely on this result.

Examples:

- Stable interface.
- Output contract.
- Dependency note.
- Next AEP compatibility.
- Rollback instruction.
- Reopen trigger.

## 7. Required seal fields

Every Seal Report must include:

```yaml
seal_id:
aep_id:
nem_id:
status:
function_complete:
poew_reference:
gate_reference:
evidence_bundle:
test_summary:
artifact_summary:
risk_summary:
downstream_dependency_note:
reopen_criteria:
reviewer:
seal_decision:
timestamp:
```

## 8. Seal decision levels

### PASS

The AEP can move to `Industrial Done`.

### PASS_WITH_LIMITATIONS

The AEP can be used, but documented limitations must be respected.

### HOLD

The AEP cannot move forward until evidence is added.

### REOPEN_REQUIRED

The AEP must return to implementation.

### REJECTED

The AEP result should not be used.

## 9. Industrial seal rule

An AEP may only be marked `Industrial Done` when:

```text
Function Complete = true
PoEW Complete = true
Gate Accepted = true
Seal Report Complete = true
Blocking Risk = false
Downstream Safe = true
```

## 10. Recommended file naming

```text
SEAL_REPORT_<AEP_ID>.md
SEAL_BUNDLE_<AEP_ID>.json
```

## 11. Minimal seal checklist

```text
[ ] Function output exists
[ ] PoEW exists
[ ] Gate result exists
[ ] Test logs exist
[ ] Summary exists
[ ] Artifacts are listed
[ ] Hashes or paths are recorded
[ ] Regression impact checked
[ ] Known risks documented
[ ] Downstream dependency documented
[ ] Reopen criteria documented
[ ] Reviewer/verifier recorded
[ ] Final seal decision recorded
```

## 12. Design philosophy

The Seal Protocol exists because AI-native engineering creates a new risk:

> AI can produce functional artifacts faster than humans can verify their long-term reliability.

Therefore, completion must become a structured protocol, not a feeling.
