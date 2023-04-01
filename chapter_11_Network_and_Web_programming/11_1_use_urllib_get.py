from urllib import request, parse


"""
It's usually easy enough to use the `urllib.request` module, 
to send a simple `GET` HTTP request to a remote service.
"""
# Base url being accessed
url = 'http://httpbin.org/get'

# Dictionary of query parameters(if any)
query = {
    "name1": "value1",
    "name2": "value2"
}

# Encode the query parameters
querystr = parse.urlencode(query)
print(querystr)

# Make a GET request and read a response
u = request.urlopen(url + '?' + querystr)
print(u.read())
