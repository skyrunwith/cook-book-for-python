"""
`socketserver` makes it relatively easy to create a TCP servers. However, you should be aware that,
By default, the servers are single threaded that can only serve one client at a time. If you want
to handle multiple clients, either use a `ForkingTCPServer` or `ThreadingTCPServer`

One issue with forking and threaded is that they spawn a new process and thread on each client connection.
There is no upper bound for the number of allowed clients. so a malicious hacker could potentially
launch a large number of simultaneous connection in an effort to make your server explode.

If this is a concern, you can create a `pre-allocated pool` of work threads or processes.
To do this, you create an instance of a normal nonthreaded server, but launch the `serve_server()` method
in a pool of multiple threads.
"""
from socketserver import ForkingTCPServer, ThreadingTCPServer

# nonthread server(pre-allocated pool)
from socketserver import TCPServer

if __name__ == '__main__':
    server = TCPServer(('', 20000), 'EchoHandler')
    Nworkers = 16
    from threading import Thread
    for i in range(Nworkers):
        t = Thread(target=server.serve_forever)
        t.daemon = True
        t.start()

    server.serve_forever()
