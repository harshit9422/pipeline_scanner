import os
from datetime import datetime

def generate_report(results):
    os.makedirs("output", exist_ok=True)
    path = os.path.join("output", "scan_report.md")

    with open(path, "w", encoding="utf-8") as fh:
        fh.write("# CI/CD Pipeline Scan Report\n\n")
        fh.write(f"_Generated on {datetime.utcnow().isoformat()}Z_\n\n")

        if not results:
            fh.write("No issues found.\n")
            return

        for entry in results:
            fh.write(f"## File: {entry['file']}\n")
            for issue in entry["issues"]:
                fh.write(f"- {issue}\n")
            fh.write("\n")

    print(f"Report saved to: {path}")
