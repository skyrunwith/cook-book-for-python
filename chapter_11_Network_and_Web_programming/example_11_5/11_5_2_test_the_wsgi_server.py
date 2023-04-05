# To test the server, you can interact with it using a browser or `urllib`
from urllib.request import urlopen

u = urlopen('http://localhost:8000/hello?name=frankie')
print(u.read().decode('utf-8'))
