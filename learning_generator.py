"""
    通过列表生成式，我们可以直接创建一个列表。
    但是，受到内存限制，列表容量肯定是有限的。
    而且，创建一个包含100万个元素的列表，
    不仅占用很大的存储空间，
    如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
    所以，如果列表元素可以按照某种算法推算出来，
    那我们是否可以在循环的过程中不断推算出后续的元素呢？
    这样就不必创建完整的list，从而节省大量的空间。
    在Python中，这种一边循环一边计算的机制，称为生成器：generator。
"""
# 生成器generator，保存的是算法
# 第一种方法，将列表生成式的[]换成()，就创建了一个generator
# a = [x for x in range(10)]
# print(a)
b = (x for x in range(10))
# print(b)
# 创建 a 和 b 的区别仅再最外层的[]和()，a是list，b是generator

# 如果要一个一个打印，可用next()函数获得generator的下一个返回值
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
"""
    generator保存的是算法，
    每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，
    没有更多的元素时，抛出StopIteration的错误
    因此，正确的方法是使用for循环，因为generator也是可迭代对象
    所以，创建一个generator后，基本上永远不会调用next()，
    而是通过for循环来迭代它，并且不需要关心StopIteration的错误
"""
for i in b:
    print(i)

# 如果推算的算法比较复杂，用类似列表生成式的for循环无法实现，可以用函数来实现
"""
著名的斐波拉契数列（Fibonacci）: 1,1,2,3,5,8,13,21,34,...
除第一个和第二个数外，任意一个数都可由前两个数相加得到
"""
def fib(num):
    