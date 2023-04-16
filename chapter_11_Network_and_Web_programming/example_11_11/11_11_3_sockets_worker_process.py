import struct
import socket


def recv_fd(sock):
    """
    Receive a single file descriptor
    """
    msg, ancdata, flags, addr = sock.recvmsg(1, socket.CMSG_LEN(struct.calcsize('i')))
    cmsg_level, cmsg_type, cmsg_data = ancdata[0]
    assert cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SCM_RIGHTS
    sock.sendall(b'OK')

    return struct.unpack('i', cmsg_data)[0]


def worker(server_address):
    serv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    serv.connect(server_address)
    while True:
        fd = recv_fd(serv)
        print('Worker: Got fd', fd)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=fd) as client:
            while True:
                msg = client.recv(1024)
                if not msg: break
                print('Worker: Recv:', msg)
                client.sendall(msg)


if __name__ == '__main__':
    worker('/tmp/servconn1')


