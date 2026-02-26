import re
from collections import defaultdict
import os
from datetime import datetime

THRESHOLD = 0
LOG_FILE = "logs/auth.log"

def scan_logs():
    failed_attempts = defaultdict(int)
    attack_timeline = defaultdict(int)

    if not os.path.exists(LOG_FILE):
        return {"attackers": [], "timeline": {}}

    with open(LOG_FILE, "r") as f:
        logs = f.readlines()

    for line in logs:
        if "Failed password" in line:

            # Extract IP
            ip_match = re.search(r'from\s+([0-9a-fA-F:\.]+)', line)
            if ip_match:
                ip = ip_match.group(1)
                failed_attempts[ip] += 1

            # Extract timestamp (Linux auth.log format)
            # Example: Feb 26 10:05:32
            time_match = re.match(r'([A-Z][a-z]{2}\s+\d+\s+\d+:\d+)', line)
            if time_match:
                try:
                    time_obj = datetime.strptime(
                        time_match.group(1) + " 2026",
                        "%b %d %H:%M %Y"
                    )
                    minute_key = time_obj.strftime("%H:%M")
                    attack_timeline[minute_key] += 1
                except:
                    pass

    # Build attacker list
    attackers = []

    for ip, attempts in failed_attempts.items():

        if attempts < 5:
            risk = "LOW"
        elif attempts < 20:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

        attackers.append({
            "ip": ip,
            "attempts": attempts,
            "risk": risk
        })

    attackers = sorted(attackers, key=lambda x: x["attempts"], reverse=True)

    # Sort timeline by time
    sorted_timeline = dict(sorted(attack_timeline.items()))

    return {
        "attackers": attackers,
        "timeline": sorted_timeline
    }