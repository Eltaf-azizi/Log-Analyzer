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