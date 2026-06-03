# AEP Lifecycle

AEP 是可分发的最小工程任务包协议。生命周期定义了一个 AEP 从创建、分发、执行、回传、验收到被 NEM 采纳或归档的完整过程。

## 状态机

```text
DRAFT
  -> READY
    -> DISPATCHED
      -> IN_PROGRESS
        -> RETURNED
          -> REVIEW
            -> ADOPTED
            -> REJECTED
            -> REVISION_REQUIRED
  -> BLOCKED
  -> ARCHIVED
```

## 状态定义

| 状态 | 含义 |
|---|---|
| `DRAFT` | AEP 仍在编写，不能分发 |
| `READY` | AEP 已具备输入、目标、输出、验收标准和回传要求，可以分发 |
| `DISPATCHED` | AEP 已发送给执行端 |
| `IN_PROGRESS` | 执行端正在执行 |
| `RETURNED` | 执行端已回传任务包 |
| `REVIEW` | 发起端正在检查 outputs、PoEW、Gate result 和 report |
| `ADOPTED` | AEP 已通过 Gate，并被目标 NEM 采纳 |
| `REJECTED` | AEP 被拒绝采纳 |
| `REVISION_REQUIRED` | AEP 有价值但需要补充执行或证据 |
| `BLOCKED` | AEP 因依赖、权限、输入缺失或目标不清而暂停 |
| `ARCHIVED` | AEP 不再继续执行，只保留历史记录 |

## 生命周期步骤

### 1. Create

发起端创建 AEP 任务包，至少包含：

- `manifest.yaml`
- `task.md`
- `agent_instructions.md`
- `inputs/`
- `validation/acceptance_criteria.md`
- `poew/poew_record.yaml`
- `gates/gate_result.yaml`
- `report.md`

创建阶段的目标是让任务离开发起端之后仍能被理解。

### 2. Ready Check

进入 `READY` 前必须检查：

- 目标是否明确。
- 输入是否列明。
- 输出是否可检查。
- 执行边界是否清楚。
- 验收标准是否可验证。
- 回传要求是否明确。

如果缺少任意一项，状态保持 `DRAFT`。

### 3. Dispatch

发起端将 AEP 目录或压缩包发送到执行端。

分发记录建议写入 `manifest.yaml`：

```yaml
dispatch:
  dispatched_at:
  dispatched_to:
  executor_type:
  package_hash:
```

### 4. Execute

执行端读取任务包，并按以下顺序执行：

```text
1. manifest.yaml
2. task.md
3. agent_instructions.md
4. inputs/
5. validation/
6. outputs/
7. poew/
8. gates/
9. report.md
```

执行端不能把 AEP 扩展成不相关的大任务。若遇到阻塞，应记录 blocker 并回传，而不是静默失败。

### 5. Return

执行端回传 return package。回传包至少包含：

- 原始任务标识。
- 所有生成 outputs。
- PoEW 记录。
- Gate 初步结果。
- 执行报告。
- 风险、限制或 blocker。

### 6. Review

发起端复核回传包：

- 输出文件是否存在。
- PoEW 是否能支持“任务已完成”的结论。
- Gate result 是否有证据。
- 是否破坏目标 NEM 的接口。
- 是否需要补充执行。

### 7. Adopt Or Reject

如果 AEP 通过 Adopt Gate，则进入目标 NEM 的 `adopted` 列表。

如果 AEP 有价值但证据不足，则进入 `REVISION_REQUIRED`。

如果 AEP 与节点目标冲突或输出不可用，则进入 `REJECTED`。

## 生命周期记录模板

```yaml
aep_lifecycle:
  aep_id:
  current_status:
  history:
    - status: DRAFT
      at:
      actor:
      note:
    - status: READY
      at:
      actor:
      note:
    - status: DISPATCHED
      at:
      actor:
      note:
    - status: RETURNED
      at:
      actor:
      note:
```

## 基本原则

- AEP 不是“写给自己看的任务说明”，而是可迁移任务包。
- 没有回传证据的 AEP 不能被 NEM 采纳。
- 没有 Gate 判断的 AEP 不能改变 NEM 状态。
- 被拒绝的 AEP 也应保留记录，因为失败证据同样有工程价值。
