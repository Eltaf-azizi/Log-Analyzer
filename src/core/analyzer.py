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



    def detect_failed_logins(self, window: str = "10min", threshold: int = 5) -> List[Dict[str, Any]]:
        """Detect bursts of failed login messages grouped by ip."""
        if "message" not in self.df.columns:
            return []
        # Heuristics for failure strings
        mask = self.df["message"].str.contains(r"failed password|authentication failure|invalid user", case=False, na=False)
        df_fail = self.df.loc[mask].copy()
        if df_fail.empty:
            return []
        if "ip" not in df_fail.columns:
            return []
        df_fail = ensure_bucket(df_fail, window)
        grp = df_fail.groupby(["ip", "bucket"]).size().rename("count").reset_index()
        anomalies = grp[grp["count"] >= threshold]
        return anomalies.to_dict(orient="records")
    


    def detect_http_5xx_spikes(self, window: str = "5min", threshold: int = 3) -> List[Dict[str, Any]]:
        """
        Detect buckets where 5xx errors exceed threshold.
        """

        if "status" not in self.df.columns or "dt" not in self.df.columns:
            return []
        
        df = self.df.copy()
        df = ensure_bucket(df, window)
        df["is5xx"] = df["status"].between(500, 599)
        grp = df.groupby("bucket")["is5xx"].sum().rename("count").reset_index()
        anomalies = grp[grp["count"] >= threshold]
        return anomalies.to_dict(orient="records")

