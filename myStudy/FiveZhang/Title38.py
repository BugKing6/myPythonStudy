#让简单接口接受函数，而不是类的实例

#python中内置的api，允许我们传入某个函数来定制它的行为。这种函数可以叫做挂钩，API在执行过程中
#会回调这些挂钩函数。比
#如list类型的sort方法就可以带有可选的key参数， 内置len函数当做挂钩传给key
#让sort方法根据长度排列这些名称
name = ['Socraeas','Asadcasdzc','Python','Alas']
name.sort(key=len, reverse=False)
print(name)
#在其他编程语言中，挂钩可能会用抽象类来定义。在python中，许多挂钩都是无状态函数，带有明确的参数和返回值。


def  log_missing():
    print('key added')
    return 0

from collections import defaultdict
current = {'green': 12, 'blue': 3,}
increments = [
    ('red', 3),
    ('blue', 12),
    ('orange', 9),
]

result = defaultdict(log_missing, current)
print('Before:', dict(result))

for key, value in increments:
    result[key] += value
print('After:', dict(result))


#统计字典有多少次键名缺失情况
def increment_with_report(current, increments):
    added_count = 0
    def missing():
        nonlocal added_count
        added_count += 1
        return 0
    result = defaultdict(missing, current)
    for key, value in increments:
        result[key] += value
    return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2


class CountMissing:
    def __init__(self):
        self.added =0

    def missing(self):
        self.added += 1
        return 0

count = CountMissing()
result = defaultdict(count.missing, current)
for key, value in increments:
    result[key] += value
assert count.added == 2


class BetterCountMissing:
    def __init__(self):
        self.added =0

    def __call__(self, *args, **kwargs):
        self.added += 1
        return 0

count = BetterCountMissing()
# assert count() == 0
assert callable(count)
print(count.added)

result = defaultdict(count, current)
for key, value in increments:
    result[key] += value
# assert count.added == 2
print(count.added)


#总结
#如果想设计简单的python接口，让组件之间能够通过接口交互，那么可以考虑让接口接受挂钩函数，而不一定非得定义新列，并要求使用者传入这种类的实例
#python的函数与方法都是头等对象，这意味着它们可以想其他类型那样，用在表达式里。
#某个类如果定义了__call__特殊方法，那么那么他的实例就可以像普通Python函数那样调用
#如果想用函数来维护状态，那么可以考虑定义一个带有__call__方法的新类，而不要用有状态的闭包去实现。