# AEP Example: MRS Validation

```yaml
aep_id: AEP-MOODIFY-MRS-VALIDATION-001
title: MRS scoring validation against sample set
status: DRAFT
version: 0.1.0
created_at: 2026-06-03
updated_at: 2026-06-03
owner: moodify-mrs
related_nem: NEM-MOODIFY-MRS-OPEN-BENCHMARK
related_chain: MRS Scoring Engineering Chain
priority: high
difficulty: medium
estimated_effort: 1d
```

## Context

MRS 用于衡量 AI 音乐处理结果的真实度和可解释性。MRS 需要一组可复现样本和稳定报告字段，才能成为可被采纳的评分节点。

## Objective

使用一组固定样本验证 MRS 输出是否稳定、字段是否完整、评分是否可解释。

## Inputs

| 输入 | 类型 | 说明 |
|---|---|---|
| `samples/mrs/baseline/` | audio set | 原始或基线样本 |
| `samples/mrs/processed/` | audio set | 处理后样本 |
| `mrs_config.yaml` | config | MRS 评分配置 |

## Outputs

| 输出 | 类型 | 验收 |
|---|---|---|
| `reports/mrs_validation.json` | json | 包含每个样本的评分字段 |
| `reports/mrs_validation.md` | report | 包含解释、异常和结论 |
| `reports/mrs_summary.csv` | table | 可用于横向比较 |

## Execution Steps

1. 固定样本集合和配置版本。
2. 对 baseline 与 processed 样本运行 MRS。
3. 生成 JSON、Markdown 和 CSV 报告。
4. 检查字段完整性和评分范围。
5. 记录异常样本和不可解释结果。

## Acceptance Criteria

- 每个样本都有 MRS 分数和字段级解释。
- 分数范围符合 MRS 定义。
- 报告字段命名稳定且可被下游解析。
- 对同一输入重复运行两次，核心分数偏差不超过预设阈值。
- 异常样本被显式记录，而不是静默跳过。

## Validation Method

```yaml
type: hybrid
command: run MRS validation pipeline
manual_review: review report interpretability
```

## PoEW Evidence

- MRS 运行日志。
- `mrs_config.yaml` 版本。
- 样本清单和 hash。
- `mrs_validation.json`。
- `mrs_validation.md`。
- Gate 评估记录。

## Risks

- 样本集太小，评分代表性不足。
- 指标名变化破坏下游报告系统。
- 人工听感和 MRS 分数存在偏差，需要解释机制。

## Rollback Plan

如果验证失败，MRS NEM 保持 `EXPERIMENTAL`，不进入 `ADOPT` 或 `STABLE`。

## Next AEP Suggestions

- MRS report field standardization
- MRS cross-version regression test
- MRS public benchmark publishing
