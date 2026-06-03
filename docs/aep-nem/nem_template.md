# NEM Template

本模板用于描述一个可持续进化的工程节点。NEM 由多个 AEP 组成，并通过 Gate 和 PoEW 记录演化过程。

```yaml
nem_id:
title:
status: CONCEPT
version: 0.1.0
created_at:
updated_at:
owner:
related_chain:

description:
  summary:
  scope:
  out_of_scope:

node_goal:
  primary:
  user_or_system_value:

included_aeps:
  - aep_id:
    title:
    status:
    role:

current_stage:
  label:
  description:

maturity_level:
  current:
  target:
  criteria:

interfaces:
  provides:
    - name:
      description:
      version:
  requires:
    - name:
      description:
      version_or_constraint:

inputs:
  - name:
    type:
    source:

outputs:
  - name:
    type:
    path_or_interface:

metrics:
  - name:
    definition:
    target:

gate_history:
  - gate_id:
    date:
    result:
    evidence:

poew_records:
  - poew_id:
    date:
    summary:
    evidence:

risks:
  - risk:
    impact:
    mitigation:

roadmap:
  - version_or_stage:
    goal:
    planned_aeps:

next_upgrade_direction:
  summary:
```

## 字段说明

| 字段 | 说明 |
|---|---|
| `nem_id` | NEM 唯一标识，例如 `NEM-MOODIFY-MRS-BENCHMARK` |
| `included_aeps` | 已纳入或计划纳入的 AEP |
| `interfaces` | NEM 对外提供和依赖的能力边界 |
| `metrics` | 衡量 NEM 成熟度的指标 |
| `gate_history` | 每次 Gate 判断的记录 |
| `poew_records` | 与该 NEM 相关的工程证据 |
| `roadmap` | 后续演化计划 |

## 编写原则

- NEM 应表示一个长期工程能力，而不是一次任务。
- NEM 的接口应比内部 AEP 更稳定。
- 每次成熟度变化都应有 Gate 记录。
- 每次采纳新 AEP 都应留下 PoEW。
