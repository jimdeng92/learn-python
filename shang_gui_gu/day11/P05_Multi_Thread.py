"""
多线程
"""

"""
# 方式一：通过 threading.Thread 创建线程
import threading
import time


def func():
    flag = 0
    while True:
        print(f"当前线程{threading.current_thread().name}", f"{flag}" * 5)
        flag ^= 1
        time.sleep(1)

if __name__ == '__main__':
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func)
    t1.start()
    t2.start()
"""

"""
# 方式二：通过继承 threading.Thread 的run方法
import time
import threading

class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        flag = 0
        while True:
            print(f"当前线程{threading.current_thread().name}", f"{flag}" * 5)
            flag ^= 1
            time.sleep(1)

if __name__ == '__main__':
    t1 = Worker()
    t2 = Worker()
    t1.start()
    t2.start()
"""

# 通过线程池创建线程
import concurrent.futures

def func(tname):
    global word
    for i, char in enumerate(word):
        word[i] = chr(ord(char) ^ 1)
        print(f"{tname}: {word}\n", end="")
    return word

if __name__ == '__main__':
    word = list("idmmn!vnsme")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        future1 = executor.submit(func, '线程1')
        future2 = executor.submit(func, '线程2')
        future3 = executor.submit(func, '线程3')
        word = future1.result()
        word = future2.result()
        word = future3.result()
        print("".join(word))
