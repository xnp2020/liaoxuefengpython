from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'nianping.xia@insolu.cn'
password = 'PCgRaG3HteehUJLN'
to_addr = ['xnp2010@outlook.com', 'xnp2010@qq.com']
smtp_server = 'smtp.exmail.qq.com'
smtp_port = 587

# 利用MIMEMultipart组合HTML和Plain，以支持老设备
msg = MIMEMultipart()
msg['From'] = _format_addr(f'Python爱好者 <{from_addr}>')
msg['To'] = _format_addr('管理员 <%s>' % to_addr)

msg['Subject'] = Header('来自STMP的问候......', 'utf-8').encode()

# 邮件正文
msg.attach(MIMEText('hello', 'plain', 'utf-8'))

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
