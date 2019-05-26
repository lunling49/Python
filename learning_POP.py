"""
收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或手机。
收取邮件最常用的协议是POP协议，目前版本号是3，俗称POP3。
Python内置一个poplib模块，实现了POP3协议，可直接用来收邮件。
注意到POP3协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本，
这和smtp协议很像，smtp发送的也是经过编码后的一大段文本。
"""
from email.parser import Parser
import poplib
from email.header import decode_header
from email.utils import parseaddr

"""
要把pop3收取的文本变成可以阅读的邮件，需用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象
收取邮件分两步
1、用poplib把邮件的原始文本下载到本地
2、用email解析原始文本，还原为邮件对象
"""
# 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

# 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示
def guess_charset(msg):
    # 从msg对象获取编码
    charset = msg.get_charset()
    if charset is None:
        # 如果获取不到，再从Content-Type字段获取
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >=0:
            charset = content_type[pos + 8:].strip()
    return charset

# Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层。
# 因此用递归打印出Message对象的层次结构
def print_info(msg, indent=0):      # indent用于缩进显示
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    # 需要解码Subject字符串
                    value = decode_str(value)
                else:
                    # 需要解码Email地址
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):        # 如果邮件对象是一个MIMEMultipart
        # get_payload()返回list，包含所有的子对象
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s----------------' % ('  ' * indent))
            # 递归打印每一个子对象
            print_info(part, indent + 1)
    else:
        # 邮件对象不是一个MIMEMultipart,就根据content_type判断
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            # 纯文本或HTML内容
            content = msg.get_payload(decode=True)
            # 要检测文本编码
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            # 不是文本,作为附件处理
            print('%sAttachment: %s' % ('  ' * indent, content_type))


# 通过pop3下载邮件
# 输入邮件地址，口令和pop3服务器地址
email = '3383054774@qq.com'
password = 'dvcqydecddkwciji'
pop3_server = 'pop.qq.com'

# 连接到pop3服务器
server = poplib.POP3(pop3_server)
# 打开或关闭调试信息
server.set_debuglevel(1)
# 可选，打印pop3服务器的欢迎文字
print(server.getwelcome().decode('utf-8'))

# 身份验证
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间
print('Messagee: %s, Size: %s' % server.stat())
# list()返回所有邮件的编号
resp, mails, octets = server.list()
# 可以查看返回的列表，类似[b'1 82923', b'2 2184', ...]
print(mails)

# 获取最新一封邮件，注意索引号从1开始
index = len(mails)
resp, lines, octets = server.retr(index)
# 用POP3获取邮件其实很简单，要获取所有邮件，只需要循环使用retr()把每一封邮件内容拿到即可

# lines存储了邮件的原始文本的每一行
# 可以获得整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 解析邮件,把邮件内容解析为Message对象
msg = Parser().parsestr(msg_content)
print_info(msg)
# 可以根据邮件索引号直接从服务器删除邮件
# server.dele(index)
# 关闭连接
server.quit()




