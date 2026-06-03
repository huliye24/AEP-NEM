# Moodify Application

Moodify 可以作为 AEP-NEM 的第一个应用示例。

在这个语境中，Moodify 是一个 AI 音乐二次处理项目：目标是让 AI 音乐从虚拟声波逐渐接近真实声波，并通过评分、处理、报告和桌面端工具形成持续演化的工程系统。

## Moodify 可建模为 E-Organism

Moodify 不是单个脚本或单个应用，而是由多条工程链组成的工程生命体。

可能的 E-Chain：

- Runtime 音频处理工程链
- MRS 真实度评分工程链
- Preset 声音工艺库工程链
- 样本资产库工程链
- 报告与可解释性工程链
- Electron 桌面端工程链
- 潮汐循环工程链
- GitHub 发布工程链

## 示例 NEM

### NEM: MRS Open Benchmark

目标：建立公开、可复现、可解释的音乐真实度评分节点。

可能包含的 AEP：

```text
AEP: MRS 公式定义
AEP: MRS v0.3.1 验证实验
AEP: MRS 命名修正
AEP: MRS 报告字段标准化
AEP: MRS 与 Night Worker 集成
AEP: MRS GitHub 文档发布
```

### NEM: Electron Desktop App

目标：建立可用的桌面端操作界面，支持导入音频、选择 preset、调用 runtime、展示 MRS 结果并导出处理后的音频。

可能包含的 AEP：

```text
AEP: Electron 项目骨架
AEP: 音频导入界面
AEP: Preset 选择界面
AEP: 后端 Runtime 调用
AEP: MRS 结果展示
AEP: 音频导出功能
AEP: GitHub Release 打包
```

## 本仓库示例

示例文件位于 [../../examples/moodify](../../examples/moodify)：

- `aep_example_runtime_smoke_test.md`
- `aep_example_mrs_validation.md`
- `nem_example_mrs_open_benchmark.md`
- `nem_example_electron_desktop_app.md`

这些示例不要求 Moodify 已经完成全部功能，它们的作用是展示如何把一个真实项目拆成 AEP 和 NEM。
