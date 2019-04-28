# 高阶函数
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

# map()函数接收 2 个参数，一个是函数，一个是Iterable。map()将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# 比如有个函数f(x)=x的二次方，把该函数作用到一个list[1,2,3,4,5]上，就可以用map()实现
from functools import reduce


def f(x):
    return x * x
a = map(f, [1, 2, 3, 4, 5])
print(list(a))
"""
map()传入的第一参数是 f，即函数对象本身。
由于结果 a 是一个Iterator（惰性序列），因此通过list()让其整个序列都计算出来并返回一个list
"""

"""
reduce()，把一个函数作用在一个序列[x1,x2,x3,...]上，这个函数必须接收 2 个参数
reduce把结果继续和序列的下一个元素做累积计算，效果如下
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1,x2), x3), x4)
"""
# 序列求和
def add(x, y):
    return x + y
b = reduce(add, [1, 3, 5, 7, 9])
print(b)
# 求和可以直接用Python内建函数sum()，没必要用reduce
# 但是如果把序列[1,3,5,7,9]变换成整数13579，reduce就可以派上用场
def fn(x, y):
    return x * 10 + y
c = reduce(fn, [1, 3, 5, 7, 9])
print(c)
