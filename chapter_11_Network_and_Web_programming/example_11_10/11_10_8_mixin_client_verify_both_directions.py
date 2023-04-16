from xmlrpc.client import SafeTransport, ServerProxy
import ssl


class VerifyCertSafeTransport(SafeTransport):
    def __init__(self, ca_file, cert_file=None, key_file=None):
        self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        self._ssl_context.load_verify_locations(ca_file)
        if cert_file:
            self._ssl_context.load_cert_chain(cert_file, key_file)
        self._ssl_context.verify_mode = ssl.CERT_REQUIRED

        SafeTransport.__init__(self, context=self._ssl_context)

    def make_connection(self, host):
        """
        Items in the passed dictionary are passed as keyword
        arguments the to http.client.HTTPSConnection constructor.
        The argument allows an ssl.SSLContext instance to be
        passed with information about the SSL configuration.
        """
        s = super().make_connection(host)
        return s


# To make the make the client presents its certificates, change the `ServerProxy` initialization to this:
s = ServerProxy("https://localhost:15000", transport=VerifyCertSafeTransport('server_cert.pem',
                                                                             "client_cert.pem",
                                                                             "client_key.pem"), allow_none=True)
s.set('foo', 'bar')
print(s.get('foo'))