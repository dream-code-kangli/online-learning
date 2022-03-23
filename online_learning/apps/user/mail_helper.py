import random
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr, parseaddr


def gen_vcode(length=6):
    return ''.join(random.choices('0123456789', k=length))


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def gen_vcode_msg(vcode, from_addr, to_addr):
    # 构建一个文本的mail对象
    text = '您好，欢迎注册在线学习平台。您的验证码是：{}, 有效期为 30 分钟, 请立即验证。'
    msg = MIMEText(text.format(vcode), 'plain', 'utf-8')
    msg['From'] = _format_addr('在线学习平台<%s>' % from_addr)
    msg['To'] = _format_addr('新用户<%s>' % to_addr)
    msg['Subject'] = Header('在线学习平台注册验证码', 'utf-8').encode()

    return msg


def send_vcode(smtp_server, from_addr, password, to_addr):
    # 构建一个 smtp 对象
    server = smtplib.SMTP(smtp_server, 25)
    # 设置一个调试级别
    server.set_debuglevel(1)
    # 登录
    server.login(from_addr, password)
    # 发送邮件
    vcode = gen_vcode()
    msg = gen_vcode_msg(vcode, from_addr, to_addr)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

    return vcode


if __name__ == '__main__':
    from_addr = 'runqian0813@163.com'
    to_addr = 'runqian0813@163.com'
    password = 'KJEESPMKNIHFATYD'
    smtp_server = 'smtp.163.com'
    send_vcode(smtp_server, from_addr, password, to_addr)
