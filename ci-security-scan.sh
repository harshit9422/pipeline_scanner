#!/usr/bin/env bash
set -euo pipefail

# Activate your virtual environment
source .venv/bin/activate

# Run your custom Python scanner
python3 scanner.py sample_configs

# Run Checkov against the same folder
checkov -d sample_configs

echo "Security scan passed!"
