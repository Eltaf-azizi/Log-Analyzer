<h1 align="center">Log-Analyzer</h1>

A beginner-friendly log analysis tool built with Python.
It parses server logs (Apache, Nginx, auth, syslog), summarizes activity, and detects anomalies such as:
 - **HTTP 5xx spikes** (server errors in short time windows)
 - **Failed login bursts** (multiple failed authentication attempts from the same IP)
Reports can be printed in the terminal with rich formatting or exported as HTML, JSON, or CSV.


## ✨ Features

 - Parse multiple log formats:
   - Apache common
   - Nginx combined
   - Auth logs
   - Syslog
 - Summaries: total rows, status code counts, top IPs
 - Anomaly detection:
   - Repeated failed logins (SSH brute force attempts)
   - Bursts of HTTP 5xx errors
 - Report export:
   - Rich CLI output
   - JSON, CSV, or HTML reports


## Project Structure

    log-analyzer-basic/
    ├── README.md
    ├── requirements.txt
    ├── .gitignore
    ├── data/
    │   ├── sample.log         # example Apache log
    │   └── auth.log           # example auth log
    ├── config/
    │   ├── patterns.yaml      # regex patterns for logs
    │   └── settings.yaml      # default thresholds & settings
    ├── src/                   # main source code
    │   ├── cli/               # CLI parsing and commands
    │   ├── core/              # log parsing, analysis, utils
    │   ├── reporting/         # report formatting & exporting
    │   └── main.py            # entry point
    └── tests/                 # pytest unit tests


## 🚀 Installation

Clone the repo and set up a virtual environment:
```
git clone https://github.com/yourname/log-analyzer-basic.git
cd log-analyzer-basic

python -m venv .venv
# activate venv
# mac/linux
source .venv/bin/activate
# windows (powershell)
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

## 🖥 Usage
#### Analyze a sample Apache log
```
python -m src.main analyze --file data/sample.log --pattern apache_common --window 5min --threshold 3 --save report.html --format html
```
#### Analyze an auth log for failed logins
```
python -m src.main analyze --file data/auth.log --pattern auth --window 10min --threshold 5
```

CLI Options

    usage: log-analyzer analyze [-h] --file FILE [--pattern {apache_common,nginx_combined,auth,syslog}]
                                [--window WINDOW] [--threshold THRESHOLD]
                                [--save SAVE] [--format {html,json,csv}] [--verbose]
    
    options:
      --file, -f       Path to log file to analyze
      --pattern, -p    Log pattern (apache_common, nginx_combined, auth, syslog)
      --window, -w     Aggregation window (e.g., 5min, 10min, 1H)
      --threshold, -t  Threshold for anomaly detection
      --save, -s       Save report to file
      --format, -o     Report format (html, json, csv)
      --verbose, -v    Verbose output

## 📊 Example Output

Terminal (Rich output):
```
────────────────────────────── Analysis Summary ──────────────────────────────
Metric        Value
────────────  ──────────────────────────────────────────────
Total rows    10
Status counts {"200": 3, "401": 1, "404": 1, "500": 3, "502": 1, "503": 1}
4xx           2
5xx           5
Top IPs       198.51.100.23: 5
              203.0.113.5: 2
              127.0.0.1: 1
              192.0.2.1: 1

─────────────────────────────── Anomalies ───────────────────────────────────
bucket                count  type
────────────────────  ─────  ───────────────
2024-12-12 19:10:00   3      http_5xx_spike
198.51.100.23 19:05   5      failed_login_burst
```

Exported report:

 - report.html → styled HTML report with summary + anomalies
 - report.json → machine-readable JSON
 - report.csv → anomaly rows in CSV format


## 🧪 Running Tests

This project uses pytest. Run tests with:
```
pytest -q
```

## 📌 Roadmap

 - Add more log formats (IIS, custom JSON logs)
 - Real-time streaming log analysis
 - Configurable anomaly detection rules
 - Docker container for easy deployment


## 🙌 Contributing

 - Contributions are welcome!
 - Fork the project
 - Create a new branch (`feature/awesome-feature`)
 - Commit your changes
 - Open a Pull Request
<h3 align="center">Happy Coding!</h3>
