from __future__ import annotations

import argparse
import json
import shutil
import sys
import zipfile
from pathlib import Path

from aep.validator import inspect_aep, validate_aep


PROJECT_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_DIR = PROJECT_ROOT / "templates" / "basic_aep"


def cmd_validate(args: argparse.Namespace) -> int:
    result = validate_aep(args.path)
    if args.json:
        print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(f"AEP validation: {result.path}")
        print(f"Status: {'PASS' if result.ok else 'FAIL'}")
        if result.errors:
            print("\nErrors:")
            for issue in result.errors:
                print(f"  - {issue.message}")
        if result.warnings:
            print("\nWarnings:")
            for issue in result.warnings:
                print(f"  - {issue.message}")
    return 0 if result.ok else 1


def cmd_inspect(args: argparse.Namespace) -> int:
    info = inspect_aep(args.path)
    print(json.dumps(info, ensure_ascii=False, indent=2))
    return 0 if info.get("ok") else 1


def _replace_tokens_in_file(path: Path, replacements: dict[str, str]) -> None:
    if not path.is_file():
        return
    if path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".txt"}:
        return
    text = path.read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = text.replace(key, value)
    path.write_text(text, encoding="utf-8")


def cmd_new(args: argparse.Namespace) -> int:
    target = Path(args.target)
    if target.exists() and any(target.iterdir()):
        print(f"Target already exists and is not empty: {target}", file=sys.stderr)
        return 2
    if not TEMPLATE_DIR.exists():
        print(f"Template directory not found: {TEMPLATE_DIR}", file=sys.stderr)
        return 2
    shutil.copytree(TEMPLATE_DIR, target, dirs_exist_ok=True)
    replacements = {
        "{{PACKAGE_ID}}": args.id,
        "{{PACKAGE_NAME}}": args.name,
    }
    for file_path in target.rglob("*"):
        _replace_tokens_in_file(file_path, replacements)
    print(f"Created AEP package: {target}")
    return 0


def cmd_pack(args: argparse.Namespace) -> int:
    folder = Path(args.folder).resolve()
    if not folder.is_dir():
        print(f"Folder not found: {folder}", file=sys.stderr)
        return 2

    result = validate_aep(folder)
    if not result.ok and not args.force:
        print("Refusing to pack invalid AEP package. Use --force to override.", file=sys.stderr)
        for issue in result.errors:
            print(f"  - {issue.message}", file=sys.stderr)
        return 1

    output = Path(args.output) if args.output else folder.with_suffix(".zip")
    output = output.resolve()
    if output.exists():
        output.unlink()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in folder.rglob("*"):
            if path.is_file():
                zf.write(path, arcname=folder.name + "/" + str(path.relative_to(folder)))
    print(f"Packed AEP package: {output}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="aep", description="AEP Protocol CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_validate = sub.add_parser("validate", help="Validate an AEP folder or zip package")
    p_validate.add_argument("path")
    p_validate.add_argument("--json", action="store_true", help="Print JSON result")
    p_validate.set_defaults(func=cmd_validate)

    p_inspect = sub.add_parser("inspect", help="Inspect an AEP package")
    p_inspect.add_argument("path")
    p_inspect.set_defaults(func=cmd_inspect)

    p_new = sub.add_parser("new", help="Create a new AEP package from template")
    p_new.add_argument("target")
    p_new.add_argument("--id", required=True, help="Package ID, e.g. AEP-001")
    p_new.add_argument("--name", required=True, help="Package name")
    p_new.set_defaults(func=cmd_new)

    p_pack = sub.add_parser("pack", help="Pack an AEP folder into a zip file")
    p_pack.add_argument("folder")
    p_pack.add_argument("-o", "--output", help="Output zip path")
    p_pack.add_argument("--force", action="store_true", help="Pack even if validation fails")
    p_pack.set_defaults(func=cmd_pack)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
