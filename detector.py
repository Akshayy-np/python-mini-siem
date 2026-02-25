import subprocess
import re
from collections import defaultdict
import csv
import os

THRESHOLD = 5

def scan_logs():
    failed_attempts = defaultdict(int)

    # Get SSH logs from journalctl
    result = subprocess.run(
        ["journalctl", "-u", "ssh", "--no-pager"],
        stdout=subprocess.PIPE,
        text=True
    )

    logs = result.stdout.split("\n")

    for line in logs:
        if "Failed password" in line:
            ip_match = re.search(r'from\s+([0-9a-fA-F:\.]+)', line)
            if ip_match:
                ip = ip_match.group(1)
                failed_attempts[ip] += 1

    suspicious = {
    ip: count for ip, count in failed_attempts.items()
    if count > THRESHOLD
}
    save_to_csv(suspicious)

    return suspicious


def save_to_csv(data):
    os.makedirs("logs", exist_ok=True)
    with open("logs/suspicious.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP", "Attempts"])
        for ip, count in data.items():
            writer.writerow([ip, count])