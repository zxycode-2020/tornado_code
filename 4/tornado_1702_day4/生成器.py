def foo():
    r1 = yield 1
    r2 = yield 2
    print r1,r2
    yield 3

generator = foo()
y1 = generator.next()
print y1

y2 = generator.send('res1')
print y2

y3 = generator.send('res2')
print y3