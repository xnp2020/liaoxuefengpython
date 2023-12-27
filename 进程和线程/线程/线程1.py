import time
import threading


def f():
    print(f'当前线程的名字是：{threading.current_thread().name}。')
    n = 0
    while n < 5:
        print(f'{threading.current_thread().name} >>> {n}')
        n = n + 1
    print(f'{threading.current_thread().name}已结束。')


if __name__ == '__main__':
    print(f'我是主线程：{threading.current_thread().name}.')
    t = threading.Thread(target=f, name='线程1')
    t.start()
    t.join()
    print(f'主线程{threading.current_thread().name}已结束。')
