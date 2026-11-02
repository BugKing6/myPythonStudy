a = ['a','b','c','d','e','f','g','h']
print('Middle two :' ,a[3:5])
print('All but ends: ',a[1:7])


assert a[:5] == a[0:5]

b = a[:20]
# print(a.__eq__(b))