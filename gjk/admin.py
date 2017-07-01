from django.contrib import admin

# Register your models here.
from gjk.models import Column, Article


class ColumnAdmin(admin.ModelAdmin):
    
    list_display = ['url', 'column']
    list_editable = ['url',  ]
    list_display_links = ['column']


class ArticleAdmin(admin.ModelAdmin):

    list_display = ['column', 'title',  'sourcefrom',]

    list_editable = ['column', 'sourcefrom', ]

    list_display_links = ['title']

    # 发布文章界面
    fieldsets = [
        (None, {
            'fields': ('column', 'title', 'content', 'sourcefrom', )
        }),
        ('高级设置', {
            'classes': ('collapse',),  # 折叠
            # 'classes': ('wide',),  # 展开
            'fields': ('abstract', 'img', 'slug_url', )
        }),
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Column, ColumnAdmin)