import sys
from pathlib import Path
from detectors import scan_file
from reporter  import generate_report

def scan_directory(folder):
    results = []

    for f in Path(folder).rglob("*.*"):
        print(f"DEBUG: Found file {f} (suffix={f.suffix})")           # ← debug
        if f.suffix in (".yml", ".yaml", ".json", ".xml", ".py"):
            content = f.read_text(encoding="utf-8", errors="ignore")
            print(f"DEBUG: Content head of {f.name!r}: {content[:80]!r}")  # ← debug
            issues = scan_file(f.name, content)
            if issues:
                print(f"Found issues in {f.name}: {issues}")
                results.append({"file": f.name, "issues": issues})
    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scanner.py <folder_to_scan>")
        sys.exit(1)

    target = sys.argv[1]
    print(f"Scanning files in: {target}")
    results = scan_directory(target)
    print(f"Results: {results}")
    generate_report(results)
