from socketserver import UDPServer, BaseRequestHandler
import time


class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)

        # Get msg and client socket
        msg, sock = self.request
        print(msg)
        reps = time.ctime()
        sock.sendto(reps.encode('ascii'), self.client_address)


if __name__ == '__main__':
    server = UDPServer(('', 20000), TimeHandler)
    server.serve_forever()