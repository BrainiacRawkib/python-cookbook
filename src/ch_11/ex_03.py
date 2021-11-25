# creating a UDP Server
# server.py (single threaded server)
import time
from socketserver import BaseRequestHandler, UDPServer


class TimeHandler(BaseRequestHandler):
    def handle(self) -> None:
        print('Got connection from', self.client_address)
        # Get message and client socket
        msg, sock = self.request  # the self.request attribute is a tuple
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)


if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serve_forever()
