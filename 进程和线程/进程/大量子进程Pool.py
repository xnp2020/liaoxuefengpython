from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print(f'Run task {name} {os.getpid()}...')
    start = time.time()
    time.sleep(random.randint(2, 10))
    end = time.time()
    print(f'Task {name} runs {(end-start):.2f}s')


if __name__ == '__main__':
    print(f'Parents process {os.getpid()} start!')
    p = Pool(3)  # Pool默认为cpu核心数
    for i in range(0, 5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
