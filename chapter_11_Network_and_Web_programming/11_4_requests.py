import requests

"""
If your interaction with a service is more compliant than this, you should probably 
look at `requests lib`(http://pypi.python.org/pypi/requests). 
For example, here is equivalent `requests` code for the preceding opeations.  
"""

# Based url being accessed
url = "http://httpbin.org/post"

# Dictionary of query parameters(if any)
params = {
    "name1": "value1",
    "name2": "value2",
}

# Extra headers
headers = {
    'User-Agent': "none"
}

# Make a request and read the response
resp = requests.post(url, data=params, headers=headers)
# Decoded text returned by requests
print(resp.text)
