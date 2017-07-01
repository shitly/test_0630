from django.contrib import admin

# Register your models here.

from .models import Msg, ChatMsg, MailMsg

admin.site.register(Msg)
admin.site.register(ChatMsg)
admin.site.register(MailMsg)


