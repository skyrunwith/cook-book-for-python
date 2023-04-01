from urllib import request, parse
from urllib.request import urlopen

"""
If you need to send the query parameters in the request body using the `POST` method,
Encode them and supply them as an optional argument to `urlopen()`
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
print(query_string.encode('ascii'))
# Make a request and read the response
resp = urlopen(url, query_string.encode('ascii'))
print(resp.read())