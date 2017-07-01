from django.db import models


# 本数据库只会用到最近的一条信息,id最大-date最近的那个
class Config(models.Model):
    modify_date = models.DateTimeField(verbose_name="修改日期")
    score_height = models.CharField(verbose_name="分数权重", max_length=244)

