from django.shortcuts import render, redirect
from .models import NewUser
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User


def home(request):
    return HttpResponse(request, "=================================")


def authenticate_NewUser(user):
    users = NewUser.objects.all()
    user_list = [{}.setdefault(x.username, x.password) for x in users]
    if {}.setdefault(user.username, user.password) in user_list:
        return True
    return False

def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['uid']
            password = form.cleaned_data['pwd']
            user = NewUser.objects.get(username=username)
            if user is not None and authenticate_NewUser(user):
                login(request, user)
                # url = request.POST.get('source_url', '/')
                url = "/student_course/" + str(user.id)
                return redirect(url)
            else:
                return render(request, 'login.html', {'form': form, 'error': "password or username is not ture!"})
        else:
            return render(request, 'login.html', {'form': form})


@login_required
def log_out(request):
    url = request.POST.get('source_url', '/')
    logout(request)
    return redirect(url)


def register(request):
    error1 = "this name is already exist"
    valid = "this name is valid"
    # phone_error = "this phone is not act"

    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            # phone = form.cleaned_data['phone']

            users = NewUser.objects.all()
            if password1 != password2:
                return render(request, 'register.html', {'form': form, 'msg': "two password is not equal"})
            else:
                if username in [x.username for x in users]:
                    user = authenticate(username=username, password=password1)
                    login(request, user)
                    # url = request.POST.get('source_url', '/')
                    return HttpResponse(request, "你已经有账号了, 可以返回主界面直接登录")
                user = NewUser(username=username, email=email, password=password1)
                user.save()
                # return render(request, 'login.html', {'success': "you have successfully registered!"})
                return redirect("/login/")
        else:
            return render(request, 'register.html', {'form': form})


