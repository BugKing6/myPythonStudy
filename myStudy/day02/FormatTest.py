a = 0b10111011
b = 0xc5f
print('Binary is %d , hex is %d' % (a,b))


key = 'my_var'
value = 1.234
formatted = '%-10s = %.2f' % (key,value)
print(formatted)


pantry = [
    ('avocados', 1.25),
    ('banans', 2.5),
    ('cherries', 15),
]

for i, (item,count) in enumerate(pantry):
    print('#%d: %s = %.2f' %(i,item,count))

name = 'brad'

print(name.title())

for i,(item,count) in enumerate(pantry):
    before = '#%d: %s = %d' %(i+1,item.title(),round(count))


    after = '#%(loop)d: %(item)-10s = %(count)d' % {
        'loop':i+1,
        'item':item.title(),
        'count':round(count),
    }
    # assert before == after
    print(before == after)
    print(before)
    print(after)

a = 111232234.5678
d2 = format(a,',.2f')
print(d2)

b = 'my string'
d3 = format(b,'^20s')
print('*',d3,'*')


d4 = '{} = {}'.format(a,b)
print(d4)

d5 = '{:<10} = {:.2f}'.format(b,a)
print(d5)

print('{1} = {0}'.format(b,a))


for i,(item,count) in enumerate(pantry):
    old_style = '#%d: %-10s = %d' % (
        i+1,
        item.title(),
        round(count)
    )

    new_style = '#{}: {:<10s} = {}'.format(
        i+1,
        item.title(),
        round(count)
    )

    assert old_style == new_style
    print(old_style)

menu = {
    "soup": "lentil",
    "oyster": 'kumamoto',
    "special": "schnitezl",
}
templat = ('Today\'s soup is %(soup)s,'
           'buy one get two %(oyster)s oysters,'
           'and our special entree is %(special)s.')
print(templat % menu)

# formatted = 'First letter is {menu[osyter][0]!r'.format(menu=menu)
