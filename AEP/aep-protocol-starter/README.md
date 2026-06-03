# AEP Protocol Starter

**AEP = AI Engineering Package**  
中文名：**AI 工程包协议**

AEP 是一种面向 AI 协作时代的标准化工程工作单元协议。它不重新发明压缩算法，而是在 ZIP / 文件夹之上定义一套可被人、AI、脚本共同读取的工程任务封装结构。

一个 AEP 包应该让任何一台电脑、任何一个 AI、任何一个协作者在打开后都能知道：

- 要做什么；
- 不要做什么；
- 输入在哪里；
- 输出到哪里；
- 按什么顺序执行；
- 怎样算成功；
- 怎样算失败；
- 如何生成可追踪的工程工作量证明（PoEW, Proof of Engineering Work）。

## 当前仓库状态

这是 AEP 协议的初始 GitHub 项目骨架，适合继续开发为独立开源项目。

仓库包含：

```text
.
├── README.md
├── docs/
│   ├── AEP_Standard_v0.1.md
│   └── AEP_Standard_v0.1.pdf
├── src/aep/
│   ├── cli.py
│   ├── validator.py
│   └── __init__.py
├── schemas/
│   ├── manifest.schema.json
│   ├── task_map.schema.json
│   └── validation_rules.schema.json
├── templates/basic_aep/
├── examples/MT-001_Runtime_Cloud_System_AEP_v0.1/
├── tests/
└── pyproject.toml
```

## 快速开始

### 1. 安装开发环境

```bash
cd aep-protocol-starter
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

pip install -e .[dev]
```

### 2. 验证示例 AEP 包

```bash
aep validate examples/MT-001_Runtime_Cloud_System_AEP_v0.1
```

或者不安装，直接运行：

```bash
PYTHONPATH=src python -m aep.cli validate examples/MT-001_Runtime_Cloud_System_AEP_v0.1
```

### 3. 查看 AEP 包信息

```bash
aep inspect examples/MT-001_Runtime_Cloud_System_AEP_v0.1
```

### 4. 创建新的 AEP 包

```bash
aep new ./work/My_First_AEP --id AEP-001 --name "My First AI Engineering Package"
```

### 5. 打包为 ZIP

```bash
aep pack examples/MT-001_Runtime_Cloud_System_AEP_v0.1 -o MT-001_Runtime_Cloud_System_AEP_v0.1.zip
```

## AEP 与 ZIP 的关系

AEP 不是要取代 ZIP。AEP 是工程协议，ZIP 是物理容器。

```text
AEP = ZIP + 标准目录结构 + manifest.json + agent_spec.md
    + task_map.yaml + validation_rules.yaml + reports
```

未来 `.aep` 可以像 `.docx` 一样，本质上仍然是 ZIP，但内部具有标准结构。

## 最小 AEP 目录结构

```text
AEP_PACKAGE/
├── 00_START_HERE.md
├── manifest.json
├── human_brief.md
├── agent_spec.md
├── rules.md
├── task_map.yaml
├── tasks/
├── validation/
│   ├── acceptance_criteria.md
│   └── validation_rules.yaml
├── outputs/
├── reports/
└── changelog.md
```

## 命令行工具

当前 CLI 提供四个基础命令：

```bash
aep validate <path>   # 校验 AEP 文件夹或 zip 包结构
aep inspect <path>    # 查看包信息
aep new <target>      # 从模板创建新 AEP 包
aep pack <folder>     # 将 AEP 文件夹打包为 zip
```

## 项目路线图

- v0.1：协议文档 + 标准目录 + 基础校验器；
- v0.2：增强 JSON Schema 校验、任务状态机、报告模板；
- v0.3：AEP Runner，按 task_map 执行任务；
- v0.4：PoEW 工程工作量证明规范；
- v1.0：稳定的 AI 任务外包基础协议。

## 许可证

本仓库默认采用 MIT License。你可以根据后续商业化和开源策略调整。
