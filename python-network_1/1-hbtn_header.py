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
res = requests.get(url)

# Checking the value of the variable X-Request-Id
print(res.headers['X-Request-Id'])
