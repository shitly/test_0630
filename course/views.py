from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Course


def sigle_course_view(request, pk):
    # course = Course.objects.get(id=int(pk))
    # return redirect(course.url)
    return redirect("/static/ciso/page/class/map.html")

def course_view(request):
    ls = Course.objects.all()

    return render(request, "course.html", {
        "ls": ls
    })


def index_v2(request):

    return render(request, "index_v2.html", {
    })


def index(request):
    return render(request, "index.html", {})

from course.models import CoruseConnectionStudent, Course


## 隐藏空间; 不准用====全能查看内容
@login_required
def stu_course(request, pk):
    if not request.user.username == "actanble":
        return student_course(request)
    
    from auths.models import NewUser
    student = NewUser.objects.get(id=int(pk))
    ccs = CoruseConnectionStudent.objects.filter(student=student)
    res = []
    for x in ccs:
        temp_dir = {}
        temp_dir.setdefault("score", x.score)
        temp_dir.setdefault("course", x.course)
        res.append(temp_dir)
    return render(request, "student_course1.html", {
        "student": student,
        "res": res,
    })

@login_required
def student_course(request):
    student = request.user
    ccs = CoruseConnectionStudent.objects.filter(student=student)
    res = []
    for x in ccs:
        temp_dir = {}
        temp_dir.setdefault("score", x.score)
        temp_dir.setdefault("course", x.course)
        temp_dir.setdefault("course_schedule", x.course_schedule)
        res.append(temp_dir)
    return render(request, "student_course1.html", {
        "student": student,
        "res": res,
    })


# 全文搜索
def serach_course_view(request, content):
    return 


# 学生选课搜索
def sc_search(request, pk, content):
    url = request.HTTP_REFERER # 进站前的url
    ip = request.REMOTE_ADDR # ip

    return 


## 基础表单的页面操作

# 刷新课程 
def flush(request):
    return 

# 课程弃选
def delete_course(request):
    return 

# 课程选择
def select_course(request, student, course):
    return 

