#赋值表达式减少重复代码 3.8引入新语法

fresh_fruit = {
    "apple": 10,
    "banana": 8,
    "lemon": 5
}

def make_lemonade(count):
    print(count)

def out_of_stock():
    print("===没有啦====")

# count = fresh_fruit.get('lemon',0)
# if(count):
#     make_lemonade(count)
# else:
#     out_of_stock()

if (count := fresh_fruit.get('lemon',0) ) >= 4:
    make_lemonade(count)
elif (count := fresh_fruit.get('banana',0) ) >= 4:
    make_lemonade(count)
else:
    out_of_stock()

print(count)

