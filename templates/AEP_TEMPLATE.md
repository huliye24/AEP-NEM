# AEP Template

Copy this directory and rename `{AEP_ID}` to your AEP identifier.

## Directory structure

```
{AEP_ID}/
├── manifest.json
├── agent_spec.md
├── human_brief.md
├── rules.md
├── task_map.yaml
├── changelog.md
├── 00_START_HERE.md
├── tasks/
│   └── {AEP_ID}-T01.md
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
  "aep_id": "{AEP_ID}",
  "version": "0.1.0",
  "title": "{TITLE}",
  "status": "draft",
  "created": "{ISO_TIMESTAMP}",
  "agent_requirements": {
    "capabilities": [],
    "min_context_window": 32000
  },
  "environment": {
    "os": ["linux", "macos", "windows"],
    "runtime": "any"
  },
  "expected_outputs": [],
  "stop_conditions": [
    "all_tasks_completed",
    "acceptance_criteria_failed",
    "manual_interrupt"
  ],
  "estimated_duration": "{DURATION}",
  "max_duration": "{MAX_DURATION}"
}
```

---

## agent_spec.md

```markdown
# Agent Specification: {TITLE}

## Context
[What problem does this AEP solve? What came before it?]

## Objective
[What must be achieved? Be specific.]

## Constraints
[What must NOT be done? What boundaries exist?]

## Input Materials
[What files, data, or resources are available?]

## Success Definition
[What does "done" mean? How is success measured?]
```

---

## human_brief.md

```markdown
# Human Brief: {TITLE}

## Why this AEP?
[One paragraph on the strategic motivation.]

## What will change?
[What will be different after this AEP completes?]

## Risks
[What could go wrong?]

## Dependencies
[What does this AEP depend on?]
```

---

## task_map.yaml

```yaml
tasks:
  - id: "T01"
    name: "{TASK_NAME}"
    description: "{TASK_DESCRIPTION}"
    dependencies: []
    estimated_duration: "{DURATION}"

gates:
  - id: "GATE01"
    name: "Acceptance Gate"
    type: "aep_gate"
    dependencies: ["T01"]
    criteria: "validation/acceptance_criteria.md"
    evaluator: "automated"
```

---

## rules.md

```markdown
# Execution Rules

## Must Do
- [Rule 1]

## Must NOT Do
- [Rule 1]

## If Stuck
- [Escalation path]

## Stop Conditions
- [Condition 1]: [Action]
```

---

## validation/acceptance_criteria.md

```markdown
# Acceptance Criteria

## Must Pass
- [ ] Criterion 1
- [ ] Criterion 2

## Should Pass
- [ ] Criterion 1

## Must Stop If
- [ ] Condition 1
```

---

## validation/validation_rules.yaml

```yaml
rules:
  - id: "STRUCTURE_VALID"
    description: "All required files present"
    type: structural
    severity: must_pass

  - id: "MANIFEST_VALID"
    description: "manifest.json is valid JSON and contains required fields"
    type: structural
    severity: must_pass

  - id: "TASK_MAP_VALID"
    description: "task_map.yaml has no circular dependencies"
    type: structural
    severity: must_pass
```

---

## 00_START_HERE.md

```markdown
# {AEP_ID}: {TITLE}

## For Humans
This AEP does: {ONE_LINE_DESCRIPTION}

## For AI Agents
1. Read `agent_spec.md`
2. Read `rules.md`
3. Follow `task_map.yaml`
4. Output to `outputs/`
5. Write final report to `reports/`
6. Check `validation/acceptance_criteria.md`

## Quick Links
- [Agent Spec](agent_spec.md)
- [Human Brief](human_brief.md)
- [Task Map](task_map.yaml)
- [Rules](rules.md)
```
