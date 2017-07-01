from django.db import models

# Create your models here.

from auths.models import NewUser

from gjk.models import Column, Article
class EArticle(Article):
    toutiao = models.BooleanField('设为头条',default=False)
    pic = models.ImageField('头条图片436*200',upload_to='uploads/top_images/',default='uploads/top_images/default.jpg')
    published = models.BooleanField('正式发布',default=True)
    pub_date = models.DateTimeField('发表日期')
    author = models.CharField('作者', default='清朗安全',max_length=255)
    fbz = models.ForeignKey(NewUser, verbose_name="发布者")
    slug_name = models.CharField('默认栏目名勿改',default='安全热点',max_length=255)

    class Meta:
        verbose_name = "稿件库编辑辅助服务"