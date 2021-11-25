# communicating simply between interpreters
# server.py
import traceback
from multiprocessing.connection import Listener


def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed!')


def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            echo_client(client)
        except Exception:
            traceback.print_exc()


echo_server(('', 25000), authkey=b'peekaboo')

if __name__ == '__main__':
    pass
