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


from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')


msg = MIMEMultipart()
msg['From'] = _format_addr(f'Python爱好者 <{from_addr}>')
msg['To'] = _format_addr(f'管理员 <{to_addr}>')
msg['Subject'] = Header('来自STMP的问候......', 'utf-8').encode()

# 邮件正文
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件
with open('vmvare.png', 'rb') as f:
    # 设置附件的MIME和文件名
    mime = MIMEBase('image', 'png', filename='vmvare.png')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='vmvare.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
