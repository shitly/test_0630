from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser
# Create your models here.


@python_2_unicode_compatible
class NewUser(AbstractUser):
    profile = models.CharField('profile', default='', max_length=256)
    name = models.CharField("真实名字", default='', max_length=256)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户"



