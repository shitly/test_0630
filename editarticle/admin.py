from django.contrib import admin

from editarticle.models import EArticle
# Register your models here.


class EArticleAdmin(admin.ModelAdmin):
    
    list_display = ['column', 'title',  'sourcefrom', 'fbz', 'pic', 'toutiao']

    list_editable = ['column', 'sourcefrom', ]

    list_display_links = ['title']

    # 发布文章界面
    fieldsets = [
        (None, {
            'fields': ('published', 'toutiao', 'column', 'title', 'content', 'sourcefrom', 'author', )
        }),
        ('高级设置', {
            'classes': ('collapse',),  # 折叠
            # 'classes': ('wide',),  # 展开
            'fields': ('abstract', 'img', 'slug_url', 'pic', 'pub_date')
        }),
    ]

admin.site.register(EArticle, EArticleAdmin)