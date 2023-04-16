from multiprocessing.connection import Client
from multiprocessing.reduction import recv_handle
import socket
import os


def worker(server_address):
    serv = Client(server_address, authkey=b'peekaboo')
    serv.send(os.getpid())
    while True:
        fd = recv_handle(serv)
        print('Worker: Got fd', fd)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=fd) as s:
            while True:
                msg = s.recv(1024)
                if not msg: break
                print('Worker: Recv:', msg)
                s.send(msg)


if __name__ == '__main__':
    worker('/tmp/servconn')
