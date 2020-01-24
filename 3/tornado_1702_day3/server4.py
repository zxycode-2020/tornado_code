#coding:utf8
import tornado.web
import tornado.ioloop
import config
import tornado.httpserver

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('<html><head><title>被攻击的网站</title></head>'
                '<body><h1>此网站的图片链接被修改了</h1>'
                '<img alt="这应该是图片" src="http://127.0.0.1/click">'
                '</body></html>'
        )


if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/',IndexHandler),
        ]
        ,**config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(8000)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()