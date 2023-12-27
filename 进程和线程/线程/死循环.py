import threading
import multiprocessing


def loop():
    x = 0
    while True:
        x = x ^ 1


for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。
