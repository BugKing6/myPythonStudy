#用zip函数同时遍历两个迭代器

names = ['phoneNumb','lise','Marry']
counts = [len(n) for n in names]
print(counts)

longest_name = ''
max_count = 0

# for i in range(len(names)):
#     count = counts[i]
#     if count > max_count:
#         longest_name = names[i]
#         max_count = count
#
# print(longest_name)

for (name,count) in zip(names,counts):
    if len(name) > len(longest_name):
        longest_name = name
        max_count = count

import itertools
names.append('phoneNumbTest')
for name,count in itertools.zip_longest(names,counts):
    print(name,count)

