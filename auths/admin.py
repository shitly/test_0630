from django.contrib import admin

# Register your models here.
from .models import NewUser

class UserAdmin(admin.ModelAdmin):

    list_display = ['username', 'password', 'email', 'name']

    list_editable = [

    ]

    list_display_links = ['username']

    # 发布文章界面
    fieldsets = [
        (None, {
            'fields': ('username', 'password', 'email')
        }),
        ('高级设置', {
            'classes':('collapse',),    # 折叠
            # 'classes': ('wide',),  # 展开
            'fields': ("name", "profile")
        }),

    ]

admin.site.register(NewUser, UserAdmin)