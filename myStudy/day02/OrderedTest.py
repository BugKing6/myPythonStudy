from collections import OrderedDict, ChainMap,Counter

d1 = dict(a=1,b=3)
d2 = dict(a=2,b=4,c=6)

chain = ChainMap(d1,d2)
print(chain['a'])
print(chain)
print(chain['b'])
print(chain['c'])

##计算Counter 是用于计算出现key的次数
ct = Counter('abracadabra')
print(ct)
ct.update('aaaaazzz')
print(ct)
print(ct.most_common(3))

#shelve.Shelf
#shelve模块 dbm模块 pickle模块

