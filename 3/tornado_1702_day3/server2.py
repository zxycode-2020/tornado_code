#coding:utf8
#文件上传
import tornado.web
import tornado.ioloop
import config
import tornado.httpserver
import uuid
import torndb
from tornado.web import StaticFileHandler
import os

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('reg.html')
    def post(self, *args, **kwargs):
        image_file = self.request.files.get('avatar')
        if image_file:
            for file in image_file:
                ftype = file['content_type']
                fname = str(uuid.uuid4()) + '.' + file['filename'].split('.')[-1]
                if ftype == 'image/jpeg' or ftype == 'image/gif':
                    # 文件上传工作
                    with open('upload/' + fname ,'wb') as f:
                        f.write(file['body'])
                else:
                    self.write('文件类型不正确')
        self.write('upload ok')

class Application(tornado.web.Application):
    def __init__(self):
        handler = [
            (r'/',IndexHandler),
            (r'/add',CityAddHandler),
            (r'/select',SelectHandler),
            (r'/upload/(.*)',StaticFileHandler,{'path':os.path.join(config.Base_dir,'upload')}),
        ]
        settings = config.settings
        self.db = torndb.Connection( # 返回数据库操作对象
            '127.0.0.1',
            'tornado',
            'root',
            '111111'
        )
        super(Application, self).__init__(handler,**settings)

# 添加数据库操作
class CityAddHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # execute 增删改操作
        try:
            sql = 'insert into xi_city(title) values("%s")' % '蒙特卡洛'
            res = self.application.db.execute(sql)
        except Exception, e:
            res = str(e)
        self.write(res)

class SelectHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        try:
            sql = 'select * from xi_city'
            rose = self.application.db.query(sql)  # [{id:1,title:'云顶山庄'},{}]
            self.render('select.html',rose=rose)

        except Exception,e:
            res = e
        self.write('ok')

if __name__ == '__main__':
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()