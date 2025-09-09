from typing import Dict, Any, List, Optional
import json
import csv
from jinja2 import Template
from pathlib import Path



HTML_TMPL = Template("""
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Log Analysis Report</title></head>
<body style="font-family: Arial, sans-serif; margin:20px">
<h1>Log Analysis Report</h1>
<h2>Summary</h2>
<pre>{{ summary | tojson(indent=2) }}</pre>
<h2>Anomalies</h2>
{% if anomalies %}
<table border="1" cellpadding="6" cellspacing="0">
<thead><tr>{% for k in keys %}<th>{{ k }}</th>{% endfor %}</tr></thead>
<tbody>
{% for a in anomalies %}
<tr>{% for k in keys %}<td>{{ a.get(k, '') }}</td>{% endfor %}</tr>
{% endfor %}
</tbody>
</table>
{% else %}
<p>No anomalies found.</p>
{% endif %}
</body>
</html>
""")



def export_json(path: str, summary: Dict[str, Any], anomalies: List[Dict[str, Any]]) -> None:
    payload = {"summary": summary, "anomalies": anomalies}
    Path(path).write_text(json.dumps(payload, default=str, indent=2), encoding="utf-8")




def export_csv(path: str, anomalies: List[Dict[str, Any]]) -> None:
    if not anomalies:
        Path(path).write_text("", encoding="utf-8"); return
    keys = sorted({k for a in anomalies for k in a.keys()})
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for a in anomalies:
            w.writerow({k: a.get(k, "") for k in keys})
            
