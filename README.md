# Python Mini SIEM - Intrusion Detection Dashboard

A lightweight intrusion detection system built in Python that detects SSH brute-force attacks and visualizes them using a Flask dashboard.

## Features
- SSH log parsing
- Failed login detection
- IP-based attack aggregation
- Risk scoring (LOW / MEDIUM / HIGH)
- Auto-generated attack graph
- CSV logging

## Tech Stack
- Python
- Flask
- Matplotlib
- Linux authentication logs

## Run

pip install -r requirements.txt
sudo python3 app.py

Open: http://127.0.0.1:5000
