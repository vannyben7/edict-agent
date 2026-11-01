#!/usr/bin/env python3
"""Safely inspect or install Edict's optional project-local Qoder Agents."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile


EXPECTED_FILES = (
    "edict-explorer.md",
    "edict-worker.md",
    "edict-reviewer.md",
    "edict-verifier.md",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Inspect or install the optional fixed-name Edict Agents in one "
            "project. This tool never writes to the user-global Qoder directory."
        )
    )
    parser.add_argument("command", choices=("install", "status"))
    parser.add_argument(
        "--project-root",
        default=".",
        help="Existing project directory (default: current directory)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace only conflicting Edict files after explicit authorization",
    )
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    return parser.parse_args()


def paths(project_root: str) -> tuple[Path, Path]:
    root = Path(project_root).expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"project root is not an existing directory: {root}")
    templates = Path(__file__).resolve().parents[1] / "assets" / "project-agent-templates"
    missing = [
        name
        for name in EXPECTED_FILES
        if not (templates / name).is_file() or (templates / name).is_symlink()
    ]
    if missing:
        raise ValueError(f"packaged templates are incomplete: {', '.join(missing)}")
    qoder_dir = root / ".qoder"
    target = qoder_dir / "agents"
    if qoder_dir.is_symlink():
        raise ValueError(f"refusing a symlinked Qoder directory: {qoder_dir}")
    if target.is_symlink():
        raise ValueError(f"refusing a symlinked Agent directory: {target}")
    return templates, target


def inspect(templates: Path, target: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for name in EXPECTED_FILES:
        destination = target / name
        if destination.is_symlink():
            result[name] = "conflict"
        elif not destination.exists():
            result[name] = "missing"
        elif not destination.is_file():
            result[name] = "conflict"
        elif destination.read_bytes() == (templates / name).read_bytes():
            result[name] = "matching"
        else:
            result[name] = "different"
    return result


def atomic_copy(source: Path, destination: Path) -> None:
    handle, temp_name = tempfile.mkstemp(prefix=f".{destination.name}.", dir=destination.parent)
    os.close(handle)
    temp_path = Path(temp_name)
    try:
        shutil.copy2(source, temp_path)
        os.replace(temp_path, destination)
    finally:
        if temp_path.exists():
            temp_path.unlink()


def install(templates: Path, target: Path, force: bool) -> dict[str, str]:
    before = inspect(templates, target)
    unsafe = [name for name, state in before.items() if state == "conflict"]
    if unsafe:
        joined = ", ".join(unsafe)
        raise RuntimeError(f"refusing unsafe non-regular project files: {joined}")
    different = [name for name, state in before.items() if state == "different"]
    if different and not force:
        joined = ", ".join(different)
        raise RuntimeError(
            f"refusing to overwrite different project files: {joined}; "
            "inspect them first and use --force only with explicit authorization"
        )

    target.mkdir(parents=True, exist_ok=True)
    result: dict[str, str] = {}
    for name, state in before.items():
        if state == "matching":
            result[name] = "unchanged"
            continue
        atomic_copy(templates / name, target / name)
        result[name] = "replaced" if state == "different" else "installed"
    return result


def emit(command: str, target: Path, files: dict[str, str], as_json: bool) -> None:
    payload = {"command": command, "scope": "project", "target": str(target), "files": files}
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
        return
    print(f"scope: project\ntarget: {target}")
    for name, state in files.items():
        print(f"{state:>9}  {name}")


def main() -> int:
    args = parse_args()
    try:
        templates, target = paths(args.project_root)
        if args.command == "status":
            result = inspect(templates, target)
        else:
            result = install(templates, target, args.force)
        emit(args.command, target, result, args.json)
        return 0
    except (OSError, RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
