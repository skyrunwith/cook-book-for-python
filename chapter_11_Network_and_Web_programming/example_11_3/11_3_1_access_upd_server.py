""""
As before, you deine a handler class that contains a `handler` method for servicing clients connections.
The `request` attribute is a tuple that contains the incoming `datagrams` and
the underlying client socket object for the server. The client_address contains the client address.
"""

# To test it, run it the open a seperate process that send msg to the server.
import socket


if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.sendto(b'Hello', ('', 20000))
    print(socket.recv(8192))
