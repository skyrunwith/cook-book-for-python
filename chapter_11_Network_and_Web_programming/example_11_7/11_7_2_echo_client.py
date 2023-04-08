"""
Using `multiprocessing.connection` client
"""
from multiprocessing.connection import Client


if __name__ == '__main__':
    client = Client(('', 25000), authkey=b'peekaboo')
    client.send(b'Hello')
    print(client.recv())

    client.send(42)
    print(client.recv())

    client.send([1, 2, 3, 4, 5])
    print(client.recv())

    client.close()