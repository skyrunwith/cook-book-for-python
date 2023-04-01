import requests

"""
A notable feature of requests is how it returns the resulting response content from a request.
As shown, the `resp.text` attribute gives you `the Unicode decoded text` from a request.
However, If you access 'resp.content', you get `the raw binary content` instead.
On the other hand, If you access `resp.json`, then you get `the response content interpreted as JSON`.    
"""

# Here is an example of using requsest to make a `HEAD` request, and extract a few fields from
# header data from the response.

url = "https://www.python.org"

resp = requests.head(url)

print(resp.status_code)
print(resp.headers['Content-Length'])

# Here is a requests example that executes a login into the Python Package index using Basic Authentication.

requests.get('http://pypi.python.org/pypi?:action=login', auth=('username', 'password'))

# Here is an example of using requests to pass it HTTP Cookies from one request result to the next.
# First request
resp = requests.get('http://httpbin.org/get')

# Second request
resp = requests.get('http://httpbin.org/get', cookies=resp.cookies)

# Last but not least, here is an example of using requests to upload content.
url = 'http://httpbin.org/post'

files = {'files': ('data.csv', open('data.csv'))}

requests.post(url, files=files)
