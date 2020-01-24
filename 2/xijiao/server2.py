#coding:utf8
import tornado.web
import tornado.ioloop
import config
import tornado.httpserver


class Handler68(tornado.web.RequestHandler):
    def get(self, *args, **kwargs): # 执行3
        info_dic = {
            'price': 10000,
            'price1': 10000,
            'price2': 10000,
            'title':'宝盛里1居室',
            'titles' : ['宝盛里','千峰','38技师'],
            'score':'5星好评',
            'comments':'洗的挺好',
            'position':'千峰3楼 38教',
            'fuwu_price' : 100,
        }
        self.render('blog/68.html',info_dic=info_dic)
        # self.send_error(500)

class Handlerxj(tornado.web.RequestHandler):
    def get(self, *args, **kwargs): # 执行3

        self.render('blog/index.html')
        # self.send_error(500)


class Handler78(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        xijiao_citys = [
            {
                'price': 10000,
                'price1': 10000,
                'price2': 10000,
                'title':'58洗脚城',
                'titles' : ['宝盛里','38技师'],
                'score':'5星好评',
                'comments':'洗的挺好',
                'position':'千峰3楼 38教',
                'fuwu_price' : 100,
            },
            {
                'price': 1000,
                'price1': 1000,
                'price2': 1000,
                'title':'千峰洗脚城',
                'titles' : ['宝盛里','千峰','36技师'],
                'score':'5星好评',
                'comments':'洗的挺好',
                'position':'千峰3楼 38教',
                'fuwu_price' : 10,
            }
        ]

        self.render('blog/78.html',info_dic=xijiao_citys)
        # self.send_error(500)


if __name__ == '__main__':
    app = tornado.web.Application(
        [

            (r'/68',Handler68),
            (r'/78',Handler78),
            (r'/xj', Handlerxj),
        ]
        ,**config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()