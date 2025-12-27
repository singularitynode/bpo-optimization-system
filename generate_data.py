import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import random
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Generate Agents (20)
np.random.seed(42)
departments = ['Billing', 'Sales', 'Customer Service', 'Technical Support']
statuses = ['active', 'offline', 'training', 'break']
agents_data = []
for i in range(1, 21):
    dept = random.choice(departments)
    perf = round(np.random.normal(80, 10), 1)
    perf = max(50, min(100, perf))
    status = random.choice(statuses)
    hire_date = (datetime.now() - timedelta(days=random.randint(1, 1460))).date().isoformat()  # up to 4 years
    avg_handle = round(np.random.normal(120, 60), 0)
    avg_handle = max(30, avg_handle)
    tickets_res = random.randint(30, 60)
    csat = round(np.random.normal(4.2, 0.5), 1)
    csat = max(1, min(5, csat))
    agents_data.append({
        'agent_id': i,
        'name': f"Agent {i}",
        'department': dept,
        'performance_score': perf,
        'status': status,
        'hire_date': str(hire_date),
        'avg_handle_time': avg_handle,
        'tickets_resolved': tickets_res,
        'csat_score': csat
    })
agents_df = pd.DataFrame(agents_data)

# Generate Tickets (100)
issue_types = ['Product Inquiry', 'Billing Inquiry', 'Service Complaint', 'Technical Support', 'Account Access']
priorities = ['low', 'medium', 'high']
statuses_t = ['resolved', 'pending', 'open', 'in-progress']
tickets_data = []
start_date = datetime(2025, 12, 1)
for i in range(1, 101):
    created = start_date + timedelta(days=random.randint(0,22), hours=random.randint(0,23), minutes=random.randint(0,59))
    issue = random.choice(issue_types)
    prio = random.choices(priorities, weights=[0.3, 0.5, 0.2])[0]
    stat = random.choice(statuses_t)
    agent = random.randint(1,20)
    handle = round(np.random.exponential(90), 0) if stat != 'pending' else np.nan
    csat = round(np.random.normal(4.1, 0.6), 1) if stat == 'resolved' else np.nan
    csat = max(1, min(5, csat)) if not np.isnan(csat) else csat
    resolved = None
    if stat == 'resolved':
        resolved = created + timedelta(minutes=handle)
    tickets_data.append({
        'ticket_id': f"TKT-{i:05d}",
        'customer_name': f"Customer {i}",
        'issue_type': issue,
        'priority': prio,
        'status': stat,
        'created_date': created.isoformat(),
        'resolved_date': resolved.isoformat() if resolved else None,
        'assigned_agent': agent,
        'handle_time': handle,
        'csat_feedback': csat
    })
tickets_df = pd.DataFrame(tickets_data)

# Generate Accounts (5)
account_names = ['Telco Voice Account', 'Hotel Lodging Chat', 'E-commerce Support', 'Healthcare BPO', 'Finance & Banking']
account_types = ['Telecommunications', 'Hospitality', 'Retail', 'Medical', 'Financial']
account_statuses = ['active', 'active', 'warning', 'active', 'critical']
accounts_data = []
for i in range(1, 6):
    accounts_data.append({
        'account_id': i,
        'name': account_names[i-1],
        'type': account_types[i-1],
        'num_agents': random.randint(15, 30),
        'status': account_statuses[i-1],
        'monthly_revenue': round(random.uniform(4.0, 12.0), 1),
        'cost_per_ticket': round(random.uniform(60, 150), 0),
        'tickets_volume': random.randint(400, 600)
    })
accounts_df = pd.DataFrame(accounts_data)

# Generate Daily Metrics (7 days x 5 types)
dates = [datetime(2025, 12, 16) + timedelta(days=i) for i in range(7)]
metric_types = ['service_level', 'cost_reduction', 'fcr_rate', 'csat', 'queue_wait']
metrics_data = []
for date in dates:
    for mtype in metric_types:
        if mtype == 'service_level':
            val = round(np.random.normal(90, 3), 2)
        elif mtype == 'cost_reduction':
            val = round(np.random.normal(80, 5), 2)
        elif mtype == 'fcr_rate':
            val = round(np.random.normal(78, 4), 2)
        elif mtype == 'csat':
            val = round(np.random.normal(4.2, 0.3), 2)
        else:  # queue_wait
            val = round(np.random.normal(5, 1.5), 2)
        metrics_data.append({
            'date': date.isoformat(),
            'metric_type': mtype,
            'value': val
        })
metrics_df = pd.DataFrame(metrics_data)

# Generate Alerts (10)
alert_types = ['danger', 'warning', 'info', 'success']
alert_titles = [
    'Low CSAT Alert', 'Cost Spike Detected', 'Performance Drop Alert', 'Queue Building Warning',
    'Optimization Complete', 'System Maintenance', 'High Priority Ticket Surge', 'Agent Training Required',
    'Revenue Target Met', 'Critical Bug Fix Needed'
]
alerts_data = []
for i in range(1, 11):
    atype = random.choice(alert_types)
    title = random.choice(alert_titles)
    message = f"Detailed description for {title.lower()} here. Generated on {datetime.now().isoformat()}. Action required: Review and resolve."
    timestamp = datetime.now() - timedelta(hours=random.randint(1, 48))
    resolved = random.choice([True, False])
    alerts_data.append({
        'alert_id': i,
        'title': title,
        'message': message,
        'type': atype,
        'timestamp': timestamp.isoformat(),
        'resolved': resolved
    })
