from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 请求用户输入
from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')


# 构造邮件

# 纯文本邮件
# msg = MIMEText('hello,send by Python...', 'plain', 'utf-8')  # MIMEText对象第一个参数是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性

# msg['From'] = _format_addr(f'Python爱好者 <{from_addr}>')
# msg['To'] = _format_addr(f'管理员 <{to_addr}>')
# msg['Subject'] = Header('来自STMP的问候......', 'utf-8').encode()

# html邮件
msg = MIMEText('<html><body><h1>Hello</h1>' +
               '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
               '</body></html>', 'html', 'utf-8')

msg['From'] = _format_addr(f'Python爱好者 <{from_addr}>')
msg['To'] = _format_addr(f'管理员 <{to_addr}>')
msg['Subject'] = Header('来自STMP的问候......', 'utf-8').encode()


# 发送邮件
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)

# as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
