# 数据类型：列表（list）、元组（tuple）、集合（set）、字典（dict）

# 列表list[] -- 有序，可更改（删除、添加元素）
a = ['data', 'you', 'have', 4, 'pop', 6]
# 获取长度
print(len(a))
# 某元素在列表中出现的个数
print(a.count('you'))
# 某元素的位置，无则报异常
print(a.index('have'))
# 末尾追加元素
a.append('me')
print(a)
# 第三个位置插入元素
a.insert(2, 'love')
print(a)
# 默认删除最后一个元素
a.pop()
print(a)
# 指定删除第二个元素
a.pop(1)
print(a)
# 删除指定下标的元素
del a[0]
print(a)
# 删除指定下表范围的元素
del a[1:3]
# 改变第一个元素
a[0] = 'here'
print(a)
# 合并两个列表
l = [1, 3, 'you']
h = [3, 'bet']
print(l + h)
l.extend(h)
print(l)
# 追加list，即合并list到l上,这里注意，使用extend函数可以一次在一个列表中插入任意多个值，而不必须每次只使用append()一次一值的插入
w = [2, 5]
l.extend(h+w)
print(l)
# 排序
e = [2, 6, 1, 6, 9, 0]
e.sort()
print(e)
# 倒序
e.reverse()
print(e)
# 复制list
e1 = e      # e1 为 e 的别名，对 e1 操作即对 e 操作
e2 = e[:]   # e2 为 e 的克隆，即另一个拷贝

# 元组tuple() -- 有序，不可更改，在赋值时决定所有元素
# tuple 没有append()、insert()、extend()方法，其他获取元素的方法与 list 一样
# 元组中元素值不允许删除，但是可以用 del 来删除整个元组
b = (123, 67, 8, 9)
del b
# print(b)
# 将列表换成元组
t = ['you', 'and']
v = tuple(t)
print(v)

# 字典dict{} -- 无序，可更改
c = {'a': 'x', 'b': 'y', 'c': 'z'}
# 清空字典
i = {'a': 'x', 'b': 'y', 'c': 'z'}
i.clear()
print(i)
# 获得键key的列表
print(c.keys())
# 获得值value的列表
print(c.values())
# 复制字典
p = c.copy()
print(p)
# 删除键key的值
c.pop('a')
print(c)
# 更新键值对，若不存在，相当于加入
c.update({'a': 'p'})
print(c)
# 获得键值对组成的列表
print(c.items())
# 读取某一个值，通过 key 的值，若不存在key，则返回 None
print(c['a'])
# 读取某一个值，通过 get 的方法，若不存在key，则返回 None
print(c.get('b'))

# 集合set{} -- 无序，可更改，可视为没有 value 的 dict，只存 key。一般用做去重或者集合求交、求并等
# set 函数
list1 = [6, 7, 7, 9, 9]
s1 = set(list1)
print(s1)           # 去掉重复的内容，且是无序的
# 添加新元素，如果再增加同一元素，会自动去重，只留一个
s = {1, 2, 4, 'you'}
s.add(5)
print(s)
# 删除元素
s.discard(6)     # 当元素不存在时,不会引发异常
s.remove(6)      # 与discard的区别在于，如果没有要删除的元素，remove会引发一个异常
s.pop()          # 因为set是无序的，所以pop会随机的从set中删除一个元素
# 固定集合
f = frozenset(s)
# f.add(5)        # 固定集合不能添加元素
# 交集 &、并集 |
one = {'x', 'y'}
two = {'x', 'u'}
print(one & two)
print(one | two)
# 所有的集合方法
s.issubset(t)                   # 如果s是t的子集,返回True，否则返回False
s.issuperset(t)                 # 如果s是t的超集,返回True，否则返回False
s.union(t)                      # 返回一个新集合, 该集合是s和t的并集
s.intersection(t)               # 返回一个新集合, 该集合是s和t的交集
s.difference(t)                 # 返回一个新集合, 该集合是s的成员, 但不是t的成员, 即返回s不同于t的元素
# s.symmetric_defference(t)       # 返回所有s和t独有的(非共同拥有)元素集合
s.copy()                        # 返回一个s的浅拷贝, 效率比工厂要好
# 方法（仅适用于可变集合）:以下方法参数必须是可哈希的
s.update(t)                         # 用t中的元素 修改s，即s现在包含s或t的成员
s.intersection_update(t)            # s中的成员是共同属于s和t的元素
s.difference_update(t)              # s中的成员是属于s但不包含在t中的元素
s.symmetric_difference_update(t)    # s中的成员更新为那些包含在s或t中，但不是s和t共有的元素
# s.add(obj)          # 在集合s中添加对象obj
# s.remove(obj)       # 从集合s中删除对象obj，如果obj不是集合s中的元素（obj not in s）,将引发keyError错误
# s.discard(obj)      # 如果obj是集合s中的元素，从集合s中删除对象obj
s.pop()             # 删除集合s中得任意一个对象，并返回它
s.clear()           # 删除集合s中的所有元素
# 集合有并集，交集，求差操作
# 并集：intersection() 方法返回一个新集合，包含在两个集合中同时出现的所有元素。
# 交集：union() 方法返回一个新集合，包含在两个 集合中出现的元素。
# 差集：difference() 方法返回的新集合中，包含所有在 集合A出现但未在集合B中的元素。
# symmetric_difference() 方法返回一个新集合，包含所有只在其中一个集合中出现的元素。





