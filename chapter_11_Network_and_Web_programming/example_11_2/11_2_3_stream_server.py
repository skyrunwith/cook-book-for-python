from socketserver import StreamRequestHandler, TCPServer


"""
In many cases, it's easier to define a slightly different kind of handler.
Here is an example that uses the `StreamRequestHandler` base class to
put a file-like object on the underlying socket.
"""


class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            # self.rfile is a file-like object for reading
            for line in self.rfile:
                # self.wfile is a file-like object for writing
                self.wfile.write(line)


if __name__ == '__main__':
    server = TCPServer(('', 20000), EchoHandler)
    server.serve_forever()
