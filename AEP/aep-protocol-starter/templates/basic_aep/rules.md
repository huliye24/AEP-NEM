# AEP Execution Rules

The executor must follow these rules:

- Do not delete original input data.
- Do not modify files outside the package unless explicitly allowed.
- Do not run destructive commands.
- Do not skip validation.
- Do not claim completion without generating required outputs.
- If blocked, write a clear report under `reports/`.
