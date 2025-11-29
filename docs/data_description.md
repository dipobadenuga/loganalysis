# Data Description

## Overview
This project uses system log files to look for signs of unauthorized access. These logs help show activity on a computer or a server. They are stored as plain text and can be read using Python. The logs include information like timestamps, IP addresses, request types, and login attempts. All logs used for this project are stored locally on my computer.

## Types of Logs Used
The project uses two main types of log files:

---

## 1. Apache Web Server Access Logs
Apache access logs record every request made to a web server. These logs are helpful for detecting unusual or suspicious behavior because they show what each user or IP address is doing.

### What Apache Logs Usually Include
- **IP address** of the user making the request  
- **Date and time** of the request  
- **HTTP method** (GET, POST, etc.)  
- **Path** requested (example: `/login`, `/admin`, `/index.html`)  
- **Status code** returned (200, 404, 401, 403, etc.)  
- **Size** of the response  

### Why These Logs Are Useful
Apache access logs help detect:
- repeated failed login attempts (status code **401**)  
- attempts to access restricted pages (**403**)  
- scanning activity or probing (lots of 404 errors)  
- unusual IP addresses making many requests  

### Data Source
For this project, the Apache logs come from:
- public sample logs (LogHub Apache datasets)  
- or a sample log file created manually to mimic real activity  

The log file is saved inside:  
`data/sample_logs/apache_access.log`

---

## 2. Windows Security Event Logs
Windows security logs show activity happening on a Windows computer. These logs are viewed using Event Viewer or exported using PowerShell.

### What Windows Security Logs Include
- **successful logins**  
- **failed logins**  
- **account lockouts**  
- **changes to accounts**  
- **security alerts**  

### Why These Logs Matter
They help detect:
- brute-force login attempts  
- unauthorized login attempts  
- suspicious activity outside normal hours  
- repeated failures for the same account  

These logs will be used to compare patterns with the Apache log analysis.

---

## Storage and Format
- All logs are stored **locally** on my computer in plain text format.  
- The Apache logs are read directly by Python.  
- Windows logs can be exported from Event Viewer and saved as text files.  
- The Python script parses the Apache log file to find suspicious patterns.

---

## How the Logs Support the Project
These logs help show real examples of unauthorized access attempts.  
By reading them with Python, the project can highlight:
- which IPs are suspicious  
- which requests failed  
- how many times login attempts were made  
- what kind of pages attackers might try to access  

This supports the project goal of using basic log analysis to detect intrusion.
