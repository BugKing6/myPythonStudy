#把数据结构直接拆分到多个变量里，不要专门通过下标访问
snack_calories = {
    'chips': 140,
    'popcorn': 80,
    'nuts': 190,
}

items = tuple(snack_calories.items())
print(items)

first = items[0]
print(first)
# items[0] = ('oh')

item = ('hello','world')
first,second = item
print(first,second)
first = 10
print(first,second)


#传统升序排序算法

def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1,len(a)):
            if a[i] < a[i-1]:
                tem = a[i]
                a[i] = a[i-1]
                a[i-1] = tem


names = ['pret','carrot','arr','bac']
bubble_sort(names)
print(names)


snacks = [{'bacon',350}, ('donut',240),('muffin',190)]

for rank,(name,snak) in enumerate(snacks,1):
    print(f'#{rank}: {name} has {snak} money')
