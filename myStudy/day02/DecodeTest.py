def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str.decode('utf-8')
    else:
        return bytes_or_str


# print(to_str(b'hello'))
print(to_str('hello') == to_str(b'hello'))
#
# print(repr(to_str(b'hello')))
# print(repr(to_str('hello')))

print(to_str(b'one'+b'two') == to_str('one'+'two'))
print('one'+'two')

#assert 作用是什么 不理解
# assert b'red' > b'blue'
# assert 'red' > 'blue'

print('red %s' % b'blue' )

print('red %s' % 'blue')

print(b'red %s' % 'blue'.encode('utf-8'))
print(b'red %s' % b'blue')


# with open('data.bin','wb') as f:
#     f.write(b'hello')

with open('data.bin','rb') as f:
    data = f.read()
    print(data)


