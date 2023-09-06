"""
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

The email must be sent in the variable email
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to error check arguments passed to the script (number or type)
Please test your script in the container provided, using the web server running on port 5000
"""

# Import the requests and sys modules
import requests
import sys

# Check if the url and email argument is provided
if len(sys.argv) != 2:
    sys.exit(1)

# Get URL from command line argument
url = sys.argv[1]

# Get email from command line argument
email = sys.argv[2]

# Create a dictionary with the email parameter
data = {'email': email}

# Send an HTTP request to the url
req = requests.post(url, data=data)

# Print the response
print(req.text)


