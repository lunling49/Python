# 列表生成式，可把多行代码转换成一行代码
a = list(range(1, 11))
print(a)

b = [i for i in range(1, 11)]
print(b)

c = [x * x for x in range(1, 11)]
print(c)

d = [x * x for x in range(1, 11) if x % 2 == 0]
print(d)

# 两层循环
e = [m + n for m in 'abc' for n in '123']
print(e)

# 列出当前目录下的所有文件和目录名
import os
f = [d for d in os.listdir('.')]
print(f)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
j = {'x': 'a', 'y': 'b', 'z': 'c'}
for k, v in j.items():
    print(k, '=', v)

# 列表生成式也可以使用 2 个变量来生成list
h = [k + '=' + v for k, v in j.items()]
print(h)

# 把list中所有的字符串变成小写
A = ['Hello', 'World', 'INM', 'Apple']
B = [s.lower() for s in A]
print(B)

# 如果list有数字、字符串，如何转换把字符串改成小写
C = ['Hello', 'World', 21, 'Apple', None]
# 使用内建的isinstance函数可以判断一个变量是不是字符串
print(isinstance(18, int))
print(isinstance(18, str))

D = [s.lower() for s in C if isinstance(s, str)]
E = [s.lower() for s in C if isinstance(s, str) == True]
print(D, '\n%s' % E)
