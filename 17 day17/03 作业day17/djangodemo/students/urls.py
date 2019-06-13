from django.urls import path, re_path

from students import views
from . views import  my_decorator


app_name = "stu_space"  # 命名空间

urlpatterns = [
    # path("index/", views.index),
    # path("index/abc", views.list),
    # path("img", views.imgs),
    # path("index2/", views.index2, name='index_rev'),
    # re_path("^index3/(\d{2})$", views.index3),
    # re_path("^index4/(?P<n>\d{3})$", views.index4),
    # path("index5/", views.index5),
    # path("login/", views.login, name='login_rev'),
    # path('register/', views.register),
    # path('userview/', views.UserView.as_view()),
    path('uapi2/', views.Uapi2.as_view()),
    path('studentview/', views.StudentView.as_view()),

]
