from typing import Iterable, Dict, Any, List
import pandas as pd
from src.core.utils import ensure_bucket
from collections import defaultdict

class Analyzer:
    """
    Analyzer accepts an iterable of parsed records (dicts) and provides:
    - summary(): counts, top IPs, 4xx/5xx counts
    - detect_failed_logins(window, threshold)
    - detect_http_5xx_spikes(window, threshold)
    """

    def __init__(self, records: Iterable[Dict[str, Any]]):
        self.df = pd.DataFrame(list(records))
        if "dt" in self.df.columns:
            self.df["dt"] = pd.to_datetime(self.df["dt"], errors="coerce")