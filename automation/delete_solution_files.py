# delete_solution_files.py
import argparse
from pathlib import Path

SEPARATOR_LINE = "-------------------"

def parse_report(report_path: Path) -> list[Path]:
    lines = report_path.read_text(encoding="utf-8").splitlines()
    dirs = []
    capture = False
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("Directories containing solution.py"):
            capture = True
            continue
        if capture:
            if line.startswith(SEPARATOR_LINE):
                break
            # Normalize Windows-style backslashes to Path format
            dirs.append(Path(line.replace("\\", "/")))
    return dirs

def delete_solution_files(repo_root: Path, dirs: list[Path]) -> tuple[int, int]:
    deleted = 0
    missing = 0
    repo_root = repo_root.resolve()

    for rel_dir in dirs:
        target = (repo_root / rel_dir / "solution.py").resolve()
        # Safety: ensure we never step outside the repo_root
        try:
            target.relative_to(repo_root)
        except ValueError:
            print(f"[SKIP] Outside repo root: {target}")
            continue

        if target.exists():
            try:
                target.unlink()
                deleted += 1
                print(f"[OK] Deleted: {target}")
            except PermissionError:
                print(f"[ERR] Permission denied: {target}")
            except OSError as e:
                print(f"[ERR] Could not delete {target}: {e}")
        else:
            missing += 1
            print(f"[MISS] Not found: {target}")
    return deleted, missing

def main():
    ap = argparse.ArgumentParser(description="Delete solution.py files listed in report.txt")
    ap.add_argument("--report", type=Path, default=Path("report.txt"),
                    help="Path to report.txt (default: report.txt)")
    ap.add_argument("--repo-root", type=Path, default=Path("."),
                    help="Path to the repository root containing the listed folders (default: .)")
    args = ap.parse_args()

    if not args.report.exists():
        raise SystemExit(f"report file not found: {args.report}")

    dirs = parse_report(args.report)
    if not dirs:
        raise SystemExit("No directories parsed from report.txt. Check the header/separator formatting.")

    deleted, missing = delete_solution_files(args.repo_root, dirs)
    print(f"\nSummary: deleted={deleted}, missing={missing}, total_listed={len(dirs)}")

if __name__ == "__main__":
    main()
