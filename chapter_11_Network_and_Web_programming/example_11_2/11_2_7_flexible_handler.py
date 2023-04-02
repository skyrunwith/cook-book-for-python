"""
In the solution, two different base handler class shown(BaseRequestHandler and StreamRequestHandler).
The `StreamRequestHandler` class is a bit more flexible, and supports some features that can be
enabled through the specification of additional class variables.
"""
from socketserver import StreamRequestHandler
import socket


class EchoHandler(StreamRequestHandler):
    # optional settings (default as shown)
    timeout = 5  # time on all socket operations
    rbufsize = -1  # Read buffer size
    wbufsize = 0  # Write buffer size
    disable_nagle_algorithm = False  # set TCP_NODELAY socket option
    def handle(self):
        print('Got connection from', self.client_address)
        try:
            for line in self.rfile:
                self.wfile.write(line)
        except socket.timeout:
            print('Time out')

