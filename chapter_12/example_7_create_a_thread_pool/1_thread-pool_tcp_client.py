from socket import socket, AF_INET, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('', 15000))
sock.send(b'fzd')
print(sock.recv(8192))
sock.close()

