import csv
import requests
import json

# Set the REMOVED API endpoint URL
url = "http://localhost:8080"

# Set your REMOVED API credentials
email = "your_email@your_domain.com"
token = "your_api_token"

# Set the CSV file path
csv_file = "labels.csv"

# Open the CSV file and read the data
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header row
    for row in reader:
        # Extract label data from the CSV file
        label_name = row[0]
        agent_list = row[1].split(',')

        # Set the JSON payload for the API request
        payload = {
            "name": label_name,
            "agents": agent_list
        }

        # Set the HTTP headers for the API request
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        # Set the authentication credentials for the API request
        auth = (email, token)

        # Send the API request
        response = requests.post(url, auth=auth, headers=headers, data=json.dumps(payload))

        # Check if the request was successful
        if not response:
            print(f"request for {payload} failed with status code {response.status_code}: {response.reason}")
        else:
            # Print something about the successful request
            print(response.content.decode('utf-8'))
