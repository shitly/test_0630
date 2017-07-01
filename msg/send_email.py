import os

###
from os.path import dirname, abspath
PROJECT_DIR = dirname(dirname(abspath(__file__)))
import sys
sys.path.insert(0, PROJECT_DIR)
os.environ["DJANGO_SETTINGS_MODULE"] = "minicms.settings"

import django
django.setup()


from django.core import mail
from django.core.mail import send_mail

'''

send_mail(
        subject="Hello",
        message="whatareyoudingars",
        # from_email='jerryceron4646@gmail.com',
        from_email='m13429888211@163.com',
        recipient_list=['m13429888211@163.com'],
)

'''

# ['actanble@aliyun.com', "2970090120@qq.com", "13429888211@sina.cn", "m13429888211@163.com", 'actanble@foxmail.com'
# 
# ]
'''
connection = mail.get_connection()


# Manually open the connection
connection.open()

# Construct an email message that uses the connection
email1 = mail.EmailMessage('Hello', 'Body goes here', 'actanble@aliyun.com',
                          ['actanble@aliyun.com', ], connection=connection)
email1.send() # Send the email


# Send the two emails in a single call -
connection.send_messages([email1, ])
# The connection was already open so send_messages() doesn't close it.
# We need to manually close the connection.
connection.close()

'''

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
 
 
from_email = settings.DEFAULT_FROM_EMAIL
# subject 主题 content 内容 to_addr 是一个列表，发送给哪些人
msg = EmailMultiAlternatives(
        "markdown测试粗体", 
       "<h1>测试<h1></br><strong>cuti</strong>", 
        'm13429888211@163.com', 
        ["m13429888211@163.com"],
)
 
msg.content_subtype = "html"
 
# 添加附件（可选）
msg.attach_file('F:\\TEST\\msg\\tests.pdf')
 
# 发送
for i in range(10):
        msg.send()