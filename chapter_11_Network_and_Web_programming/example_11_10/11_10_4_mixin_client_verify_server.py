from xmlrpc.server import SimpleXMLRPCServer
from mixin_server_11_10_3 import SSLMixin


# XML-RPC server with SSL
class SSLSimpleXMLRPCServer(SSLMixin, SimpleXMLRPCServer):
    pass


class KeyValueSever:
    _rpc_methods = ['get', 'set', 'exists', 'delete', 'keys']

    def __init__(self, *args, **kwargs):
        self._data = {}
        self._serv = SSLSimpleXMLRPCServer(*args, allow_none=True, **kwargs)
        for method in self._rpc_methods:
            self._serv.register_function(getattr(self, method))

    def get(self, name):
        return self._data[name]

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def serve_forever(self):
        self._serv.serve_forever()


if __name__ == "__main__":
    KEYFILE = 'server_key.pem'  # Private key of the server
    CERTFILE = 'server_cert.pem'  # server certificate
    server = KeyValueSever(('', 15000), key_file=KEYFILE, cert_file=CERTFILE)
    server.serve_forever()
