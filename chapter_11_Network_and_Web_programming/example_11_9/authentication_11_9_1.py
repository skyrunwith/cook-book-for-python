import hmac
import os


def client_authenticate(connection, secret_key):
    """
    Authenticate a client to a remote service.
    connection represents a network connection.
    secret_key is a key known only both to client/server.
    """
    message = connection.recv(32)
    hash = hmac.new(secret_key, message, 'MD5')
    digest = hash.digest()
    connection.send(digest)


def server_authenticate(connection, secret_key):
    """
    Request client authentication.
    """
    message = os.urandom(32)
    connection.send(message)
    hash = hmac.new(secret_key, message, 'MD5')
    digest = hash.digest()
    response = connection.recv(len(digest))
    return hmac.compare_digest(response, digest)
