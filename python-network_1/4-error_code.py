"""
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
Please test your script in the container provided, using the web server running on port 5000
"""

# Import the requests and sys modules
import requests
import sys

# Check if the URL is provided
if len(sys.argv) != 2:
    sys.exit(1)

# Get url from comand line
url = sys.argv[1]

# Send an HTTP get request from the url
response = requests.get(url)

# Display the body of the response
print(response.text)

# CHeck if the status code is greater than or equal to 400, indicating an error
if response.status_code == 400:
    print(f"Error code: {response.status_code}")
