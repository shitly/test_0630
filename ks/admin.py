from django.contrib import admin

# Register your models here.

from .models import QA

class QAdmin(admin.ModelAdmin):
    list_display = ['q', 'a', 'tag', 'x1', 'x2', 'x3', 'x4']

admin.site.register(QA, QAdmin)
