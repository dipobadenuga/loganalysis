Log Analysis Project: Detecting Unauthorized Access

This repository contains a simple log analysis project that looks for signs of unauthorized access using Apache access logs and Windows Security logs. The project uses Python, Event Viewer, and PowerShell to detect suspicious activity such as repeated failed logins and unusual IP addresses.

Project Goal
The goal is to show how basic log analysis can help identify security issues. By checking logs and reading patterns, we can detect:
- repeated failed login attempts  
- unknown or suspicious IP addresses  
- requests to restricted pages  
- activity at unusual times  

Tools Used
- Python 3
- Windows Event Viewer
- PowerShell
- Apache access logs
- macOS Terminal (for running the script when or if using a Mac)

Repository Structure
log-analysis-detect-unauthorized-access/
├── data/
│ ├── sample_logs/
│ │ └── apache_access.log
│ └── simulated_logs/
├── scripts/
│ └── log_analysis.py
├── results/
│ ├── screenshots/
│ └── findings.txt
└── docs/
├── project_overview.md
└── data_description.md
