from typing import Dict, List, Any
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import json


console = Console()


def print_summary(summary: Dict[str, Any]) -> None:
    console.rule("[bold cyan]Analysis Summary")
    t = Table(show_header=False, box=box.SIMPLE)
    t.add_column("Metric")
    t.add_column("Value", overflow="fold")
    t.add_row("Total rows", str(summary.get("total_rows", 0)))
    if "status_counts" in summary:
        t.add_row("Status counts", json.dumps(summary["status_counts"]))
        t.add_row("4xx", str(summary.get("4xx", 0)))
        t.add_row("5xx", str(summary.get("5xx", 0)))
    t.add_row("Top IPs", "\n".join(f"{k}: {v}" for k, v in summary.get("top_ips", {}).items()) or "N/A")
    console.print(t)



def print_anomalies(anomalies: List[Dict[str, Any]]) -> None:
    console.rule("[bold red]Anomalies")
    if not anomalies:
        console.print(Panel("[green]No anomalies detected[/green]"))
        return
    # Build flexible table of keys
    keys = sorted({k for a in anomalies for k in a.keys()})
    table = Table(*keys, box=box.MINIMAL, header_style="bold yellow")
    for a in anomalies:
        row = [str(a.get(k, "")) for k in keys]
        table.add_row(*row)
    console.print(table)

    