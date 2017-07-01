from django.contrib import admin

# Register your models here.

from .models import Course, CoruseConnectionStudent, Tag


class CourseAdmin(admin.ModelAdmin):

    list_display = ['tag', 'name', 'score', 'start_date', 'end_date', 'state', 'level', 'teacher']

    list_editable = ['score', 'start_date', 'end_date', 'state', 'level', 'teacher']

    list_display_links = ['name']

    # 发布文章界面
    fieldsets = [
        (None, {
            'fields': ('tag', 'name', 'teacher', 'start_date', 'img', 'desc', )
        }),
        ('高级设置', {
            'classes': ('collapse',),  # 折叠
            # 'classes': ('wide',),  # 展开
            'fields': ('end_date', 'URL', 'score', 'level', 'state')
        }),
    ]


class CCSAdmin(admin.ModelAdmin):

    list_display = ['student', 'course', 'course_schedule']


admin.site.register(Course, CourseAdmin)
admin.site.register(CoruseConnectionStudent, CCSAdmin)
admin.site.register(Tag)


