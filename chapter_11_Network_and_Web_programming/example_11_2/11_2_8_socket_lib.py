"""
Finally, it should be noted that most of Python's high-level networking modules
(e.g., HTTP, XML_RPC, etc.) are built on top of `socketserver` functionality.
This is said, it is not difficult to implement servers using the `socket` library.
"""

# Here is a simple example of directly programing with the `Sockets`
from socket import socket, AF_INET, SOCK_STREAM


def echo_handler(client, client_address):
    print('Got connection from', client_address)
    while True:
        msg = client.recv(8192)
        if not msg:
            break
        client.send(msg)
    client.close()


def echo_server(address, backlog=5):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(address)
    server.listen(backlog)
    while True:
        client, client_address = server.accept()
        echo_handler(client, client_address)


if __name__ == '__main__':
    echo_server(('', 20000), 5)

