# delete_one_solution.py
from pathlib import Path

HEADER = "Directories containing solution.py"

def parse_report(report_path: Path) -> list[Path]:
    lines = report_path.read_text(encoding="utf-8").splitlines()
    dirs, capture = [], False
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        if not capture:
            if line.startswith(HEADER):
                capture = True
            continue
        # After the header, every non-empty line is a path (e.g., "Python\Foo Bar")
        dirs.append(Path(line.replace("\\", "/")))
    return dirs

def delete_first_solution(repo_root: Path, dirs: list[Path]) -> bool:
    repo_root = repo_root.resolve()
    for rel_dir in dirs:
        target = (repo_root / rel_dir / "solution.py").resolve()

        # Safety: ensure target is inside repo_root
        try:
            target.relative_to(repo_root)
        except ValueError:
            print(f"[SKIP] Outside repo root: {target}")
            continue

        if target.exists():
            try:
                target.unlink()
                print(f"[OK] Deleted: {target}")
                return True
            except PermissionError:
                print(f"[ERR] Permission denied: {target}")
                return False
            except OSError as e:
                print(f"[ERR] Could not delete {target}: {e}")
                return False
    print("[DONE] No solution.py found for any listed directory.")
    return False

def main():
    repo_root = Path(".")
    report_path = Path("report.txt")

    if not report_path.exists():
        raise SystemExit("report.txt not found in the current directory.")

    dirs = parse_report(report_path)
    if not dirs:
        raise SystemExit("No directories parsed from report.txt. Check the header line.")

    deleted = delete_first_solution(repo_root, dirs)
    if deleted:
        print("Summary: 1 file deleted.")
    else:
        print("Summary: 0 files deleted.")

if __name__ == "__main__":
    main()
