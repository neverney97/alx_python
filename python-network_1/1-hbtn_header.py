"""
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

You must use the packages requests and sys
You are not allow to import other packages than requests and sys
The value of this variable is different for each request
You don’t need to check script arguments (number and type)
"""

# Import the requests and sys packages
import requests
import sys

# The url name
url = 'https://alu-intranet.hbtn.io/status'

# Send an HTTP GET request to the url
req = requests.get(url)

# Check if the request was successful
if req.status_code == 200:
    # Try to access the 'X-Request-Id' header and display its value
    x_request_id = req.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")
else:
    print("Error: Unable to retrieve data from the URL. Status code:", req.status_code)
