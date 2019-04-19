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
"""
    生成器generator，保存的是算法
    generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator
"""
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
    n, x, y = 0, 0, 1
    while n < num:
        print(y)
        x, y = y, x + y     # 赋值语句
        n += 1
    return 'done'

"""
    赋值语句  x, y = y, x+y
    相当于  t=(y, x+y)     t是一个tuple
            x=t[0]
            y=t[1]
"""
i = fib(5)
print(i)

"""
    fib函数实际上是定义了斐波拉契数列的推算规则，
    可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
    也就是说，上面的函数和generator仅一步之遥。
    要把fib函数变成generator，只需要把print(b)改为yield b就可以了
    这就是定义generator的另一种方法。
    如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
    在执行过程中，遇到yield就中断，下次又继续执行。
    已经没有yield可以执行了，所以，后面调用就报错。
"""
def fibo(num):
    n, x, y = 0, 0, 1
    while n < num:
        yield y
        x, y = y, x + y     # 赋值语句
        n += 1
    return 'done'

for f in fibo(5):
    print(f)

"""
    用for循环调用generator时，发现拿不到generator的return语句的返回值。
    如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
"""
g = fibo(5)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 杨辉三角
def triangles():
    l = [1]
    while True:
        yield l
        l = [1] + [l[i] + l[i + 1] for i in range(len(l)-1)] + [1]

n = 1
for i in triangles():
    print(i)
    n += 1
    if n == 5:
        break
