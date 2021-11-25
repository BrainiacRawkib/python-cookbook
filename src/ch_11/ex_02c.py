# To define a slightly different kind of server that put
# a file-like interface
# NB: this server can only support one client at a time
# server.py
from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    def handle(self) -> None:
        print('Got connection from', self.client_address)
        # self.rfile is a file-like object for reading
        for line in self.rfile:
            # self.wfile is a file-like object for writing
            self.wfile.write(line)


if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
