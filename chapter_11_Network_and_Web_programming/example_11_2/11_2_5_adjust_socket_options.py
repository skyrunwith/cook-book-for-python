"""
Normally, a `TCPServer` binds and activates the underlying socket upon instantiation.
However, sometimes you might want to adjust the underlying socket by setting options.
To do this, supply the `bind_and_activate=False` argument.
"""
from socketserver import TCPServer
import socket

if __name__ == '__main__':
    server = TCPServer(('localhost', 20000), 'EchoHandler', bind_and_activate=False)
    # set up various socket options
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # Bind and activate
    server.server_bind()
    server.server_activate()
    server.serve_forever()