alerts_df = pd.DataFrame(alerts_data)

# Compute Analytics
# Agent Performance by Department
dept_summary = agents_df.groupby('department').agg({
    'performance_score': ['mean', 'std', lambda x: (x > 90).sum()],
    'tickets_resolved': 'sum',
    'csat_score': 'mean'
}).round(2)
dept_summary.columns = ['Avg Perf %', 'Perf Std', 'High Performers (>90%)', 'Total Tickets Resolved', 'Avg CSAT (/5)']
dept_summary = dept_summary.reset_index()

# Ticket Stats by Issue Type
ticket_stats = tickets_df.groupby('issue_type').agg({
    'handle_time': ['mean', 'median'],
    'priority': lambda x: (x == 'high').sum(),
    'status': lambda x: (x == 'resolved').sum(),
    'csat_feedback': lambda x: x.dropna().mean()
}).round(2)
ticket_stats.columns = ['Avg Handle Time (min)', 'Median Handle Time (min)', 'High Priority Count', 'Resolved Count', 'Avg CSAT (/5)']
ticket_stats = ticket_stats.reset_index()

# Financial Impact
baseline_cost = 100
avg_handle_min = tickets_df['handle_time'].mean()
optimized_cost_per_ticket = round((avg_handle_min / 60) * 20 + 50, 1)  # Simplified model: ₱20/min + base
monthly_tickets = 1000  # Assumption
monthly_savings = round((baseline_cost - optimized_cost_per_ticket) * monthly_tickets, 0)
annual_savings = round(monthly_savings * 12, 0)
roi_timeline = '3 days'
confidence = 99.8

# Predictive Insights (Service Level Forecast)
service_levels = metrics_df[metrics_df['metric_type'] == 'service_level']['value'].values
X = np.arange(len(service_levels)).reshape(-1, 1)
y = service_levels
model = LinearRegression().fit(X, y)
next_week = model.predict([[len(service_levels)]])[0]
r2 = round(r2_score(y, model.predict(X)), 3)
trend = 'up' if next_week > service_levels[-1] else 'down'

# Correlation Matrix (Sample on tickets + agents)
corr_df = tickets_df.merge(agents_df[['agent_id', 'performance_score']], left_on='assigned_agent', right_on='agent_id', how='left')
corr_df = corr_df[['handle_time', 'csat_feedback', 'priority', 'performance_score']].dropna()
priority_num = corr_df['priority'].map({'low': 1, 'medium': 2, 'high': 3})
corr_matrix = pd.concat([corr_df[['handle_time', 'csat_feedback', 'performance_score']], priority_num], axis=1).corr().round(3)

# Key Insights (Hardcoded based on data)
avg_agent_perf = round(agents_df['performance_score'].mean(), 1)
overall_csat = round(tickets_df['csat_feedback'].mean(), 1)
avg_handle_time = round(tickets_df['handle_time'].mean(), 1)
high_priority_count = len(tickets_df[tickets_df['priority'] == 'high'])
high_priority_pct = round((high_priority_count / len(tickets_df)) * 100, 1)

# Full JSON Output
full_data = {
    'metadata': {
        'generated_on': datetime.now().isoformat(),
        'total_agents': len(agents_df),
        'total_tickets': len(tickets_df),
        'total_accounts': len(accounts_df),
        'metrics_period_days': 7
    },
    'entities': {
        'agents': agents_df.to_dict('records'),
        'tickets': tickets_df.to_dict('records'),
        'accounts': accounts_df.to_dict('records'),
        'daily_metrics': metrics_df.to_dict('records'),
        'alerts': alerts_df.to_dict('records')
    },
    'analytics': {
        'agent_performance_by_dept': dept_summary.to_dict('records'),
        'ticket_stats_by_issue': ticket_stats.to_dict('records'),
        'financial_impact': {
            'baseline_cost_per_ticket': baseline_cost,
            'optimized_cost_per_ticket': float(optimized_cost_per_ticket),
            'monthly_savings': monthly_savings,
            'annual_savings': annual_savings,
            'roi_timeline': roi_timeline,
            'confidence': confidence
        },
        'predictive_insights': {
            'service_level_forecast_next_week': round(next_week, 1),
            'current_service_level': float(service_levels[-1]),
            'trend': trend,
            'model_r2': r2
        },
        'correlation_matrix': corr_matrix.to_dict(),
        'key_insights': {
            'avg_agent_performance': avg_agent_perf,
            'overall_csat': overall_csat,
            'avg_handle_time_min': avg_handle_time,
            'high_priority_tickets_count': high_priority_count,
            'high_priority_tickets_pct': high_priority_pct
        }
    }
}

print(json.dumps(full_data, indent=2, default=str))