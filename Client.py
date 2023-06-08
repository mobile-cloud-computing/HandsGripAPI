import requests

# Define the URL endpoint where you expect to receive the JSON data
url = "http://127.0.0.1:8000/test"

# Create a sample JSON payload
json_payload = {
    "light": 0.273793,
    "gender": 0,
    "size": 0,
    "age": 0.2
}
# Send the HTTP POST request with the JSON payload
response = requests.post(url, json=json_payload)

# Check the response status code
if response.status_code == 200:
    # Successful request
    print("JSON data received successfully!")
    print(response.json())
else:
    # Request failed
    print("Failed to receive JSON data. Status code:", response.status_code)