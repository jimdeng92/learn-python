import random
import os
import multiprocessing
import time

def func1(que):
    while True:
        num = random.randint(1, 100)
        que.put(num)
        print(f"进程{os.getpid()}put了数字{num}")
        time.sleep(1)

def func2(que):
    while True:
        num = que.get()
        print(f"进程{os.getpid()}get了数字{num}")
        # time.sleep(1)

if __name__ == '__main__':
    que = multiprocessing.Queue() # 队列
    p1 = multiprocessing.Process(target=func1, args=(que,))
    p2 = multiprocessing.Process(target=func2, args=(que,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
