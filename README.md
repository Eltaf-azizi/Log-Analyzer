<h1 align="center">Log-Analyzer</h1>

A beginner-friendly log analysis tool built with Python.
It parses server logs (Apache, Nginx, auth, syslog), summarizes activity, and detects anomalies such as:
 - **HTTP 5xx spikes** (server errors in short time windows)
 - **Failed login bursts** (multiple failed authentication attempts from the same IP)
Reports can be printed in the terminal with rich formatting or exported as HTML, JSON, or CSV.
