"""
Adding SSL to Network services
Problem
    You want to implement a network service involving sockets where servers and clients authenticate themselves
    and encrypt transmitted data using SSL.
Solution
    The `ssl` module support for adding SSL to low-level socket connections. In particular, the `ssl.wrap_socket()`
    function takes an existing socket and wraps an SSL layer around it. For example, here is an example of an
    echo sever that presents a server certificate to connecting clients:
        11_10_1_certificate_server.py

    Here is an interactive session that shows how to connect to a server as a client. The client requires the
    server to presents its certificate and verifies it.
        11_10_2_cert_client.py.py

    The problem with all of this low-level socket hacking is that it doesn't play well with existing network services
    already implemented in the Standard library. For example, most server code(HTTP, XML-RPC, etc) is actually
    based on the `socketserver` library. Client is also implemented as a higher level. It is possible to add
    `SSL` to existing network services, but a slightly different approach is needed.

    First, for servers, SSL can be added through the use of a mixin class like this:
        mixin_server_11_10_3.py
    To use the mixin class, you can mixin it with other server classes. Here is an example of
    defining an XML-RPC server that operates over SSL.
        11_10_4_mixin_client_verify_server.py
    Here is the `XML-RPC server` from Recipe 11.6 modified only slightly to use SSL.
        11_10_4_mixin_client_verify_server.py

    To use the server, you can connect using the `xmlrpc.client` module. Just specify a `https:` in the URL.
    For example:
        11_10_5_xmlrpc_ssl_client.py

    One complicated issue with `SSL client` is performing extra steps to verify the server certificate
    or to present the server with client credentials(such as a client certificate). Unfortunately, theree
    are no standardized way to accomplish this, so research is required. However, here is an example of
    how to set up a `XML-RPC` connection that verifies the server certificate.
        11_10_6_client_verify_client.py

    As shown, the server presents a certificate to the client and the client verifies it. This verification
    can go both directions. If the server wants to verify the client, change the server startup to the following.
       11_10_7_mixin_server_verify_both_directions.py

    To make the `XML-RPC` client presents its certificates, change the `ServerProxy` initialization to this:
        11_10_8_mixin_client_verify_both_directions.py

Discussion
    Getting this recipe work to test your system configuration skills and understanding of `SSL`.
    Perhaps the biggest challenge is getting initial configuration of keys, certificates, and other
    matter in order.

    To clarify what's required, each endpoint of an SSL connection typically has a private key and
    a signed certificate file. The certificate file contains the public key and is presented to
    the remote peer on each connection. For public servers, certificates are normally signed by
    `certificate authority` such as Verisign, Equifax, or similar organizations(something that cost money).
    To verify the server, clients maintain a file containing the certificates of the certificate authorities.
    For example, web browsers maintain certificates corresponding to the major certificate authorities and
    use them to verify the integrity of certificates presented by web server during HTTPS connection.

    For the purposes of this recipe, you can create what's known as self-signed certificates. Here is
    how you do it:
        bash % openssl req -new -x509 -days 365 -nodes -out server_cert.pem -keyout server_key.pem

    When creating the certificate file, the value for the various fields often are arbitrary. However,
    the "Common Name" often contains the DNS hostname of servers. If you're just test things out on your
    own machine, use "localhost", Otherwise, use the domain name of the machine that's going to run the server.

    As a result of this configuration, you will have a `server_key.pem` file that contains the private key,
    a `server_cert.pem` file that contains the certificate.

    In server-related code, both the private key and certificate file are presented to various `SSL-related`
    wrapping functions. The certificate is what gets presented to clients. The private key should be protected
    and remains on the server.

    In client-related code, a special file of valid certificate authorities should be maintained to verify
    the server's certificate. If you have no such file, at the very least, you can put a copy of server's
    certificate on the client machine and use that as a means for verification. During the connection,
    the server will present its certificate, and then the client will use the stored certificate to
    verify that it's correct.

    Servers can also elect to the identity of clients. To do that, clients need to have their own private
    key and certificate. The server would also maintain a file of trusted certificate authorities for verifying
    the client certificates.

    If you intend to add SSL support to a network service for real, this recipe only gives a small taste of
    how to set it up. You will definitely want to consult the documentation(http://docs.python.org/3/library/ssl.html)
    for more of the finer points. Be prepared to spend a significant amount of time experiment with it to get things
    to work.

    """
__author__ = 'Frankie Fu'
