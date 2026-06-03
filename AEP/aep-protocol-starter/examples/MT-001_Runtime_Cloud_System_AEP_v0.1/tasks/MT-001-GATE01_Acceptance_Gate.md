# MT-001-GATE01 — Runtime Acceptance Gate

## Goal

Decide whether MT-001 enters PASS, HOLD, or FAIL.

## Required Reports

- `reports/node_protocol.md`
- `reports/structure_check.md`
- `reports/final_report.md`

## Decision Rule

- PASS: all required reports exist and no critical structure errors.
- HOLD: reports are incomplete but package is recoverable.
- FAIL: package cannot be executed or validation is impossible.
