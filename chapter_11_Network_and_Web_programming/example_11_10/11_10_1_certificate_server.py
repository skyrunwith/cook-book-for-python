from socket import socket, AF_INET, SOCK_STREAM
import ssl


KEYFILE = 'server_key.pem'  # Private key of the server
CERTFILE = 'server_cert.pem'  # Server certificate(given to client)


def echo_client(s):
    while True:
        msg = s.recv(8192)
        if msg == b'':
            break
        s.send(msg)
    s.close()
    print('Connection closed')


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    s_ssl = ssl.wrap_socket(sock, keyfile=KEYFILE, certfile=CERTFILE, server_side=True)
    while True:
        try:
            c, a = s_ssl.accept()
            print('Got connection from', c, a)
            echo_client(c)
        except Exception as e:
            print(f"{e.__class__.__name__}:{e}")


if __name__ == '__main__':
    echo_server(('', 20000))

