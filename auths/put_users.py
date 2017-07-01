import os

###
from os.path import dirname, abspath
PROJECT_DIR = dirname(dirname(abspath(__file__)))
import sys
sys.path.insert(0, PROJECT_DIR)
os.environ["DJANGO_SETTINGS_MODULE"] = "minicms.settings"

import django
django.setup()

from auths.models import NewUser

from datetime import datetime as dt


from numpy.random import randint

def get_users(n):
    
    for i in range(n):
        username = str( 2017115200 + i)
        password = "123456"
        email = "test@qq.com"
        user = NewUser(username=username, email=email, password=password)
        user.save()
    print("写入结束")

get_users(30)