# NEM Example: Electron Desktop App

```yaml
nem_id: NEM-MOODIFY-ELECTRON-DESKTOP
title: Electron Desktop App
status: CONCEPT
version: 0.1.0
created_at: 2026-06-03
updated_at: 2026-06-03
owner: moodify-desktop
related_chain: Electron Desktop Engineering Chain
```

## Description

Electron Desktop App 是 Moodify 的桌面端工程节点，用于把音频导入、preset 选择、Runtime 调用、MRS 结果展示和音频导出组织成一个可用工作流。

## Node Goal

让非命令行用户可以完成一次完整的 Moodify 音频处理流程，并看到可解释的评分结果。

## Included AEPs

| AEP | 状态 | 角色 |
|---|---|---|
| `AEP-MOODIFY-ELECTRON-SHELL-001` | DRAFT | 建立 Electron 项目骨架 |
| `AEP-MOODIFY-AUDIO-IMPORT-001` | DRAFT | 音频导入界面 |
| `AEP-MOODIFY-PRESET-SELECT-001` | DRAFT | Preset 选择界面 |
| `AEP-MOODIFY-RUNTIME-BRIDGE-001` | DRAFT | 调用后端 Runtime |
| `AEP-MOODIFY-MRS-VIEW-001` | DRAFT | 展示 MRS 结果 |
| `AEP-MOODIFY-AUDIO-EXPORT-001` | DRAFT | 导出处理后音频 |
| `AEP-MOODIFY-RELEASE-PACKAGING-001` | DRAFT | GitHub Release 打包 |

## Current Stage

```yaml
label: concept
description: workflow and interface boundaries are being defined
```

## Maturity Level

```yaml
current: BASIC
target: ADOPT
criteria:
  - import-process-export flow works locally
  - runtime failures are visible to the user
  - MRS result fields render correctly
  - packaged build can be installed and launched
```

## Interfaces

```yaml
provides:
  - name: desktop_workflow
    description: import, process, score, export audio
    version: 0.1.0
requires:
  - name: moodify_runtime
    description: backend processing command or API
    version_or_constraint: ">=0.1.0"
  - name: mrs_report
    description: report fields produced by MRS NEM
    version_or_constraint: ">=0.1.0"
```

## Inputs

- Local audio files.
- Preset definitions.
- Runtime executable or API endpoint.
- MRS report JSON.

## Outputs

- Processed audio file.
- Runtime log surfaced to UI.
- MRS score and explanation view.
- Release package.

## Metrics

| 指标 | 定义 | 目标 |
|---|---|---|
| workflow_completion | 用户完成导入到导出的比例 | >= target in testing |
| runtime_error_visibility | Runtime 错误可见性 | 100% |
| package_launch_success | 安装包启动成功率 | 100% in smoke test |

## Gate History

| Gate | 结果 | 证据 |
|---|---|---|
| `GATE-ELECTRON-CONCEPT-001` | NEEDS_REVIEW | 需要确认 Runtime 接口 |

## PoEW Records

| PoEW | 摘要 |
|---|---|
| pending | desktop skeleton not yet executed |

## Risks

- Runtime 接口频繁变化导致桌面端桥接不稳定。
- UI 过早复杂化，拖慢基础工作流验证。
- 打包流程和系统权限问题影响发布。

## Roadmap

| 阶段 | 目标 | AEP |
|---|---|---|
| v0.1 | 最小桌面骨架 | shell, import |
| v0.2 | Runtime 调用闭环 | preset, runtime bridge |
| v0.3 | MRS 展示与导出 | mrs view, export |
| v1.0 | 可发布桌面端 | release packaging |

## Next Upgrade Direction

先固定 Runtime 调用接口，再实现最小导入-处理-导出闭环。桌面端不应早于 Runtime 和 MRS 的基础 Gate。
