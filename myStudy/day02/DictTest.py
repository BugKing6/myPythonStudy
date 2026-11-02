from collections import abc

dial_codes = [(900,'e'),(880,'a'),(55,'b'),(86,'c'),(91,'d')]

country_dict = {c : code for code,c in dial_codes}
print(country_dict)

dict = {}
for k in country_dict.keys():
    v = country_dict[k]
    k = k.upper()
    dict[k] = v

print(dict)

print(sorted(dict.items(),key=lambda x:x[0]))


print(dict)



def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'bo   ok'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')

dict1 = {'type':"movie",'api':2, 'director':"",'author':[1,2,3]}
dict2 = {'type':"book",'api':2,'authors':[1,2,3]}
dict = {'type':"book",'api':1,'author':[1,2,3]}


print(get_creators(dict))
print(get_creators(dict2))


print(dict.get("ad"))
print(dict['type'])

print("==============")

def get_creators_list(list) -> str:
    match list:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return name
        case {'type': 'bo   ok'}:
            raise ValueError(f"Invalid 'book' record: {list!r}")
        case {'type': 'movie', 'director': name}:
            return name
        case _:
            raise ValueError(f'Invalid record: {list!r}')

dict1 = {'type':"movie",'api':2, 'director':"",'author':[1,2,3]}
dict2 = {'type':"book",'api':2,'authors':[1,2,3]}
dict = {'type':"book",'api':1,'author':[1,2,3]}

print(','.join(str(key) for key in get_creators_list(dict)))
print(','.join(str(key) for key in get_creators_list(dict2)))



my_dict = {}

print(isinstance(my_dict,abc.Mapping))

print(isinstance(my_dict,abc.MutableMapping))

##哈希码
tt = (1,2,(30,40))

print(hash(tt))

#list不可哈希
# t1 = (1,2,[30,40])
# print(hash(t1))

tf = (1,2,frozenset([30,40]))
print(hash(tf))
