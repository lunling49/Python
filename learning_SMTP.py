# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件
# Python对SMTP支持有smtplib和email两个模块，email复制构造邮件，smtplib复制发送邮件

import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr


def _format_addr(s):
    """格式化邮箱地址"""
    # 解析邮件地址，保证有别名可以显示
    name, addr = parseaddr(s)
    # 防止中文问题，进行转码处理，并格式化为str返回
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
    :param smtp_server: SMTP服务器
    :param port: 端口
    :return:
    """
    # 第三方 SMTP 服务
    mail_host = 'smtp.%s' % smtp_server         # 设置服务器
    # 注意到构造MIMEText对象时，第一个参数--邮件正文，第二个参数--MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain',最后一定要用utf-8编码保证多语言兼容性
    msg = MIMEText(content, 'plain', 'utf-8')
    # 发件人信息
    msg['From'] = _format_addr('%s <%s>' % (sender_name, sender))
    # 收件人信息，msg['To']接收的是字符串而不是list，如果有多个邮件地址，用 , 分隔即可
    msg['To'] = _format_addr('%s <%s>' % (receivers_name, receivers))
    # 邮件标题
    msg['Subject'] = Header('%s' % email_title, 'utf-8').encode()

    email_server = smtplib.SMTP(mail_host, port)        # SMTP协议默认端口是25
    # 打印出和SMTP服务器交互的所有信息
    email_server.set_debuglevel(1)
    # 登录SMTP服务器
    email_server.login(sender, sender_authorization_code)
    # 发送邮件
    email_server.sendmail(sender, receivers, msg.as_string())
    # 退出SMTP服务器
    email_server.quit()

if __name__ == '__main__':
    sender = '3383054774@qq.com'
    sender_authorization_code = 'dvcqydecddkwciji'
    receivers = '3383054774@qq.com', '873119216@qq.com'
    smtp_server = 'qq.com'
    content = '写方法发邮件'
    sender_name = '大小姐'
    receivers_name = '你厉害'
    email_title = '来自SMTP发邮件的测试'
    send_text_email(sender, receivers, content, sender_name, email_title, smtp_server, sender_authorization_code, receivers_name)



