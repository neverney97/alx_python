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

# Replace 'YOUR_USERNAME' with your GitHub username (neverney97)
username = 'neverney97'

# Replace 'YOUR_ACCESS_TOKEN' with your GitHub personal access token
access_token = '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'

# Define the API endpoint for the user's information
url = f'https://api.github.com/users/{username}'

# Create a Basic Authentication header with the access token
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Send a GET request to the GitHub API
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    user_data = response.json()
    # Display the user's ID
    print(f"GitHub User ID: {user_data['id']}")
else:
    print("None")

