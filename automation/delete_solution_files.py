# automation/delete_solution_files.py
from pathlib import Path
from typing import List, Optional
import webbrowser

HEADER = "Directories containing solution.py"

BASE_PROMPT = (
    "You will be given a problem and you have to solve it with multiple ways one with brute force "
    "one space optimized one time optimized if also both or also optimal algorithms if possible. "
    "You can look the internet for other mathematical or known algorithms for a solution.\n"
    "every solution should be complete executable code not a downloadable file\n"
    "each solution should be a in separate code snippet\n"
    "also each solution has to have the file name.\n"
    "CODE ONLY IN PYTHON\n\n"
    "----- PROBLEM BELOW -----\n"
)

def copy_to_clipboard(text: str) -> bool:
    """Cross-platform clipboard copy with tkinter (no extra deps)."""
    try:
        import tkinter as tk
        r = tk.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(text)
        r.update()
        r.destroy()
        return True
    except Exception as e:
        print(f"[WARN] Could not copy to clipboard automatically: {e}")
        return False

def parse_report(report_path: Path) -> List[Path]:
    lines = report_path.read_text(encoding="utf-8", errors="replace").splitlines()
    dirs, capture = [], False
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        if not capture:
            if line.startswith(HEADER):
                capture = True
            continue
        # Each subsequent non-empty line is a relative path like "Python\Foo"
        dirs.append(Path(line.replace("\\", "/")))
    return dirs

def find_problem_txt(dir_path: Path) -> Optional[Path]:
    """Prefer problem.txt, then README.txt, else first *.txt in the folder."""
    for name in ("problem.txt", "README.txt"):
        p = dir_path / name
        if p.exists() and p.is_file():
            return p
    for txt in sorted(dir_path.glob("*.txt")):
        return txt
    return None

def main():
    repo_root = Path(".").resolve()
    report_path = Path("report.txt")
    if not report_path.exists():
        raise SystemExit("report.txt not found in the current directory.")

    dirs = parse_report(report_path)
    if not dirs:
        raise SystemExit("No directories parsed from report.txt. Check the header line exactly matches:\n"
                         f"'{HEADER}'")

    deleted_dir = None

    # 1) Delete exactly one solution.py (the first that exists)
    for rel_dir in dirs:
        target = (repo_root / rel_dir / "solution.py").resolve()
        # Safety: ensure inside repo_root
        try:
            target.relative_to(repo_root)
        except ValueError:
            print(f"[SKIP] Outside repo root: {target}")
            continue

        if target.exists():
            try:
                target.unlink()
                deleted_dir = target.parent
                print(f"[OK] Deleted: {target}")
                break
            except Exception as e:
                print(f"[ERR] Could not delete {target}: {e}")
                break

    if deleted_dir is None:
        print("[DONE] No solution.py found to delete. Nothing else to do.")
        return

    # 2) Read problem text from that directory
    problem_path = find_problem_txt(deleted_dir)
    if not problem_path:
        print(f"[MISS] No .txt problem file found in {deleted_dir}.")
        return

    problem_text = problem_path.read_text(encoding="utf-8", errors="replace").strip()
    final_prompt = BASE_PROMPT + problem_text

    # 3) Copy to clipboard and open ChatGPT
    if copy_to_clipboard(final_prompt):
        print("[OK] Prompt copied to clipboard.")
    else:
        print("\n[INFO] Copy failed. Here is the prompt — copy it manually:\n")
        print(final_prompt)
        print("\n[INFO] End of prompt.\n")

    try:
        webbrowser.open("https://chat.openai.com/")
        print("[OK] Opened ChatGPT in your browser. Paste the prompt and send.")
    except Exception as e:
        print(f"[WARN] Could not open browser automatically: {e}")

if __name__ == "__main__":
    main()
