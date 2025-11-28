# Using Basic Log Analysis to Detect Unauthorized Access

This project shows how simple log analysis can help detect signs of unauthorized access.  
It focuses on reading and analyzing log files using Python and basic Windows tools.

## Project Goal

The main goal is to look for patterns in log data that may point to:

- Repeated failed login attempts  
- Unusual or unknown IP addresses  
- Activity at strange times of day  
- Very high numbers of requests from the same source

By the end of the project, there is a working Python script, sample outputs, and basic recommendations for using logs to support security monitoring and intrusion detection.

## Environment and Tools

This project is done on a Windows computer:

- Python 3  
- Simple Python scripts for log parsing  
- Windows Event Viewer to view local security logs  
- PowerShell for basic log searches and exporting logs

No virtual machine is required. All work is done in a local and safe test environment.

## Data Sources

The data used in this project comes from:

- Apache web server access logs  
- Windows security event logs

The Apache logs can come from public sample datasets. For example, the LogPai LogHub project contains many real world log samples that can be used for testing log analysis.

Windows security logs can be viewed and exported from Event Viewer on a Windows system.

## Repository Structure

```text
log-analysis-detect-unauthorized-access/
│
├── README.md
├── data/
│   ├── sample_logs/
│   └── simulated_logs/
├── scripts/
│   └── log_analysis.py
├── results/
│   ├── screenshots/
│   └── findings.txt
└── docs/
    ├── project_overview.md
    └── data_description.md
