"""project_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app_name import views as learn_views

urlpatterns = [
    url(r'^$', learn_views.hello),
    url(r'^hello$', learn_views.hello),
    url(r'^admin/', admin.site.urls),
    url(r'^table$', learn_views.table),
    url(r'^weibor/(\d+)/$', learn_views.weiborelation),
    url(r'^zhihur$', learn_views.zhihurelation),
    url(r'^monitor$', learn_views.monitor),
    url(r'^weibo_data$', learn_views.weibo_data),
    url(r'^zhihu_data$', learn_views.zhihu_data),
    url(r'^data_pic$', learn_views.data_pic),
    url(r'^provice_weibo_data/(\d+)$', learn_views.provice_weibo_data),
    url(r'^data1$', learn_views.data1),
    url(r'^data2$', learn_views.data2),
    url(r'^login$', learn_views.login),
    url(r'^search/(\w+)$', learn_views.search),

]
