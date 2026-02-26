import random
from datetime import datetime
import os

# IPs with specific attack counts
ips = {
    "192.168.1.10": 3,
    "10.0.0.5": 8,
    "172.16.0.8": 25,
    "203.45.67.89": 50,
    "185.22.33.44": 120,
    "45.67.89.12": 15
}

os.makedirs("logs", exist_ok=True)

with open("logs/auth.log", "w") as f:
    for ip, count in ips.items():
        for _ in range(count):
            timestamp = datetime.now().strftime("%b %d %H:%M:%S")
            line = f"{timestamp} kali sshd[1234]: Failed password for invalid user root from {ip} port 22 ssh2\n"
            f.write(line)

print("Realistic auth.log generated successfully.")