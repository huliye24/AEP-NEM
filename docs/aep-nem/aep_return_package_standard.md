# AEP Return Package Standard

AEP Return Package 是执行端完成任务后回传给发起端的结果包。它用于证明任务是否被执行、输出是否存在、证据是否足够、是否可以被 NEM 采纳。

## 回传包目标

一个合格的回传包必须回答四个问题：

- 任务做完了吗？
- 产出了什么？
- 如何证明产出有效？
- 这个 AEP 是否可以被 NEM 采纳？

## 最小回传结构

```text
AEP-{PROJECT}-{DOMAIN}-{NNN}-return/
  manifest.yaml
  outputs/
  poew/
    poew_record.yaml
  gates/
    gate_result.yaml
  report.md
  logs/
    execution.log
```

## manifest.yaml 回传字段

```yaml
aep_id:
title:
version:
status: RETURNED
related_nem:

return_package:
  returned_at:
  executor:
    type:
    name:
    environment:
  source_package_hash:
  return_package_hash:
  completion_status:
  blocked: false
```

## outputs/

`outputs/` 存放任务产物。每个产物都应能在 PoEW 中找到记录。

推荐约束：

- 不把临时缓存放入 outputs。
- 不把无法解释来源的文件放入 outputs。
- 大文件可以只回传索引、hash 和下载地址。

## poew/poew_record.yaml

```yaml
poew_id:
aep_id:
created_at:

executor:
  type:
  name:
  environment:

commands:
  - command:
    started_at:
    finished_at:
    exit_code:
    log_path:

artifacts:
  - path:
    type:
    size:
    hash:
    description:

validation:
  - method:
    result:
    evidence:

limitations:
  - item:
```

## gates/gate_result.yaml

```yaml
gate_id:
aep_id:
gate_type: Adopt Gate
result:
evaluated_at:
evaluator:

must_pass:
  - id:
    description:
    result:
    evidence:

should_pass:
  - id:
    description:
    result:
    evidence:

decision:
  recommended_action:
  can_be_adopted:
  reason:
```

Gate result 可以由执行端先给出建议，但最终是否采纳由发起端或目标 NEM 的维护者决定。

## report.md

```markdown
# AEP Return Report

## Summary

## Execution Result

## Output Files

## Validation

## PoEW Evidence

## Gate Recommendation

## Risks And Limitations

## Suggested Next AEP
```

## 回传结果枚举

```text
SUCCESS
PARTIAL_SUCCESS
BLOCKED
FAILED
NEEDS_REVIEW
```

| 结果 | 含义 |
|---|---|
| `SUCCESS` | 所有必须输出和验收标准都满足 |
| `PARTIAL_SUCCESS` | 产生了部分有效成果，但未完全满足验收标准 |
| `BLOCKED` | 因外部条件无法继续 |
| `FAILED` | 执行失败且没有可采纳成果 |
| `NEEDS_REVIEW` | 结果需要人工判断 |

## 采纳要求

一个回传包想被 NEM 采纳，至少必须满足：

- `completion_status` 为 `SUCCESS` 或明确可接受的 `PARTIAL_SUCCESS`。
- 必要 outputs 存在。
- PoEW 记录完整。
- Gate result 为 `PASS` 或经维护者复核后通过。
- 风险和限制已记录。
- 不破坏目标 NEM 的接口。

## 不合格回传包

以下情况不能直接采纳：

- 只有文字说明，没有 outputs。
- 有 outputs，但没有 PoEW。
- 有 PoEW，但没有验证结果。
- 任务范围被执行端擅自扩大。
- 输出依赖无法访问的本地路径。
- 结果无法对应原始 AEP ID。

## 推荐回传流程

```text
1. 执行端完成任务
2. 执行端整理 outputs
3. 执行端生成 PoEW
4. 执行端生成 Gate recommendation
5. 执行端写 report
6. 执行端计算 return package hash
7. 发起端接收并复核
8. 发起端决定 ADOPTED / REJECTED / REVISION_REQUIRED
```
