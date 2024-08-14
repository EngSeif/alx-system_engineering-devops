#!/usr/bin/python3
import requests

api_key = '3be1cadd387eeecd97d47682faf1c755'
app_key = 'd7657dd9db02742cd6c44ac84aba9b0fe0637aed'
dashboard_name = 'I/O Requests Monitoring'  # Replace with your dashboard name

url = "https://api.datadoghq.com/api/v1/dashboard"
params = {
    'api_key': api_key,
    'application_key': app_key,
}

response = requests.get(url, params=params)

if response.status_code == 200:
    dashboards = response.json().get('dashboards', [])
    dashboard_id = None
    for dashboard in dashboards:
        if dashboard.get('title') == dashboard_name:
            dashboard_id = dashboard.get('id')
            break

    if dashboard_id:
        print(f"Dashboard ID: {dashboard_id}")
        # Write the dashboard_id to the answer file
        with open('2-setup_datadog', 'w') as file:
            file.write(dashboard_id)
    else:
        print("Dashboard not found.")
else:
    print(f"Failed to retrieve dashboards: {response.status_code}")
