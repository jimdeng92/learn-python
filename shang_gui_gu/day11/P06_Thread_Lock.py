"""
多线程处理全局变量是不安全的，我们可以使用互斥锁将逻辑锁定。只有释放锁后才能进行其他线程的修改
"""
import threading
import time

def func():
    global g_num
    for i in range(10):
        lock.acquire() # 获取锁
        tmp = g_num + 1
        time.sleep(0.01)
        g_num = tmp
        print(f"当前线程{threading.current_thread().name}", g_num)
        lock.release() # 释放锁

if __name__ == '__main__':
    g_num = 0
    lock = threading.Lock() # 创建锁
    threads = [threading.Thread(target=func, name="线程" + str(i)) for i in range(1, 4)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f"当前线程{threading.current_thread().name}", g_num)
