from django.shortcuts import render

from editarticle.forms import SerachForm
# Create your views here.

from course.models import Course, Tag, CoruseConnectionStudent

def index(request):

    if request.method == 'GET':
        form = SerachForm()
        return render(request, 'index1.html', {'form': form})

    if request.method == 'POST':
        form = SerachForm(request.POST)

        if form.is_valid():
            tag = form.cleaned_data['tag']
            # lever = form.cleaned_data['lever']
            # start_date = form.cleaned_data['start_date']
            
            query_set = Course.objects.filter(tag=tag)
            return render(request, 'result.html', {'s': query_set})
        print("不合法表单")
        return render(request, 'index1.html', {'form': form})


from django.http import HttpResponse
from django.shortcuts import render_to_response
 
# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'search' in request.GET:
        leaver = request.GET['search']
        res = Course.objects.filter(level = leaver)
    else:
        return HttpResponse("你提交了空表单")

    return render(request, 'result.html', {'s': res})