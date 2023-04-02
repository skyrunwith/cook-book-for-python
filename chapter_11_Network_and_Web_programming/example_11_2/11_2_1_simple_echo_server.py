from socketserver import BaseRequestHandler, TCPServer

"""
In this code, you define a special handler class that implements a `handle()` method for
servicing client connections. The `request` attribute is the underlying client socket 
and `client_address` has client address.
"""


class EchoServer(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(1)
            if not msg:
                break
            self.request.send(msg)


if __name__ == '__main__':
    server = TCPServer(('', 20000), EchoServer)
    server.serve_forever()
