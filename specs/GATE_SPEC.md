# Gate Specification v0.1

**Full name:** Evolution Gate Specification
**Version:** v0.1 Draft
**Status:** Draft — open for feedback

---

## 0. Abstract

Gate (Evolution Gate) is the quality checkpoint in the AEP-NEM protocol. Every Gate evaluates whether engineering work meets the criteria to pass to the next phase — whether that's an AEP completing, a NEM maturing, or a branch merging.

---

## 1. Definition

> **Gate is a structured quality checkpoint that determines whether engineering work advances to the next phase.**

Gates are not optional. Every AEP execution must pass through its defined Gates. Every NEM maturity transition must pass through a Gate.

---

## 2. Gate Structure

```yaml
# gate.yaml
gate_id: "GATE-STABLE-001"
gate_type: maturity_gate
target: "NEM-TIDECYCLE"
target_version: "0.1.0"
target_maturity: STABLE

criteria:
  must_pass:
    - id: "ALL_AEP_PASSED"
      description: "All constituent AEPs have passed their own gates"
    - id: "TEST_COVERAGE_80"
      description: "Test coverage >= 80%"
      threshold: 80

  should_pass:
    - id: "PERFORMANCE_BENCHMARK"
      description: "Performance within 20% of baseline"
      threshold: 20

  must_stop:
    - id: "SECURITY_CRITICAL"
      description: "No critical security vulnerabilities"
    - id: "DATA_LOSS"
      description: "No data loss in migration path"

evidence_required:
  - type: "test_report"
  - type: "poew_log"
  - type: "performance_benchmark"

evaluator: "automated"  # or "human" or "hybrid"
```

---

## 3. Gate Types

| Type | Applies To | Evaluator |
|---|---|---|
| **task_gate** | Individual tasks within an AEP | Automated |
| **aep_gate** | Complete AEP execution | Automated or hybrid |
| **maturity_gate** | NEM maturity transition | Hybrid or human |
| **merge_gate** | E-Chain branch merge | Automated |
| **release_gate** | E-Organism release | Human |

---

## 4. Gate Criteria Categories

### 4.1 Must-Pass
Non-negotiable. Every criterion in this category must be met. If any `must_pass` fails, the gate result is **FAIL**.

### 4.2 Should-Pass
Quality targets. Failure does not block passage but is recorded. Accumulated `should_pass` failures may trigger a review gate.

### 4.3 Must-Stop
Hard stop conditions. If any `must_stop` triggers, execution halts immediately. These are safety-critical conditions.

---

## 5. Gate Results

```yaml
# gate_result.yaml
gate_id: "GATE-STABLE-001"
timestamp: "2026-06-02T14:30:00Z"
result: PASS  # PASS | CONDITIONAL_PASS | FAIL | STOP

must_pass_results:
  - id: "ALL_AEP_PASSED"
    result: PASS

should_pass_results:
  - id: "PERFORMANCE_BENCHMARK"
    result: PASS
    value: 15  # 15% deviation, under 20% threshold

evidence:
  - type: "test_report"
    path: "outputs/test_report.json"
  - type: "poew_log"
    path: "poew/poew_log.yaml"

evaluator_signature: "auto-gate-v0.1.0"
```

---

## 6. Gate Chain

Gates can be chained:

```
AEP Execution
    │
    ▼
GATE-TASK-001 (automated task check)
    │
    ▼
GATE-AEP-001 (automated AEP check)
    │
    ▼
GATE-BASIC (maturity gate for NEM v0.1)
    │
    ▼
GATE-STABLE (maturity gate for NEM v0.3)
```

Each gate in the chain must pass before the next is evaluated.

---

## 7. Gate Automation

| Evaluator | When Used |
|---|---|
| **automated** | Structural validation, test coverage thresholds, schema checks |
| **human** | Strategic decisions, UX evaluation, architecture approval |
| **hybrid** | Automated checks run first, then human reviews the results |

---

## 8. Gate Records

All gate results are permanently recorded as part of the PoEW trail. A gate result cannot be modified after it is recorded. If a NEM is re-evaluated, a new gate instance is created (not an overwrite).
