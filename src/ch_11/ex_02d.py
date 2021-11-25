# multithreaded_server.py
from socketserver import ThreadingTCPServer, BaseRequestHandler


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


"""
One issue with forking and threaded servers is that they spawn a new process or thread
on each client connection. There is no upper bound on the number of allowed clients,
so a malicious hacker could potentially launch a large number of simultaneous connections
in an effort to make your server explode.
"""
if __name__ == '__main__':
    serv = ThreadingTCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
