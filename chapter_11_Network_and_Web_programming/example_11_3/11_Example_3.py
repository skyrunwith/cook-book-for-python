"""
Creating a UDPServer
Problem
    you want to implement a server that communicates with clients using the UDP internet protocol.
Solution
    As with TCP, UDP servers are also very easy to create using the `socketserver` library.
Discussion
    A typical UPD server receives an incoming datagram along with a client address. If the server is to respond,
    the server send a datagram back to the client. For transmission of datagrams, you should use `sendto` and
    `recvfrom`methods of a socket. Although the the traditional `send` and `recv` methods also might work,
    The former two methods are more commonly used with UDP communication.

    Given that there is no underlying connections, the UDP server is much easier to write than TCP server.
    However, UPD is also inherently unreliable(e.g., no `connection` is established and messages might be lost).
    Thus, it would be up to you figure out how to deal with lost messages. That's a topic beyond the scope of
    this book, but typically you might need to introduce sequence numbers, retries, timeouts, and other mechanisms
    to ensure reliability if it matters for your application. UDP is often used in case where the requirement of
    reliable delivery can be relaxed. For instances, in real-time application such as multimedia streams and games
    where there is simply no option to go back in time and recover the lost packet(the program simply skips it and
    keeps moving forward)

    The UDPServer class is single threaded, which means only one request can be serviced at a time. In practice,
    this is less of an issue with UDP than with TCP connections. However should you want to concurrent operations,
    instantiate `ForkingUDPServer` or `ThreadingUDPServer`.
"""

__author__ = 'Frankie Fu'

import time
# Implement a UDP server directly using sockets is also not difficult.
from socket import socket, AF_INET, SOCK_DGRAM


def time_server(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(address)
    while True:
        msg, addr = sock.recvfrom(8192)
        print('Got connection from', addr)
        print(msg)
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), addr)


if __name__ == '__main__':
    time_server(('', 20000))
