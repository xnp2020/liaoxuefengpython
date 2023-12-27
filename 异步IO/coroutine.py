#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def consumer():
    r = ''
    while True:
        # yield r 是将 r 返回给外部调用程序，交出控制权，暂停；
        # n = yield 可以接收外部程序通过send()发送的信息，并赋值给n
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)  # 生成器必须先启动
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
