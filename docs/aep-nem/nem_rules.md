# NEM Rules

NEM 是由多个 AEP 组成并持续进化的项目节点协议。它不是单个任务，也不是文件夹命名方式，而是一个项目能力节点的组织、采纳、版本和演化规则。

## 1. NEM 的基本定义

一个 NEM 必须代表一个可持续维护的项目节点，例如：

- Runtime audio processing
- MRS open benchmark
- Preset craft library
- Electron desktop app
- Report and explainability system

一个 NEM 不应该代表一次性任务。一次性任务应写成 AEP。

## 2. NEM 最小结构

```text
NEM-{PROJECT}-{NODE}/
  nem.yaml
  README.md
  aeps/
    adopted/
    pending/
    rejected/
  gates/
    gate_history.yaml
  poew/
    poew_index.yaml
  roadmap.md
  changelog.md
```

## 3. nem.yaml

```yaml
nem_id: NEM-MOODIFY-MRS-OPEN-BENCHMARK
title: MRS Open Benchmark
status: EXPERIMENTAL
version: 0.1.0
created_at: 2026-06-03
updated_at: 2026-06-03
owner: moodify-mrs
related_chain: MRS Scoring Engineering Chain

node_goal:
  primary: Build a reproducible and explainable music realism scoring node.
  value: Provide stable MRS scores and reports for Moodify processing results.

interfaces:
  provides:
    - name: mrs_score
      version: 0.1.0
      description: Score and explanation for one audio sample.
  requires:
    - name: audio_sample_set
      version_or_constraint: fixed hash list
      description: Baseline and processed audio samples.

included_aeps:
  adopted: []
  pending:
    - AEP-MOODIFY-MRS-VALIDATION-001
  rejected: []

maturity:
  current: BASIC
  target: STABLE

metrics:
  - name: field_completeness
    target: 100%
  - name: score_reproducibility
    target: within configured threshold
```

## 4. AEP 采纳规则

一个 AEP 只有满足以下条件，才可以进入 NEM 的 `adopted` 列表：

- AEP 的 `related_nem` 指向当前 NEM。
- AEP 回传包包含 outputs、PoEW、Gate result 和 report。
- AEP 的 Adopt Gate 结果为 `PASS`。
- AEP 输出没有破坏 NEM 的已声明接口。
- AEP 的风险和限制已经记录。

如果 AEP 有价值但证据不足，应进入 `pending`，Gate 结果为 `NEEDS_REVIEW` 或 `HOLD`。

如果 AEP 与节点目标冲突、输出不可用或证据不足且无法补救，应进入 `rejected`。

## 5. NEM 状态规则

```text
CONCEPT       # 节点概念成立，但尚未有有效 AEP
EXPERIMENTAL  # 已有实验 AEP，但接口和指标未稳定
HOLD          # 暂停演化，等待依赖或决策
ADOPT         # 已可被项目主线采纳
STABLE        # 接口、指标和 Gate 基本稳定
RELEASED      # 可对外发布
DEPRECATED    # 不再推荐使用
```

状态转换必须由 Gate 记录支撑。

## 6. NEM 成熟度规则

```text
BASIC
  至少有一个核心 AEP 被采纳，节点目标可被演示。

STABLE
  核心接口稳定，关键指标可重复验证，主要 AEP 有 PoEW。

ADOPTED
  已被其他 NEM 或主工程链依赖。

REFACTORED
  内部结构经过重构，但对外接口保持可迁移或有明确迁移方案。
```

## 7. Gate 规则

NEM 至少需要以下 Gate：

| Gate | 触发时机 | 作用 |
|---|---|---|
| Adopt Gate | AEP 准备进入 NEM | 判断 AEP 是否可采纳 |
| Maturity Gate | NEM 准备升级成熟度 | 判断节点是否可进入下一阶段 |
| Interface Gate | 接口准备变化 | 判断是否破坏下游依赖 |
| Release Gate | 准备对外发布 | 判断文档、证据和版本是否足够 |

任何 NEM 版本升级都必须至少经过 Maturity Gate。

## 8. 版本规则

NEM 使用语义化版本：

```text
MAJOR.MINOR.PATCH
```

- `PATCH`: 文档、记录、非破坏性修正。
- `MINOR`: 新增 AEP、新增能力、指标增强。
- `MAJOR`: 接口变化、节点边界变化、迁移成本较高的重构。

版本变化必须写入 `changelog.md`。

## 9. PoEW 索引规则

NEM 不需要复制每个 AEP 的完整证据，但必须维护索引：

```yaml
poew_records:
  - poew_id:
    aep_id:
    date:
    result:
    evidence_path:
    summary:
```

PoEW 索引回答三个问题：

- 哪些 AEP 真的被执行过？
- 哪些证据支撑 NEM 当前状态？
- 当前版本是否可以被外部复核？

## 10. Roadmap 规则

NEM 的 roadmap 必须由 AEP 驱动，而不是抽象愿望。

推荐写法：

```markdown
## Roadmap

| Stage | Goal | Required AEPs | Gate |
|---|---|---|---|
| BASIC | Minimum scoring run | AEP-MRS-FORMULA, AEP-MRS-VALIDATION | GATE-MRS-BASIC |
| STABLE | Reproducible benchmark | AEP-MRS-REGRESSION, AEP-MRS-FIELD-STANDARD | GATE-MRS-STABLE |
```

## 11. NEM 不应该做什么

- 不把无关 AEP 塞进同一个节点。
- 不在没有 Gate 的情况下升级状态。
- 不把聊天记录当作 PoEW。
- 不让单个 AEP 同时改变多个节点的核心接口。
- 不用玄学命名替代可验证的工程边界。
