#coding:utf-8
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
import smtplib
from email.header import Header
import os
#格式化收件人的显示名字，貌似现在不起作用了
def _format_addr(s):
    '''格式化一个邮件地址。因为如果包含中文，需要通过Header对象进行编码'''
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#打开测试报告
def open_report(file_path):
    file = file_path + 'result1478008428.605949.html'
    print(file)


# 输入Email地址和口令:
from_addr = "hulinjun2006@126.com"
password = "tanglirong520"
# 输入收件人地址:
to_addr = "453105647@qq.com"
# 输入SMTP服务器地址:
smtp_server = "smtp.126.com"
#发送纯文本
#msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
#发送html格式的
msg = MIMEText('<html><body><h1>你好：</h1><p>我是来自<a href="http://www.baidu.com">打开百度</a></p></body></html>','html','utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['Subject'] = Header(u'来自大西洋的问候', 'utf8').encode()
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)#打印发送过程
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
print("邮件发送成功")
server.quit()

if __name__ == "__main__":
    file_path = "./bbs/report/"
    open_report(file_path)
