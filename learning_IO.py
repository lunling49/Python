# 读取文件，传入文件名和标示符
f = open('D:/test.txt', 'r')    # 标示符'r'表示读,文件路径用"/"或者"\\"
# 如果文件不存在，open()函数会抛出IOError错误，并给出错误码和详细信息

# 若文件打开成功，接下来调用read()方法一次读取文件的全部内容，用str对象表示
a = f.read()
print(a)

# 最后调用close()关闭文件。文件使用完后必须关闭，因为文件对象会占用操作系统的资源，且操作系统同一时间能打开的文件数量也是有限的
f.close()

# 由于文件读写时都有可能产生IOError，一旦出错，f.close()就不会调用。
# 为了保证无论是否出错都能正确地关闭文件，可try...finally实现
try:
    f = open('d:/test.txt', 'r')     # 返回的f存在为空和不为空2种情况
    print(f.read())
finally:
    if f:        # 这句的意思是f不为空
        f.close()

# 每次都用try...finally太繁琐，Python引入了with语句自动调用close()方法
with open('d:/test.txt', 'r') as f:
    print(f.read())
# with跟try...finally是一样的，代码更简洁，且不必调用close()方法

"""
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了
所以保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容
另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
"""

# 若文件很小，read()一次性读取最方便；若不确定文件大小，反复调用read(size)比较保险；若是配置文件，调用readlines()最方便
with open('d:/test.txt') as t:
    for line in t.readlines():
        print(line.strip())     # 把末尾的'\n'删掉

"""
file-like Object
像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object
除了file外，还可以是内存的字节流，网络流，自定义流等
file-like Object不要求从特定类继承，只要写个read()方法就行
StringIO就是在内存中创建的file-like Object，常用作临时缓冲
"""

"""
二进制文件
上面所讲的默认都是读取文本文件，且是utf-8编码的文本文件，
要读取二进制文件，如图片、视频等，用'rb'模式打开文件即可
"""
i = open('d:/test.jpg', 'rb')
print(i.read())

"""
字符编码
读取非utf-8编码的文本文件，需要给open()函数传入encoding参数
"""
# 例如，读取gbk编码的文件
s = open('d:/gbk.txt', 'r', encoding='gbk')
print(s.read())
"""
遇到有些编码不规范的文件，可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符
这种情况，open()函数还接收一个error参数，表示如果遇到编码错误后如何处理，最简单的方式就是直接忽略
"""
h = open('d:/gbk.txt', 'r', encoding='gbk', errors='ignore')

"""
写文件
写文件和读文件是一样的，唯一的区别是调用open()函数是，传入标示符'w'或者'wb'，表示写文本文件或二进制文件
"""
x = open('d:/test.txt', 'w')
x.write('you are nice')
x.close()
"""
可以反复调用write()来写入文件，然后务必要调用close()来关闭文件
当写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。
所以，还是用with语句来得保险
"""
with open('d:/test.txt', 'w') as f:     # 如果文件不存在，会自动创建，'w'表示写数据，写之前会清空原文件中的原有数据
    f.write('you are lucky')

with open('d:/test.txt', 'a') as f:     # 'a'表示append，即在原来文件内容后继续写数据（不清除原有数据）
    f.write('you are lucky')
# 要写入特定编码的文本文件，给open()函数传入encoding参数，将字符串自动转换成指定编码

# 定位
f.seek(2, 0)    # 第一个数字表示偏移量，第二个数字表示文件从哪里开始的位置
# 当前位置
f.tell()        # 返回当前文件位置

"""
标示符         打开方式            指针位置
b           二进制模式
t           文字模式（默认）
+           打开磁盘文件进行更新（读写）
r           只读（默认模式）    指针在文件开头，文件不存在则报错
rb          二进制格式只读      指针在文件开头，文件不存在则报错
r+          可读可写            指针在文件开头，文件不存在则报错
rb+         二进制格式可读可写  指针在文件开头，文件不存在则报错
w           只写                文件存在，则覆盖；不存在，则创建
wb          二进制格式只写      文件存在，则覆盖；不存在，则创建
w+          可读可写            文件存在，则覆盖；不存在，则创建
wb+         二进制格式可读可写  文件存在，则覆盖；不存在，则创建
a           追加                文件存在，指针在文件尾追加；不存在，则创建
ab          二进制格式追加      文件存在，指针在文件尾追加；不存在，则创建
a+          可读可写            文件存在，指针在文件尾追加；不存在，则创建
ab+         二进制格式可读可写  文件存在，指针在文件尾追加；不存在，则创建
"""
