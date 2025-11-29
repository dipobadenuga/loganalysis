# Project Overview

## Title
Using Basic Log Analysis to Detect Unauthorized Access

## Setup
This project is done on my Windows computer. I will use Python to write simple scripts that read and analyze log files. I will also use Windows tools like Event Viewer and PowerShell to look at security log entries. No virtual machine is needed because everything can be done locally in a safe environment. I am also using Windows for this project because I am more familiar with it than Linux.

## Goal of the Project
The goal of this project is to show how basic log analysis can help detect signs of unauthorized access. Logs record activities such as login attempts, requests from different IP addresses, and the times those requests happened. By reading these logs, we can look for unusual patterns that may point to suspicious behavior.

## Data Used
The project uses two kinds of log files:

1. **Windows Security Event Logs**  
   These logs show information such as:
   - successful and failed login attempts  
   - account lockouts  
   - security-related events  

2. **Apache Web Server Access Logs**  
   These logs show:
   - IP addresses  
   - timestamps  
   - request types (GET, POST, etc.)  
   - response status codes (200, 404, 401, 403, etc.)  

I will use publicly available Apache access logs or create sample logs to test the script. These logs help show activity patterns such as repeated failed logins, suspicious IP addresses, or attempts to access protected pages.

## What I Expect to Find
By analyzing the logs, I expect to find patterns such as:
- multiple failed login attempts  
- unknown or unusual IP addresses  
- activity at times when no one should be logging in  
- attempts to access restricted pages like `/admin`, `/login`, or `/config.php`  

These patterns are common signs of brute-force attacks or scanning activity.

## Final Output
At the end of the project, I will have:
- a working Python log analysis script  
- an Apache log file used for testing  
- screenshots from Event Viewer and PowerShell  
- a findings summary with suspicious patterns  
- basic recommendations on how log analysis can help detect intrusion  
