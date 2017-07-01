from django.db import models

# Create your models here.

from auths.models import NewUser


# 消息推送
class Msg(models.Model):
    user = models.ForeignKey(NewUser, verbose_name="发送者", )
    msg = models.TextField("消息", default="")

    class Meta:
        verbose_name = "普通消息推送"


class ChatMsg(Msg):
    dt = models.DateTimeField("时间")
    other = models.ForeignKey(NewUser, verbose_name="接收者",)

    class Meta:
        verbose_name = "私聊消息"


class MailMsg(ChatMsg):

    class Meta:
        verbose_name = "邮箱消息"
