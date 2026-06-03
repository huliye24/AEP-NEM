# Terminology

## AEP

**Atomic Engineering Package**，工程原子包。

AEP 是可分发的最小工程任务包协议。它应该足够小，能被 AI 或人类稳定执行；也应该足够完整，能独立说明上下文、目标、输入、输出、验收方式、交付证据和回传要求。

## NEM

**Node Evolution Molecule**，节点进化分子。

NEM 是由多个 AEP 组成并持续进化的项目节点协议。它通常对应一个模块、一条能力线、一个子系统或一个可持续升级的工程对象。

## E-Chain

**Engineering Chain**，工程链。

E-Chain 是多个 NEM 形成的主线或支线工程路径。例如 Runtime 工程链、MRS 评分工程链、Electron 桌面端工程链。

## E-Organism

**Engineering Organism**，工程生命体。

E-Organism 是由多条 E-Chain 共同组成的完整工程系统。它强调项目不是单个仓库或脚本，而是一个持续演化的工程生命体。

## E-Mesh

**Engineering Mesh**，工程网格。

E-Mesh 是多个 E-Organism 之间通过开放协议互相引用、验证、分叉和合并形成的网络。

## PoEW

**Proof of Engineering Work**，工程工作量证明。

PoEW 是工程成果的证据记录，可以包括 commit、测试日志、运行结果、报告、benchmark、生成文件、代码 diff、实验记录和用户可验证输出。

## Gate

**Evolution Gate**，进化闸门。

Gate 是判断 AEP 或 NEM 是否可以进入下一阶段的机制。Gate 不只检查“有没有完成”，也检查“是否值得采纳”。

## Status

AEP 推荐状态：

```text
DRAFT
READY
IN_PROGRESS
BLOCKED
REVIEW
ADOPTED
REJECTED
ARCHIVED
```

NEM 推荐状态：

```text
CONCEPT
EXPERIMENTAL
HOLD
ADOPT
STABLE
RELEASED
DEPRECATED
```

Gate 推荐状态：

```text
PASS
FAIL
HOLD
NEEDS_REVIEW
```
