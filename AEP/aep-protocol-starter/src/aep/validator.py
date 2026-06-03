from __future__ import annotations

import json
import tempfile
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


REQUIRED_FILES = [
    "00_START_HERE.md",
    "manifest.json",
    "human_brief.md",
    "agent_spec.md",
    "rules.md",
    "task_map.yaml",
    "validation/acceptance_criteria.md",
    "validation/validation_rules.yaml",
    "changelog.md",
]

REQUIRED_DIRS = [
    "tasks",
    "validation",
    "outputs",
    "reports",
]

REQUIRED_MANIFEST_FIELDS = [
    "format",
    "format_version",
    "package_id",
    "package_name",
    "status",
    "entry_file",
    "agent_spec",
    "task_map",
    "validation",
    "output_dir",
    "report_dir",
]

VALID_PACKAGE_STATUSES = {
    "DRAFT",
    "READY",
    "ACTIVE",
    "HOLD",
    "PARTIAL",
    "PASS",
    "FAIL",
    "ADOPT",
    "ARCHIVED",
}

VALID_TASK_STATUSES = {
    "TODO",
    "READY",
    "RUNNING",
    "PASS",
    "FAIL",
    "BLOCKED",
    "SKIPPED",
    "RETRY",
    "DONE",
}


@dataclass
class ValidationIssue:
    level: str  # ERROR / WARNING
    message: str


@dataclass
class ValidationResult:
    path: Path
    ok: bool
    issues: list[ValidationIssue] = field(default_factory=list)
    manifest: dict[str, Any] | None = None
    task_map: dict[str, Any] | None = None

    @property
    def errors(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.level == "ERROR"]

    @property
    def warnings(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.level == "WARNING"]

    def to_dict(self) -> dict[str, Any]:
        return {
            "path": str(self.path),
            "ok": self.ok,
            "errors": [i.message for i in self.errors],
            "warnings": [i.message for i in self.warnings],
            "manifest": self.manifest,
        }


def _load_json(path: Path, issues: list[ValidationIssue]) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        issues.append(ValidationIssue("ERROR", f"Cannot parse JSON: {path}: {exc}"))
        return None


def _load_yaml(path: Path, issues: list[ValidationIssue]) -> dict[str, Any] | None:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if data is None:
            return {}
        if not isinstance(data, dict):
            issues.append(ValidationIssue("ERROR", f"YAML root must be an object: {path}"))
            return None
        return data
    except Exception as exc:  # noqa: BLE001
        issues.append(ValidationIssue("ERROR", f"Cannot parse YAML: {path}: {exc}"))
        return None


def _validate_folder(folder: Path) -> ValidationResult:
    issues: list[ValidationIssue] = []
    folder = folder.resolve()

    if not folder.exists():
        return ValidationResult(folder, False, [ValidationIssue("ERROR", "Path does not exist")])
    if not folder.is_dir():
        return ValidationResult(folder, False, [ValidationIssue("ERROR", "Path is not a directory")])

    for rel in REQUIRED_FILES:
        if not (folder / rel).is_file():
            issues.append(ValidationIssue("ERROR", f"Missing required file: {rel}"))

    for rel in REQUIRED_DIRS:
        if not (folder / rel).is_dir():
            issues.append(ValidationIssue("ERROR", f"Missing required directory: {rel}/"))

    manifest = None
    manifest_path = folder / "manifest.json"
    if manifest_path.exists():
        manifest = _load_json(manifest_path, issues)
        if manifest:
            _validate_manifest(manifest, issues)

    task_map = None
    task_map_path = folder / "task_map.yaml"
    if task_map_path.exists():
        task_map = _load_yaml(task_map_path, issues)
        if task_map:
            _validate_task_map(task_map, folder, issues)

    validation_rules_path = folder / "validation" / "validation_rules.yaml"
    if validation_rules_path.exists():
        validation_rules = _load_yaml(validation_rules_path, issues)
        if validation_rules is not None:
            _validate_validation_rules(validation_rules, issues)

    ok = len([i for i in issues if i.level == "ERROR"]) == 0
    return ValidationResult(folder, ok, issues, manifest, task_map)


