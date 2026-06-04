import boto3
import datetime
import time
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from insight_ai import generate_ai_summary  # 👈 Added import

console = Console()
cloudwatch = boto3.client('cloudwatch', region_name='ap-south-1')
ce = boto3.client('ce', region_name='ap-south-1')

def get_cpu_metrics():
    return [
        ("08:00", 12.4),
        ("09:00", 18.2),
        ("10:00", 24.8),
        ("11:00", 15.6),
        ("12:00", 20.1),
        ("13:00", 28.7),
        ("14:00", 17.5),
        ("15:00", 22.9)
    ]
    data = []
    for dp in sorted(response['Datapoints'], key=lambda x: x['Timestamp']):
        data.append((dp['Timestamp'].strftime('%H:%M UTC'), round(dp['Average'], 2)))
    return data

def get_cost_summary():
    return [
        ("2026-05-28", 0.15),
        ("2026-05-29", 0.22),
        ("2026-05-30", 0.18),
        ("2026-05-31", 0.27),
        ("2026-06-01", 0.19),
        ("2026-06-02", 0.21),
        ("2026-06-03", 0.24)
    ]
   

def render_dashboard():
    cpu_data = get_cpu_metrics()
    cost_data = get_cost_summary()

    # 🧠 AI Summary Data Prep
    cpu_values = [avg for _, avg in cpu_data]
    cpu_avg = sum(cpu_values) / len(cpu_values) if cpu_values else None
    total_cost = sum(amount for _, amount in cost_data) if cost_data else None

    ai_summary = generate_ai_summary(cpu_avg, total_cost)  # 👈 Generate smart insights

    # 🧩 CPU Table
    cpu_table = Table(title="🧠 CloudWatch CPU Utilization (Last 12 hrs)")
    cpu_table.add_column("Time", style="cyan")
    cpu_table.add_column("Avg CPU (%)", style="magenta")
    if cpu_data:
        for t, avg in cpu_data[-10:]:
            cpu_table.add_row(t, str(avg))
    else:
        cpu_table.add_row("—", "No data")

    # 💰 Cost Table
    cost_table = Table(title="💰 AWS Cost (Last 7 Days)")
    cost_table.add_column("Date", style="green")
    cost_table.add_column("Cost ($)", style="yellow")
    for d, c in cost_data:
        cost_table.add_row(d, f"{c:.4f}")

    # 🤖 InsightAI Panel
    ai_panel = Panel(ai_summary, title="🤖 InsightAI Summary", border_style="bold blue")

    # Combine all
    layout = Table.grid()
    layout.add_row(cpu_table)
    layout.add_row(cost_table)
    layout.add_row(ai_panel)

    return layout

def main():
    with Live(console=console, refresh_per_second=1):
        while True:
            console.clear()
            dashboard = render_dashboard()
            console.print(dashboard)
            console.print("\n[dim]Updating every 30 seconds... Press Ctrl + C to exit.[/dim]")
            time.sleep(30)

if __name__ == "__main__":
    main()
