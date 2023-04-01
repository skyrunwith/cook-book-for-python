from urllib import request, parse
from urllib.request import urlopen

"""
If you need to supply some Custom HTTP headers in the outgoing request such as a change to 
the user-agent field, make a dictionary container their value and create a `Request` instance
and pass it to `urlopen()`
"""

# Based url being accessed
url = "http://httpbin.org/post"

# Dictionary of query parameters(if any)
params = {
    "name1": "value1",
    "name2": "value2",
}

# Encode the query string
query_string = parse.urlencode(params)

# Extra headers
headers = {
    'User-Agent': "none"
}
req = request.Request(url, query_string.encode('ascii'), headers=headers)
# Make a request and read the response
resp = urlopen(req)
print(resp.read())