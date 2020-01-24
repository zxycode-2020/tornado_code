#coding:utf8
import time

def req_a():
    print '开始处理请求a'
    time.sleep(5)
    print '结束处理请求a'

def req_b():
    print('开始处理请求b')
    print('结束处理请求b')

if __name__ == '__main__':
    req_a()
    req_b()
