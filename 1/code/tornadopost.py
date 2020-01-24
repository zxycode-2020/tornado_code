#coding:utf-8
import tornado.web
import tornado.ioloop
class IndexHandler(tornado.web.RequestHandler):
    def post(self):
        self.write("Hellow zhuxuanyu")

if __name__=="__main__":
    app=tornado.web.Application([
        (r"/",IndexHandler),
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()