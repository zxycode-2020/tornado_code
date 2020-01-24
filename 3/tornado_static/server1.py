#coding:utf8
import tornado.web
import tornado.ioloop
import config
import tornado.httpserver
from tornado.web import StaticFileHandler
import os

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/',IndexHandler),
            (r'/(.*)',StaticFileHandler,{'path':os.path.join(config.Base_dir,'upload')}),
        ]
        ,**config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()