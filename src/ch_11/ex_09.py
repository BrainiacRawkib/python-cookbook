# authenticating clients simply
import hmac
import os


def client_authenticate(connection, secret_key):
    """
    Authenticate client to a remote service.
    connection represents a network connection.
    secret_key is a key known only to both client/server.
    :param connection:
    :param secret_key:
    :return:
    """
    message = connection.recv(32)
    hash_ = hmac.new(secret_key, message)
    digest = hash_.digest()
    connection.send(digest)


def server_authenticate(connection, secret_key):
    """
    Request client authentication.
    :param connection:
    :param secret_key:
    :return:
    """
    message = os.urandom(32)
    connection.send(message)
    hash_ = hmac.new(secret_key, message)
    digest = hash_.digest()
    response = connection.recv(len(digest))
    return hmac.compare_digest(digest, response)
