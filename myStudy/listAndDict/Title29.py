#用赋值表达式消除推导中的重复代码
stock = {
    'nails': 125,
    'screws': 35,
    'wings': 8,
    'washers': 24,
}

order = ['screws', 'wings', 'clips']

def get_batches(count, size=8):
    return count // size

result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count)
    if batches:
        result[name] = batches

print(result)


found = {name:  get_batches(stock.get(name, 0)) for name in order
         if get_batches(stock.get(name, 0))}
print(found)

found = {name:  batches
         for name in order
         if (batches := get_batches(stock.get(name, 0))) }

print(found)

#总结
#编写推导式与生成器表达式时，可以在描述条件的那一部分通过赋值表达式定义变量，并在其他部分复用该变量，可以使程序简单易读
#对于推导式与生成器表达式来说，虽然赋值表达式也可以出现在描述条件的那一部分之外，但最好别这么写。

#30条 不要让函数直接返回列表，应该让它逐个生成列表里的值

def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result

address = 'Four score and seven years ago...'
result = index_words(address)
print(result)


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

it = index_words_iter(address)
print(next(it))
print(next(it))

result = list(index_words_iter(address))
print(result)

def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

#总结
#用生成器来实现比函数把结果收集合到列表里再返回，要更加清晰一些
#生成器函数所返回的迭代器可以产生一系列值，每次产生的那个值都是由函数体的下一条yield表达式所决定的
#不管输入的数据量有多大，生成器函数每次都只需要根据其中的一小部分来计算当前这次输出值。不用把整个输入值全部读取进来，也不用
#一次就把所有的输出值全部算好。

def normalize(numbers):
    total = sum(numbers)
    result = []
    for number in numbers:
        percent = number * 100 / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)

assert  sum(percentages) == 100.0


def normalize_yeild(numbers):
    total = sum(numbers)
    for numer in numbers:
        yield numer * 100 / total

per = list(normalize_yeild(visits))
print(per)

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_visits("my_numbers.txt")
print(list(it))
print(list(it))
pers = normalize(it)
print(pers)

def normalize_copy(numbers):
    number_copy = list(numbers)
    total = sum(number_copy)
    result = []
    for number in numbers:
        percent = number * 100 / total
        result.append(percent)
    return result

it = read_visits("my_numbers.txt")
per = normalize_copy(visits)
print(per)
assert sum(per) == 100.0

def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for number in get_iter():
        percent = number * 100 / total
        result.append(percent)
    return result

# per = normalize_func(read_visits('my_numbers.txt'))
# print(per)

class ReadVisits:

    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits("my_numbers.txt")
per = normalize(visits)
print(per)


def normalize_defensive(numbers):
    if iter(numbers) is numbers:
        raise TypeError('Must supply a  container')
    total = sum(numbers)
    result = []
    for number in numbers:
        percent = number * 100 / total
        result.append(percent)
    return result


#总结 31条
#函数和方法如果要把收到参数遍历很多遍，那就必须特别小心，因为如果这些参数为迭代器，那么程序可能得不到预期值，从而出现奇怪的效果
#Python的迭代器协议确定了容器与迭代器应该怎样跟内置的iter及next函数、for循环及相关的表达式交互
#要想让自定义的容器类型可以迭代，只需要把__iter__方法实现为生成器即可。
#可以把值传给iter函数，检测它返回的是不是那个值本身。如果是，就说明这是个普通的迭代器，而不是可以迭代器容器。
#可以使用内置isinstance函数判断该值是不是collections.abc.Iterator类的实例。

it = (len(x) for x in open('my_numbers.txt'))
# print(list(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

#总结 32条  通过列表推导来处理大量输入数据，可能会占用许多内存。
#改用生成器表达式来做，可以避免内存使用量过大的问题，因为这种表达式所形成的迭代器每次只会计算一项结果
#生成器表达式所形成的迭代器可以当成for预警的子表达式出现在另一个生成器表达式里
#把生成器表达式组合起来使用，能够写出执行速度快且占用内存少的代码

#33 通过yield from 把多个生成器连起来用
def move(period, speed):
    for _ in range(period):
        yield speed

def pause(delay):
    for _ in range(delay):
        yield 0

def animate():
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.0):
        yield delta

def render(delta):
    print(f'Delta: {delta:.1f}')

def run(func):
    for delta in func():
        render(delta)

run(animate)
print("==========")
def animate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)

run(animate_composed)