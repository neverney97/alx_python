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

# Check if the URL and email arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

# Get the URL and email from the command line arguments
url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the email parameter
data = {'email': email}

# Send an HTTP POST request to the URL with the email parameter
response = requests.post(url, data=data)

# Check if the request was successful
if response.status_code == 200:
    # Display the body of the response
    print(response.text)
else:
    print("Error: Unable to retrieve data from the URL. Status code:", response.status_code)

