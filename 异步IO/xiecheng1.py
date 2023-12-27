def coroutine():
    while True:
        print('aaa')
        x = yield
        print('Received:', x)


coro = coroutine()
next(coro)
coro.send('hello')
coro.send('world')
