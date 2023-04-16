from multiprocessing.connection import Listener
from multiprocessing.reduction import send_handle
import socket


def server(worker_address, port):
    # Wait for the worker to connect
    work_serv = Listener(worker_address, authkey=b'peekaboo')
    worker = work_serv.accept()
    worker_pid = worker.recv()

    # Now run a TCP/IP server and send clients to worker
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(('', port))
    s.listen(1)
    while True:
        client, addr = s.accept()
        print('Got connection from:', addr)
        send_handle(worker, client.fileno(), worker_pid)
        client.close()


if __name__ == '__main__':
    server('/tmp/servconn', 15000)
