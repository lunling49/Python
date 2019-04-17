import ssl
import sys
from urllib import request
import re
import html
import time
res = request.urlopen('http://blog.leanote.com/qq-alan')
ret = res.read()
print(ret)

a = re.findall('abc', 'aaaaabcccabccd')
print(a)

b = re.findall('\d', 'avc1de3di4d')
print(b)

c = re.findall('\d\d\d\d', '123abv5644djg8993dg')
print(c)

"""
r 代表原始的，没有经过转义的
. 表示匹配任意字符
* 表示匹配无限个
(.*) 贪懒匹配，就是把div中的内容尽量多匹配出来
(.*?) 非贪懒匹配
"""
d = re.findall(r'<div>(.*)</div>', '<div>hello</div>')
print(d)

e = re.findall(r'<div>(.*)</div>', '<div>hello</div><div>world</div>')
print(e)

f = re.findall(r'<div>(.*?)</div>', '<div>hello</div><div>world</div>')
print(f)

# 提取博客的title
response = request.urlopen('http://blog.leanote.com/qq-alan')
content = response.read().decode('utf-8')
# 设置爬出内容的编码
# content = html.decode('utf-8')
# print(content)
m = re.findall(r'<title>(.*?)</title>', content, re.S)
for t in m:
    print(t)

"""
正则表达式语法
\n 表示换行符
"""
# 匹配除了换行符之外的所有字符
h = re.findall('.', 'aa\ndgeige')
print(h)
# 转义字符
i = re.findall('\.', 'a.c')
print(i)
# 字符集，中括号里任意一个匹配都可以
j = re.findall('a[bcd]e', 'abeaceadeabce')
print(j)
# 数字
m = re.findall('\d', 'av3d43dg7')
print(m)
# 非数字
n = re.findall('\D', 'av3d43dg7')
print(n)
# 空白字符
k = re.findall('\s', 'avc a\tber3')
print(k)
# 非空白字符
x = re.findall('\S', 'avc a\tber3')
print(x)
# 数字和字母
m = re.findall('\w', 'abi95dg#h--')
print(m)
# 非数字和字母
m = re.findall('\W', 'abi95dg#h--')
print(m)
# 匹配开头
m = re.findall('^abc', 'abcabc')
print(m)
# 匹配结尾
m = re.findall('abc$', 'abcabc')
print(m)
# 不区分大小写，用 re.I
m = re.findall('abc', 'abcaBcABC', re.I)
print(m)
# 匹配换行，用 re.S
s = '<div>hello\nworld</div>'
m = re.findall(r'<div>(.*)</div>', s, re.S)
print(m)
# 不区分大小写匹配换行,用或“|”位运算符
s = '<diV>hello\nworld</DIV>'
m = re.findall(r'<div>(.*)</div>', s, re.S | re.I)
print(m)
# 匹配多行，用 re.M
m = re.findall('^abc', 'abc\nabc', re.M)
print(m)
# 匹配一个或0个b，用 ？   （匹配的是符号前面的字符）
m = re.findall('ab?', 'ababbabbba')
print(m)
# 匹配至少一个b，用 +
m = re.findall('ab+', 'aababbabbbb')
print(m)
# 匹配至少0个，用 *
m = re.findall('ab*', 'aababbbaaabbb')
print(m)
# 匹配com结尾的邮箱
m = re.findall('\w+@+\w+\.com', '123456@qq.com,123456@qq.org')
print(m)

# 其他方法，如果是多次调用某个正则，则最好先编译后使用
p = re.compile('^abc', re.M | re.I)
m = p.findall('abc\nabc')
print(m)
m = p.findall("abcdef\nfdsfabc")
g = p.findall("dabcdef\nefdsfabc")
print(m, g)

# 爬取糗事百科的段子
def crawl_joke_list(page=1):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
    url = 'https://www.qiushibaike.com/text/page/' + str(page)
    req = request.Request(url, headers=headers)
    res = request.urlopen(req).read().decode('utf-8')
    # 获取每个段子的正则
    pattern = re.compile('<div class=\"article block untagged mb15.*?<div class=\"content\">.*?</div>', re.S)
    # 把<br/>替换成换行
    body = html.unescape(res).replace('<br/>', '\n')
    m = pattern.findall(body)
    # 获取用户名的正则
    user_pattern = re.compile('<div class=\"author clearfix\">.*?<h2>(.*?)</h2>', re.S)
    # 获取段子的正则
    content_pattern = re.compile('<div class=\"content\">.*?<span>(.*?)</span>.*?</div>', re.S)
    for joke in m:
        user = user_pattern.findall(joke)
        content = content_pattern.findall(joke)
        output = []
        if len(user) > 0:
            output.append(user[0])
        if len(content) > 0:
            output.append(content[0].replace('\n', ''))
        print('\t'.join(output))
        time.sleep(2)

if __name__ == '__main__':
    for i in range(1, 6):
        crawl_joke_list(i)
