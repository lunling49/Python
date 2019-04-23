"""
装饰器，为已存在的函数或对象添加额外的功能
*args -- 可变参数
**kwargs -- 关键字参数
装饰器顺序：一个函数可同时定义多个装饰器
执行顺序是从里到外，最先调用里层的装饰器，最后调用最外层的装饰器
本质上，decorator就是一个返回函数的高阶函数
"""

# 函数对象有一个__name__属性，可以拿到函数的名字

"""
需要把原始函数的__name__等属性复制到wrapper()函数中，
否则，有些依赖函数签名的代码执行就会出错。
不需要编写wrapper.__name__ = func.__name__这样的代码，
Python内置的functools.wraps就是干这个事的.
所以，一个完整的decorator的写法如下
"""
import functools

# 需记住在定义wrapper()的前面加上@functools.wraps(func)
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 或者针对带参数的decorator
def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

