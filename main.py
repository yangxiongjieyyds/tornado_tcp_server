# coding:utf-8

from tornado import ioloop

from server import connection
import config

if __name__ == '__main__':
    config.load_config()
    listen_port = config.conf['server']['port']
    assert listen_port > 1000

    server = connection.MyTCPServer()
    server.listen(listen_port)
    ioloop.IOLoop.current().start()
