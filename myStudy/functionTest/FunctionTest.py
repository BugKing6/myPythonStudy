#用functools.wraps定义函数修饰器
#修饰器作用用于 程序在执行这个函数之前与执行完这个函数之后，分别运行某些代码
from itertools import count


def trace(func):
    def warpper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r},{kwargs!r})' 
                f'-> {result}')
        return result
    return warpper

@trace
def fibonacci(n):
    if n in (0,1):
        return n
    return (fibonacci(n-1) + fibonacci(n-2))

fibonacci1 = trace(fibonacci)
fibonacci(4)
print(fibonacci1)

help(fibonacci1)
import pickle

# pickle.dumps(fibonacci1)

from functools import wraps
#使用functools内置模块的wraps辅助函数来实现。wraps本身也是个修饰器，它可以帮助你编写修饰器。
def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r},{kwargs!r})'
              f'-> {result}')
        return result
    return wrapper

@trace
def fibonacci2(n):
    if n in (0,1):
        return n
    return (fibonacci2(n-1) + fibonacci2(n-2))
print("=======================")
fibonacci2 = trace(fibonacci2)
print("======")
fibonacci2(4)
help(fibonacci2)
print(pickle.dumps(fibonacci2))

#修饰器是Python中的一种写法，能够把一个函数封装在另外一个函数里面，这样程序在执行原来函数之前与执行完毕之后，
#就有机会执行其他一些逻辑。
#修饰器可能会让那些利用反射机制运作的工具（调试器）产生奇怪的行为
#Python内置的functools模块里有个叫做wraps的装饰器，可以帮助我们正确定义自己的修饰器，从而避开相关问题。


print("==========第四章推导与生成==========")

a = [1,2,3,4,5,6,7,8,9,10]

squars = []
for x in a :
    squars.append(x**2)
print(squars)


squarses = [x ** 2 for x in a]

print(squarses)

alt = map(lambda x: x**2, a )
for x,y in enumerate(alt):
    print(x,y)

squarsFile = [x ** 2 for x in a if x % 2 == 0]
print(squarsFile)
alt2 = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert squarsFile == list(alt2)

#总结 列表推导要比内置的map与filter函数清晰，因为它不用另外定义lambda表达式。
#列表推导可以很容易地跳过原列表的某些数据，假如改用map实现，那么必须搭配filter才能实现
#字典与集合也可使用推导来创建

print("=========28条 控制推导逻辑的子表达式不要超过两个===========")

m = [[1,2,3],[4,5,6],[7,8,9]]
flat = [x for row in m for x in row]
print(flat)

squared = [[x**2 for x in row ] for row in m]
print(squared)

my_list = [
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]],
]

three = [x for sublist1 in my_list
         for sublist2 in sublist1
         for x in sublist2
         ]

print(three)

print("====29条 用赋值表达式消除推导中的重复代码")

stock = {
    'nails' : 125,
    'screw' : 35,
    'winguts': 8,
    'washers': 24,
}

order = ['screw','winguts','clips']

def get_batches(count, size):
    return count // size

result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches

print(result)

rsult1 = {name: get_batches(stock.get(name, 0), 8)
         for name in order
         if get_batches(stock.get(name,0),8)}

print(rsult1)


result2 = {name : batches2 for name in order
           if (batches2 := get_batches(stock.get(name,0),8))}
print(batches2)
print(result2)


half = [(last := count //2) for count in stock.values()]
print(half)
print(last)
print("===")
half = [count // 2 for count in stock.values()]

print(half)
print(count)

#总结 编写推导式与生成器表达式时，可以在描述条件的那一部分通过赋值表达式定义变量，并在其它部分复用该变量，
#杜宇推导式与生成器表达式来说，虽然赋值表达式也可以出现在描述条件的那一部分之外，但最好别这么写

