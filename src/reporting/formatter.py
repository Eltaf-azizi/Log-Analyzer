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