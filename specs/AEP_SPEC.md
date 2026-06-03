# AEP Specification v0.1

**Full name:** Atomic Engineering Package Specification
**Version:** v0.1 Draft
**Status:** Draft — open for feedback

---

## 0. Abstract

AEP (Atomic Engineering Package) is the standard format for the smallest unit of engineering work in the AEP-NEM protocol.

An AEP encapsulates: task objective, execution rules, input materials, environment requirements, task map, acceptance criteria, output paths, stop conditions, and final report — all in a self-contained, migratable package.

Anyone or any AI that opens an AEP should be able to: understand the task, execute it, verify the results, and generate traceable proof of engineering work.

---

## 1. Minimum Viable AEP

```
AEP = ZIP + standard directory structure + manifest.json
    + agent_spec.md + task_map.yaml + validation_rules.yaml + reports
```

The first-stage goal is not to replace ZIP. It is to define an AI-era engineering task packaging standard on top of ZIP.

---

## 2. Directory Structure

```
{AEP_ID}/
├── manifest.json              # Machine-readable metadata
├── agent_spec.md              # Task specification for the executor
├── human_brief.md             # Human-readable task description
├── rules.md                   # Execution rules and constraints
├── task_map.yaml              # Task dependency graph
├── changelog.md               # Version change log
├── 00_START_HERE.md           # Entry point for humans reading the AEP
│
├── tasks/                     # Individual task definitions
│   └── {AEP_ID}-{TASK_ID}.md
│
├── validation/
│   ├── acceptance_criteria.md # Must-pass criteria
│   └── validation_rules.yaml  # Machine-validatable rules
│
├── outputs/                   # Execution artifacts
│   └── README.md
│
└── reports/
    └── final_report_template.md
```

---

## 3. manifest.json

The manifest is the machine-readable entry point. Minimum required fields:

```json
{
  "aep_id": "AEP-EXAMPLE-001",
  "version": "0.1.0",
  "title": "Example AEP",
  "status": "draft",
  "created": "2026-06-02T00:00:00Z",
  "agent_requirements": {
    "capabilities": ["code_generation", "file_io"],
    "min_context_window": 32000
  },
  "environment": {
    "os": ["linux", "macos", "windows"],
    "runtime": "any"
  },
  "expected_outputs": [
    "source code files",
    "test results",
    "documentation"
  ],
  "stop_conditions": [
    "all_tasks_completed",
    "acceptance_criteria_failed",
    "manual_interrupt"
  ],
  "estimated_duration": "30m",
  "max_duration": "2h"
}
```

**Full schema:** [`../schemas/aep.schema.json`](../schemas/aep.schema.json)

---

## 4. agent_spec.md

The task specification written for the executor. Must follow this structure:

1. **Context** — What problem does this AEP solve?
2. **Objective** — What must be achieved?
3. **Constraints** — What must NOT be done?
4. **Input Materials** — What resources are available?
5. **Success Definition** — What does "done" mean?

---

## 5. task_map.yaml

Defines the dependency graph of tasks within the AEP:

```yaml
tasks:
  - id: T01
    name: "Setup project structure"
    dependencies: []
    estimated_duration: "5m"

  - id: T02
    name: "Implement core logic"
    dependencies: ["T01"]
    estimated_duration: "20m"

  - id: GATE01
    name: "Acceptance Gate"
    type: gate
    dependencies: ["T02"]
    criteria: "validation/acceptance_criteria.md"
```

---

## 6. Validation

Validation happens at two levels:

### 6.1 Structural validation
- All required files present
- manifest.json parses correctly
- task_map.yaml is valid
- Directory naming follows convention

### 6.2 Acceptance validation
- All acceptance criteria must pass
- All gate tasks must succeed
- Stop conditions must not trigger unexpectedly

---

## 7. Execution Flow

```
1. Agent reads 00_START_HERE.md and manifest.json
2. Agent reads agent_spec.md for task understanding
3. Agent reads rules.md for constraints
4. Agent reads task_map.yaml for execution order
5. Agent executes tasks in dependency order
6. Agent writes outputs to outputs/
7. Agent checks validation/acceptance_criteria.md
8. Agent produces final report in reports/
9. Agent generates PoEW record
```

---

## 8. Naming Convention

```
{AEP_ID} = {PROJECT_PREFIX}-{AEP_TYPE}-{DOMAIN}-{NNN}

Examples:
  MT-001              # Moodify task 001
  AEP-OVERDARK-GATE-CALIBRATION-001
  AEP-EXAMPLE-001
```

---

## 9. Versioning

AEP versions follow: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking change to structure or format
- **MINOR**: New fields, new tasks, extended scope
- **PATCH**: Fixes, clarifications, non-breaking updates
