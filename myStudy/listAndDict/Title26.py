#用修饰器来封装某个函数，从而让程序在执行这个函数之前与执行完这个函数之后，分别运行某些代码。
#这就意味着，调用者传给函数的参数值、函数返回给调用者的值，以及函数抛出的异常，都可以由修饰器
#访问并修改。可以确保用户以正确的方式使用函数，也能用来调式程序或实现函数注册功能。
from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}: ({args!r},{kwargs!r}) -> {result!r} ')
        return result
    return wrapper

@trace
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)


fibonacci = trace(fibonacci)
fibonacci(4)

print(fibonacci)

help(fibonacci)

import pickle

print(pickle.dumps(fibonacci))



#总结 修饰器是Python中的一种写法，能够把一个函数封装在另一个函数里面，这样程序在执行原函数之前与执行完毕之后，就有机会执行其他一些逻辑
#修饰器可能会让那些利用反射机制运作的工具产生奇怪的行为
#Python内置的functools模块里有个叫做wrps修饰器，可以帮助我们正确定义自己的修饰器，从而避免相关问题。