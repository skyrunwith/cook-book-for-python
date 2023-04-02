"""
The socket option shown is actually very common setting that allows the server to
rebind to a previously used port number. It's actually so common that it's class
variable that can be set on `TCPServer`. Set it before instantiating the server.
"""
from socketserver import TCPServer


if __name__ == "__main__":
    TCPServer.allow_reuse_address = True
    server = TCPServer(('', 20000), 'Echohandler')
    server.serve_forever()