d1 = {"a":1,"b":3,'c':4}

d2 = {"a":2,"b":4,"c":5}

d1 | d2
print(d1 | d2)
print(d1 == d2)

print("=====")

d1 |= d2

print(d1)

print(d2 == d1)