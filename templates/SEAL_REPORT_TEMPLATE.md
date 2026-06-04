# Seal Report Template

## 1. Basic information

```yaml
seal_id:
aep_id:
nem_id:
e_chain_id:
project:
version:
created_at:
executor:
reviewer:
seal_status:
```

Recommended `seal_status` values:

```text
HOLD
PASS
PASS_WITH_LIMITATIONS
REOPEN_REQUIRED
REJECTED
```

## 2. Function completion statement

### 2.1 Claimed functional result

Describe what has been completed.

```text
The AEP has completed:
-
-
-
```

### 2.2 Function Complete decision

```yaml
function_complete: true / false
evidence:
  - 
```

## 3. PoEW reference

```yaml
poew_id:
poew_file:
poew_hash:
execution_timestamp:
execution_duration:
executor_type:
environment:
```

## 4. Gate reference

```yaml
gate_id:
gate_file:
gate_result:
must_pass_total:
must_pass_passed:
must_stop_triggered:
evidence_required_completed:
```

## 5. Evidence bundle

### 5.1 Functional evidence

```text
-
-
-
```

### 5.2 Execution evidence

```text
-
-
-
```

### 5.3 Quality evidence

```text
-
-
-
```

### 5.4 Integrity evidence

```text
-
-
-
```

### 5.5 Risk evidence

```text
-
-
-
```

### 5.6 Downstream evidence

```text
-
-
-
```

## 6. Test summary

```yaml
tests_total:
tests_passed:
tests_failed:
tests_skipped:
success_rate:
critical_failures:
```

### Test details

| Test | Type | Result | Evidence |
|---|---|---|---|
|  |  |  |  |

## 7. Artifact summary

| Artifact | Path | Hash | Purpose |
|---|---|---|---|
|  |  |  |  |

## 8. Regression / non-breaking check

```yaml
regression_checked: true / false
affected_modules:
  -
breaking_change_detected: true / false
notes:
```

## 9. Risk summary

| Risk | Severity | Blocking | Mitigation |
|---|---|---|---|
|  |  |  |  |

## 10. Downstream dependency note

Explain whether this AEP can be safely used by later AEPs / NEMs.

```text
Stable dependency:
Unstable areas:
Required caution:
Recommended next AEP:
```

## 11. Reopen criteria

This AEP must be reopened if:

```text
-
-
-
```

## 12. Seal decision

```yaml
seal_decision:
decision_reason:
approved_by:
approved_at:
next_status:
```

Recommended final mapping:

| Seal decision | Next status |
|---|---|
| PASS | INDUSTRIAL_DONE |
| PASS_WITH_LIMITATIONS | INDUSTRIAL_DONE_LIMITED |
| HOLD | EVIDENCE_PENDING |
| REOPEN_REQUIRED | REWORK_IN_PROGRESS |
| REJECTED | REJECTED |

## 13. Final statement

```text
This AEP is / is not approved for Industrial Done status.
```
