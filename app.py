import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from flask import Flask, render_template
from detector import scan_logs
from ai_detector import risk_score

app = Flask(__name__)

@app.route("/")
def dashboard():
    suspicious = scan_logs()
    data = []

    for ip, attempts in suspicious.items():
        data.append({
            "ip": ip,
            "attempts": attempts,
            "risk": risk_score(attempts)
        })
        if data:
                ips = [item["ip"] for item in data]
                attempts = [item["attempts"] for item in data]

                plt.figure(figsize=(8,4))
                plt.tight_layout()
                plt.bar(ips, attempts)
                plt.xlabel("IP Address")
                plt.ylabel("Failed Attempts")
                plt.title("Attack Attempts by IP")
                os.makedirs("static", exist_ok=True)
                plt.savefig("static/graph.png")
                plt.close()

    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)