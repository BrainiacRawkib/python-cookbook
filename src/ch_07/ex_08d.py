from functools import partial
from socketserver import StreamRequestHandler, TCPServer
from ch_07.ex_08b import points, distance, pt


class EchoHandler(StreamRequestHandler):
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super(EchoHandler, self).__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'GOT:' + line)


serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED'))
serv.serve_forever()

# or using lambda instead of functools.partial
points.sort(key=lambda p: distance(pt, p))


serv = TCPServer(('', 15000), lambda *args, **kwargs: EchoHandler(*args,
                                                                  ack=b'RECEIVED',
                                                                  **kwargs))

if __name__ == '__main__':
    pass
