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
