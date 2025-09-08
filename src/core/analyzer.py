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



    def summary(self) -> Dict[str, Any]:
        out = {}
        out["total_rows"] = int(len(self.df))
        if "status" in self.df.columns:
            out["status_counts"] = self.df["status"].value_counts().sort_index().to_dict()
            out["4xx"] = int(self.df["status"].between(400, 499).sum())
            out["5xx"] = int(self.df["status"].between(500, 599).sum())
        if "ip" in self.df.columns:
            out["top_ips"] = self.df["ip"].value_counts().head(10).to_dict()
        else:
            out["top_ips"] = {}
        return out


