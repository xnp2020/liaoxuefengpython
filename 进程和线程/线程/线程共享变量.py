import threading

balance = 0
lock = threading.Lock()


def cal(m):
    global balance
    balance = balance + m
    balance = balance - m


def run(x):
    for i in range(20000000):
        lock.acquire()
        try:
            cal(x)
        finally:
            lock.release()


t1 = threading.Thread(target=run, args=(5,))
t2 = threading.Thread(target=run, args=(10,))

t1.start()
t2.start()
t1.join()
t2.join()

print(balance)
