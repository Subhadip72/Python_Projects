import json
import requests

url = "https://data.covid19india.org/v4/min/timeseries.min.json"

response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()

    print(json.dumps(json_data, indent=4))
else:
    print("Failed to fetch data. Status code:", response.status_code)
