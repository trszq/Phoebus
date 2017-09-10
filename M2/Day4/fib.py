# Author: Zhang Qing

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        yield b         # 保存函数中断状态
        a, b = b, a + b
        n = n + 1
    return '---done---'

data = fib(10)

print(data)
for n in fib(10):
    print(n)
