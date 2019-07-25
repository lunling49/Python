# 递归函数--在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

"""
阶乘 n! = 1 * 2 * 3 * 4 * 5 * ... * n
用函数 fact(n) 表示， fact(n) = n! = 1 * 2 * 3 * ... * (n-1) * n = (n-1)! * n = fact(n-1) * n
所以fact(n) 可表示为 n * fact(n-1)，只有 n=1 时要特殊处理
"""
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
#
# print(fact(1))
# print(fact(5))
# print(fact(100))


"""
递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
使用递归函数需要注意防止栈溢出。
在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)
"""
# print(fact(1000))

"""
通过尾递归优化解决递归调用栈溢出，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
尾递归,指在函数返回的时候，调用自身本身，并且return语句不能包含表达式。
这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。
要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中
"""
def fact(n):
    return fact_iter(n, 1)

def fact_iter(n, total):
    if n == 1:
        return total
    return fact_iter(n - 1, n * total)
# return fact_iter(n-1,n*total)仅返回递归函数本身，n-1和n*total在函数调用前就会被计算，不影响函数调用


print(fact(5))

"""
小结: Python有循环，因此 python 有循环就没必要用尾递归
    使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
    针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
    Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
"""
