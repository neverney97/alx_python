"""
Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a personal access token as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""

# Imprt requests and sys modules
import requests
import sys

# Username variable
username = 'neverney97'

# My Access token
access_token = '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'

# Define the API endpoint for my information
url = f'https://api.github.com/users/neverney97'

# Creat a Basic Authentication hedader with the access token
headers = {
    'Authorization': f'Basic neverney97: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'
}

# Send a GET response to the GitHub API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # parse the JSON response
    user_data = response.json()
    #Display the user's ID
    print(f"GitHub User ID: {user_data['id']}")

