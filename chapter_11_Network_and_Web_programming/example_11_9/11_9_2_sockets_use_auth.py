from socket import socket, AF_INET, SOCK_STREAM

from chapter_11_Network_and_Web_programming.example_11_9.authentication_11_9_1 import server_authenticate

secret_key = b'peekaboo'


def echo_handler(client_sock):
    if not server_authenticate(client_sock, secret_key):
        client_sock.close()
        return
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    while True:
        client_sock, a = sock.accept()
        echo_handler(client_sock)


if __name__ == "__main__":
    echo_server(('', 18000))
