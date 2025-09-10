import argparse
from typing import Any


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="log-analyzer", description="Basic log analyzer (failed logins, error spikes)")
    sub = p.add_subparsers(dest="command", required=True)

    analyze = sub.add_parser("analyze", help="Parse and analyze a log file")
    analyze.add_argument("--file", "-f", required=True, help="Path to log file to analyze")
    analyze.add_argument("--pattern", "-p", default=None, choices=["apache_common", "nginx_combined", "auth", "syslog"], help="Log pattern to use")
    analyze.add_argument("--window", "-w", default=None, help="Aggregation window (e.g., 5min, 10min, 1H)")
    analyze.add_argument("--threshold", "-t", type=int, default=None, help="Threshold for anomaly detection (int)")
    analyze.add_argument("--save", "-s", default=None, help="Path to save report (requires --format)")
    analyze.add_argument("--format", "-o", default="html", choices=["html","json","csv"], help="Report format when using --save")
    analyze.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    return p
