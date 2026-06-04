#!/usr/bin/env python3
# Simple AEP Seal Report JSON validator.
#
# Usage:
#     python tools/validate_seal_report.py path/to/seal_report.json
#
# This script validates a JSON seal report against schemas/seal_report.schema.json.
# If jsonschema is not installed, it performs a minimal required-field check.

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_FIELDS = [
    "seal_id",
    "aep_id",
    "status",
    "function_complete",
    "poew_reference",
    "gate_reference",
    "evidence_bundle",
    "test_summary",
    "artifact_summary",
    "risk_summary",
    "downstream_dependency_note",
    "reopen_criteria",
    "seal_decision",
    "timestamp",
]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def minimal_validate(data: dict) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")

    status = data.get("status")
    allowed_status = {"HOLD", "PASS", "PASS_WITH_LIMITATIONS", "REOPEN_REQUIRED", "REJECTED"}
    if status is not None and status not in allowed_status:
        errors.append(f"Invalid status: {status}")

    if not isinstance(data.get("function_complete"), bool):
        errors.append("function_complete must be boolean")

    decision = data.get("seal_decision", {})
    if isinstance(decision, dict):
        allowed_decision = {"PASS", "PASS_WITH_LIMITATIONS", "HOLD", "REOPEN_REQUIRED", "REJECTED"}
        if decision.get("decision") not in allowed_decision:
            errors.append(f"Invalid seal_decision.decision: {decision.get('decision')}")
    else:
        errors.append("seal_decision must be an object")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/validate_seal_report.py path/to/seal_report.json")
        return 2

    report_path = Path(sys.argv[1]).resolve()
    if not report_path.exists():
        print(f"Report file not found: {report_path}")
        return 2

    data = load_json(report_path)

    schema_path = Path(__file__).resolve().parents[1] / "schemas" / "seal_report.schema.json"

    try:
        import jsonschema  # type: ignore
        schema = load_json(schema_path)
        jsonschema.validate(instance=data, schema=schema)
        print("PASS: Seal report is valid against JSON Schema.")
        return 0
    except ModuleNotFoundError:
        errors = minimal_validate(data)
        if errors:
            print("FAIL: Minimal validation failed:")
            for err in errors:
                print(f" - {err}")
            return 1
        print("PASS: Minimal validation passed. Install jsonschema for full validation.")
        return 0
    except Exception as exc:
        print(f"FAIL: Schema validation failed: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
