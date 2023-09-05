"""
Write a Python script that fetches https://alu-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following example (tabulation before -)
"""
import requests
"""
This statement imports the requests module
what does this module or library do? It is a library for making HTTP requests.
"""

request = requests.get("https://alu-intranet.htbn.io/status")
"""
This fetches the links in the quotes

"""
