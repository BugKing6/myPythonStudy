#字典说明
bady_names = {
    'cat': 'kitten',
    'dog': 'puppy',
}

print(bady_names)

print(list(bady_names.keys()))
print(list(bady_names.values()))
print(list(bady_names.items()))



def sort_priotity(numbers, group):
    found = False
    def helper(x):
        if x in group:
            nonlocal found
            found = True
            return (0,x)
        return (1,x)
    numbers.sort(key=helper)
    print("====函数内====")
    print(found)
    return found
found = 1
nums = [1,2,3,4,5,10]
group = {4,5}
print('数值',found)
found = sort_priotity(nums, group)

print("Found:" , found)
print(nums)

#用数量可变的位置参数给函数设计清晰的参数列表
def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print(f'message: {message}, values: {values_str}')

log('My nubers are',[1, 2])
log('Hi there', [])

#在Python里，可以给最后一个位置参数加前缀*，这样调用者就只需要提供不带星号的
#那些参数，然后可以不在指定其他参数
def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print(f'message: {message}, values: {values_str}')

log('My nubers are',[1, 2])
log('Hi there')

favorites = [6,3,12]
log('Favorites', *favorites)


def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)


def raminder(number, divisor):
    if number % divisor == 0:
        return number // divisor
    else:
        return number % divisor

assert raminder(20, 7) == 6

assert raminder(divisor= 7,number= 20) == 6

#函数的参数可以按位置指定，也可以用关键字的形式指定
#关键字可以让每个参数作用更加明了，因为在调用函数时只按位置指定参数，可能导致
#这些参数含义不够明确。
#应该通过带默认值的关键字参数来扩展函数的行为，因为这不会影响原有的函数调用代码
#可选的关键字参数总是应该通过参数名来传递，而不应该按位置传递

#用None和docstring来描述默认值会变的参数

from time import sleep
from datetime import datetime

def log(message,when = datetime.now()):
    print(f'{when} : {message}')

log('Hi there')
sleep(1)
log('hello world')

#datetime.now()  只执行了一次

def log(message,when = None):
    """
      Log a message with a timestamp
    :param message:
    :param when:
    :return:
    """
    if when is None:
        when = datetime.now()
    print(f'{when} : {message}')

log('Hi there')
sleep(1)
log('hello world')

import json

def decode(data, default= {}):
    try:
        return json.loads(data)
    except ValueError:
        return default



foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad data')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:',bar)


def decode(data, default= None):
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default



foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad data')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:',bar)

from typing import Optional

def log_typed(mesage: str,
              when: Optional[datetime] = None) -> None:
    if when is None:
        when = datetime.now()
    print(f'{when} : {mesage}')

log_typed('hello world')
sleep(0.1)
log_typed('bad data')


