import re

# 正则表达式
"""
要匹配边长的字符，在正则表达式中，
用 * 表示任意个字符（包括0个），
用 + 表示至少一个字符，
用 ？ 表示 0 个或 1 个字符，
用 {n} 表示 n 个字符，
用 {n,m} 表示 n-m 个字符
"""

"""
\d{3}\s+\d{3,8}
\d{3} -- 表示匹配3个数字，例：'003'
\s -- 可以匹配一个空格（也包括tab等空白符），例：' ','  '
\d{3,8} -- 表示3-8个字符，例：'123456'
"""

"""
更精准地匹配，可以用[]表示范围
[0-9a-zA-Z\_] -- 可以匹配一个数字、字母或者下划线
[0-9a-zA-Z\_]+ -- 可以匹配至少由一个数字、字母或者下划线组成的字符串，例:'a100','0_z','Py3000'
[a-zA-z\_][0-9a-zA-Z\_]* -- 可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量
[a-zA-Z\_][0-9a-zA-Z\_]{0,19} -- 更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）
A|B -- 可以匹配A或B，所以(P|p)ython可以匹配'python'或'Python'
^ -- 表示行的开头，^\d -- 表示必须以数字开头
$ -- 表示行结束，\d$ -- 表示必须以数字结束
py可以匹配'python'，但加上^py$就变成了整行匹配，就只能匹配'py'
"""

"""
re模块，包含所有正则表达式的功能，
由于Python的字符串本身也用\转义，因此写的时候要特别注意，例：s = 'abc\\-001'
强烈建议使用Python的r前缀，就不用考虑转义的问题，例：s = r'abc\-001'
"""
"""
判断正则表达式是否匹配
import re
re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
match()方法判断是否匹配，如果匹配成功，返回一个match对象，否则返回None
"""
# 常见判断方法
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

# 切分字符串
# 用正则表达式切分字符串比用固定的字符更灵活，正常的切分代码如下
a = 'a b   c'.split(' ')
print(a)

# 无法识别连续的空格，用正则表达式如下
b = re.split(r'\s+', 'a b   c')
print(b)

# 无论多少个空格都可以正常分割，加入,试试
c = re.split(r'[\s\,]+', 'a,b,  c   d')
print(c)

# 再加入 ; 试试
d = re.split(r'[\s\,\;]+', 'a,b;; c   d')
print(d)

# 分组 --正则表达式有提取子串的强大功能，用()表示的就是要提取的分组（Group）
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-123456')
print(m.group(0))
print(m.group(1))
print(m.group(2))
"""
如果正则表达式定义了组，就可以再match对象上用group()方法提取出子串来
注意到group(0)永远是原始字符串，group(1)、group(2)...表示第1、2、...个子串
"""

t = '16:08:45'
f = re.match(r'^(0[0-9]|1[0-9]|2[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(f.groups())

# 贪婪匹配 -- 正则匹配默认是贪婪匹配，就是匹配尽可能多的字符
e = re.match(r'^(\d+)(0*)$', '12036500').groups()
print(e)
# 由于\d+采用贪婪匹配，直接把后面的 0 全部匹配了，结果 0* 只能匹配空字符串
g = re.match(r'^(\d+?)(0*)$', '12036500').groups()
print(g)
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的 0 匹配处理，加个？就可以让\d+采用非贪婪匹配

# 编译
"""
在Python中使用正则表达式时，re模块内部会干两件事情
1、编译正则表达式，如果正则表达式的字符串本身不合法，会报错
2、用编译后的正则表达式去匹配字符串
如果一个正则表达式要重复使用几千次，出于效率的考虑，可以预编译该正则表达式，
接下来重复使用时就不需要编译这个步骤，直接匹配
"""
# 编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用
x = re_telephone.match('010-123456').groups()
print(x)
y = re_telephone.match('010-8978860').groups()
print(y)
# 编译后生成的正则表达对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串
