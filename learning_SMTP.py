"""
 SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件
 Python对SMTP支持有smtplib和email两个模块，email复制构造邮件，smtplib复制发送邮件
"""

"""
常用服务器名称、地址和ssl协议端口
IMAP -- imap.qq.com -- 993
SMTP -- smtp.qq.com -- 25/465/587
POP3 -- POP3.qq.com -- 995
 POP3和IMAP的区别：
 POP3在客户端邮箱中所做的操作不会反馈到邮箱服务器，
 IMAP则会反馈到邮箱服务器，会做相应的操作
"""

import smtplib
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr


def _format_addr(s):
    """格式化邮箱地址"""
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_text_email(sender, receivers, content, sender_name, email_title, smtp_server, sender_authorization_code=None, receivers_name=None, port=25):
    """
    SMTP发送纯文本邮件
    :param sender: 发件人邮箱
    :param sender_authorization_code: 发件人邮箱授权码
    :param receivers: 收件人邮箱
    :param content: 邮件正文内容
    :param sender_name: 发件人名称
    :param receivers_name: 收件人名称
    :param email_title: 邮件标题
    :param smtp_server: 第三方SMTP服务器，根据需求自己设置服务器
    :param port: 端口
    :return:
    """
    """
        构造MIMEText对象时，第一个参数--邮件正文，第二个参数--MIME的subtype，
        传入'plain'表示纯文本，最终的MIME就是'text/plain',最后一定要用utf-8编码保证多语言兼容性
    """
    # 纯文本--plain, HTML--html
    # msg = MIMEText(content, 'plain', 'utf-8')
    """
        带附件的邮件可看作包含若干部分的邮件：文本和各个附件本身，
        所以可构造一个MIMEMultipart对象代表邮件本身，
        然后往里加一个MIMEText作为邮件正文，
        再继续往里加上表示附件的MIMEBase对象即可
    """
    # 构造一个MIMEMultipart对象代表邮件本身，利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative
    msg = MIMEMultipart('alternative')
    msg.attach(MIMEText(content, 'html', 'utf-8'))         # 正文内容，plain代表纯文本，html代表支持html
    # 发件人信息
    msg['From'] = _format_addr('%s <%s>' % (sender_name, sender))
    # 收件人信息，msg['To']接收的是字符串而不是list，如果有多个邮件地址，用 , 分隔即可
    for rec in receivers:
        msg['To'] = _format_addr('%s <%s>' % (receivers_name, rec))
    # 邮件标题
    msg['Subject'] = Header('%s' % email_title, 'utf-8').encode()


    # 添加附件--方法1，就是加上一个MIMEBase，从本地读取文件
    # with open('文件路径', 'rb') as f:
    #     # 设置附件的MIME和文件名，第一个参数：附件类型（text,image），第二个参数：附件后缀名
    #     mime = MIMEBase('text', 'txt', filename='文件名')
    #     # 加上必要的头信息，filename任意写，写什么名字，邮箱中就显示什么名字
    #     mime.add_header('Content-Dispostion', 'attachment', filename='xxxx')
    #     # 把附件的内容读进来
    #     mime.set_payload(f.read())
    #     encoders.encode_base64(mime)    # 主要是处理图片的时候有很大用处，不然图片会有问题
    #     # 作为附件添加到邮件
    #     msg.attach(mime)

    # 添加附件--方法2
    # att1 = MIMEText(open(r'C:\Users\Administrator\Desktop\dog.jpg', 'rb').read(), 'base64', 'utf-8')
    # att1['Content-Type'] = 'application/octet-stream'
    # # filename任意写，写什么名字，邮箱中就显示什么名字
    # att1['Content-disposition'] = 'attachment;filename="test.jpg"'
    # msg.attach(att1)
    # 多附件，可以复制黏贴以上方法

    # 将图片显示在正文
    with open(r'C:\Users\Administrator\Desktop\dog.jpg', 'rb') as f:
        # 图片添加到正文
        msgImage = MIMEImage(f.read())
        # 定义图片id
        msgImage.add_header('Content-ID', '<0>')
        # msgImage.add_header('X-Attachment_Id', '0')
        msg.attach(msgImage)

    try:
        smtp = smtplib.SMTP(smtp_server, port)        # SMTP协议默认端口是25
        # 只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接
        smtp.starttls()
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(1)
        # 登录SMTP服务器
        smtp.login(sender, sender_authorization_code)
        # 发送邮件,邮件正文是一个str，as_string()把MIMEText对象变成str
        smtp.sendmail(sender, receivers, msg.as_string())
        # 退出SMTP服务器
        print('邮件发送成功')
        smtp.quit()
    except smtplib.SMTPException as e:
        print('邮件发送失败--%s' % e)

if __name__ == '__main__':
    sender = '3383054774@qq.com'
    sender_authorization_code = 'dvcqydecddkwciji'
    # 由于可以一次发给多个人，所以传入一个list
    receivers = ['873119216@qq.com', '3383054774@qq.com']
    receivers_name = 'test'
    smtp_server = 'smtp.qq.com'
    # content = '<html><body><h1>hello</h1>' + '<p><img src="cid:0"></p>' + '</body></html>'
    content = '''
            <h2 style="color:red">hello, send by python</h2>
            <a href="https://www.baidu.com">this is a html</a>
            <p><img src="cid:0"></p>
    '''
    sender_name = '大小姐'
    email_title = '来自SMTP发邮件的测试'
    send_text_email(sender, receivers, content, sender_name, email_title, smtp_server, sender_authorization_code,
                    receivers_name)



