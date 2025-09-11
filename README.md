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
