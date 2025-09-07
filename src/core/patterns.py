import re
from typing import Dict, Pattern


# Precompiled patterns used by parser
PATTERNS: Dict[str, Pattern] = {
    "apache_common": re.compile(
        r'^(?P<ip>\S+)\s+\S+\s+\S+\s+\[(?P<timestamp>[^\]]+)\]\s+"(?P<method>\S+)\s+(?P<path>[^\s"]+)\s*(?P<proto>[^"]*)"\s+(?P<status>\d{3})\s+(?P<size>\S+)'
    ),
    "nginx_combined": re.compile(
        r'^(?P<ip>\S+)\s+-\s+\S+\s+\[(?P<timestamp>[^\]]+)\]\s+"(?P<method>\S+)\s+(?P<path>[^\s"]+)\s*(?P<proto>[^"]*)"\s+(?P<status>\d{3})\s+(?P<size>\S+)\s+"(?P<referrer>[^"]*)"\s+"(?P<agent>[^"]*)"'
    ),
    "auth": re.compile(
        r'^(?P<timestamp>\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(?P<host>\S+)\s+(?P<program>\S+)(?:\[\d+\])?:\s+(?P<message>.*)$'
    ),
    "syslog": re.compile(
        r'^(?P<timestamp>\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(?P<host>\S+)\s+(?P<program>\S+):\s+(?P<message>.*)$'
    ),
}