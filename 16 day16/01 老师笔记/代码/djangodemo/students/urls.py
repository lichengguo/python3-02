from django.urls import path    # 不需要使用正则
from django.urls import re_path  # 需要使用正则
from . import views
app_name="home"
urlpatterns = [
	# path("访问url地址", 视图函数名, name="路由别名")
	path("", views.index,name="index"), # 为了防止用户访问出错,我们强烈建议每次声明路由访问地址,以 / 斜杠结尾
	re_path("^list/$",views.list),
	re_path("^list/(?P<mobile>\d{11})/$", views.list2 ),
	re_path("^list/(?P<cat>\d+)/(?P<pn>\d+)/$", views.list3),
	re_path("^list2/(\d+)/(.+)/$", views.list4 ),
	path("detail/", views.detail ),
	path("detail2/", views.detail2 ),
	path("detail3/", views.detail3 ),
	path("detail4/", views.detail4 ),
	path("detail5/", views.detail5 ),
	path("res1/", views.res1),
	path("res2/", views.res2),
]