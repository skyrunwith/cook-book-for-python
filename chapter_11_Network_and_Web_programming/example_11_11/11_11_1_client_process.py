from socket import socket, AF_INET, SOCK_STREAM


if __name__ == '__main__':
    socket = socket(AF_INET, SOCK_STREAM)
    socket.connect(('', 15000))
    socket.send(b'Hello')
    print(socket.recv(1024))
