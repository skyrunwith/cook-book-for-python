from socket import socket, AF_INET, SOCK_STREAM


"""
To test the server, run it and open a separate python process that that connects to it. 
"""
socket = socket(AF_INET, SOCK_STREAM)
socket.connect(('127.0.0.1', 20000))
socket.send(b'Hello, world')
print(socket.recv(8124))
socket.close()
