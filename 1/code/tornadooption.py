#coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define("port",default=8000,type=int,help="run server on the given port.")
tornado.options.define("zhuxuanyu",default=[],type=str,multiple=True,help="zhuxuanyu subjects.")

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("dashuaigezhuxuanyu")

if __name__=="__main__":
    tornado.options.parse_command_line()
    print tornado.options.options.zhuxuanyu
    app=tornado.web.Application([
        (r"/",IndexHandler),
    ])
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()