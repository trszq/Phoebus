# Author: Zhang Qing

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b         # 保存函数中断状态
        a, b = b, a + b
        n = n + 1
    return '---done---'

