# format 格式化函数
"""
函数str.format()，增强了字符串格式化的功能
基本语法是通过 {} 和 : 来替代以前的 %
format 函数可以接受不限个数参数，位置可以不按顺序
"""
# 数字(0, 1, ...)即代表format()里面的元素, 所以可以使用"."调用元素的方法
print('{} {}'.format('hello', 'world'))          # 不设置指定位置，按默认顺序'hello world'
print('{0} {1}'.format('hello', 'world'))          # 设置指定位置'hello world'
print('{1} {0}'.format('hello', 'world'))          # 设置指定位置'world hello'
print('{1} {0} {1}'.format('hello', 'world'))          # 设置指定位置'world hello world'

# 也可以设置参数
print('网址：{name}  地址：{url}'.format(name='百度', url='www.baidu.com'))
# 通过列表索引设置参数
l = ['百度', 'www.baidu.com']
print('网址：{0[0]}  地址：{0[1]}'.format(l))     # '0'是可选的

# str.format() 方法还可以使用 *元组 和 **字典 的形式传参，两者可以混合使用。
# 位置参数、关键字参数、*元组 和 **字典 也可以同时使用，但是要注意，位置参数要在关键字参数前面，*元组 要在 **字典 前面。
# 通过字典设置参数
s = {'name': '百度', 'url': 'www.baidu.com'}
print('网址：{name}  地址：{url}'.format(**s))        # 通过关键字，可用字典当关键字传入值时，在字典前加**即可
# 通过元组设置参数
t = 'super man', 66, 'boy'
print('I am a {},{} years old'.format(*t))
print('I am a {2},{1} years old'.format(*t))
# 同时使用元组和字典传参
a = '你大爷', '拳头'
b = {'name': '黄妈妈', 'weapon': '口水'}
print('我是{}，我怕{weapon}'.format(*a, **b))
print('我是{name}，我怕{1}'.format(*a, **b))
# 同时使用位置参数、元组、关键字参数、字典传参
"""
注意：位置参数要在关键字参数前面，*元组要在**字典前面
"""
tup = '大妈',
dic = {'weapon': '剑'}
text = '我是{1}，我怕{weakness}。我是{0}，我用{weapon}'
text = text.format(*tup, 'girl', weakness='boy', **dic)
print(text)

# 填充
"""
只能是一个字符
不指定默认用空格填充
如果指定填充字符，则必须要同时指定对齐方式
"""
# 对齐
"""
^：居中，   <：左对齐，  >：右对齐。后面带宽度
=：在正负号（如果有的话）和数字之间填充，该对齐选项仅对数字类型有效。
它可以输出类似 +0000120 这样的字符串。
注意：
    如果不给定最小宽度 width，对齐方式毫无意义。
"""
# 使用":", 指定代表元素需要的操作, 如":.3"小数点三位, ":8"占8个字符空间等
print('{:^15}'.format('hello'))
print('{:<15}'.format('hello'))
print('{:>15}'.format('hello'))
print('{:*<15}'.format('hello'))
print('{:$>15}'.format('hello'))
# 精度常和f一起使用
print('{:.3f}'.format(3.1415926))
print('{:.4f}'.format(4.1))
# b、o、d、x 分别表示二、八、十、十六进制
print('{:b}'.format(20))
print('{:o}'.format(20))
print('{:d}'.format(20))
print('{:x}'.format(20))
# 千分位分隔符，只针对数字
print('{:,}'.format(10000000))
print('{:,}'.format(2568552.5554))

# 如果在字符串中需要直接展示花括号，则用另一个花括号包裹起来转义
print('{{我很好}}:{}'.format('nice'))

# 复合字段名：同时使用了数字和变量名两种形式的字段名
# 复合字段支持两种操作符：[]方括号   .点号
# .点号的使用
"""
传递位置参数
    替换字段形式: {数字.属性名}
    只有一个替换字段的时候可以省略数字
"""
# 复合字段名中使用点号传递对象属性
class Person:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

p = Person('辣妹子','重庆')
print('我是{0.name}，家在{0.addr}'.format(p))
# 只有一个替换字段，可以省略数字
print('我是{.name}'.format(p))
# 试试传递文件对象的属性
f = open('out.txt', 'w')
print('文件名为：{.name}'.format(f))
f.close()

"""
传递关键字参数
    替换字段形式：{关键字参数名.属性名}
"""
# 点号用法：传递关键字参数
print('我是{girl.name}，家在{girl.addr}'.format(girl=p))
print('我是{p.name}，家在{p.addr}'.format(p=p))

# []方括号的使用
"""
传递位置参数：1、列表     2、元组        3、字典
"""
# 列表传参
infos = ['star', 8569]
food = ['flower', 'water']
print('我叫{0[0]}，学号{0[1]}，爱吃{1[0]}'.format(infos, food))
# 元组传参
foods = ('ice', 'milk')
print('我叫{0[0]}，年龄{1}，爱吃{0[1]}'.format(foods, 66))
# 字典传参
d = dict(name='star', pid=8596)
print('我是{[name]}'.format(d))
# 多个替换字段，不能省略数字
print('I am a {0[name]}, num is {0[pid]}'.format(d))

"""
传递关键字参数：1、列表    2、元组    3、字典
"""
names = ['皮卡丘']
dic = {'name': '妙蛙花'}
skills = ('十万伏特', '飞叶快刀')
t = '我是{names[0]}，我会{skills[0]}。我是{dic[name]}，我会{skills[1]}。'
t = t.format(names=names, skills=skills, dic=dic)
print(t)

# 转换字段
"""
转换字段 conversion field 的取值有三种，前面要加 !
    s：传递参数之前先对参数调用 str()
    r：传递参数之前先对参数调用 repr()
    a：传递参数之前先对参数调用 ascii()
    ascii() 函数类似 repr() 函数，返回一个可以表示对象的字符串。
    但是对于非 ASCII 字符，使用 \\x，\\u 或 \\U转义
"""
print('I am {!s}'.format('nice 漂亮'))
print('I am {!r}'.format('nice 漂亮'))
print('I am {!a}'.format('nice 漂亮'))

# 格式说明符
# 在替换字段中，格式说明符前面与一个冒号，格式{字段名!转换字段:格式说明符}
print('{0:{1}}'.format(3.1415926, '.4f'))

# 标准格式说明符的格式
"""
如果不通过重写 __format__ 方法来进行自定义的话，标准格式说明符的形式如下。其中方括号是可选的
    [[fill]align][sign][#][0][width][grouping_option][.precision][type]
中文形式可以写作：
    [[填充]对齐方式][正负号][#][0][宽度][分组选项][.精度][类型码]
"""





