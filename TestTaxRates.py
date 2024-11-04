import requests
import json

# URL to fetch local tax rates from Ohio Department of Taxation's Finder tool
url = "https://ohio.gov/wps/portal/gov/site/residents/resources/local-tax-information"

# Send a request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response content
    data = response.json()

    # Extract local tax rates (assuming they are stored under a key named 'local_tax_rates')
    local_tax_rates = data.get('local_tax_rates', [])

    # Convert the local tax rates to JSON format
    local_tax_rates_json = json.dumps(local_tax_rates, indent=4)

    # Save the JSON data to a file
    with open('local_tax_rates_ohio.json', 'w') as json_file:
        json_file.write(local_tax_rates_json)

    print("Local tax rates saved to local_tax_rates_ohio.json")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
