#字典api接口学习
#d.clear() 删除所有项
#d.__contains__(k)  判断key是否在字典里 k in d
#d.copy() 浅拷贝
#d.__copy__() 为copy.copy(d) 提供支持
#d.default_factory 为__missing__ 调用的可调用对象 用于设置缺失值 比如不存在key是不会报错而是赋值默认值
#d.move_to_end(k,[last]) 把kyidao开头或结尾 last默认为true 只有OrderedDict
#d.__or__(other)  d1 | d2 合并d1和d2，新建一个dict对象
#d.__ior__(other) d1 |= d2 使用d2中项更新d1
#d.pop(k,[default]) 删除并返回k对应项，如何没有键k，则返回default或None
#d.popitem() 删除并返回（key,valu) 形式最后插入的项
#d.__reversed__() reverse(d) ：按照插入顺序从后向前返回遍历键的迭代器
#d.__ror__(other) other | dd ：反向合并运算符
#d.setdefault(k,[default]) 如果d中有键k，则返回d[k]：否则，把d[K]设为defaule，并返回default
#d.__setitem__(k,v) d[k] = v 把键k对应的值设为v
#d.update(m,[**kwargs]) 使用映射或可迭代对象的键值对更新d
#d.values() 获取值视图
from collections import defaultdict

d = {"10":"20"}
d = defaultdict(str,d)
print(d["30"])


# d.update({"10":"30","20":"40"})
d.update([('10',40),('50',40)])
print(d)