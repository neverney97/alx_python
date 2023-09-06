"""
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

You must use the packages requests and sys
You are not allow to import other packages than requests and sys
The value of this variable is different for each request
You don’t need to check script arguments (number and type)
"""

import requests
import sys

# Check if the URL argument is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

# Get the URL from the command line argument
url = sys.argv[1]

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Try to access the 'X-Request-Id' header and display its value
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")
else:
    print("Error: Unable to retrieve data from the URL. Status code:", response.status_code)
