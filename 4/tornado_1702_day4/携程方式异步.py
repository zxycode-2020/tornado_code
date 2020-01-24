#coding:utf8
import time,threading

generator = None

def long_io():
    def fun():
        global generator
        print '开始执行长延时操作'
        time.sleep(5)
        print '结束执行长延时操作'
        try:
            generator.send('LONG_IO_RESULT')
        except StopIteration,e:
            pass
    t = threading.Thread(target=fun)
    t.start()


def req_a():
    print '开始处理请求a'
    resp = yield long_io()
    print '结束处理请求a'

def req_b():
    print '开始处理请求b'
    time.sleep(2)
    print '结束处理请求b'

def main():
    global generator
    generator = req_a()
    generator.next()
    req_b()

if __name__ == '__main__':
    main()