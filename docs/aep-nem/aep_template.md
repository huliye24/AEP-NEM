# AEP Template

本模板用于描述一个最小工程原子包。实际项目可以复制本文件，并将占位内容替换为真实工程信息。

```yaml
aep_id:
title:
status: DRAFT
version: 0.1.0
created_at:
updated_at:
owner:
related_nem:
related_chain:
priority:
difficulty:
estimated_effort:

context:
  summary:
  background:
  problem:

objective:
  primary:
  non_goals:

inputs:
  - name:
    type:
    path_or_source:
    required: true

outputs:
  - name:
    type:
    path:
    required: true

execution_steps:
  - step:
    description:
    expected_result:

acceptance_criteria:
  - id:
    description:
    required: true

validation_method:
  type:
  command:
  manual_review:

poew_evidence:
  - type:
    path:
    description:

risks:
  - risk:
    impact:
    mitigation:

dependencies:
  - type:
    name:
    version_or_ref:

rollback_plan:
  description:

next_aep_suggestions:
  - title:
    reason:
```

## 字段说明

| 字段 | 说明 |
|---|---|
| `aep_id` | AEP 唯一标识，例如 `AEP-MOODIFY-RUNTIME-SMOKE-001` |
| `status` | 当前状态，建议使用标准 AEP 状态枚举 |
| `related_nem` | 该 AEP 所属或计划采纳到的 NEM |
| `objective` | 本 AEP 的明确目标和非目标 |
| `outputs` | 可验证交付物 |
| `acceptance_criteria` | 必须通过的验收条件 |
| `validation_method` | 自动或人工验证方式 |
| `poew_evidence` | 工程工作量证明 |
| `rollback_plan` | 失败、误采纳或破坏主线时的回退方式 |

## 编写原则

- 一个 AEP 只做一件可验证的工程事。
- 不把长期路线图塞进单个 AEP。
- 不用“优化体验”“提升质量”这类无法验收的目标。
- 每个输出都要有路径、格式或可检查标准。
- 每个验收标准都要能被自动检查或人工复核。
