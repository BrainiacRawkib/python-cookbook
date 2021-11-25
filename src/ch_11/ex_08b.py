# RPCServer.py
from multiprocessing.connection import Listener
from threading import Thread
from ch_11.ex_08 import RPCHandler


def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()


# Some remote functions
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


# Register with a handler
handler = RPCHandler()
handler.register_function(add)
handler.register_function(sub)

# Run the server
rpc_server(handler, ('localhost', 17000), authkey=b'peekaboo')

if __name__ == '__main__':
    pass
