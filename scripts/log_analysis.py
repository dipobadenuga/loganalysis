"""
Basic log analysis script to detect possible unauthorized access.

This script:
- Reads an Apache style access log from a text file
- Counts how many requests each IP address makes
- Counts how many error or failed responses each IP has
- Prints out IP addresses that look suspicious
"""

import os
from collections import defaultdict

# Path to the log file.
# Change this if your file has a different name or location.
LOG_FILE_PATH = os.path.join("..", "data", "sample_logs", "apache_access.log")


def parse_apache_line(line):
    """
    Try to parse one line from an Apache access log.

    Expected simple format:
    IP - - [date] "METHOD PATH PROTOCOL" STATUS SIZE

    Returns a dictionary with:
    - ip: string
    - status: integer status code

    If the line cannot be parsed, returns None.
    """
    parts = line.split()

    # Need at least 9 parts for a basic Apache format
    if len(parts) < 9:
        return None

    ip = parts[0]

    # Status code is usually the second value after the closing quote
    # Example: "GET /index.html HTTP/1.1" 200 1024
    try:
        status = int(parts[-2])
    except ValueError:
        return None

    return {"ip": ip, "status": status}


def analyze_log(file_path):
    """
    Read the log file and count:
    - total requests per IP
    - error or failed responses per IP

    Returns two dictionaries:
    - total_requests[ip] = count
    - failed_requests[ip] = count
    """
    total_requests = defaultdict(int)
    failed_requests = defaultdict(int)

    if not os.path.exists(file_path):
        print(f"Log file not found at: {file_path}")
        print("Please check the path or place your log file in data/sample_logs.")
        return total_requests, failed_requests

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            parsed = parse_apache_line(line)
            if not parsed:
                continue

            ip = parsed["ip"]
            status = parsed["status"]

            total_requests[ip] += 1

            # Treat status codes 400 and above as failures or errors
            if status >= 400:
                failed_requests[ip] += 1

    return total_requests, failed_requests


def print_suspicious_ips(total_requests, failed_requests,
                         min_total=50, min_failed=5, failed_ratio=0.2):
    """
    Print IP addresses that may be suspicious.

    An IP is marked as suspicious if:
    - it has at least min_total total requests, or
    - it has at least min_failed failed requests, or
    - the fraction of failed requests is higher than failed_ratio
    """
    print("=== Suspicious IP Report ===")

    any_suspicious = False

    for ip, total in total_requests.items():
        fails = failed_requests.get(ip, 0)

        if total == 0:
            continue

        ratio = fails / total

        if total >= min_total or fails >= min_failed or ratio >= failed_ratio:
            any_suspicious = True
            print(f"\nIP address: {ip}")
            print(f"  Total requests: {total}")
            print(f"  Failed or error responses: {fails}")
            print(f"  Failure ratio: {ratio:.2f}")

    if not any_suspicious:
        print("No IP addresses met the suspicious criteria.")
        print("You can lower the thresholds in print_suspicious_ips if needed.")


def main():
    """
    Main entry point for the script.
    """
    print("Starting basic log analysis...")
    print(f"Reading log file from: {LOG_FILE_PATH}")

    total_requests, failed_requests = analyze_log(LOG_FILE_PATH)

    print(f"\nTotal unique IP addresses: {len(total_requests)}")
    print_suspicious_ips(total_requests, failed_requests)


if __name__ == "__main__":
    main()
