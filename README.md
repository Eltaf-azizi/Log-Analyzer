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
