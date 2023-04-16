import ssl


class SSLMixin:
    """
    Mixin class that add support for SSL to existing server based on the `socketserver` module.
    """
    def __init__(self, *args, key_file=None, cert_file=None, ca_certs=None, cert_reqs=ssl.CERT_NONE, **kwargs):
        self._key_file = key_file
        self._cert_file = cert_file
        self._ca_certs = ca_certs
        self._cert_reqs = cert_reqs
        super().__init__(*args, **kwargs)

    def get_request(self):
        client, addr = super().get_request()
        s_ssl = ssl.wrap_socket(client, keyfile=self._key_file, certfile=self._cert_file,
                                ca_certs=self._ca_certs, cert_reqs=self._cert_reqs, server_side=True)
        return s_ssl, addr


