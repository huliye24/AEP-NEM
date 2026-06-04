# Generic Seal Report Example

## 1. Basic information

```yaml
seal_id: SEAL-GENERIC-001
aep_id: AEP-GENERIC-001
nem_id: NEM-GENERIC-001
e_chain_id: ECHAIN-GENERIC-001
project: generic-example
version: v0.1
created_at: 2026-06-04T00:00:00Z
executor: ai-agent
reviewer: human-reviewer
seal_status: HOLD
```

## 2. Function completion statement

The AEP completed the primary function and produced the expected artifact.

```yaml
function_complete: true
evidence:
  - outputs/generic/result.txt
  - logs/run_generic_001.log
```

## 3. PoEW reference

```yaml
poew_id: POEW-GENERIC-001
poew_file: poew/POEW_GENERIC_001.md
poew_hash: pending
execution_timestamp: 2026-06-04T00:00:00Z
execution_duration: 42s
executor_type: ai-agent
environment: ubuntu-22.04 / python-3.11
```

## 4. Gate reference

```yaml
gate_id: GATE-GENERIC-001
gate_file: gates/GATE_GENERIC_001.md
gate_result: PASS_WITH_LIMITATIONS
must_pass_total: 6
must_pass_passed: 6
must_stop_triggered: false
evidence_required_completed: false
```

## 5. Evidence bundle

### Functional evidence

- The expected output file exists.
- The command completed with exit code 0.

### Execution evidence

- Runtime log exists.
- Input/output paths are recorded.

### Quality evidence

- Smoke test passed.
- Regression check not yet completed.

### Integrity evidence

- Output hash pending.

### Risk evidence

- No critical runtime failure.
- Regression evidence missing.

### Downstream evidence

- Output contract is stable.
- Downstream use should wait until hash and regression evidence are added.

## 6. Test summary

```yaml
tests_total: 4
tests_passed: 3
tests_failed: 0
tests_skipped: 1
success_rate: 0.75
critical_failures: 0
```

## 7. Artifact summary

| Artifact | Path | Hash | Purpose |
|---|---|---|---|
| Result file | outputs/generic/result.txt | pending | Main output |
| Run log | logs/run_generic_001.log | pending | Execution evidence |

## 8. Regression / non-breaking check

```yaml
regression_checked: false
affected_modules:
  - generic_module
breaking_change_detected: false
notes: Regression check must be added before Industrial Done.
```

## 9. Risk summary

| Risk | Severity | Blocking | Mitigation |
|---|---|---|---|
| Missing regression evidence | MEDIUM | true | Run regression suite |
| Missing artifact hash | LOW | true | Generate checksum |

## 10. Downstream dependency note

This AEP is functionally complete but should not become an industrial dependency until regression evidence and artifact hashes are added.

## 11. Reopen criteria

- Reopen if regression test fails.
- Reopen if output artifact changes without updated hash.
- Reopen if downstream AEP reports incompatible output contract.

## 12. Seal decision

```yaml
seal_decision: HOLD
decision_reason: Function is complete, but closure evidence is incomplete.
approved_by: none
approved_at: null
next_status: EVIDENCE_PENDING
```

## 13. Final statement

This AEP is **not** approved for Industrial Done status yet.
