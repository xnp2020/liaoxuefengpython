import smtplib
from email.mime.text import MIMEText  # 邮件正⽂
from email.header import Header  # 邮件头

# 登录邮件服务器
smtp_obj = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  # 发件⼈邮箱中的SMTP服务器，端⼝是25
smtp_obj.login("nianping.xia@insolu.cn",
               "PCgRaG3HteehUJLN")  # 括号中对应的是发件⼈邮箱账号、邮箱密码
# smtp_obj.set_debuglevel(1)  # 显示调试信息

# 设置邮件头信息
name = 'xianianping'
name = 'xianianping'
html_body = f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <h3>Dear {name}:</h3>
    <p>辛苦了！请查收你5月的工资条：</p>
    <table border: 1px solid black; >
        <tr>
            <th>姓名</th>
            <th>邮箱</th>
        </tr>
        <tr>
            <td>{name}</td>
            <td>xxx@xx.com</td>
        </tr>
    </table>


</body>

</html>
"""


msg = MIMEText(html_body, "html", "utf-8")
msg["From"] = 'nianping.xia@insolu.cn'  # 发送者
msg["To"] = 'nianping.xia@insolu.cn,xnp2010@qq.com'  # 接收者
msg["Subject"] = Header("工资条", "utf-8")  # 主题
# 发送
smtp_obj.sendmail("nianping.xia@insolu.cn",
                  ["nianping.xia@insolu.cn", "xnp2010@qq.com"], msg.as_string())