def _validate_manifest(manifest: dict[str, Any], issues: list[ValidationIssue]) -> None:
    for field_name in REQUIRED_MANIFEST_FIELDS:
        if field_name not in manifest:
            issues.append(ValidationIssue("ERROR", f"manifest.json missing field: {field_name}"))

    if manifest.get("format") != "AEP":
        issues.append(ValidationIssue("ERROR", "manifest.format must be 'AEP'"))

    status = manifest.get("status")
    if status and status not in VALID_PACKAGE_STATUSES:
        issues.append(
            ValidationIssue(
                "ERROR",
                f"manifest.status '{status}' is invalid. Expected one of: {sorted(VALID_PACKAGE_STATUSES)}",
            )
        )


def _validate_task_map(task_map: dict[str, Any], folder: Path, issues: list[ValidationIssue]) -> None:
    tasks = task_map.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        issues.append(ValidationIssue("ERROR", "task_map.yaml must contain a non-empty tasks list"))
        return

    ids: set[str] = set()
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            issues.append(ValidationIssue("ERROR", f"tasks[{index}] must be an object"))
            continue
        task_id = task.get("id")
        if not task_id:
            issues.append(ValidationIssue("ERROR", f"tasks[{index}] missing id"))
            continue
        if task_id in ids:
            issues.append(ValidationIssue("ERROR", f"Duplicate task id: {task_id}"))
        ids.add(task_id)

        for field_name in ["name", "type", "priority", "status"]:
            if field_name not in task:
                issues.append(ValidationIssue("ERROR", f"Task {task_id} missing field: {field_name}"))

        status = task.get("status")
        if status and status not in VALID_TASK_STATUSES:
            issues.append(ValidationIssue("ERROR", f"Task {task_id} has invalid status: {status}"))

        task_file = task.get("file")
        if task_file and not (folder / task_file).is_file():
            issues.append(ValidationIssue("ERROR", f"Task {task_id} points to missing file: {task_file}"))

    for task in tasks:
        depends_on = task.get("depends_on", [])
        if depends_on is None:
            depends_on = []
        if not isinstance(depends_on, list):
            issues.append(ValidationIssue("ERROR", f"Task {task.get('id')} depends_on must be a list"))
            continue
        for dep in depends_on:
            if dep not in ids:
                issues.append(ValidationIssue("ERROR", f"Task {task.get('id')} depends on unknown task: {dep}"))


def _validate_validation_rules(rules: dict[str, Any], issues: list[ValidationIssue]) -> None:
    if "acceptance" not in rules:
        issues.append(ValidationIssue("ERROR", "validation_rules.yaml missing acceptance section"))
        return
    acceptance = rules.get("acceptance")
    if not isinstance(acceptance, dict):
        issues.append(ValidationIssue("ERROR", "validation_rules.acceptance must be an object"))
        return
    if "required_outputs" not in acceptance:
        issues.append(ValidationIssue("WARNING", "acceptance.required_outputs is not defined"))
    if "pass_conditions" not in acceptance:
        issues.append(ValidationIssue("WARNING", "acceptance.pass_conditions is not defined"))
    if "fail_conditions" not in acceptance:
        issues.append(ValidationIssue("WARNING", "acceptance.fail_conditions is not defined"))


def validate_aep(path: str | Path) -> ValidationResult:
    """Validate an AEP folder or zip package."""
    path = Path(path)
    if path.is_file() and path.suffix.lower() in {".zip", ".aep"}:
        with tempfile.TemporaryDirectory(prefix="aep_validate_") as td:
            with zipfile.ZipFile(path, "r") as zf:
                zf.extractall(td)
            extracted = Path(td)
            children = [p for p in extracted.iterdir() if p.is_dir()]
            folder = children[0] if len(children) == 1 else extracted
            result = _validate_folder(folder)
            result.path = path.resolve()
            return result
    return _validate_folder(path)


def inspect_aep(path: str | Path) -> dict[str, Any]:
    result = validate_aep(path)
    manifest = result.manifest or {}
    task_count = 0
    if result.task_map and isinstance(result.task_map.get("tasks"), list):
        task_count = len(result.task_map["tasks"])
    return {
        "ok": result.ok,
        "package_id": manifest.get("package_id"),
        "package_name": manifest.get("package_name"),
        "format_version": manifest.get("format_version"),
        "status": manifest.get("status"),
        "task_count": task_count,
        "errors": [i.message for i in result.errors],
        "warnings": [i.message for i in result.warnings],
    }
