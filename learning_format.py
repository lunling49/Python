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
注意：如果不给定最小宽度 width，对齐方式毫无意义。
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

# 千分位分隔符，只针对数字
print('{:,}'.format(10000000))
print('{:,}'.format(2568552.5554))

# 如果在字符串中需要直接展示花括号，则用另一个花括号包裹起来转义
print('{{我很好}}:{}'.format('nice'))
print('{{{}}}'.format('nice'))



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



# 正负号
"""
正负号选项仅对数字类型生效
取值有三种：
    + 正数前面添加正号，负数前面添加负号
    - 仅在负数前面添加负号（默认行为）
    空格：正数前面需要添加一个空格，以便与负数对齐
"""
print('{:哈=+8.2f}'.format(3.14159))
print('{:哈=+8.2f}'.format(-3.14159))
print('{:哈=+8.2f}'.format(0))
print('{:哈=+8.2f}'.format(-0))



"""
# 号：
    给u二进制数加上 0b 前缀
    给八进制数加上 0o 前缀
    给十六进制数加上 0x 前缀
"""



"""
最小宽度 width：
    如果不指定，最小字段宽度由内容决定，与内容相等
    如果最小宽度前面有一个前导 0，意味着用 0 填充
    这等价于指定了 0= 的填充和对齐方式
"""



"""
分组选项grouping_option 的取值有两种
    1、逗号 ,：使用逗号对数字以千为单位进行分隔。n 类型的数字可以使用本地化的分隔符
    2、下划线 _：使用下划线对浮点数和 d 类型的整数以千为单位进行分隔。对于 b、o、x 和 X 类型，每四位插入一个下划线，其他类型都会报错。
    备注：n 类型在本机无法使用分组选项 ,原因可能是中文没有数字分隔符
"""
# n 类型使用本地化的分组选项 ,
# 此项报错，怀疑是因为中文没有数字的分隔符
# print('数字：{0:,n}'.format(6666))
# 使用 d 类型确实是可以的
print('数字：{0:,d}'.format(6666))

# 分组选项 _ 作用于 b 类型
print('数字：{0:_b}'.format(0b100111011))
# 分组选项 _ 作用于 o 类型
print('数字：{0:_o}'.format(0o426754316))
# 分组选项 _ 作用于 x 类型
print('数字：{0:_x}'.format(0x2a846e98d))
# 分组选项 _ 作用于 X 类型
print('数字：{0:_X}'.format(0X2a846e98d))
# 分组选项 _ 作用于其他类型（比如 n 类型）
# print('字符串：{0:_n}'.format(1234567))



"""
精度：
    精度指定了小数点后面要展示多少位小数
    对于非数字类型，精度指定了最大字段宽度
    整数类型不能指定精度
"""
# 对于非数字类型，精度指定最大字段宽度
print('{0:.3}'.format('哇哈哈哈哈哈'))
# 整数类型不能指定精度
# print('{:.3d}'.format(666))

# 类型码可以分为三大类：1、字符串类型    2、整数类型    3、浮点数类型
# 字符串类型：1、s 字符串类型。这是字符串的默认类型，可以省略   2、None 不指定类型。同 s 类型
# s 类型
print('{0:s}'.format('略略略'))
# s 类型可以省略
print('{0:}'.format('略略略'))

# 整数类型
# b 二进制
print('{:b}'.format(20))
# o 八进制
print('{:o}'.format(20))
# d 十进制
print('{:d}'.format(20))
# x 十六进制数，a 到 f 小写
print('{:x}'.format(20))
# X 十六进制数，A 到 F 大写
print('{:X}'.format(20))
# c 字符。把整数转换为相应的 Unicode 字符，然后再打印
print('{:c}'.format(97))
# n 数字 number 类型，与 d 相同，只不过它会使用本地化的数字分隔符
"""
经试验，在本机为 n 类型指定任何分组选项（, 和 _）都会报错。ValueError: Cannot specify ',' with 'n'.
"""
print('{:n}'.format(66666))
# 经试验，本机无法为 n 指定任何分组选项（,_）
# print('{:,n}'.format(66666)
# None 不指定类型，与 d 相同

# 浮点数类型
# e 科学记数法，用 e 来表示指数。默认精度为 6 位
print('{:e}'.format(1234565.35878989))
# E 与 e 相同，但是使用大写的 E 表示指数
print('{:E}'.format(1234565.35878989))
# 修改精度为10位
print('{:.10E}'.format(1234565.35878989))

# f 定点记法，默认精度为 6
print('{:f}'.format(1234565.35878989))
# F 定点记法，同 f，但是会把 nan 转换成 NAN，把 inf 转换成 INF
nan = float('nan')
inf = float('inf')
print('{:F}\n{:F}'.format(nan, inf))

# g 通用 general 格式。自动转换到 e 或者 f 格式，具体的转换规则在此省略。
# 正无穷、负无穷、正零、负零和非数字分别显示为 inf，-inf，0，-0，nan。指定精度为 0 时等价于精度为 1。默认精度为 6 位
print('{:g}'.format(1234565.35878989))
print('{:g}'.format(1234.3587))
# G 通用 general 格式。自动转换到 E 或者 F 格式，转换规则同上，相应表示方式换成大写。
print('{:G}'.format(1234565.35878989))
print('{:G}'.format(1234.3587))

# n 数字 number 类型。跟 g 一样，只不过用本地化的分隔符来分隔数字。
print('{:n}'.format(1234565.35878989))
print('{:n}'.format(1234.3587))
# 经试验，本机指定分组选项会报错
# print('{:,n}'.format(1234.3587))
# print('{:_n}'.format(1234.3587))

# % 百分号类型。会将数字乘以 100，然后以 f 定点 fixed-point 格式显示，最后加上一个百分号 %
print('{:%}'.format(1))

# None 不指定类型。输出效果类似调用 str() 函数


# 对象可以自定义格式说明符来替换标准格式说明符，比如 datetime 类
from datetime import datetime
print('today is {0:%a %b %d %H:%M:%S %Y}'.format(datetime.now()))
print('today is {0:%c}'.format(datetime.now()))

