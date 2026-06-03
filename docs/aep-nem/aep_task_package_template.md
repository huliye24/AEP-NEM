# AEP Task Package Template

AEP 是可分发的最小工程任务包协议。一个 AEP 不只是任务说明，而是一个可以被复制、传输、交给 AI 或人类执行、再把结果回传的完整任务包。

## 最小目录结构

```text
AEP-{PROJECT}-{DOMAIN}-{NNN}/
  manifest.yaml
  task.md
  agent_instructions.md
  inputs/
    README.md
  outputs/
    README.md
  validation/
    acceptance_criteria.md
    validation_rules.yaml
  poew/
    poew_record.yaml
  gates/
    gate_result.yaml
  report.md
```

## manifest.yaml

```yaml
aep_id: AEP-MOODIFY-RUNTIME-SMOKE-001
title: Runtime audio processing smoke test
status: DRAFT
version: 0.1.0
created_at: 2026-06-03
updated_at: 2026-06-03
owner: moodify-core

related_nem: NEM-MOODIFY-RUNTIME
related_chain: Runtime Engineering Chain

priority: high
difficulty: low
estimated_effort: 0.5d

distribution:
  package_format: directory
  portable: true
  allowed_executor_types:
    - ai_agent
    - human
    - automated_runner
  return_required: true

runtime_requirements:
  os:
    - windows
    - macos
    - linux
  tools:
    - name: python
      version: ">=3.10"
      required: false
  network_required: false

expected_outputs:
  - outputs/smoke/output.wav
  - outputs/smoke/runtime.log
  - outputs/smoke/metrics.json

return_package:
  required_files:
    - outputs/
    - poew/poew_record.yaml
    - gates/gate_result.yaml
    - report.md
```

## task.md

```markdown
# Task

## Context

说明这个任务为什么存在，它属于哪个 NEM，解决什么最小工程问题。

## Objective

用一句话说明任务完成后必须产生什么结果。

## Inputs

| 输入 | 路径 | 说明 |
|---|---|---|
| | | |

## Outputs

| 输出 | 路径 | 验收方式 |
|---|---|---|
| | | |

## Execution Steps

1. 
2. 
3. 

## Non-goals

- 本 AEP 不解决什么问题。
- 哪些改动不允许在本任务中发生。
```

## agent_instructions.md

```markdown
# Agent Instructions

## You Must

- Read `manifest.yaml` first.
- Only modify files inside allowed output paths unless explicitly instructed.
- Record every generated artifact in `poew/poew_record.yaml`.
- Run the validation steps before returning the package.

## You Must Not

- Expand the task into unrelated refactors.
- Mark the task complete without output evidence.
- Delete input materials.

## If Blocked

Write the blocker into `report.md`, set Gate result to `HOLD`, and return the package.
```

## validation/acceptance_criteria.md

```markdown
# Acceptance Criteria

## Must Pass

- [ ] Required output files exist.
- [ ] Validation command or manual validation has been recorded.
- [ ] PoEW record lists generated artifacts.
- [ ] No stop condition was triggered.

## Should Pass

- [ ] Output is reproducible from the provided inputs.
- [ ] Logs are readable and explain failures.

## Must Stop If

- [ ] Required input files are missing.
- [ ] Executor cannot determine the intended output.
- [ ] Task requires access outside the allowed scope.
```

## poew/poew_record.yaml

```yaml
poew_id:
date:
aep_id:
executor:
  type:
  name:
  environment:

execution:
  started_at:
  finished_at:
  status:
  commands_run:
    - command:
      result:

artifacts:
  - path:
    type:
    hash:
    description:

validation:
  method:
  result:
  log:

notes:
```

## gates/gate_result.yaml

```yaml
gate_id:
aep_id:
gate_type: Adopt Gate
result: NEEDS_REVIEW
evaluated_at:
evaluator:

must_pass:
  - id:
    result:
    evidence:

decision:
  adopted: false
  reason:
  next_action:
```

## report.md

```markdown
# AEP Return Report

## Summary

## What Was Done

## Outputs

## Validation Result

## PoEW Evidence

## Risks Or Blockers

## Suggested Next AEP
```

## 分发与回传流程

```text
1. 创建 AEP 任务包
2. 将整个目录或压缩包发送到执行端
3. 执行端读取 manifest.yaml 和 task.md
4. 执行端生成 outputs、PoEW、Gate result 和 report
5. 执行端回传整个 AEP 包或 return_package
6. 发起端复核 Gate result
7. 通过后采纳到 NEM
```

## 最低合格标准

一个 AEP 任务包至少必须做到：

- 离开发起方环境后仍能被理解。
- 执行端知道输入、输出、边界和验收标准。
- 回传包里有输出、有证据、有报告。
- NEM 可以根据 Gate 结果决定是否采纳。
