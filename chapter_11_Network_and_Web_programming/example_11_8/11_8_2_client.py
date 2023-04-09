import pickle
from multiprocessing.connection import Client


class RPCProxy:
    def __init__(self, connection):
        self.connection = connection

    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self.connection.send(pickle.dumps((name, args, kwargs)))
            result = pickle.loads(self.connection.recv())
            if isinstance(result, Exception):
                raise result
            return result
        return do_rpc


if __name__ == "__main__":
    client = Client(('', 17000), authkey=b'peekaboo')
    rpc = RPCProxy(client)
    print(rpc.add(2, 3))
    print(rpc.sub(2, 3))
    print(rpc.sub([1, 2], 3))
