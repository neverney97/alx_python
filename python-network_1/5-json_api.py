"""
Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
Please test your script in the container provided, using the web server running on port 5000. All JSON generated by this server are random.
"""
# Import requests and sys modules
import requests
import sys

# Define the url for the POST request
url = 'http://0.0.0.0:5000/search_user'

# Set the letter parameter 'q' based on command-line argument or defualt to an empty string
if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""

# Create a dictionary with thee 'q' parameter
data = {'q': q}

# Send a POST request to the URL with the letter as a parameter
response = requests.post(url, data=data)

try:
    #Attempt to parse the JSON response
    json_response = response.json()
    if json_response:
        # Display the id and name if the JSON is valid and not empty
        print("[{}] {}".format(json_response['id'], json_response['name']))
    else:
        # Display no result if JSON is empty
        print("No result")
except ValueError:
    # Display not a valid JSON result if JSON is invalid
    print("No result")
