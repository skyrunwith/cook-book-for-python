from xmlrpc.client import ServerProxy


s = ServerProxy('https://localhost:15000', allow_none=True)
s.set('foo', 1)
print(s.get('foo'))

s.set('spam', [1, 2, 3])
print(s.get('spam'))

s.delete('spam')
print(s.exists('spam'))

print(s.keys())