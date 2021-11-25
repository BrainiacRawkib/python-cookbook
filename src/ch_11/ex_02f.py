import socket
from socketserver import BaseRequestHandler, TCPServer


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


if __name__ == '__main__':
    # To allow the server to rebind to a previously used port number
    TCPServer.allow_reuse_address = True
    # To manually enable TCPServer default bind and activate feature
    serv = TCPServer(('', 20000), EchoHandler, bind_and_activate=False)
    # Set up various socket options
    serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # Bind and activate
    serv.server_bind()
    serv.server_activate()
    serv.serve_forever()
