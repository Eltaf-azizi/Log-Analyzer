from src.core.analyzer import Analyzer
import pandas as pd



def make_dummy_http_records():

    base = pd.Timestamp("2024-12-12 19:00:00")
    rows = []
    # stable requests
    for i in range(10):
        rows.append({"dt": base + pd.Timedelta(minutes=i), "status": 200, "ip": "1.1.1.1"})
    # spike of 5xx at minute 5
    for j in range(5):
        rows.append({"dt": base + pd.Timedelta(minutes=5), "status": 500, "ip": "2.2.2.2"})
    return rows

