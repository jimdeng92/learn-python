# 进程之间的数据不共享
import multiprocessing
import os
import time


def func(arr):
    for i in range(10):
        arr.append(i)
        print(os.getpid(), arr)
        time.sleep(0.5)


if __name__ == '__main__':
    arr = []
    p1 = multiprocessing.Process(target=func, args=(arr,))
    p2 = multiprocessing.Process(target=func, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"end")
