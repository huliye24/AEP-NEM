# AEP Example: Runtime Smoke Test

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
```

## Context

Moodify 的 Runtime 负责执行音频二次处理。任何 preset、MRS 或桌面端能力都依赖 Runtime 能稳定完成一次最小处理流程。

本 AEP 只验证 Runtime 是否能完成 smoke test，不评估最终音质。

## Objective

用一个短音频样本执行一次最小处理流程，并产出可检查的输出文件、运行日志和基础指标。

## Inputs

| 输入 | 类型 | 说明 |
|---|---|---|
| `samples/smoke/input.wav` | audio | 5-15 秒测试音频 |
| `presets/smoke/default.json` | preset | 最小处理 preset |
| Runtime command | command | 项目当前可用的处理入口 |

## Outputs

| 输出 | 类型 | 验收 |
|---|---|---|
| `outputs/smoke/output.wav` | audio | 文件存在且可被读取 |
| `outputs/smoke/runtime.log` | log | 包含开始、结束和错误状态 |
| `outputs/smoke/metrics.json` | json | 包含 duration、sample_rate、channels |

## Execution Steps

1. 准备 smoke test 输入音频和 preset。
2. 执行 Runtime 最小处理命令。
3. 检查输出音频文件是否生成。
4. 检查日志中是否存在 fatal error。
5. 写入基础 metrics。

## Acceptance Criteria

- 输出音频文件存在且大小大于 0。
- Runtime 进程退出码为 0。
- 日志中没有 `fatal`、`panic` 或未捕获异常。
- `metrics.json` 是合法 JSON。
- 输出音频时长与输入音频时长偏差不超过 5%。

## Validation Method

```yaml
type: automated
command: run runtime smoke test and inspect outputs
manual_review: optional
```

## PoEW Evidence

- Runtime 命令和退出码。
- `outputs/smoke/runtime.log`。
- `outputs/smoke/metrics.json`。
- 输入和输出音频文件 hash。

## Risks

- Runtime 入口尚未统一，导致命令不可复用。
- 测试样本过短，不能暴露真实处理问题。
- preset 格式变化导致 smoke test 失效。

## Rollback Plan

如果 smoke test 失败，不采纳到 Runtime NEM；保留日志并创建后续修复 AEP。

## Next AEP Suggestions

- Runtime batch processing validation
- Runtime preset compatibility check
- Runtime error-report standardization
