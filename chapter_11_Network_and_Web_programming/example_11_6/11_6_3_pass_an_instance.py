from xmlrpc.client import ServerProxy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(1, 2)
server = ServerProxy('http://localhost:15000')
print(point)
server.set('p', point)
print(server.get('p'))
