import os

def scan_directories(base_dir):
    found_dirs = []

    # Walk through all subdirectories
    for root, dirs, files in os.walk(base_dir):
        if 'solution.py' in files or 'Solution.py' in files:
            found_dirs.append(root)

    return found_dirs

def write_report(found_dirs, report_file):
    with open(report_file, 'w', encoding='utf-8') as f:
        if found_dirs:
            f.write("Directories containing solution.py:\n")
            for directory in found_dirs:
                f.write(directory + "\n")
        else:
            f.write("No directories with solution.py found.\n")

if __name__ == "__main__":
    base_directory = "Python"  # Name of the main directory
    report_filename = "report.txt"

    directories_with_solution = scan_directories(base_directory)
    write_report(directories_with_solution, report_filename)

    print(f"Report generated: {report_filename}")
