import struct
import socket


def send_fd(sock, fd):
    """
    Send a single file descriptor
    """
    sock.sendmsg([b'x'], [(socket.SOL_SOCKET, socket.SCM_RIGHTS, struct.pack('i', fd))])
    ack = sock.recv(2)
    assert ack == b'OK'


def server(work_address, port):
    # Wait for the worker to connect
    worker_serv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    worker_serv.bind(work_address)
    worker_serv.listen(1)
    worker, addr = worker_serv.accept()

    # Now run a TCP/IP server and send clients to worker
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(('', port))
    s.listen(1)
    while True:
        client, addr = s.accept()
        print("Got connection from", addr)
        send_fd(worker, client.fileno())
        client.fileno()


if __name__ == "__main__":
    server('/tmp/servconn1', 15000)



