# multithreaded UDP server
import time
from socketserver import BaseRequestHandler, ThreadingUDPServer


class TimeHandler(BaseRequestHandler):
    def handle(self) -> None:
        print('Got connection from', self.client_address)
        # Get message and client socket
        msg, sock = self.request  # the self.request attribute is a tuple
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)


if __name__ == '__main__':
    serv = ThreadingUDPServer(('', 20000), TimeHandler)
    serv.serve_forever()


