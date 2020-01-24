#coding:utf8
import os

Base_dir = os.path.dirname(__file__)

port=8000


settings = {
    'debug' : True,  # 开启调试模式
    'template_path' : os.path.join(Base_dir,'templates'),  # 配置模板路径
    'static_path' : os.path.join(Base_dir,'static')  # 静态资源路径
}