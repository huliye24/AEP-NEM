# Agent Spec — MT-001 Runtime Cloud System

## Node Definition

Runtime is the cloud engineering engine of Moodify. It should support repeatable execution, logs, summaries, failure classification, resume behavior, and validation.

## In Scope

- Define the Runtime node protocol.
- Run baseline structure checks.
- Generate a final report.
- Decide whether the node can move to the next stage.

## Out of Scope

- Do not modify MRS formula.
- Do not change audio processing presets.
- Do not build UI.
- Do not perform commercial packaging.

## Outputs

- `reports/node_protocol.md`
- `reports/final_report.md`
- `outputs/result_summary.json`

## Stop Conditions

- Required files are missing.
- Runtime commands are unknown.
- Outputs cannot be written.
- Safety rules are violated.
