import json
import time


def decode(data, default= {}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5
print(foo)

bar = decode('also bad data')
bar['meep'] = 1
print('Foo:',foo)

print('Bar:',bar)

print(foo == bar)




def decode(data, default= None):
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default

foo = decode('bad data')
foo['stuff'] = 5
print(foo)

bar = decode('also bad data')
bar['meep'] = 1
print('Foo:',foo)

print('Bar:',bar)

print(foo == bar)

from typing import Optional
from datetime import datetime

def log_typed(message : str, when: Optional[datetime] =None ) -> None:
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

log_typed('hello world')
time.sleep(1)
log_typed('hello world too')

print("===================================")

def safe_division(number, divisor,
                  ignore_overflow=False,
                  ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# print(safe_division(10,0,True,False))


assert safe_division(1.0,10**500,True,False) == 0



def safe_division(number, divisor, *,#参数列表里的*符号把参数分成两组，左边是位置参数，右边是只能关键字指定参数
                  ignore_overflow=False,
                  ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

safe_division(1.0,10**500,ignore_overflow = True)


def safe_division_c(number, divisor,/ , *,# /符号前的参数只能使用位置赋值，参数列表里的*符号把参数分成两组，左边是位置参数，右边是只能关键字指定参数
                  ignore_overflow=False,
                  ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

safe_division_c(number=1.0,divisor=10**500,ignore_overflow = True)
