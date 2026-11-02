#用列表推导取代map 与filter
from myStudy.functionTest.FunctionTest import squars

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squars = [x ** 2 for x in a]
print(squars)


even_squares = [x ** 2 for x in a if x % 2 == 0]
print(even_squares)

alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)

even_squares_dicts = {x : x**2 for x in a if x % 2 == 0}
three_cubed_set = {x**3 for x in a if x % 3 == 0}

print(even_squares_dicts)
print(three_cubed_set)

#总结
#列表推导要比内置的map与filter函数清晰，因为它不用另外定义lambda表达式
#列表推导式可以很容易地跳过原列表中的某些数据，假如改用map实现，那么必须搭配filter才能实现。
#字典与集合也可以通过推导来创建