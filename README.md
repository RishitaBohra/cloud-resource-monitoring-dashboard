# Cloud Resource Monitoring Dashboard

A Python-based cloud monitoring and cost analysis dashboard that provides insights into resource utilization and cloud spending trends through an interactive command-line interface.

The dashboard simulates cloud monitoring workflows by tracking CPU utilization metrics, analyzing cost patterns, and generating intelligent summaries to support operational decision-making and resource optimization.

## Overview

Cloud environments generate large amounts of operational and cost-related data. Monitoring this information manually can be time-consuming and inefficient.

This project provides:

* Resource utilization monitoring
* Cost trend analysis
* Daily usage summaries
* Intelligent insight generation
* Terminal-based dashboard visualization

## Features

### Resource Monitoring

* Tracks CPU utilization metrics
* Displays historical usage patterns
* Provides utilization summaries
* Supports operational monitoring workflows

### Cost Analysis

* Tracks cloud spending trends
* Displays daily cost summaries
* Provides visibility into resource consumption
* Helps identify optimization opportunities

### Insight Engine

* Generates automated usage summaries
* Analyzes utilization patterns
* Highlights potential efficiency improvements
* Provides trend-based observations

### Dashboard Interface

* Interactive terminal dashboard
* Auto-refreshing metric display
* Structured tabular reporting
* Lightweight and easy to use

## Technology Stack

| Component              | Technology          |
| ---------------------- | ------------------- |
| Language               | Python 3            |
| Cloud SDK              | Boto3               |
| CLI Framework          | Rich                |
| Data Processing        | Pandas              |
| Scheduling             | Schedule            |
| Environment Management | Python-dotenv       |
| Analytics Engine       | Custom Python Logic |

## Project Structure

```text
Cloud-Resource-Monitoring-Dashboard/
│
├── cli_dashboard.py
├── daily_summary.py
├── insight_ai.py
├── requirements.txt
├── assets/
└── README.md
```

### File Description

| File             | Purpose                            |
| ---------------- | ---------------------------------- |
| cli_dashboard.py | Main dashboard interface           |
| daily_summary.py | Generates usage and cost summaries |
| insight_ai.py    | Insight generation module          |
| requirements.txt | Project dependencies               |
| assets/          | Project assets and screenshots     |

## Installation

### Clone Repository

```bash
git clone https://github.com/RishitaBohra/cloud-resource-monitoring-dashboard.git
cd cloud-resource-monitoring-dashboard
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python cli_dashboard.py
```

## Sample Output

### CPU Utilization

```text
Time    Avg CPU (%)
08:00   12.4
09:00   18.2
10:00   24.8
11:00   15.6
12:00   20.1
13:00   28.7
14:00   17.5
15:00   22.9
```

### Cost Summary

```text
Date          Cost ($)
2026-05-28    0.15
2026-05-29    0.22
2026-05-30    0.18
2026-05-31    0.27
2026-06-01    0.19
2026-06-02    0.21
2026-06-03    0.24
```

### Generated Insight

```text
Resource utilization remains within normal operating range.
No unusual CPU spikes detected.
Cloud spending trend appears stable.
Continued monitoring recommended for optimization opportunities.
```

## Skills Demonstrated

* Cloud Monitoring Concepts
* AWS CloudWatch Integration
* Python Automation
* Data Processing and Analysis
* Command-Line Application Development
* Operational Monitoring
* Cost Analysis and Reporting

## Future Enhancements

* Real AWS CloudWatch integration
* Service-wise cost breakdown
* Historical trend visualization
* Email alert notifications
* Resource optimization recommendations
* Dashboard export functionality

## Author

Rishita Bohra

GitHub: https://github.com/RishitaBohra
LinkedIn: https://www.linkedin.com/in/rishita-bohra-0b8095326

## License

This project is intended for educational and portfolio purposes.








