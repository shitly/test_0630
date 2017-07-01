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


def put_course():
    from course.models import Course, Tag

    tags0 = ["类目" + str(i) for i in range(6)]
    for i in range(len(tags0)):
        Tag.objects.create(tag=tags0[i])

    tags = Tag.objects.all()

    from datetime import timedelta
    for i in range(len(tags)):
        for j in range(20):
            Course.objects.create(
                tag=tags[i],
                name = tags[i].tag + "子课程" +str(j),
                teacher = NewUser.objects.all()[0],
                start_date = dt.now(),
                end_date = dt.now() + timedelta(days=1),
                score = randint(3) + 1,
                desc = "描述====" + tags[i].tag + "子课程" +str(j),
                URL = "/kc/",
            )
        print("写入=====END")

from course.models import CoruseConnectionStudent, Course

def set_course_student():
    students = NewUser.objects.all()
    courses = Course.objects.all()
    for s in students:
        for c in courses:
            CoruseConnectionStudent.objects.create(course=c, student=s, score=0)
    print("写入关系完成")
    

# put_course()
# set_course_student()