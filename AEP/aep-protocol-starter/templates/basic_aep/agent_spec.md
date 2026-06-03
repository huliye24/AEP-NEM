# Agent Spec — {{PACKAGE_NAME}}

## 1. Task Definition

This AEP package asks the executor to complete a bounded engineering task.

## 2. Scope

### In Scope

- Read the package files.
- Execute tasks listed in `task_map.yaml`.
- Write outputs to `outputs/` and reports to `reports/`.

### Out of Scope

- Do not modify unrelated project files.
- Do not delete input data.
- Do not skip validation.

## 3. Inputs

See `inputs/README.md` if present.

## 4. Outputs

All outputs must go to `outputs/` or `reports/`.

## 5. Completion

Completion requires passing the acceptance criteria under `validation/`.
