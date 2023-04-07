from xmlrpc.client import ServerProxy


server = ServerProxy('http://localhost:15000')
server.set('foo', b'Hello, world')
_ = server.get('foo')
print(_)
print(_.data)
