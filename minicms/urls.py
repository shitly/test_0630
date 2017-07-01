"""minicms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from auths import views

from course import t_views, views as c_view
from ks import views as ks_views
from ciso import views as ciso_views
from editarticle import views as s_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    # 稿件库服务
    url(r'^gaojianku/', include("gjk.urls"), name="gaojianku"),

    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),

    url(r'^home/$', views.home, name='home'),

    # course_view
    url(r'^course/', include("course.urls"), name="course_view"),
    

    url(r'^index_v2/', c_view.index_v2, name="index_v2"),
    url(r'^i/', c_view.index, name="index"),
    
    url(r'^student_course/$', c_view.student_course, name="request_user_view"),
    url(r'^student_course/(?P<pk>[0-9]+)/$', c_view.stu_course, name="stu_course_view_of"),
    url(r'^student_course/(?P<pk>[0-9]+)/$', c_view.sc_search, name="sc_serach"), 

    url(r'^ks/', ks_views.index, name="ks_view"),
    url(r'^ciso/', ciso_views.homepage, name="ciso_index"),

    url(r'^manager/', t_views.homepage, name="t_index"),


    # url(r'^get/(?P<s1>/w+)/(?P<2>/w+)/(?P<s3>/w+)/$', s_views.index, name="s_index"),
    url(r'^get/$', s_views.index, name="s_index"),


    url(r'^search-form$', s_views.search_form),
    url(r'^search$', s_views.search),
]

# if setting.DEBUG:
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
