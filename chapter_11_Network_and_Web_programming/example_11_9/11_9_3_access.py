from socket import socket, AF_INET, SOCK_STREAM
from authentication_11_9_1 import client_authenticate


if __name__ == '__main__':
    secret_key = b'peekaboo'
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('', 18000))
    client_authenticate(sock, secret_key)
    sock.send(b'fzd')
    print(sock.recv(1024))
