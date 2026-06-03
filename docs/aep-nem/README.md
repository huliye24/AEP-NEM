# AEP-NEM Engineering System

AEP-NEM Engineering System 是一套面向 AI 原生工程时代的任务组织、工程协作与项目进化协议。

它不是任务管理工具，也不是 Todo List。它定义的是一组可读、可执行、可验证、可复用的工程语言，用来帮助 AI、人类开发者、研究者和产品设计者围绕同一个项目持续协作。

## 核心目标

- 把复杂工程拆成可执行的最小工程单元。
- 让每个工程单元都有明确输入、输出、验收标准和证据。
- 让多个工程单元组合成可持续进化的工程节点。
- 通过 Gate 和 PoEW 记录工程成果是否真实有效。
- 支持多中心发布、验证、分叉、合并和升级。

## 层级结构

```text
AEP
  -> NEM
    -> E-Chain
      -> E-Organism
        -> E-Mesh
```

| 层级 | 英文名 | 中文名 | 作用 |
|---|---|---|---|
| AEP | Atomic Engineering Package | 工程原子包 | 可分发的最小工程任务包协议 |
| NEM | Node Evolution Molecule | 节点进化分子 | 由多个 AEP 组成并持续进化的项目节点协议 |
| E-Chain | Engineering Chain | 工程链 | 多个 NEM 形成的主线或支线工程路径 |
| E-Organism | Engineering Organism | 工程生命体 | 多条工程链组成的完整项目 |
| E-Mesh | Engineering Mesh | 工程网格 | 多个工程生命体连接形成的开放网络 |

## 第一阶段内容

本目录提供 AEP-NEM 的中文协议入口和可复用模板：

- [protocol_overview.md](protocol_overview.md): 协议总览
- [terminology.md](terminology.md): 核心术语
- [aep_template.md](aep_template.md): AEP 模板
- [aep_task_package_template.md](aep_task_package_template.md): 可分发 AEP 任务包模板
- [aep_lifecycle.md](aep_lifecycle.md): AEP 生命周期
- [aep_return_package_standard.md](aep_return_package_standard.md): AEP 回传包标准
- [nem_template.md](nem_template.md): NEM 模板
- [nem_rules.md](nem_rules.md): NEM 节点规则
- [gate_standard.md](gate_standard.md): Gate 标准
- [poew_standard.md](poew_standard.md): PoEW 标准
- [decentralized_design_principles.md](decentralized_design_principles.md): 去中心化设计原则
- [moodify_application.md](moodify_application.md): Moodify 应用方式

## 使用建议

1. 先用 AEP 任务包模板描述一个可分发、可执行、可回传的最小任务。
2. 为每个 AEP 定义明确的验收标准和 PoEW 证据。
3. 将一组相关 AEP 组合为 NEM。
4. 用 Gate 判断 AEP 是否可被 NEM 采纳。
5. 用 NEM 的 roadmap 描述后续升级方向。

第一阶段不需要 Web 平台。一个 Markdown 文档、一个 JSON Schema 和一组可复用示例，就足以让协议开始被真实项目使用。
