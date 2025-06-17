# Pipeline Security Scanner

A lightweight, customizable CI/CD pipeline scanning tool that detects potential security issues in YAML, JSON, XML, and Python files, and integrates with Checkov for infrastructure-as-code policy checks.

## Features

* **Custom Detectors**: Hand-crafted rules to spot hardcoded secrets (AWS keys, passwords) and insecure patterns in pipeline configurations.
* **Pluggable Frameworks**: Easily extend or replace detectors by editing `detectors.py`.
* **Report Generation**: Generates a Markdown report (`output/scan_report.md`) summarizing findings.
* **Checkov Integration**: Runs [Checkov](https://github.com/bridgecrewio/checkov) against your configuration directory for IaC policy checks.
* **GitHub Actions CI**: Sample workflow provided to automatically run scans on every push to `main`.

## Repository Structure

```
├── .github/workflows     # GitHub Actions definitions
│   └── security-scan.yml # CI job for custom scanner + Checkov
├── ci-security-scan.sh   # Shell wrapper for local CI runs
├── sample_configs        # Example pipeline config files to scan
│   └── test_pipeline.yml # Contains hardcoded AWS_SECRET_KEY & password
├── scanner.py            # Main entrypoint to run detectors & report
├── detectors.py          # Definition of scanning rules
├── reporter.py           # Markdown report generator
├── output                # Auto-generated scan outputs
│   └── scan_report.md    # Example report
└── security-scan.yml     # Configuration for external tools (if any)
```

## Getting Started

### Prerequisites

* Python 3.8+ installed
* (Optional) Docker, if containerizing

### Installation

```bash
git clone git@github.com:harshit9422/pipeline_scanner.git
cd pipeline_scanner
python3 -m venv .venv
source .venv/bin/activate
pip install checkov
```

### Usage

#### Local Scan

```bash
# Activate venv
source .venv/bin/activate

# Run custom pipeline scanner against sample_configs
python scanner.py sample_configs

# View the generated report
less output/scan_report.md
```

#### GitHub Actions CI

Push your changes to the `main` branch. The workflow defined in `.github/workflows/security-scan.yml` will:

1. Check out the repo
2. Set up Python and install dependencies
3. Execute your custom scanner
4. Run Checkov policy checks

Monitor the run under the **Actions** tab in your GitHub repository.

## Writing Your Own Detectors

1. Open `detectors.py`.
2. Implement a function that takes `(filename: str, content: str) -> List[str]`.
3. Append the detector function to the `DETECTORS` list.
4. Re-run `scanner.py` to see new detections.

## Contributing

Feel free to open issues or submit pull requests to add more detectors, support additional file types, or improve reporting formats.

## License

MIT © Harshit Rai
