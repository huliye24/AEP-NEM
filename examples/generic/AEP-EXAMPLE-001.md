# AEP-EXAMPLE-001: Hello World AEP

This is the simplest possible AEP — a "Hello World" for the AEP-NEM protocol. Use it to understand the format and test your tooling.

---

## Purpose

Demonstrate the minimum viable AEP structure. An AI agent should be able to open this AEP, understand the task, execute it, produce output, and generate a valid PoEW record.

---

## Directory Structure

```
AEP-EXAMPLE-001/
├── manifest.json
├── agent_spec.md
├── human_brief.md
├── rules.md
├── task_map.yaml
├── changelog.md
├── 00_START_HERE.md
├── tasks/
│   └── AEP-EXAMPLE-001-T01.md
├── validation/
│   ├── acceptance_criteria.md
│   └── validation_rules.yaml
├── outputs/
│   └── README.md
└── reports/
    └── final_report_template.md
```

---

## manifest.json

```json
{
  "aep_id": "AEP-EXAMPLE-001",
  "version": "0.1.0",
  "title": "Hello World AEP",
  "status": "ready",
  "created": "2026-06-02T00:00:00Z",
  "agent_requirements": {
    "capabilities": ["file_io"],
    "min_context_window": 8000
  },
  "environment": {
    "os": ["any"],
    "runtime": "any"
  },
  "expected_outputs": [
    "A hello_world.txt file",
    "A final report"
  ],
  "stop_conditions": [
    "all_tasks_completed",
    "manual_interrupt"
  ],
  "estimated_duration": "5m",
  "max_duration": "15m"
}
```

---

## agent_spec.md

```markdown
# Agent Specification: Hello World AEP

## Context
This is the simplest possible AEP. It exists to test that the AEP format and tooling work correctly.

## Objective
Create a file called `hello_world.txt` in the `outputs/` directory containing the text "Hello from AEP-NEM Protocol!"

## Constraints
- Do not modify files outside the AEP directory
- Do not make network requests
- Do not create additional files beyond what is specified

## Input Materials
- This AEP directory (self-contained, no external inputs)

## Success Definition
- `outputs/hello_world.txt` exists
- File contains the exact text: "Hello from AEP-NEM Protocol!"
- Final report is written to `reports/final_report.md`
```

---

## human_brief.md

```markdown
# Human Brief: Hello World AEP

## Why this AEP?
To verify that the AEP format is working end-to-end: from human intent → AEP packaging → AI execution → verifiable output.

## What will change?
A single file will be created. Nothing else.

## Risks
None. This is a smoke test.

## Dependencies
None.
```

---

## task_map.yaml

```yaml
tasks:
  - id: "T01"
    name: "Create hello world file"
    description: "Create outputs/hello_world.txt with the greeting message"
    dependencies: []
    estimated_duration: "2m"

gates:
  - id: "GATE01"
    name: "Acceptance Gate"
    type: "aep_gate"
    dependencies: ["T01"]
    criteria: "validation/acceptance_criteria.md"
    evaluator: "automated"
```

---

## validation/acceptance_criteria.md

```markdown
# Acceptance Criteria

## Must Pass
- [ ] `outputs/hello_world.txt` exists
- [ ] File contains "Hello from AEP-NEM Protocol!"
- [ ] `reports/final_report.md` exists

## Should Pass
- [ ] File encoding is UTF-8

## Must Stop If
- [ ] Any file outside the AEP directory would be modified
```

---

## Expected Output

After execution:
```
outputs/
└── hello_world.txt   # Contains: "Hello from AEP-NEM Protocol!"

reports/
└── final_report.md   # Execution summary
```
