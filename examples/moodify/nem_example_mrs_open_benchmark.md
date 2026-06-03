# NEM Example: MRS Open Benchmark

```yaml
nem_id: NEM-MOODIFY-MRS-OPEN-BENCHMARK
title: MRS Open Benchmark
status: EXPERIMENTAL
version: 0.1.0
created_at: 2026-06-03
updated_at: 2026-06-03
owner: moodify-mrs
related_chain: MRS Scoring Engineering Chain
```

## Description

MRS Open Benchmark 是 Moodify 的真实度评分节点，用于评估 AI 音乐处理前后的真实感、稳定性和可解释性。

## Node Goal

建立一套可复现、可公开讨论、可被下游报告系统解析的评分基准。

## Included AEPs

| AEP | 状态 | 角色 |
|---|---|---|
| `AEP-MOODIFY-MRS-FORMULA-001` | DRAFT | 定义 MRS 公式 |
| `AEP-MOODIFY-MRS-VALIDATION-001` | DRAFT | 验证样本集评分 |
| `AEP-MOODIFY-MRS-FIELD-STANDARD-001` | DRAFT | 标准化报告字段 |
| `AEP-MOODIFY-MRS-PUBLISH-001` | DRAFT | 发布 benchmark 文档 |

## Current Stage

```yaml
label: experimental
description: formula and report shape are still being validated
```

## Maturity Level

```yaml
current: BASIC
target: STABLE
criteria:
  - stable scoring fields
  - reproducible sample set
  - documented benchmark reports
  - no silent sample failure
```

## Interfaces

```yaml
provides:
  - name: mrs_score
    description: score and explanation for one audio sample
    version: 0.1.0
  - name: mrs_report
    description: JSON and Markdown report for a sample set
    version: 0.1.0
requires:
  - name: audio_sample_set
    description: baseline and processed audio samples
    version_or_constraint: fixed hash list
```

## Metrics

| 指标 | 定义 | 目标 |
|---|---|---|
| score_reproducibility | 同一输入重复评分偏差 | <= configured threshold |
| field_completeness | 报告字段完整率 | 100% |
| sample_failure_visibility | 异常样本显式记录率 | 100% |

## Gate History

| Gate | 结果 | 证据 |
|---|---|---|
| `GATE-MRS-BASIC-001` | HOLD | 等待公式和样本集固定 |

## PoEW Records

| PoEW | 摘要 |
|---|---|
| pending | first validation run not yet recorded |

## Risks

- 指标解释不足，导致分数无法指导工程改进。
- 样本集偏小或偏单一。
- 报告字段变化频繁，破坏下游集成。

## Roadmap

| 阶段 | 目标 | AEP |
|---|---|---|
| v0.1 | 基础评分与报告 | formula, validation |
| v0.3 | 稳定 benchmark | regression, field standard |
| v1.0 | 对外发布 | public docs, release gate |

## Next Upgrade Direction

优先固定 MRS 报告字段和样本集 hash，使评分结果可复现、可比较、可被其他 NEM 消费。
