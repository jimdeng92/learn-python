"""
with 关键字的原理（上下文管理器 Context Manager）

with 语句用于管理资源（如文件、网络连接、锁等），保证资源在使用完毕后被正确释放，
即使代码块中途抛出异常也能自动清理，避免资源泄漏。

底层依赖“上下文管理器协议”，即对象需要实现两个特殊方法：
- __enter__(self)：进入 with 代码块前调用，返回值会赋给 as 后面的变量。
- __exit__(self, exc_type, exc_val, exc_tb)：离开 with 代码块时调用，
  无论是正常结束还是发生异常都会执行，负责释放资源（如关闭文件）。
  三个参数分别是异常类型、异常值、异常追踪信息；若无异常则均为 None。
  若 __exit__ 返回 True，则表示异常已被处理，不再向外抛出。

执行流程：
    with 表达式 as 变量:
        代码块
等价于（简化）：
    mgr = 表达式
    变量 = mgr.__enter__()
    try:
        代码块
    finally:
        mgr.__exit__(...)

以下例子中，open() 返回的文件对象就是一个上下文管理器，
with 代码块结束后会自动调用 __exit__ 关闭文件，因此 f.closed 为 True。
"""

try:
    with open('test.txt','w') as f:
        f.write('hello')
finally:
    print('文件是否关闭：', f.closed)
