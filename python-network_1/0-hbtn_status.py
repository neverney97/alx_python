"""
Write a Python script that fetches https://alu-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following example (tabulation before -)
"""
# Import the requests package
import requests

# Define the URL to fetch data from
url = 'https://alu-intranet.hbtn.io/status'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Print the response body with appropriate tabulation
print("Body response:")

# Display the type of the response content
print("\t- type:", type(response.text))

# Display the content of the response
print("\t- content:", response.text)
