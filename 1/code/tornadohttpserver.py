import tornado.web
import tornado.ioloop
import tornado.httpserver
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello zhuxanyu")

if __name__=="__main__":
    app=tornado.web.Application([
        (r"/",IndexHandler),
    ])
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.current().start()
