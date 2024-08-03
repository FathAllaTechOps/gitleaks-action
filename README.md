# Gitleaks Action

# Run [GitLeaks][gitleaks] action

![GitHub release (latest by date)](https://img.shields.io/github/v/release/yourusername/gitleaks-action)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/yourusername/gitleaks-action/ci.yml)
![GitHub](https://img.shields.io/github/license/yourusername/gitleaks-action)


## Description

This GitHub composite action installs and runs Gitleaks to scan for leaks in your source code and generates a report.

## Author

[fathalla.ebrahem22@gmail.com](mailto:fathalla.ebrahem@gmail.com)

## Inputs

| Input Name       | Description                           | Required | Default                   |
|------------------|---------------------------------------|----------|---------------------------|
| `source`         | The source directory to scan for leaks| false    | `.`                       |
| `report-output-path` | Path to Gitleaks report file      | false    | `gitleaks-report.html`    |

## Usage

```yaml
name: Run Gitleaks
on: [push, pull_request]
jobs:
  gitleaks:
    runs-on: self-hosted
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          repository: VFGroup-VBIT/<Repository_Name>
          path: <Repository_Name>
          token: ${{ secrets.TOKEN }}

      - name: Run Gitleaks
        uses: FathAllaTechOps/gitleaks-action@main
        with:
          source: <Repository_Name>
          report-output-path: <Repository_Name>_report.html
```
