from typing import Iterable, Dict, Any, Optional
from src.core.patterns import PATTERNS
from src.core.utils import parse_timestamp, extract_ip_from_text

class LogParser:
    """
    Parse log lines using a named pattern from src.core.patterns.PATTERNS.

    parse(lines) yields dictionaries with normalized fields:
      - dt (pandas.Timestamp)
      - ip (if available)
      - status (int) for HTTP logs
      - message/host/program for auth/syslog logs
    """

    
    def __init__(self, pattern_name: str = "apache_common"):
        if pattern_name not in PATTERNS:
            raise ValueError(f"Unknown pattern: {pattern_name}")
        self.pattern_name = pattern_name
        self.regex = PATTERNS[pattern_name]



    def parse_line(self, line: str) -> Optional[Dict[str, Any]]:
        m = self.regex.match(line.strip())
        if not m:
            return None
        d = m.groupdict()
        # Normalize timestamp
        if "timestamp" in d:
            d["dt"] = parse_timestamp(d.get("timestamp"))
        # Normalize status if present
        if "status" in d and d.get("status") is not None:
            try:
                d["status"] = int(d["status"])
            except Exception:
                pass
