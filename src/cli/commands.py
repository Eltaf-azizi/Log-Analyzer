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