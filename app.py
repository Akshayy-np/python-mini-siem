from flask import Flask, render_template, jsonify
from detector import scan_logs

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/data")
def data():
    return jsonify(scan_logs())

if __name__ == "__main__":
    app.run(debug=True)