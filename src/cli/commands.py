from typing import Optional
import yaml
from pathlib import Path
from src.core.parser import LogParser
from src.core.analyzer import Analyzer
from src.reporting.formatter import print_summary, print_anomalies
from src.reporting.exporter import export_report




def load_defaults() -> dict:
    cfg = Path(__file__).parents[2] / "config" / "settings.yaml"
    if cfg.exists():
        with open(cfg, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
            return data.get("defaults", {})
    return {}




def run_analyze(args):

    defaults = load_defaults()
    pattern = args.pattern or defaults.get("pattern", "apache_common")
    window = args.window or defaults.get("window", "5min")
    threshold = args.threshold or defaults.get("http_5xx_threshold", defaults.get("http_5xx_threshold", 3))
    failed_login_threshold = defaults.get("failed_login_threshold", 5)


    path = Path(args.file)
    if not path.exists():
        raise SystemExit(f"File not found: {args.file}")
    

    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    parser = LogParser(pattern)
    records = list(parser.parse(lines))
    analyzer = Analyzer(records)


    summary = analyzer.summary()
    http_anoms = analyzer.detect_http_5xx_spikes(window=window, threshold=threshold)
    failed_anoms = analyzer.detect_failed_logins(window=window, threshold=failed_login_threshold)

    # Annotate types
    anomalies = []
    for a in http_anoms:
        a_copy = dict(a)
        a_copy["type"] = "http_5xx_spike"
        anomalies.append(a_copy)

    for a in failed_anoms:
        a_copy = dict(a)
        a_copy["type"] = "failed_login_burst"
        anomalies.append(a_copy)

    print_summary(summary)
    print_anomalies(anomalies)

    if args.save:
        out = export_report(args.save, args.format, summary, anomalies)
        if out:
            print(f"Report saved: {out}")
        else:
            print("Unsupported format for saving.")



# Expose friendly function used by main
def run_command(args):
    if args.command == "analyze":
        return run_analyze(args)
    
    