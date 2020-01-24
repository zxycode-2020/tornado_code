#coding:utf-8
import tornado.web
import tornado.ioloop
import config
import tornado.httpserver
import json

# class IndexHandler(tornado.web.RequestHandler):
#     def initialize(self):
#         print "调用了initialize()"
#
#     def prepare(self):
#         print "调用了prepare()"
#
#     def set_default_headers(self):
#         print "调用了set_default_headers()"
#
#     def write_error(self, status_code, **kwargs):
#         print "调用了write_error()"
#
#     def get(self,*args,**kwargs):
#         self.render('blog/article.html',title="周杰伦错去",content="朕错了吗",author="大脸猫")
#
#         print "调用了get()"
#
#     def post(self):
#         #print "调用了post()"
#         self.send_error(200)  # 注意此出抛出了错误
#
#     def on_finish(self):
#         print "调用了on_finish()"

        # def get(self, *args, **kwargs):
    #     err_code=self.get_argument("code",None)
    #     err_title=self.get_argument("title","")
    #     err_content=self.get_argument("content","")
    #     if err_code:
    #         self.send_error(err_code, title=err_title,content=err_content)
    #     else:
    #         self.write("主页")
    # def write_error(self, status_code, **kwargs):
    #     self.write(u"<h1>出错了，程序员GG正在赶过来！</h1>")
    #     self.write(u"<p>错误名：%s</p>" % kwargs["title"])
    #     self.write(u"<p>错误详情：%s</p>" % kwargs["content"])

        # self.write("主页")
        # self.send_error(404, content="出现404错误")
        # self.write("结束")

    # def get(self):
    #     stu={
    #     "name":"zhangsan",
    #     "age":24,
    #     "gender":1
    #     }
        #stu_json=json.dumps(stu)
        #self.write(stu_json)

        # self.write(stu)

        # stu_json=json.dumps(stu)
        # self.write(stu_json)
        # self.set_header("Content_Type","application/json;charset=UTF-8")
    # def set_default_headers(self):
    #     print "执行了 set_default_headers()"
    #     self.set_header("Content-Type", "application/json; charset=UTF-8")
    #     self.set_header("qianfeng","python")
    #
    # def get(self, *args, **kwargs):
    #     print "执行了get()"
    #     stu = {
    #         "name":"zhangsan",
    #         "age":24,
    #         "gender":1
    #         }
    #     stu_json = json.dumps(stu)
    #     self.write(stu_json)
    #     self.set_header("qianfeng", "i love python")
    #
    # def post(self):
    #     print "执行了post()"
    #
    #     stu = {
    #         "name": "zhangsan",
    #         "age": 24,
    #         "gender": 1
    #     }
    #     stu_json = json.dumps(stu)
    #     self.write(stu_json)

# class Err210Handler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("hello qianfeng")
#         self.set_status(210,"qianfeng good")
# class LoginHandler(tornado.web.RequestHandler):
#     def get(self, *args, **kwargs):
#         self.write('<form method="post"><input type="submit" value="登陆"></form>')
#     def post(self, *args, **kwargs):
#         self.redirect("/")
class Handler58(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        info_dic={
            'price':10000,
            'price1': 10000,
            'price2': 10000,
            'title':'宝盛里1居室',
            'titles':['宝盛里','千锋','28技师'],
            'score':"五星好评",
            'comments':'洗的很好',
            'position':"千锋三楼38教室",
            'fuwu_price':100,

        }
        self.render('blog/58.html',**info_dic)

class Handler68(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        info_dic={
            'price':10000,
            'price1': 10000,
            'price2': 10000,
            'title':'宝盛里1居室',
            'titles':['宝盛里','千锋','28技师'],
            'score':"五星好评",
            'comments':'洗的很好',
            'position':"千锋三楼38教室",
            'fuwu_price':100,

        }
        self.render('blog/68.html', info_dic=info_dic)

if __name__=='__main__':
    app=tornado.web.Application(
        [
            #(r'/',IndexHandler),
            # (r'/error',Err210Handler),
            #(r'/tz/',LoginHandler),
            (r'/58',Handler58),
            (r'/68', Handler68),
        ],
        **config.settings
    )
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()



