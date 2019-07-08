from django.urls import path,re_path
from . import views
urlpatterns  =[
	# 使用序列化器对数据进行序列化,提供给客户端
	path("students/",views.StudentsView.as_view()),
	re_path("students/(?P<pk>\d+)/",views.StudentView.as_view()),
	# 使用序列化器对数据进行验证,接收客户端的数据
	path("students2/",views.Student2View.as_view()),
	# 使用序列化器对数据进行验证并反序列化处理
	path("students3/",views.Student3View.as_view()),
	re_path("students4/(?P<pk>\d+)/",views.Student4View.as_view()),

	# 序列化器的整体使用
path("students5/",views.Student5View.as_view()),
	# 模型类序列化器的创建和使用
path("students6/",views.Student6View.as_view()),
]