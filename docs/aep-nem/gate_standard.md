# Gate Standard

Gate 是 AEP-NEM 中的进化闸门，用于判断工程成果是否可以进入下一阶段。

## Gate 的作用

- 判断 AEP 是否可以被 NEM 采纳。
- 判断 NEM 是否可以从实验状态进入稳定状态。
- 判断工程链上的分支成果是否可以合并。
- 阻止没有证据、不可复现或质量不足的成果进入主线。

## Gate 类型

| Gate | 作用 |
|---|---|
| Draft Gate | 判断草案是否清晰、可读、可执行 |
| Build Gate | 判断代码、脚本或文档结构是否可运行或可生成 |
| Test Gate | 判断测试、验证或检查是否通过 |
| Report Gate | 判断结果是否可解释、可审计 |
| Adopt Gate | 判断 AEP 是否可以被 NEM 采纳 |
| Release Gate | 判断成果是否可以对外发布 |

## Gate 结果

```text
PASS
FAIL
HOLD
NEEDS_REVIEW
```

| 结果 | 含义 |
|---|---|
| `PASS` | 已满足必要条件，可以进入下一阶段 |
| `FAIL` | 未满足必要条件，不可采纳 |
| `HOLD` | 暂停判断，等待依赖、数据或外部条件 |
| `NEEDS_REVIEW` | 自动证据不足，需要人工复核 |

## Gate 记录模板

```yaml
gate_id:
gate_type:
target_type:
target_id:
target_version:
date:
result:
evaluator:

criteria:
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

stop_conditions:
  - id:
    description:
    triggered: false

decision:
  summary:
  adopted: false
  next_action:
```

## 最低通过要求

一个 Gate 至少应检查：

- 目标是否明确。
- 输出是否存在。
- 验收标准是否可验证。
- PoEW 证据是否足够。
- 是否触发 stop condition。
- 是否有明确下一步动作。
