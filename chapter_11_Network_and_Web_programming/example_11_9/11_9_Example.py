"""
Authenticating clients simply
Problem
    You want a simple way to authenticate clients connecting to server in a distributed system,
    but you don't want the complexity of something like SSL.
Solution
    Simple but effective authentication can be performed by implementing `a connection handshake`
    using `hmac` module. For example:
    authentication_11_9_1.py

    The general idea is that upon connection, the server presents the client with a message
    of random bytes(return by os.urandom(), in this case). The server and client both compute
    a cryptographic hash of the random data using `hmac` and a secret key  known only to both ends.
    The client send its computed digest back to the server, where it is compared and decide whether
    to accept or reject the connection.

    Comparison of resulting digest should be performed using the `hmac.compare_digest` function.
    This function has been written in a way that avoids timing-analysis-based attacks and should
    be used to instead of the comparison operator(==)

    To use these functions, you would incorporate them into existing networking or messaging code.
    For example, such as sockets, the server code might look something like this:
    11_9_2_sockets_use_auth.py

    Within a client, you would do this:
    11_9_3_access.py
Discussion
    A common use of authentication is in the internal messaging system and interprocess communication.
    For example, if you are writing a system that involving multiprocess communication across a cluster
    of machines. you can use  approacthish to make sure that only allowed processes are allowed to connect
    to one another. In fact, `HMAC-based` authentication is used internally by the `multiprocessing` library
    when it sets up communication with subprocesses.

    It's important to stress that authenticating a connection is not the same as encryption. Subsequent
    communication on a connection is sent in the clear. and would be visible to anyone inclined to
    sniff the traffic(although the secret key known to both sides is never transmitted).

    The authentication algorithm used by `hmac` is based on cryptographic hashing functions.
    such as MD5, SHA-1, and is described in detail in (IETF RFC 2104) http://tools.ietf.org/html/rfc2104.html
"""

__author__ = 'Frankie Fu'
