# coding:utf-8

from tornado import tcpserver, gen, iostream

import interface


class Connection:
    clients = set()

    def __init__(self, stream, address):
        Connection.clients.add(self)
        self._stream = stream
        self._address = address
        self._stream.set_close_callback(self.on_close)

    @gen.coroutine
    def recv_message(self):
        message = yield self._stream.read_bytes(4)
        ret_data = yield interface.foo(message)
        yield self._stream.write(ret_data.encode())

    def on_close(self):
        if self in Connection.clients:
            Connection.clients.remove(self)


class MyTCPServer(tcpserver.TCPServer):
    @gen.coroutine
    def handle_stream(self, stream, address):
        conn = Connection(stream, address)
        while True:
            try:
                yield conn.recv_message()
            except iostream.StreamClosedError:
                conn.on_close()
                break
