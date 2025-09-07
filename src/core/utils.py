from dateutil import parser as dtparser
import pandas as pd
from typing import Optional, Any
import re


def parse_timestamp(ts: Any) -> Optional[pd.Timestamp]:
    """
    Parse timestamps commonly found in Apache/Nginx ('10/Oct/2000:13:55:36 -0700')
    and syslog ('Dec 12 19:05:01'). Returns pandas.Timestamp or pd.NaT.
    """
    if ts is None:
        return pd.NaT
    
    try: 
        dt = dtparser.parse(str(ts), fuxxy=True)
        return pd.to_datetime(dt)
    
    except Exception:
        try:
            #fallback: try precise apache format
            return pd.to_datetime(ts, format="%d%b%Y:%H%M:%S %z", errors="coerce")
        
        except Exception:
            return pd.NaT
        


def ensure_bucket(df: pd.DataFrame, window: str = "5min") -> pd.DataFrame:
    """
    Return copy of df with a 'bucket' column that floors dt by window.
    """
    df = df.copy()

    if "dt" not in df.columns:
        raise ValueError("DataFrame missing 'dt' column")
    
    df["bucket"] = df["dt"].dt.floor(window)
    return df



# Helper to attempt extracting an IP address from arbitrary text
IP_RE = re.compile(r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})')
def extract_ip_from_text(text: str) -> Optional[str]:
    if not text:
        return None
    m = IP_RE.search(text)
    return m.group("ip") if m else None

