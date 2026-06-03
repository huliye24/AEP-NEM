# PoEW Standard

PoEW 是 Proof of Engineering Work，即工程工作量证明。

PoEW 的目的不是记录“谁说自己做了什么”，而是记录“哪些可验证证据证明工程成果已经产生”。

## PoEW 可以包含什么

- Git commit 或代码 diff。
- 测试日志、构建日志、运行日志。
- 生成文件、报告、截图、音频样本或 benchmark 结果。
- Schema 校验结果。
- 手动验收记录。
- Gate 判断结果。
- 输入输出 hash 或可复现实验说明。

## PoEW 记录模板

```yaml
poew_id:
date:
target_type:
target_id:
target_version:

executor:
  type:
  name:
  environment:

work_summary:
  objective:
  completed_steps:
  changed_files:

evidence:
  - type:
    path_or_ref:
    description:
    hash:

validation:
  method:
  command:
  result:
  log_path:

gate_results:
  - gate_id:
    result:
    evidence:

reproducibility:
  input_refs:
  output_refs:
  notes:

limitations:
  - item:
```

## 证据等级

| 等级 | 说明 |
|---|---|
| L0 | 只有文字说明，没有交付证据 |
| L1 | 有交付文件，但缺少验证 |
| L2 | 有交付文件和人工验收 |
| L3 | 有自动化测试、日志或可重复命令 |
| L4 | 有可复现实验、hash、版本和完整 Gate 记录 |

第一阶段建议至少达到 L2；涉及代码、模型、音频处理或发布流程的 AEP 应尽量达到 L3。

## 非目标

- PoEW 不是加密货币。
- PoEW 不要求区块链。
- PoEW 不要求中心化服务器。
- PoEW 不替代人工判断，而是为判断提供证据。
