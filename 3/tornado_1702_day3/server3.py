#coding:utf8
import tornado.web
import tornado.ioloop
import config
import tornado.httpserver
import time

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # # 设置cookie
        # self.set_cookie('hotid','100',expires=time.mktime(time.strptime('2017-08-15 23:59:59','%Y-%m-%d %H:%M:%S')),)
        #
        # #获取cookie
        # hotid = self.get_cookie('hotid')
        # self.write(hotid)


        # hotid = self.get_cookie('hotid')
        # if hotid is None:
        #     self.set_cookie('hotid','100',expires=time.mktime(time.strptime('2017-08-15 23:59:59','%Y-%m-%d %H:%M:%S')),path='/')
        #     hotid = '100'
        # else:
        #     hotid = self.get_cookie('hotid')
        # self.write(hotid)

        # 设置安全cookie
        self.set_header('Set-Cookie','kami=666; Path=/')

class ClickCountHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        count = self.get_cookie('count')
        if count is None:  # 首次登陆
            count = '1'
            self.set_cookie('count','1')
        else: # 以前登陆过，去累加次数
            count = int(count) + 1
            count = str(count)
            self.set_cookie('count',count)
        self.write('您第%s次登陆' % count)

class ClearHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie('count')

class SignCookie(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 设置安全cookie
        # self.set_secure_cookie('alice','18')

        # 获取安全cookie
        age = self.get_secure_cookie('alice')
        self.write(age)

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/',IndexHandler),
            (r'/click',ClickCountHandler),
            (r'/clear',ClearHandler),
            (r'/sign',SignCookie),
        ]
        ,**config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()