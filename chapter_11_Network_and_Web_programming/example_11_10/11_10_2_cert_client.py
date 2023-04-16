from socket import socket, AF_INET, SOCK_STREAM
import ssl


if __name__ == "__main__":
    sock = socket(AF_INET, SOCK_STREAM)
    s_ssl = ssl.wrap_socket(sock, ca_certs='server_cert.pem', cert_reqs=ssl.CERT_REQUIRED)
    s_ssl.connect(('', 20000))
    print(s_ssl.send(b'Hello World'))
    print(s_ssl.recv(8192))
