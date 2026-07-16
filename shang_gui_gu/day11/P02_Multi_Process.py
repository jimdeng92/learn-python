"""
多进程
"""

"""
# 方式1：通过 multiprocessing.Process 创建
import time
import multiprocessing


def write_file():
    with open('test.txt', 'at') as f:
        while True:
            f.write('hello world\n')
            f.flush()
            time.sleep(1)

def read_file():
    with open('test.txt', 'rt') as f:
        while True:
            time.sleep(1)
            line = f.readline()
            print(line)

if __name__ == '__main__':
    multiprocessing.Process(target=write_file).start()
    multiprocessing.Process(target=read_file).start()
"""

"""
# 方式2：通过继承multiprocessing.Process创建
import multiprocessing
import os

class Worker(multiprocessing.Process):
    def run(self):
        print(f'当前进程名：{self.name}，进程ID:{os.getpid()}，父进程ID:{os.getppid()}，name:{__name__}')

# 当前进程名：Worker-1，进程ID:18072，父进程ID:22692，name:__mp_main__
# 当前进程名：Worker-2，进程ID:5700，父进程ID:22692，name:__mp_main__
# 当前进程名：Worker-3，进程ID:27456，父进程ID:22692，name:__mp_main__

if __name__ == '__main__':
    for i in range(3):
        Worker().start()
"""

# 方式3：使用 multiprocessing.Pool 创建
import os
import time
import multiprocessing

print(os.cpu_count()) # 16

def func():
    for i in range(4):
        print(os.getpid(), i)
        time.sleep(1)

if __name__ == '__main__':
    process_num = 3
    pool = multiprocessing.Pool(process_num)
    for _ in range(process_num):
        pool.apply_async(func, args=())

    pool.close() # 不允许添加新的进程，所有进程结束后关闭
    pool.join() # 阻塞进程，防止主线程直接结束所有的子进程（守护进程）还没开始就结束了
    print(f"当前进程名字：{multiprocessing.current_process().name}")
