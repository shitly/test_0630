# -*- coding:utf-8 -*-
from django.db import models
from DjangoUeditor.models import UEditorField

from auths.models import NewUser
# Create your models here.


class Tag(models.Model):
    tag = models.CharField("父栏目", max_length=244, default="")

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "栏目"


# 课程字段; 【课程名称, 教师, 开始时间, 结束时间, 总学分, 课程缩略图, 课程简要描述, 课程URL, 难度, 状态】
class Course(models.Model):
    tag = models.ForeignKey(Tag, verbose_name="父栏目")
    name = models.CharField("课程名称", max_length=255)
    teacher = models.ForeignKey(NewUser, verbose_name="教师")
    start_date = models.DateTimeField(verbose_name="开始时间")
    end_date = models.DateTimeField(verbose_name="结束日期")
    score = models.FloatField(verbose_name="学分")
    img = models.ImageField('课程缩略图', upload_to='uploads/course/images/',
                             default='uploads/course/images/default.jpg')
    desc = UEditorField('课程描述', height=400, width=800,
        default='', blank=True, imagePath="uploads/images/%(basename)s_%(datetime)s.%(extname)s",
        toolbars='full', filePath='uploads/files/%(basename)s_%(datetime)s.%(extname)s')
    URL = models.CharField(verbose_name="课程链接", max_length=115, default="")
    level = models.CharField("课程难度", max_length=200, default="easy")
    state = models.BooleanField(verbose_name = "状态", default = True)

    def __str__(self):
        return self.tag.tag + "_" + self.name
    
    class Meta:
        verbose_name = "课程"


class CoruseConnectionStudent(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(NewUser)
    course_schedule = models.IntegerField("课程进度", default=0)
    score = models.IntegerField(verbose_name="分数")

    class Meta:
        verbose_name = "课程学生映射关系"






