#用辅助函数取代复杂的表达式
from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)
print(my_values)

print(my_values.get('red'))
print(my_values['blue'])

print(my_values.get('white'))
print(my_values)

red = my_values.get('red',[''])
print(f'red: {red!r}')

red = my_values.get('red',[''])[0] or 0
print(red)

green = my_values.get('green',[''])[0] or 0
print(green)

white = my_values.get('white',[''])[0] or 0
print(white)
