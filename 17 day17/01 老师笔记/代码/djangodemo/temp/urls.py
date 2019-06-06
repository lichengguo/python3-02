# pycharm里面提供了快速导报的方式给我们
# 快捷键: Alt[换挡] + Enter[回车键]  -> import xxx ->> 找到对应的包目录进行导入即可
from django.urls import path
from . import views

urlpatterns = [
	path("index/", views.index),
	path("home/", views.HomeView.as_view()),
	path("index/index/", views.IndexView.as_view()),
	path("index/list/", views.ListView.as_view()),
	path("user/", views.UserView.as_view()),
	path("user2/", views.User2View.as_view()),
]