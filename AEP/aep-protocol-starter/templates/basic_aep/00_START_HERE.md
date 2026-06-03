# {{PACKAGE_ID}} — {{PACKAGE_NAME}}

You are opening an AEP package.

Read files in this order:

1. `manifest.json`
2. `agent_spec.md`
3. `rules.md`
4. `task_map.yaml`
5. Current task card under `tasks/`
6. `validation/acceptance_criteria.md`
7. `validation/validation_rules.yaml`

Do not start execution before reading `rules.md` and `validation/acceptance_criteria.md`.

All outputs must be written to `outputs/` or `reports/`.
