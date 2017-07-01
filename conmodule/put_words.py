import os

###
from os.path import dirname, abspath
PROJECT_DIR = dirname(dirname(abspath(__file__)))
import sys
sys.path.insert(0, PROJECT_DIR)
os.environ["DJANGO_SETTINGS_MODULE"] = "minicms.settings"

import django
django.setup()


def post_cate_into_minicms():
    from conmodule.models import Word
    for i in range(100):
        word = "词"+str(i)
        Word.objects.create(word=word)

    print("写入词完成")


if __name__ == "__main__":
    post_cate_into_minicms()## 切记不要重复导入