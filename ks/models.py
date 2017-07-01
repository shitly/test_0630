from django.db import models

# Create your models here.


class Tag(models.Model):
    tag = models.CharField("问题标签类别", max_length=155)


class QA(models.Model):
    q = models.CharField('问题', max_length=144, default="")
    a = models.IntegerField("答案|1234")
    x1 = models.CharField('选项1', max_length=144, default="")
    x2 = models.CharField('选项2', max_length=144, default="")
    x3 = models.CharField('选项3', max_length=144, default="")
    x4 = models.CharField('选项4', max_length=144, default="")
    x4 = models.CharField('选项5', max_length=144, default="")

    tag = models.ForeignKey(Tag, verbose_name="类别", )

    class Meta:
        verbose_name = "问题和答案"


'''
批量导入试题：
    全部固定; 选项id固定了; 但是页面的排布可以A3B2等。
    答案中的 a 为 ABCD的list, [1,2,3,4] <=> 1234 <==> [a,b,c,d]

'''

