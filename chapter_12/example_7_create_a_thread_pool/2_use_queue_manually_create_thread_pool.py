from socket import socket, AF_INET, SOCK_STREAM
from queue import Queue
from threading import Thread


def echo_client(q):
    sock, address = q.get()
    print('Got connection from', address)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('Close connection')
    sock.close()


def echo_server(addr, nworkers):
    q = Queue()
    for n in range(nworkers):
        t = Thread(target=echo_client, args=(q,))
        t.daemon = True
        t.start()
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, addr = sock.accept()
        q.put((client_sock, addr))


echo_server(('', 15000), 10)
