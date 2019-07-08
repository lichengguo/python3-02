"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls

import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    # 接口文档
    path('docs/', include_docs_urls(title='站点页面标题')),
    # admin后台站点
    path('admin/', admin.site.urls),
    # xadmin
    path(r'xadmin/', xadmin.site.urls),

    path('students/', include("student.urls")),
    path('ser/', include("ser.urls")),
    path('view/', include("myview.urls")),
    path('four/', include("four.urls")),
]
