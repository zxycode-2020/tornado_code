#coding:utf8
import tornado.web
import tornado.ioloop
import config
import tornado.httpserver
from tornado.web import StaticFileHandler
import os

def add(price1,price2):
    return int(price1) + int(price2)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index page ok')


class FuncHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('fuc.html',price='1000',add=add)

class BaseHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('article.html')

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/',IndexHandler),
            (r'/fuc',FuncHandler),
            (r'/base',BaseHandler),
            (r'/st/(.*)',StaticFileHandler,{'path':os.path.join(config.Base_dir,'statics')}),
        ]
        ,**config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()