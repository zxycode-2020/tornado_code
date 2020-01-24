#coding:utf8
import tornado.web
import tornado.ioloop
import config
import tornado.httpserver
from tornado.web import asynchronous
import tornado.httpclient
import time
import json
from tornado.gen import coroutine

# 携程异步
class IndexHandler(tornado.web.RequestHandler):
    @coroutine
    def get(self, *args, **kwargs):
        ip = self.get_query_argument('ip',None)
        if ip is not None:
            client = tornado.httpclient.AsyncHTTPClient() # 建立异步客户端
            response = yield client.fetch('http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=%s' % ip,)

            data = response.body
            data = json.loads(data)
            country = data.get('country','')
            province = data.get('province','')
            city = data.get('city','')

            self.write('%s %s %s' % (country,province,city))
            vip = self.get_cookie('vip')
            if vip is not None:
                self.finish() #结束请求，给客户端做响应
            else:
                time.sleep(10)
                self.finish()
        else:
            self.write('输入错误')


# 回调异步
# class IndexHandler(tornado.web.RequestHandler):
#     @asynchronous
#     def get(self, *args, **kwargs):
#         ip = self.get_query_argument('ip',None)
#         if ip is not None:
#             client = tornado.httpclient.AsyncHTTPClient() # 建立异步客户端
#             client.fetch('http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=%s' % ip,callback=self.on_response)
#         else:
#             self.write('输入错误')
#
#     # 回调函数
#     def on_response(self,response):
#         data = response.body
#         data = json.loads(data)
#         country = data.get('country','')
#         province = data.get('province','')
#         city = data.get('city','')
#
#         self.write('%s %s %s' % (country,province,city))
#         vip = self.get_cookie('vip')
#         if vip is not None:
#             self.finish() #结束请求，给客户端做响应
#         else:
#             time.sleep(10)
#             self.finish()

class VIPHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie('vip','super')

class IPHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('ip.html')

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/',IndexHandler),
            (r'/vip',VIPHandler),
            (r'/ip',IPHandler),
        ]
        ,**config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()