"""
Storing Thread-Specific State
Problem
    You need to store state that's specify to currently executing thread and not visible to other threads.
Solution
    `threading.local()`: a thread-local storage object, store data that's only specific to the currently
    executing thread.
Discussion
    Under the covers, an instance of `threading.local()` maintains a separate instance dictionary for
    each thread. ALL the usual instance operations of getting, setting, deleting values just manipulate
    per-thread dictionary. The fact that each thread uses a separate dictionary is what provides
    the isolation of data.
"""
import threading
from socket import socket, AF_INET, SOCK_STREAM


# Use `LazyConnection` context-manager class in Recipe 8.3
class LazyConnection:
    def __init__(self, address, family=AF_INET, sock=SOCK_STREAM):
        self._address = address
        self._family = family
        self._type = sock
        self._local = threading.local()

    def __enter__(self):
        if hasattr(self._local, 'sock'):
            raise RuntimeError('Address connected')
        self._local.sock = socket(self._family, self._type)
        self._local.sock.connect(self._address)
        return self._local.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._local.sock.close()
        del self._local.sock


from functools import partial


def test(conn):
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        print(f'Got {len(resp)} bytes')


if __name__ == '__main__':
    conn = LazyConnection(('www.python.org', 80))
    a = threading.Thread(target=test, args=(conn, ))
    b = threading.Thread(target=test, args=(conn,))
    a.start()
    b.start()
    a.join()
    b.join()