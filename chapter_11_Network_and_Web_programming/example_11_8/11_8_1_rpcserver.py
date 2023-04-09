import pickle
from multiprocessing.connection import Listener
from threading import Thread


class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register_function(self, name, func):
        self._functions[name] = func

    def handle_connection(self, connection):
        try:
            while True:
                func_name, args, kwargs = pickle.loads(connection.recv())
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass


def rpc_server(handler: 'RPCHandler', address, authkey):
    server = Listener(address, authkey=authkey)
    while True:
        client = server.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


if __name__ == "__main__":
    handler = RPCHandler()
    handler.register_function('add', add)
    handler.register_function('sub', sub)

    rpc_server(handler, ('', 17000), authkey=b'peekaboo')