#!/usr/bin/env python3
# coding:UTF-8
# 参考链接：
# https://blog.csdn.net/u011846143/article/details/78274911?locationNum=9&fps=1
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832745198026a685614e7462fb57dbf733cc9f3ad000

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
# setting account.
from_addr = 'klsmuej@126.com'
password = '901129ming'
smtp_server = 'smtp.126.com'

to_addr = '715555876@qq.com'

# format address
def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((\
		Header(name,'utf-8').encode(),\
		addr.encode('utf-8') if isinstance(addr,str) else addr))

# set email content
msg = MIMEText('第二封测试邮件...', 'plain', 'utf-8')
msg['From'] = f'Leon_126 {from_addr}'
msg['To'] = f'Leon——qq {to_addr}'
msg['Subject'] = Header(u'Pythony邮件发送测试', 'utf-8').encode()

# connect to smtp.
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
