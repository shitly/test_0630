from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Course, CoruseConnectionStudent

'''
教师管理平台：
    1, 可以访问每个学生的课程主页; 但是不能进行修改。
    2, 统计学生基本信息
        a, 学生学号, 各个类目的课程完成百分比
        b, 学生最近完成时间
        c, 学生的

    3, 可以进行打分
    4, 可以进行记录导入和导出

'''
def homepage(request):
    return 