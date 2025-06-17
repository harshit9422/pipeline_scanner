import re

def scan_file(filename: str, content: str):
    issues = []

    # hard-coded AWS secret key
    if re.search(
        r'AWS[_-]?SECRET[_-]?KEY\s*[:=]\s*["\']?[A-Za-z0-9/=+]+',
        content
    ):
        issues.append("Potential hardcoded AWS secret key")

    # plaintext password
    if re.search(
        r'password\s*[:=]\s*["\']?.{3,}',
        content,
        re.IGNORECASE
    ):
        issues.append("Plaintext password detected")

    return issues
