#coding:utf-8
import tornado.options
from tornado.web import url
import tornado.web
import config
import tornado.ioloop

tornado.options.define("port",default=8000,type=int,help="run server on the given port.")
tornado.options.define("zhuxuanyu", default=[], type=str, multiple=True, help="zhuxuanyu subjects.")

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        """对应http的get请求方式"""
        self.write("zhuxuanyugaofushui!")

class TornadoHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        """对应http的get请求方式"""
        self.write("zhuxuanyuyouqian!")


class GetHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('reg.html')



        #get
        # a=self.get_query_argument('a',default=None)
        # b=self.get_query_argument('b',default=None)
        # a_list= self.get_query_argument('a')
        # print a_list
        # self.write('get ok')

    def post(self,*args,**kwargs):
        #在post接口中获得查询
        a =self.get_body_argument('a')
        b = self.get_body_argument('b')
        c=self.get_body_argument('c')
        print a,b,c
        username=self.get_body_argument('username',default=None)
        password=self.get_body_argument('password',default=None)

        gender=self.get_body_argument("gender",default=None)
        interest=self.get_body_arguments("interest")
        print username,password

        if username and password:
            if username =='dachui' and password =='123':
                self.write('登陆成功<br>')
                self.write(' '.join(interest))
            else:
                self.write('登陆失败')
        else:
            self.write('用户名密码不能为空')


if __name__ == "__main__":
    tornado.options.parse_config_file("config") # 仅仅修改了此处
    print tornado.options.options.zhuxuanyu # 输出多值选项
    app = tornado.web.Application([

        (r"/", IndexHandler,),
        url(r'/tornado',TornadoHandler,name='tornado'),
        url(r'/get',GetHandler, name='get')
       ],
      **config.setting
      )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()